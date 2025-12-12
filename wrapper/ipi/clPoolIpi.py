import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils, clLib

import ctypes

CL_POOL_MAX_SIZE = 0
CL_POOL_ALIGNMENT = 0x8
CL_POOL_ALIGNMENT_MASK = CL_POOL_ALIGNMENT - 1

ClPoolT = clCommon.ClPtrT
ClExtendedPoolT = clCommon.ClPtrT

ClPoolFlagsT = clCommon.ClInt32T
class eClPoolFlagsT(clUtils.CEnum):
    CL_POOL_DEFAULT_FLAG    = 0x0,
    CL_POOL_LAZY_FLAG       = 0x1,
    CL_POOL_DEBUG_FLAG      = 0x2,

class ClPoolConfigT(ctypes.Structure):
    _fields_ = [
        ("chunkSize", clCommon.ClUint32T),
        ("initialPoolSize", clCommon.ClUint32T),
        ("incrementPoolSize", clCommon.ClUint32T),
        ("maxPoolSize", clCommon.ClUint32T)
    ]

class ClPoolStatsT(ctypes.Structure):
    _fields_ = [
        ("poolConfig", ClPoolConfigT),
        ("numExtendedPools", clCommon.ClUint32T),
        ("maxNumExtendedPools", clCommon.ClUint32T),
        ("numAllocs", clCommon.ClUint32T),
        ("numFrees", clCommon.ClUint32T),
        ("maxNumAllocs", clCommon.ClUint32T)
    ]

ClPoolShrinkFlagsT = clCommon.ClInt32T
class eClPoolShrinkFlagsT(clUtils.CEnum):
    CL_POOL_SHRINK_DEFAULT = 0,
    CL_POOL_SHRINK_ONE = 1,
    CL_POOL_SHRINK_ALL = 2

class ClPoolShrinkOptionsT(ctypes.Structure):
    _fields_ = [
        ("shrinkFlags", ClPoolShrinkFlagsT)
    ]

def clPoolCreate(pHandle, flags, pPoolConfig):
    """
    arg types:
        ClPoolT *pHandle,
        ClPoolFlagsT flags,
        ClPoolConfigT *pPoolConfig
    return type:
        ClRcT
    """
    clLib.libmw_so.clPoolCreate(pHandle, flags, pPoolConfig)

def clPoolDestroy(poolHandle):
    """
    arg types:
        ClPoolT poolHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clPoolDestroy(poolHandle)


def clPoolShrink(poolHandle, pShrinkOptions):
    """
    arg types:
        ClPoolT poolHandle,
        ClPoolShrinkOptionsT *pShrinkOptions
    return type:
        ClRcT
    """
    return clLib.libmw_so.clPoolShrink(poolHandle, pShrinkOptions)


def clPoolAllocate(poolHandle, ppChunk, ppCookie):
    """
    arg types:
        ClPoolT poolHandle,
        ClUint8T** ppChunk,
        void **ppCookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clPoolAllocate(poolHandle, ppChunk, ppCookie)


def clPoolFree(pChunk, pCookie):
    """
    arg types:
        ClUint8T* pChunk,
        void *pCookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clPoolFree(pChunk, pCookie)


def clPoolStatsGet(pool, pPoolStats):
    """
    arg types:
        ClPoolT pool,
        ClPoolStatsT *pPoolStats
    return type:
        ClRcT
    """
    return clLib.libmw_so.clPoolStatsGet(pool, pPoolStats)


def clPoolChunkSizeGet(pCookie, pSize):
    """
    arg types:
        void *pCookie,
        ClUint32T* pSize
    return type:
        ClRcT
    """
    return clLib.libmw_so.clPoolChunkSizeGet(pCookie, pSize)


def clPoolStartGet(pCookie, ppAddress):
    """
    arg types:
        void *pCookie,
        void **ppAddress
    return type:
        ClRcT
    """
    return clLib.libmw_so.clPoolStartGet(pCookie, ppAddress)


def clPoolDestroyForce(poolHandle):
    """
    arg types:
        ClPoolT poolHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clPoolDestroyForce(poolHandle)


def clHeapReferenceLargeChunk(chunk, size):
    """
    arg types:
        ClPtrT chunk,
        ClUint32T size
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHeapReferenceLargeChunk(chunk, size)
