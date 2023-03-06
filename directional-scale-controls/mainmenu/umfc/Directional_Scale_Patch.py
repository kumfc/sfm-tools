import ctypes
import traceback
import sys
import struct
from PySide import *

try:
    sfm
except NameError:
    from sfm_runtime_builtins import *


class Log():
    @staticmethod
    def info(msg):
        sfm.Msg('[Python] [*] ' + str(msg) + '\n')

    @staticmethod
    def debug(msg):
        if debug:
            sfm.Msg('[Python] [DEBUG] ' + str(msg) + '\n')


def MessageBoxInfo(text, window):
    msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, "Info", text, QtGui.QMessageBox.NoButton, window)
    msgBox.addButton("&Continue", QtGui.QMessageBox.RejectRole)
    if msgBox.exec_() == QtGui.QMessageBox.AcceptRole:
        pass


def MessageBoxError(text, window):
    msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error", text, QtGui.QMessageBox.NoButton, window)
    msgBox.addButton("&Continue", QtGui.QMessageBox.RejectRole)
    if msgBox.exec_() == QtGui.QMessageBox.AcceptRole:
        pass


debug = True
log = Log()
w = QtGui.QMainWindow()

read_process_memory = ctypes.windll.kernel32.ReadProcessMemory
write_process_memory = ctypes.windll.kernel32.WriteProcessMemory
get_current_process = ctypes.windll.kernel32.GetCurrentProcess
virtual_protect = ctypes.windll.kernel32.VirtualProtect


def mread(addr, length):
    to = ctypes.create_string_buffer(length)
    data = ctypes.c_size_t()
    read_process_memory(get_current_process(), addr, to, length, ctypes.byref(data))
    return ctypes.string_at(to, length)


def mwrite(addr, data):
    if debug:
        data_str = ' '.join('{:02x}'.format(x) for x in bytearray(data)).upper()
        log.debug('Writing "{}" to {}'.format(data_str, hex(addr)))

    patch = c_char_buf(len(data)).from_buffer(bytearray(data))

    bytes_to_write = ctypes.sizeof(patch)
    bytes_written = ctypes.c_size_t(0)

    write_process_memory(get_current_process(), addr, get_addr(patch), bytes_to_write, ctypes.byref(bytes_written))


def get_addr(obj):
    if type(obj) == ctypes.c_char_p:
        return ctypes.c_void_p.from_buffer(obj).value
    else:
        return ctypes.addressof(obj)


def c_char_buf(l):
    return ctypes.c_char * l


def prepare_rescale_patch(get_bone_addr, get_attr, scale_x, scale_y, scale_z):
    return (
        # pushad
        b"\x60"
        # sub    esp,0x10
        b"\x83\xec\x10"
        # movdqu XMMWORD PTR [esp],xmm0
        b"\xf3\x0f\x7f\x04\x24"
        # mov    ecx,DWORD PTR [esp+0x80]
        b"\x8b\x8c\x24\x80\x00\x00\x00"
        # cmp ecx, 00
        b"\x83\xF9\x00"
        # je <skip>
        b"\x0f\x84\xc3\x00\x00\x00"
        # push   edi
        b"\x57"
        # call   DWORD PTR ds:0x12345678 // p_get_bone_addr
        b"\xff\x15" + get_bone_addr +
        # mov    esi,eax
        b"\x89\xc6"
        # push   DWORD PTR ds:0x22334455 // str:scale_x
        b"\xff\x35" + scale_x +
        # mov    ecx,esi
        b"\x89\xf1"
        # call   DWORD PTR ds:0x12345679 // p_get_attr
        b"\xff\x15" + get_attr +
        # cmp    eax,0x0
        b"\x83\xf8\x00"
        # je     d3 <skip>
        b"\x0f\x84\xa3\x00\x00\x00"
        # mov    eax,DWORD PTR [eax+0x4]
        b"\x8b\x40\x04"
        # movss  xmm0,DWORD PTR [ebp-0xc]
        b"\xf3\x0f\x10\x45\xf4"
        # mulss  xmm0,DWORD PTR [eax]
        b"\xf3\x0f\x59\x00"
        # movss  DWORD PTR [ebp-0xc],xmm0
        b"\xf3\x0f\x11\x45\xf4"
        # movss  xmm0,DWORD PTR [ebp-0x1c]
        b"\xf3\x0f\x10\x45\xe4"
        # mulss  xmm0,DWORD PTR [eax]
        b"\xf3\x0f\x59\x00"
        # movss  DWORD PTR [ebp-0x1c],xmm0
        b"\xf3\x0f\x11\x45\xe4"
        # movss  xmm0,DWORD PTR [ebp-0x2c]
        b"\xf3\x0f\x10\x45\xd4"
        # mulss  xmm0,DWORD PTR [eax]
        b"\xf3\x0f\x59\x00"
        # movss  DWORD PTR [ebp-0x2c],xmm0
        b"\xf3\x0f\x11\x45\xd4"
        # push   DWORD PTR ds:0x22334456 // str:scale_y
        b"\xff\x35" + scale_y +
        # mov    ecx,esi
        b"\x89\xf1"
        # call   DWORD PTR ds:0x12345679 // p_get_attr
        b"\xff\x15" + get_attr +
        # mov    eax,DWORD PTR [eax+0x4]
        b"\x8b\x40\x04"
        # movss  xmm0,DWORD PTR [ebp-0x10]
        b"\xf3\x0f\x10\x45\xf0"
        # mulss  xmm0,DWORD PTR [eax]
        b"\xf3\x0f\x59\x00"
        # movss  DWORD PTR [ebp-0x10],xmm0
        b"\xf3\x0f\x11\x45\xf0"
        # movss  xmm0,DWORD PTR [ebp-0x30]
        b"\xf3\x0f\x10\x45\xd0"
        # mulss  xmm0,DWORD PTR [eax]
        b"\xf3\x0f\x59\x00"
        # movss  DWORD PTR [ebp-0x30],xmm0
        b"\xf3\x0f\x11\x45\xd0"
        # movss  xmm0,DWORD PTR [ebp-0x20]
        b"\xf3\x0f\x10\x45\xe0"
        # mulss  xmm0,DWORD PTR [eax]
        b"\xf3\x0f\x59\x00"
        # movss  DWORD PTR [ebp-0x20],xmm0
        b"\xf3\x0f\x11\x45\xe0"
        # push   DWORD PTR ds:0x22334457 // str:scale_z
        b"\xff\x35" + scale_z +
        # mov    ecx,esi
        b"\x89\xf1"
        # call   DWORD PTR ds:0x12345679 // p_get_attr
        b"\xff\x15" + get_attr +
        # mov    eax,DWORD PTR [eax+0x4]
        b"\x8b\x40\x04"
        # movss  xmm0,DWORD PTR [ebp-0x24]
        b"\xf3\x0f\x10\x45\xdc"
        # mulss  xmm0,DWORD PTR [eax]
        b"\xf3\x0f\x59\x00"
        # movss  DWORD PTR [ebp-0x24],xmm0
        b"\xf3\x0f\x11\x45\xdc"
        # movss  xmm0,DWORD PTR [ebp-0x14]
        b"\xf3\x0f\x10\x45\xec"
        # mulss  xmm0,DWORD PTR [eax]
        b"\xf3\x0f\x59\x00"
        # movss  DWORD PTR [ebp-0x14],xmm0
        b"\xf3\x0f\x11\x45\xec"
        # movss  xmm0,DWORD PTR [ebp-0x34]
        b"\xf3\x0f\x10\x45\xcc"
        # mulss  xmm0,DWORD PTR [eax]
        b"\xf3\x0f\x59\x00"
        # movss  DWORD PTR [ebp-0x34],xmm0
        b"\xf3\x0f\x11\x45\xcc"
        # movdqu xmm0,XMMWORD PTR [esp]
        b"\xf3\x0f\x6f\x04\x24"
        # add    esp,0x10
        b"\x83\xc4\x10"
        # popad
        b"\x61"
        # movss  xmm1,DWORD PTR [ebp-0x34]
        b"\xf3\x0f\x10\x4d\xcc"
        # ret
        b"\xc3")


