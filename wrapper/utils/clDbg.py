import sys
sys.path.append("..")

from utils import clLib, clUtils

def clDbgInitialize():
    clLib.libmw_so.clDbgInitialize()

def clDbgPauseFn(_file, line):
    """
    arg types:
        const char* file,
        int line
    """
    clLib.libmw_so.clDbgPauseFn(clUtils.toCharP(_file), line)

def clDbgResume():
    clLib.libmw_so.clDbgResume()

def clDbgMsg(pid, _file, line, _fn, level, _str):
    """
    arg types:
        int pid,
        const char* file,
        int line,
        const char* fn,
        int level,
        const char* str
    """
    clLib.libmw_so.clDbgMsg(pid, clUtils.toCharP(_file), line, clUtils.toCharP(_fn), level, clUtils.toCharP(_str))

# TODO: there're remaining codes in the original header file
