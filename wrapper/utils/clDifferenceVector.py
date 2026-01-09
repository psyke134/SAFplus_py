import sys
sys.path.append("..")

from common import clCommon
from utils import clHash, clMD5Api, clLib

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
    return clLib.libmw_so.clDifferenceVectorGet(key, data, offset, size, copyData, vector)


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
    return clLib.libmw_so.clDifferenceVectorGetWithReset(key, data, offset, size, copyData, vector)


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
    return clLib.libmw_so.clDifferenceVectorMergeWithData(lastData, lastDataSize, vector, offset, size)


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
    return clLib.libmw_so.clDifferenceVectorMerge(key, vector, offset, size)


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
    return clLib.libmw_so.clDifferenceVectorMergeWithReset(key, vector, offset, size)


def clDifferenceVectorCopy(dest, src):
    """
    arg types:
        ClDifferenceVectorT *dest,
        ClDifferenceVectorT *src
    return type:
        void
    """
    return clLib.libmw_so.clDifferenceVectorCopy(dest, src)


def clDifferenceVectorDelete(key):
    """
    arg types:
        ClDifferenceVectorKeyT *key
    return type:
        ClRcT
    """
    return clLib.libmw_so.clDifferenceVectorDelete(key)


def clDifferenceVectorDestroy():
    """
    arg types:
        void
    return type:
        void
    """
    return clLib.libmw_so.clDifferenceVectorDestroy()


def clDifferenceVectorKeyFree(key):
    """
    arg types:
        ClDifferenceVectorKeyT *key
    return type:
        void
    """
    return clLib.libmw_so.clDifferenceVectorKeyFree(key)


def clDifferenceVectorFree(differenceVector, freeDataVector):
    """
    arg types:
        ClDifferenceVectorT *differenceVector,
        ClBoolT freeDataVector
    return type:
        void
    """
    return clLib.libmw_so.clDifferenceVectorFree(differenceVector, freeDataVector)


# Note: The C prototype uses a variadic argument list (printf style) for sectionFmt,
# which is represented simply as positional arguments in the Python wrapper.
def clDifferenceVectorKeyMake(key, groupKey, sectionFmt, *args):
    """
    arg types:
        ClDifferenceVectorKeyT *key,
        const ClNameT *groupKey,
        const ClCharT *sectionFmt,
        ... (variadic arguments)
    return type:
        ClDifferenceVectorKeyT *
    """
    # In a real implementation, you'd need ctypes/cffi to handle the variadic arguments.
    # Here, we pass the format string and potential extra arguments (if any).
    return clLib.libmw_so.clDifferenceVectorKeyMake(key, groupKey, sectionFmt, *args)


def clDifferenceVectorKeyCheck(key):
    """
    arg types:
        ClDifferenceVectorKeyT *key
    return type:
        ClBoolT
    """
    return clLib.libmw_so.clDifferenceVectorKeyCheck(key)


def clDifferenceVectorKeyCheckAndAdd(key):
    """
    arg types:
        ClDifferenceVectorKeyT *key
    return type:
        ClBoolT
    """
    return clLib.libmw_so.clDifferenceVectorKeyCheckAndAdd(key)