def apply_patches():
    base = ctypes.windll.ifm._handle
    f_get_bone_addr = base + 0x5C3580
    f_get_attr = base + 0x35DD50
    i_patch_skip_write = base + 0x241B2C
    i_patch_skip_read = base + 0x241411
    i_patch_rescale = base + 0x24141E

    sfm.scale_patch_constants = [ctypes.c_char_p('scale_x'), ctypes.c_char_p('scale_y'), ctypes.c_char_p('scale_z'),
                                 ctypes.c_float(1337.0), ctypes.c_void_p(f_get_bone_addr), ctypes.c_void_p(f_get_attr)]
    sfm.scale_patch_constants += [ctypes.c_void_p(get_addr(i)) for i in sfm.scale_patch_constants[:3]]
    addr_list = [struct.pack('<I', get_addr(x)) for x in sfm.scale_patch_constants]

    # fp(0)
    patch_skip_write = b'\x8D\x3D' + addr_list[3]
    mwrite(i_patch_skip_write, patch_skip_write)
    # movss xmm1, [addr]
    patch_skip_write_1  = b'\xF3\x0F\x10\x0D' + addr_list[3]
    mwrite(i_patch_skip_write + 11, patch_skip_write_1)
    # ucomiss xmm0, [addr]
    patch_skip_read = b'\x0F\x2E\x05' + addr_list[3]
    mwrite(i_patch_skip_read, patch_skip_read)

    rescale_patch = prepare_rescale_patch(addr_list[4], addr_list[5], addr_list[6], addr_list[7], addr_list[8])
    sfm.scale_patch_alloc = c_char_buf(len(rescale_patch)).from_buffer(bytearray(rescale_patch))
    scale_patch_addr = get_addr(sfm.scale_patch_alloc)

    log.debug('Patch allocated at ' + hex(scale_patch_addr))

    old_protect = ctypes.c_long(1)
    virtual_protect(ctypes.c_void_p(scale_patch_addr), ctypes.c_int(len(rescale_patch)), 0x40, ctypes.byref(old_protect))

    rescale_patch_jmp_offset = scale_patch_addr - i_patch_rescale - 0x5
    if rescale_patch_jmp_offset < 0:
        rescale_patch_jmp_offset += 2 ** 32

    log.debug(hex(rescale_patch_jmp_offset))

    # call
    patch_rescale_jump = b'\xE8' + struct.pack('<I', rescale_patch_jmp_offset)
    mwrite(i_patch_rescale, patch_rescale_jump)

    log.debug('Patch applied!')


def restore_original_behaviour():
    #  BYTE unpatch[5] = { 0xF3, 0x0F, 0x10, 0x4D, 0xCC };
    pass


def main():
    try:
        sfm.scale_patch_applied
        MessageBoxInfo('Already patched!', w)
    except AttributeError:
        apply_patches()
        MessageBoxInfo('Successfully patched!\n\nExecute this script every time you restart SFM in order to see the scale changes.', w)
        sfm.scale_patch_applied = True


try:
    main()
except:
    MessageBoxError('An exception occurred while patching, check console for detailed information.', w)
    traceback.print_exc(file=sys.stderr)
