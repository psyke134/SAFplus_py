import sys
sys.path.append("..")

from utils import libc, clDbg, clUtils
from log import clLogApi, clLogUtilApi
import ctypes

CL_DEBUG_CRITICAL = 3

CL_DEBUG_ERROR = 4

CL_DEBUG_WARN = 5

CL_DEBUG_INFO = 7

CL_DEBUG_TRACE = 0xc

# TODO: there're remaining codes in the original header file

CL_DEBUG_LEVEL_THRESHOLD = CL_DEBUG_ERROR

def CL_DEBUG_PRINT(severity, fmt, *va_arg):
    _str = (ctypes.c_char * 256)()
    libc.snprintf(_str, 256, fmt, *va_arg)
    if severity <= CL_DEBUG_LEVEL_THRESHOLD:
        clLogUtilApi.clLog(
            severity,
            None,
            None,
            _str
        )

    funcname, filename, linenum = clUtils.getCallerInfo()
    clDbg.clDbgMsg(libc.getpid(), filename, linenum, funcname, severity, _str)

def CL_DEBUG_PRINT_CONSOLE(severity, fmt, *va_arg):
    _str = (ctypes.c_char * 256)()
    libc.snprintf(_str, 256, fmt, *va_arg)
    if severity <= CL_DEBUG_LEVEL_THRESHOLD:
        clLogUtilApi.clLogConsole(
            severity,
            None,
            None,
            _str
        )

    funcname, filename, linenum = clUtils.getCallerInfo()
    clDbg.clDbgMsg(libc.getpid(), filename, linenum, funcname, severity, _str)

