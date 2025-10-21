import ctypes
import enum
import inspect

class CEnum(enum.Enum):
    def __new__(cls, *args):
        dummy = 0
        return ctypes.c_int(dummy)

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
        cVaArgs.append(arg)

    return (cVaArgs, argTypes)

def toCharP(pythonStr):
    return ctypes.c_char_p(pythonStr.encode("utf-8"))

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

    return (filename, line_number)
