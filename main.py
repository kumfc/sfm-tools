from PySide import QtGui
import ctypes
import traceback
import sys

debug = False

w = QtGui.QMainWindow()

read_process_memory = ctypes.windll.kernel32.ReadProcessMemory
write_process_memory = ctypes.windll.kernel32.WriteProcessMemory
get_current_process = ctypes.windll.kernel32.GetCurrentProcess

nop, jmp = '\x90', '\xEB'


def MessageBoxSuccess(text, window):
    msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, "Success", text, QtGui.QMessageBox.NoButton, window)
    msgBox.addButton("&Continue", QtGui.QMessageBox.RejectRole)
    if msgBox.exec_() == QtGui.QMessageBox.AcceptRole:pass


def MessageBoxError(text, window):
    msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error", text, QtGui.QMessageBox.NoButton, window)
    msgBox.addButton("&Continue", QtGui.QMessageBox.RejectRole)
    if msgBox.exec_() == QtGui.QMessageBox.AcceptRole:pass 


def get_object_callables(obj):
    return [str(e) for e in obj.__dict__ if callable(obj.__dict__[e])]

class Log():
    @staticmethod
    def info(msg):
        sfm.Msg('[Python] [*] ' + str(msg) + '\n')
    
    @staticmethod
    def debug(msg):
        if debug:
            sfm.Msg('[Python] [DEBUG] ' + str(msg) + '\n')


log = Log()

def to_hex_str(s):
    return ' '.join(['%0.2X' % ord(i) for i in s])


def mread(addr, length):
    to = ctypes.create_string_buffer(length)
    data = ctypes.c_size_t()
    read_process_memory(get_current_process(), addr, to, length, ctypes.byref(data))
    return ctypes.string_at(to, length)


def mwrite(addr, data, ctype):
    if debug:
        if type(data) in (int, long):
            ldata = hex(data)[2:-1].upper()
            ldata = [ldata[i:i+2] for i in range(0, len(ldata), 2)]
            ldata.reverse()
            ldata = " ".join(ldata)
        elif type(data) == str:
            ldata = " ".join("{:02x}".format(ord(i)) for i in data).upper()
        else:
            ldata = str(data)
        log.debug('Writing ' + ldata + ' to ' + hex(addr))
    
    patch = ctype(data)
    bytes_to_write = ctypes.sizeof(patch)
    bytes_written = ctypes.c_size_t(0)

    write_process_memory(get_current_process(), addr, ctypes.addressof(patch), bytes_to_write, ctypes.byref(bytes_written))



def patch_CStudioRender_RampFlexWeight():
    base = ctypes.windll.studiorender._handle
    log.debug('studiorender.dll base = ' + hex(base))

    loc = base + 0x12e73
    log.debug('Write loc = ' + hex(loc))
    log.debug('Memory: ' + to_hex_str(mread(loc, 16)))

    patch = 0x90909000000078E9
    mwrite(loc, patch, ctypes.c_ulonglong)
    log.debug('Updated memory: ' + to_hex_str(mread(loc, 16)))


def patch_CStudioHdr_RunFlexRules():
    base = ctypes.windll.ifm._handle

    mwrite(base + 0x5D9C8A, nop, ctypes.c_char)
    mwrite(base + 0x5D9C8B, nop, ctypes.c_char)
    mwrite(base + 0x5D9C8C, nop, ctypes.c_char)
    mwrite(base + 0x5D9CA1, nop, ctypes.c_char)
    mwrite(base + 0x5D9CA2, nop, ctypes.c_char)
    mwrite(base + 0x5D9CA3, nop, ctypes.c_char)


def patch_interface_limitations():
    base = ctypes.windll.ifm._handle
    log.debug('ifm.dll base = ' + hex(base))

    mwrite(base + 0x263EF9, jmp, ctypes.c_char)
    mwrite(base + 0x263F09, jmp, ctypes.c_char)
    mwrite(base + 0xBCFEC, nop, ctypes.c_char)
    mwrite(base + 0xBCFED, nop, ctypes.c_char)
    mwrite(base + 0xBCFF4, nop, ctypes.c_char)
    mwrite(base + 0xBCFF5, nop, ctypes.c_char)


def main():
    try:
        log.info('Patching studiorender...')
        patch_CStudioRender_RampFlexWeight()
        log.info('Patching studiohdr...')
        patch_CStudioHdr_RunFlexRules()
        log.info('Patching interface...')
        patch_interface_limitations()
        log.info('Success!')
        MessageBoxSuccess('Successfully patched!', w)
    except Exception as e:
        MessageBoxError('An exception occured during patching, check console for detailed information.', w)
        traceback.print_exc(file=sys.stderr)


main()
