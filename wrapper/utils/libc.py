# Mostly to handle libc file descriptors
import sys
sys.path.append("..")

import ctypes
from utils import clUtils

libc = ctypes.CDLL("libc.so.6", use_errno = True) #GNU C library

FD_SETSIZE = 1024
NFDBITS = 8 * ctypes.sizeof(ctypes.c_long)
_NFDWORDS = FD_SETSIZE // NFDBITS

class fd_set(ctypes.Structure):
    _fields_ = [
        ("fds_bits", ctypes.c_long* _NFDWORDS)
    ]

def FD_ZERO(fdset):
    for i in range(len(fdset.fds_bits)):
        fdset.fds_bits[i] = 0

def FD_SET(fd, fdset):
    fdset.fds_bits[fd // NFDBITS] |= (1  << (fd % NFDBITS))

def errno():
    return ctypes.get_errno()

def snprintf(des, maxLen, fmt, *va_args):
    pDes = ctypes.cast(des, ctypes.c_char_p)
    pFmt = clUtils.toCharP(fmt)
    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)

    libc.snprintf.argtypes = [ctypes.c_char_p, ctypes.c_uint, ctypes.c_char_p] + argTypes
    libc.snprintf(pDes, maxLen, pFmt, *cVaArgs)

def strlen(cArray):
    pTemp = ctypes.cast(cArray, ctypes.c_char_p)
    return libc.strlen(pTemp)

select = libc.select
getpid = libc.getpid
