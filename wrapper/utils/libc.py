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
    fdset.fds_bits[fd.value // NFDBITS] |= (1  << (fd.value % NFDBITS))

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

def select(nfds, readfds, writefds, exceptfds, timeout):
    return libc.select(nfds, clUtils.byref(readfds), clUtils.byref(writefds), clUtils.byref(exceptfds), clUtils.byref(timeout))

getpid = libc.getpid
memcpy = libc.memcpy

SIZEOF_SEM_T = 32

class sem_t(ctypes.Union):
    _fields_ = [
        ("__size", ctypes.c_char * SIZEOF_SEM_T),
        ("__align", ctypes.c_long)
    ]

_SIZEOF_PTHREAD_MUTEX_T = 40

class _pthread_list_t(ctypes.Structure):
    pass
_pthread_list_t._fields_ = [
    ("__prev", ctypes.POINTER(_pthread_list_t)),
    ("__next", ctypes.POINTER(_pthread_list_t))
]

class _pthread_mutex_s(ctypes.Structure):
    _fields_ = [
        ("__lock", ctypes.c_int),
        ("__count", ctypes.c_uint),
        ("owner", ctypes.c_int),
        ("__nusers", ctypes.c_uint),
        ("__kind", ctypes.c_int),
        ("__spins", ctypes.c_short),
        ("__elision", ctypes.c_short),
        ("__list", _pthread_list_t),
    ]

class pthread_mutex_t(ctypes.Union):
    _fields_ = [
        ("__data", _pthread_mutex_s),
        ("__size", ctypes.c_char * _SIZEOF_PTHREAD_MUTEX_T),
        ("__align", ctypes.c_long)
    ]

_SIZEOF_PTHREAD_MUTEXATTR_T = 4

class pthread_mutexattr_t(ctypes.Union):
    _fields_ = [
        ("__size", ctypes.c_char * _SIZEOF_PTHREAD_MUTEXATTR_T),
        ("__align", ctypes.c_int)
    ]

_SIZEOF_PTHREAD_CONDATTR_T = 4

class pthread_condattr_t(ctypes.Union):
    _fields_ = [
        ("__size", ctypes.c_char * _SIZEOF_PTHREAD_CONDATTR_T),
        ("__align", ctypes.c_int)
    ]

class _value32(ctypes.Structure):
    _fields_ = [
        ("__low", ctypes.c_uint),
        ("__high", ctypes.c_uint)
    ]

class _atomic_wide_counter(ctypes.Union):
    _fields_ = [
        ("__value64", ctypes.c_ulonglong),
        ("__value32", _value32)
    ]

class _pthread_cond_s(ctypes.Structure):
    _fields_ = [
        ("__wseq", _atomic_wide_counter),
        ("__g1_start", _atomic_wide_counter),
        ("__g_refs", ctypes.c_uint * 2),
        ("__g_size", ctypes.c_uint * 2),
        ("__g1_orig_size", ctypes.c_uint),
        ("__wrefs", ctypes.c_uint),
        ("__g_signals", ctypes.c_uint * 2)
    ]

_SIZEOF_PTHREAD_COND_T = 48

class pthread_cond_t(ctypes.Union):
    _fields_ = [
        ("__data", _pthread_cond_s),
        ("__size", ctypes.c_char * _SIZEOF_PTHREAD_COND_T),
        ("__align", ctypes.c_longlong)
    ]

_time_t = ctypes.c_long
_syscall_slong_t = ctypes.c_long

class timespec(ctypes.Structure):
    _fields_ = [
        ("tv_sec", _time_t),
        ("tv_nsec", _syscall_slong_t)
    ]

class iovec(ctypes.Structure):
    _fields_ = [
        ("iov_base", ctypes.c_void_p),
        ("iov_len", ctypes.c_size_t)
    ]
