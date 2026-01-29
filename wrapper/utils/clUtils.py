import ctypes
import inspect

class Enum():
    @classmethod
    def str(cls, val):
        for k, v in cls.__dict__.items():
            if v == val:
                return k
        return "Uknown"

def handleVarArgs(*va_args):
    cVaArgs = []
    argTypes = []
    for arg in va_args:
        if isinstance(arg, int):
            argTypes.append(ctypes.c_int)
        elif isinstance(arg, float):
            argTypes.append(ctypes.c_double)
        elif isinstance(arg, str):
            argTypes.append(ctypes.c_char_p)
            arg = arg.encode("utf-8")
        elif isinstance(arg, bytes):
            argTypes.append(ctypes.c_char_p)
        else:
            argTypes.append(type(arg))
        cVaArgs.append(arg)

    return (cVaArgs, argTypes)

def toCharP(pythonStr):
    if isinstance(pythonStr, str):
        return ctypes.c_char_p(pythonStr.encode("utf-8"))
    else: # already bytes
        return ctypes.c_char_p(pythonStr)

def toUint8P(pythonStr):
    """
    Python string represent as unsigned 8bit integer buffer
    """
    char_p = toCharP(pythonStr)
    return ctypes.cast(char_p, ctypes.POINTER(ctypes.c_ubyte))

def getCallerInfo():
    """Get filename, line of the caller of this function's caller"""
    previous_frame = inspect.currentframe().f_back.f_back

    (
        filename,
        line_number,
        function_name,
        lines,
        index,
    ) = inspect.getframeinfo(previous_frame)

    return (function_name, filename, line_number)
