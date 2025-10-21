# Mostly to handle libc file descriptors
import ctypes

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
    fdset.fds_bits[fd // NFDBITS] |= (1  << (fd // NFDBITS))

def errno():
    return ctypes.get_errno()

select = libc.select
getpid = libc.getpid
