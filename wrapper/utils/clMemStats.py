import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils, clLib

import ctypes

CL_MEM_STATS_MAX_LIMIT = 0

ClMemDirectionT = clCommon.ClInt32T
class eClMemDirectionT(clUtils.Enum):
    CL_MEM_ALLOC = 0x0
    CL_MEM_FREE  = 0x1

class ClMemStatsT(ctypes.Structure):
    _fields_ = [
        ("numAllocs", clCommon.ClUint32T),
        ("numFrees", clCommon.ClUint32T),
        ("currentAllocSize", clCommon.ClUint32T),
        ("maxAllocSize", clCommon.ClUint32T),
        ("numPools", clCommon.ClUint32T)
    ]

class ClEoMemConfigT(ctypes.Structure):
    _fields_ = [
        ("memLimit", clCommon.ClUint32T),
        ("memLowWaterMark", clCommon.ClWaterMarkT),
        ("memHighWaterMark", clCommon.ClWaterMarkT),
        ("memMediumWaterMark", clCommon.ClWaterMarkT)
    ]

def CL_MEM_STATS_CHECK_WRAP_INCR(v,incr,wrapped):
    if v + incr < v:
        wrapped.value = clCommon.CL_TRUE
        v = 0
    v += incr
    return v

def CL_MEM_STATS_CHECK_WRAP_DECR(v,decr,wrapped):
    v -= decr
    if v < 0:
        wrapped.value = clCommon.CL_TRUE
        v = 0
    return v

def CL_MEM_STATS_UPDATE_ALLOCS(stats, wrapped):
    stats.numAllocs = CL_MEM_STATS_CHECK_WRAP_INCR(stats.numAllocs, 1, wrapped)

def CL_MEM_STATS_UPDATE_FREES(stats, wrapped):
    stats.numFrees = CL_MEM_STATS_CHECK_WRAP_INCR(stats.numFrees, 1, wrapped)

def CL_MEM_STATS_ALLOCSIZE_INCR(stats, size):
    stats.currentAllocSize += size

def CL_MEM_STATS_ALLOCSIZE_DECR(stats, size):
    stats.currentAllocSize -= size

def CL_MEM_STATS_UPDATE_ALLOC(stats, size, wrapped):
    stats.currentAllocSize = CL_MEM_STATS_CHECK_WRAP_INCR(stats.currentAllocSize, size, wrapped)
    CL_MEM_STATS_UPDATE_ALLOCS(stats, wrapped)

def CL_MEM_STATS_UPDATE_FREE(stats,size,wrapped):
    if stats.currentAllocSize > stats.maxAllocSize:
        stats.maxAllocSize = stats.currentAllocSize

    stats.currentAllocSize = CL_MEM_STATS_CHECK_WRAP_DECR(stats.currentAllocSize, size, wrapped)
    CL_MEM_STATS_UPDATE_FREES(stats, wrapped)

def clMemStatsInitialize(pConfig):
    """
    arg types:
        ClEoMemConfigT *pConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clMemStatsInitialize(clUtils.byref(pConfig))

def clMemStatsFinalize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clMemStatsFinalize()

def clMemStatsWaterMarksSet(pMemConfig):
    """
    arg types:
        ClEoMemConfigT *pMemConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clMemStatsWaterMarksSet(clUtils.byref(pMemConfig))


def clEoMemWaterMarksUpdate(memDir):
    """
    arg types:
        ClMemDirectionT memDir
    return type:
        void
    """
    return clLib.libmw_so.clEoMemWaterMarksUpdate(memDir)

def clEoMemAdmitAllocate(size):
    """
    arg types:
        ClUint32T size
    return type:
        ClBoolT
    """
    clLib.libmw_so.clEoMemAdmitAllocate.restype = clCommon.ClBoolT
    return clLib.libmw_so.clEoMemAdmitAllocate(size)


def clEoMemNotifyFree(size):
    """
    arg types:
        ClUint32T size
    return type:
        void
    """
    return clLib.libmw_so.clEoMemNotifyFree(size)
