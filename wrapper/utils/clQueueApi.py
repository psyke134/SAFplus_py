import sys
sys.path.append("..")

from common import clCommon
from utils import clLib

import ctypes

ClQueueT = clCommon.ClPtrT
ClQueueNodeT = clCommon.ClHandleT
ClQueueDataT = clCommon.ClPtrT

ClQueueWalkCallbackT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ClQueueDataT,
    clCommon.ClPtrT
)

ClQueueDequeueCallbackT = ctypes.CFUNCTYPE(
    None,
    ClQueueDataT
)

def clQueueCreate(maxSize, fpUserDequeueCallBack, fpUserDestroyCallBack, pQueueHandle):
    """
    arg types: 
        ClUint32T maxSize, 
        ClQueueDequeueCallbackT fpUserDequeueCallBack, 
        ClQueueDequeueCallbackT fpUserDestroyCallBack, 
        ClQueueT *pQueueHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clQueueCreate(maxSize, fpUserDequeueCallBack, fpUserDestroyCallBack, pQueueHandle)

def clQueueDelete(pQueueHandle):
    """
    arg types:
        ClQueueT* pQueueHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clQueueDelete(pQueueHandle)

def clQueueNodeInsert(queueHandle, userData):
    """
    arg types:
        ClQueueT queueHandle,
        ClQueueDataT userData
    return type:
        ClRcT
    """
    return clLib.libmw_so.clQueueNodeInsert(queueHandle, userData)

def clQueueNodeDelete(queueHandle, userData):
    """
    arg types:
        ClQueueT queueHandle,
        ClQueueDataT* userData
    return type:
        ClRcT
    """
    return clLib.libmw_so.clQueueNodeDelete(queueHandle, userData)

def clQueueWalk(queueHandle, fpUserWalkFunction, userArg):
    """
    arg types: 
        ClQueueT queueHandle, 
        ClQueueWalkCallbackT fpUserWalkFunction, 
        void* userArg
    return type:
        ClRcT
    """
    return clLib.libmw_so.clQueueWalk(queueHandle, fpUserWalkFunction, userArg)

def clQueueSizeGet(queueHandle, pSize):
    """
    arg types:
        ClQueueT queueHandle,
        ClUint32T *pSize
    return type:
        ClRcT
    """
    return clLib.libmw_so.clQueueSizeGet(queueHandle, pSize)
