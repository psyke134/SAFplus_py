import sys
sys.path.append("..")

from common import clCommon
from utils import clHash, clMD5Api, clLib, clUtils

import ctypes

CL_DIFFERENCE_VECTOR_BLOCK_SHIFT = (12)
CL_DIFFERENCE_VECTOR_BLOCK_SIZE = ( 1 << CL_DIFFERENCE_VECTOR_BLOCK_SHIFT )
CL_DIFFERENCE_VECTOR_BLOCK_MASK = ( CL_DIFFERENCE_VECTOR_BLOCK_SIZE - 1 )

class ClDifferenceVectorKeyT(ctypes.Structure):
    _fields_ = [
        ("groupKey", ctypes.POINTER(clCommon.ClStringT)),
        ("sectionKey", ctypes.POINTER(clCommon.ClStringT))
    ]

class ClDifferenceBlockT(ctypes.Structure):
    _fields_ = [
        ("hash", clHash.hashStruct),
        ("key", ClDifferenceVectorKeyT),
        ("size", clCommon.ClSizeT),
        ("data", ctypes.POINTER(clCommon.ClUint8T)),
        ("md5Blocks", clCommon.ClUint32T),
        ("md5List", ctypes.POINTER(clMD5Api.ClMD5T))
    ]

class ClDataVectorT(ctypes.Structure):
    _fields_ = [
        ("dataBlock", clCommon.ClUint32T),
        ("dataSize", clCommon.ClSizeT),
        ("dataBase", ctypes.POINTER(clCommon.ClUint8T))
    ]

class ClDifferenceVectorT(ctypes.Structure):
    _fields_ = [
        ("numDataVectors", clCommon.ClUint32T),
        ("dataVectors", ctypes.POINTER(ClDataVectorT)),
        ("md5Blocks", clCommon.ClUint32T),
        ("md5List", ctypes.POINTER(clMD5Api.ClMD5T))
    ]

def clDifferenceVectorGet(key, data, offset, size, copyData, vector):
    """
    arg types:
        ClDifferenceVectorKeyT *key,
        ClUint8T *data,
        ClOffsetT offset,
        ClSizeT size,
        ClBoolT copyData,
        ClDifferenceVectorT *vector
    return type:
        ClRcT
    """
    return clLib.libmw_so.clDifferenceVectorGet(clUtils.byref(key), data, offset, size, copyData, clUtils.byref(vector))


def clDifferenceVectorGetWithReset(key, data, offset, size, copyData, vector):
    """
    arg types:
        ClDifferenceVectorKeyT *key,
        ClUint8T *data,
        ClOffsetT offset,
        ClSizeT size,
        ClBoolT copyData,
        ClDifferenceVectorT *vector
    return type:
        ClRcT
    """
    return clLib.libmw_so.clDifferenceVectorGetWithReset(clUtils.byref(key), data, offset, size, copyData, clUtils.byref(vector))


def clDifferenceVectorMergeWithData(lastData, lastDataSize, vector, offset, size):
    """
    arg types:
        ClUint8T *lastData,
        ClSizeT lastDataSize,
        ClDifferenceVectorT *vector,
        ClOffsetT offset,
        ClSizeT size
    return type:
        ClUint8T *
    """
    clLib.libmw_so.clDifferenceVectorMergeWithData.restype = ctypes.POINTER(clCommon.ClUint8T)
    return clLib.libmw_so.clDifferenceVectorMergeWithData(lastData, lastDataSize, clUtils.byref(vector), offset, size)


def clDifferenceVectorMerge(key, vector, offset, size):
    """
    arg types:
        ClDifferenceVectorKeyT *key,
        ClDifferenceVectorT *vector,
        ClOffsetT offset,
        ClSizeT size
    return type:
        ClUint8T *
    """
    clLib.libmw_so.clDifferenceVectorMerge.restype = ctypes.POINTER(clCommon.ClUint8T)
    return clLib.libmw_so.clDifferenceVectorMerge(clUtils.byref(key), clUtils.byref(vector), offset, size)


def clDifferenceVectorMergeWithReset(key, vector, offset, size):
    """
    arg types:
        ClDifferenceVectorKeyT *key,
        ClDifferenceVectorT *vector,
        ClOffsetT offset,
        ClSizeT size
    return type:
        ClUint8T *
    """
    clLib.libmw_so.clDifferenceVectorMergeWithReset.restype = ctypes.POINTER(clCommon.ClUint8T)
    return clLib.libmw_so.clDifferenceVectorMergeWithReset(clUtils.byref(key), clUtils.byref(vector), offset, size)


def clDifferenceVectorCopy(dest, src):
    """
    arg types:
        ClDifferenceVectorT *dest,
        ClDifferenceVectorT *src
    """
    clLib.libmw_so.clDifferenceVectorCopy(clUtils.byref(dest), clUtils.byref(src))


def clDifferenceVectorDelete(key):
    """
    arg types:
        ClDifferenceVectorKeyT *key
    return type:
        ClRcT
    """
    return clLib.libmw_so.clDifferenceVectorDelete(clUtils.byref(key))


def clDifferenceVectorDestroy():
    """
    arg types:
        void
    """
    clLib.libmw_so.clDifferenceVectorDestroy()


def clDifferenceVectorKeyFree(key):
    """
    arg types:
        ClDifferenceVectorKeyT *key
    """
    clLib.libmw_so.clDifferenceVectorKeyFree(clUtils.byref(key))


def clDifferenceVectorFree(differenceVector, freeDataVector):
    """
    arg types:
        ClDifferenceVectorT *differenceVector,
        ClBoolT freeDataVector
    """
    clLib.libmw_so.clDifferenceVectorFree(clUtils.byref(differenceVector), freeDataVector)


def clDifferenceVectorKeyMake(key, groupKey, sectionFmt, *va_args):
    """
    arg types:
        ClDifferenceVectorKeyT *key,
        const ClNameT *groupKey,
        const ClCharT *sectionFmt,
        ... (variadic arguments)
    return type:
        ClDifferenceVectorKeyT *
    """
    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clDifferenceVectorKeyMake.argtypes = [ctypes.POINTER(ClDifferenceVectorKeyT), ctypes.POINTER(clCommon.ClNameT), ctypes.c_char_p] + argTypes
    clLib.libmw_so.clDifferenceVectorKeyMake.restype = ctypes.pointer(ClDifferenceVectorKeyT)
    return clLib.libmw_so.clDifferenceVectorKeyMake(clUtils.byref(key), clUtils.byref(groupKey), clUtils.toCharP(sectionFmt), *cVaArgs)


def clDifferenceVectorKeyCheck(key):
    """
    arg types:
        ClDifferenceVectorKeyT *key
    return type:
        ClBoolT
    """
    clLib.libmw_so.clDifferenceVectorKeyCheck.restype = clCommon.ClBoolT
    return clLib.libmw_so.clDifferenceVectorKeyCheck(clUtils.byref(key))


def clDifferenceVectorKeyCheckAndAdd(key):
    """
    arg types:
        ClDifferenceVectorKeyT *key
    return type:
        ClBoolT
    """
    clLib.libmw_so.clDifferenceVectorKeyCheckAndAdd.restype = clCommon.ClBoolT
    return clLib.libmw_so.clDifferenceVectorKeyCheckAndAdd(clUtils.byref(key))
