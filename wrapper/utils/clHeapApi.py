import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils, clLib
from ipi import clPoolIpi

import ctypes

ClHeapModeT = clCommon.ClInt32T
class eClHeapModeT(clUtils.Enum):
    CL_HEAP_PREALLOCATED_MODE = 0
    CL_HEAP_NATIVE_MODE = 1
    CL_HEAP_CUSTOM_MODE = 2

class ClHeapConfigT(ctypes.Structure):
    _fields_ = [
        ("mode", ClHeapModeT),
        ("lazy", clCommon.ClBoolT),
        ("pPoolConfig", clPoolIpi.ClPoolConfigT),
        ("numPools", clCommon.ClUint32T)
    ]

def clHeapAllocate(size):
    """
    arg types:
        ClUint32T size
    return type:
        ClPtrT
    """
    return clLib.libmw_so.clHeapAllocate(size)


def clHeapFree(pAddress):
    """
    arg types:
        ClPtrT pAddress
    return type:
        void
    """
    return clLib.libmw_so.clHeapFree(pAddress)


def clHeapCalloc(numChunks, chunkSize):
    """
    arg types:
        ClUint32T numChunks,
        ClUint32T chunkSize
    return type:
        ClPtrT
    """
    return clLib.libmw_so.clHeapCalloc(numChunks, chunkSize)


def clHeapLibInitialize(pHeapConfig):
    """
    arg types:
        ClHeapConfigT *pHeapConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapLibInitialize(pHeapConfig)


def clHeapLibFinalize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapLibFinalize()


def clHeapInit():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapInit()


def clHeapExit():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapExit()


def clHeapRealloc(pAddress, size):
    """
    arg types:
        ClPtrT pAddress,
        ClUint32T size
    return type:
        ClPtrT
    """
    return clLib.libmw_so.clHeapRealloc(pAddress, size)


def clHeapShrink(pShrinkOptions):
    """
    arg types:
        ClPoolShrinkOptionsT *pShrinkOptions
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapShrink(pShrinkOptions)


def clHeapModeGet(pMode):
    """
    arg types:
        ClHeapModeT *pMode
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapModeGet(pMode)


def clHeapStatsGet(pHeapStats):
    """
    arg types:
        ClMemStatsT *pHeapStats
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapStatsGet(pHeapStats)


def clHeapPoolStatsGet(numPools, pPoolSize, pHeapPoolStats):
    """
    arg types:
        ClUint32T numPools,
        ClUint32T *pPoolSize,
        ClPoolStatsT *pHeapPoolStats
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapPoolStatsGet(numPools, pPoolSize, pHeapPoolStats)


def clHeapLibCustomInitialize(pHeapConfig):
    """
    arg types:
        ClHeapConfigT *pHeapConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapLibCustomInitialize(pHeapConfig)


def clHeapLibCustomFinalize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapLibCustomFinalize()

allocHookT = ctypes.CFUNCTYPE(clCommon.ClPtrT, clCommon.ClUint32T)
reallocHookT = ctypes.CFUNCTYPE(clCommon.ClPtrT, clCommon.ClPtrT, clCommon.ClUint32T)
callocHookT = ctypes.CFUNCTYPE(clCommon.ClPtrT, clCommon.ClUint32T, clCommon.ClUint32T)
freeHookT = ctypes.CFUNCTYPE(None, clCommon.ClPtrT)

def clHeapHooksRegister(allocHook, reallocHook, callocHook, freeHook):
    """
    arg types:
        allocHookT allocHook,
        reallocHookT reallocHook,
        callocHookT callocHook,
        freeHookT freeHook
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapHooksRegister(allocHook, reallocHook, callocHook, freeHook)


def clHeapHooksDeregister():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapHooksDeregister()
