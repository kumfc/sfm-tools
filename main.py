from PySide import QtGui
import ctypes
import traceback
import sys

debug = True

w = QtGui.QMainWindow()

read_process_memory = ctypes.windll.kernel32.ReadProcessMemory
write_process_memory = ctypes.windll.kernel32.WriteProcessMemory
get_current_process = ctypes.windll.kernel32.GetCurrentProcess


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
    log.debug('Writing ' + str(data) + ' to ' + hex(addr))
    patch = ctype(data)
    bytes_to_write = ctypes.sizeof(patch)
    bytes_written = ctypes.c_size_t(0)

    write_process_memory(get_current_process(), addr, ctypes.addressof(patch), bytes_to_write, ctypes.byref(bytes_written))



def patch_CStudioRender_RampFlexWeight():
    base = ctypes.windll.studiorender._handle
    log.debug('studiorender.dll base = ' + hex(base))

    loc = base + 0x12e73
    log.debug('Write loc = ' + hex(loc))
    log.debug('Data: ' + to_hex_str(mread(loc, 16)))

    patch = 0x90909000000078E9
    mwrite(loc, patch, ctypes.c_ulonglong)
    log.debug('New data: ' + to_hex_str(mread(loc, 16)))


def patch_ifm_limitations():
    base = ctypes.windll.ifm._handle
    log.debug('ifm.dll base = ' + hex(base))
    nop, jmp = '\x90', '\xEB'
    mwrite(base + 0x263EF9, jmp, ctypes.c_char)
    mwrite(base + 0x263F09, jmp, ctypes.c_char)


def main():
    try:
        log.info('Patching studiorender...')
        patch_CStudioRender_RampFlexWeight()
        log.info('Patching ifm...')
        patch_ifm_limitations()
        log.info('Success!')
        MessageBoxSuccess('Successfully patched!', w)
    except Exception as e:
        MessageBoxError('An exception occured during patching, check console for detailed information.', w)
        traceback.print_exc(file=sys.stderr)


main()
