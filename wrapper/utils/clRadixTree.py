import sys
sys.path.append("..")

from common import clCommon
from utils import clLib, clUtils

ClRadixTreeHandleT = clCommon.ClPtrT

def clRadixTreeInit(handle):
    """
    arg types:
        ClRadixTreeHandleT *handle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRadixTreeInit(handle)


def clRadixTreeInsert(handle, index, item, lastItem):
    """
    arg types:
        ClRadixTreeHandleT handle,
        ClUint32T index,
        ClPtrT item,
        ClPtrT *lastItem
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRadixTreeInsert(handle, index, item, clUtils.byref(lastItem))


def clRadixTreeLookup(handle, index, item):
    """
    arg types:
        ClRadixTreeHandleT handle,
        ClUint32T index,
        ClPtrT *item
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRadixTreeLookup(handle, index, clUtils.byref(item))


def clRadixTreeDelete(handle, index, item):
    """
    arg types:
        ClRadixTreeHandleT handle,
        ClUint32T index,
        ClPtrT *item
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRadixTreeDelete(handle, index, clUtils.byref(item))
