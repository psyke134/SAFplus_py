import sys
sys.path.append("..")

from utils import clLib

def clDbgInitialize():
    clLib.libmw_so.clDbgInitialize()

def clDbgPauseFn(file, line):
    """
    arg types:
        const char* file,
        int line
    """
    clLib.libmw_so.clDbgPauseFn(file, line)

def clDbgResume():
    clLib.libmw_so.clDbgResume()

def clDbgMsg(pid, file, line, fn, level, str):
    """
    arg types:
        int pid,
        const char* file,
        int line,
        const char* fn,
        int level,
        const char* str
    """
    clLib.libmw_so.clDbgMsg(pid, file, line, fn, level, str)

# TODO: there're remaining codes in the original header file
