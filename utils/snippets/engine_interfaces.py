########
def c_char_buf(*args):
    pass


def virtual_alloc(*args):
    pass


log = None
########


import ctypes


class ICvar(ctypes.Structure):
    _fields_ = [
        ("char_pad", c_char_buf(64)),
        ("FindVar", ctypes.c_void_p),
    ]


class ConVar(ctypes.Structure):
    _fields_ = [
        ("char_pad_01", c_char_buf(12)),
        ("name", ctypes.c_char_p),
        ("char_pad_02", c_char_buf(16)),
        ("default_value", ctypes.c_char_p),
        ("value", ctypes.c_char_p),
    ]


def thiscall(func, restype, arg_types, this, *args):
    buf = virtual_alloc(0, 4096, 0x3000, 0x40)
    code = "\x8b\x4c\x24\x08\x8f\x44\x24\x04\xc3"
    ctypes.memmove(buf, code, len(code))

    return ctypes.WINFUNCTYPE(restype, ctypes.c_void_p, ctypes.c_void_p, *arg_types)(buf)(func, this, *args)


def get_cvar_value(name):
    interface_ptr = ctypes.c_void_p.from_address(ctypes.windll.vstdlib.CreateInterface('VEngineCvar007'))
    interface = ICvar.from_address(interface_ptr.value)

    cvar_ptr = thiscall(interface.FindVar, ctypes.c_int, (ctypes.c_char_p,), ctypes.byref(interface_ptr), name)

    if cvar_ptr:
        cvar_obj = ConVar.from_address(cvar_ptr)

        log.debug('Current value of {} is {}'.format(name, cvar_obj.value))

        return cvar_obj.value