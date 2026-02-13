import sys
sys.path.append("..")

import ctypes
from common import clCommon
from buffer import clBufferApi
from utils import clUtils, clLib, clHeapApi

ClTimerCallBackT = ctypes.CFUNCTYPE(clCommon.ClRcT, clCommon.ClPtrT)
ClTimerReplicationCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, clBufferApi.ClBufferHandleT)

ClTimerHandleT = clCommon.ClPtrT

class ClTimerTimeOutT(ctypes.Structure):
    _fields_ = [
        ("tsSec", clCommon.ClUint32T),
        ("tsMilliSec", clCommon.ClUint32T)
    ]

class ClTimerConfigT(ctypes.Structure):
    _fields_ = [
        ("timerResolution", clCommon.ClUint32T),
        ("timerTaskPriority", clCommon.ClUint32T)
    ]

ClTimerTypeT = clCommon.ClInt32T
class eClTimerTypeT(clUtils.Enum):
    CL_TIMER_ONE_SHOT = 0
    CL_TIMER_REPETITIVE = 1
    CL_TIMER_VOLATILE = 2
    CL_TIMER_MAX_TYPE = 3

ClTimerContextT = clCommon.ClInt32T
class eClTimerContextT(clUtils.Enum):
    CL_TIMER_TASK_CONTEXT = 0
    CL_TIMER_SEPARATE_CONTEXT = 1
    CL_TIMER_MAX_CONTEXT = 3

def CL_TIMER_TYPE_STR(t):
    if t == eClTimerTypeT.CL_TIMER_ONE_SHOT:
        return "one shot"
    elif t == eClTimerTypeT.CL_TIMER_REPETITIVE:
        return "repetitive"
    else:
        return "volatile"
    
def CL_TIMER_CONTEXT_STR(ctxt):
    if ctxt == eClTimerContextT.CL_TIMER_SEPARATE_CONTEXT:
        return "thread"
    else:
        return "inline"
    
class ClTimerStatsT(ctypes.Structure):
    _fields_ = [
        ("type", ClTimerTypeT),
        ("context", ClTimerContextT),
        ("timeOut", clCommon.ClTimeT),
        ("expiry", clCommon.ClTimeT)
    ]

def clTimerConfigInitialize(pConfigData):
    """
    arg types:
        void* pConfigData
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerConfigInitialize(pConfigData)


def clTimerInitialize(pConfig):
    """
    arg types:
        ClPtrT pConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerInitialize(pConfig)


def clTimerFinalize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerFinalize()

def clTimerCreate(timeOut, timerType, timerTaskSpawn, fpAction, pActionArgument, pTimerHandle):
    """
    arg types:
        ClTimerTimeOutT timeOut,
        ClTimerTypeT timerType,
        ClTimerContextT timerTaskSpawn,
        ClTimerCallBackT fpAction,
        void* pActionArgument,
        ClTimerHandleT* pTimerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerCreate(timeOut, timerType, timerTaskSpawn, fpAction, pActionArgument, clUtils.byref(pTimerHandle))


def clTimerDelete(pTimerHandle):
    """
    arg types:
        ClTimerHandleT* pTimerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerDelete(clUtils.byref(pTimerHandle))


def clTimerDeleteAsync(pTimerHandle):
    """
    arg types:
        ClTimerHandleT *pTimerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerDeleteAsync(clUtils.byref(pTimerHandle))


def clTimerStart(timerHandle):
    """
    arg types:
        ClTimerHandleT timerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerStart(timerHandle)


def clTimerStop(timerHandle):
    """
    arg types:
        ClTimerHandleT timerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerStop(timerHandle)


def clTimerCreateAndStart(timeOut, timerType, timerTaskSpawn, fpAction, pActionArgument, pTimerHandle):
    """
    arg types:
        ClTimerTimeOutT timeOut,
        ClTimerTypeT timerType,
        ClTimerContextT timerTaskSpawn,
        ClTimerCallBackT fpAction,
        void *pActionArgument,
        ClTimerHandleT *pTimerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerCreateAndStart(timeOut, timerType, timerTaskSpawn, fpAction, pActionArgument, clUtils.byref(pTimerHandle))


def clTimerRestart(timerHandle):
    """
    arg types:
        ClTimerHandleT timerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerRestart(timerHandle)


def clTimerUpdate(timerHandle, newTimeout):
    """
    arg types:
        ClTimerHandleT timerHandle,
        ClTimerTimeOutT newTimeout
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerUpdate(timerHandle, newTimeout)

def clTimerTypeGet(timerHandle, pTimerType):
    """
    arg types:
        ClTimerHandleT timerHandle,
        ClUint32T* pTimerType
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerTypeGet(timerHandle, clUtils.byref(pTimerType))


def clTimerIsRunning(timerHandle, pState):
    """
    arg types:
        ClTimerHandleT timerHandle,
        ClBoolT *pState
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerIsRunning(timerHandle, clUtils.byref(pState))


def clTimerIsStopped(timerHandle, pState):
    """
    arg types:
        ClTimerHandleT timerHandle,
        ClBoolT *pState
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerIsStopped(timerHandle, clUtils.byref(pState))


def clTimerStatsGet(ppStats, pNumTimers):
    """
    arg types:
        ClTimerStatsT **ppStats,
        ClUint32T *pNumTimers
    return type:
        ClRcT
    """
    temp = ctypes.POINTER(ClTimerStatsT)()
    rc = clLib.libmw_so.clTimerStatsGet(clUtils.byref(temp), clUtils.byref(pNumTimers))
    if temp:
        ctypes.memmove(clUtils.byref(ppStats), temp, ctypes.sizeof(ClTimerStatsT))
        clHeapApi.clHeapFree(temp)
    return rc

def clTimerCheckAndDelete(pTimerHandle):
    """
    arg types:
        ClTimerHandleT *pTimerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerCheckAndDelete(clUtils.byref(pTimerHandle))

def clTimerClusterRegister(clusterCallback, replicationCallback):
    """
    arg types:
        ClTimerCallBackT clusterCallback,
        ClTimerReplicationCallbackT replicationCallback
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerClusterRegister(clusterCallback, replicationCallback)


def clTimerCreateCluster(timeOut, timerType, timerContext, timerData, timerDataSize, pTimerHandle):
    """
    arg types:
        ClTimerTimeOutT timeOut,
        ClTimerTypeT timerType,
        ClTimerContextT timerContext,
        void *timerData,
        ClUint32T timerDataSize,
        ClTimerHandleT *pTimerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerCreateCluster(timeOut, timerType, timerContext, timerData, timerDataSize, clUtils.byref(pTimerHandle))


def clTimerCreateAndStartCluster(timeOut, timerType, timerContext, timerData, timerDataSize, pTimerHandle):
    """
    arg types:
        ClTimerTimeOutT timeOut,
        ClTimerTypeT timerType,
        ClTimerContextT timerContext,
        void *timerData,
        ClUint32T timerDataSize,
        ClTimerHandleT *pTimerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerCreateAndStartCluster(timeOut, timerType, timerContext, timerData, timerDataSize, clUtils.byref(pTimerHandle))


def clTimerClusterPack(timer, msg):
    """
    arg types:
        ClTimerHandleT timer,
        ClBufferHandleT msg
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerClusterPack(timer, msg)


def clTimerClusterPackAll(msg):
    """
    arg types:
        ClBufferHandleT msg
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerClusterPackAll(msg)


def clTimerClusterUnpack(msg, pTimerHandle):
    """
    arg types:
        ClBufferHandleT msg,
        ClTimerHandleT *pTimerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerClusterUnpack(msg, clUtils.byref(pTimerHandle))


def clTimerClusterUnpackAll(msg):
    """
    arg types:
        ClBufferHandleT msg
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerClusterUnpackAll(msg)


def clTimerClusterFree(pTimerHandle):
    """
    arg types:
        ClTimerHandleT *pTimerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerClusterFree(clUtils.byref(pTimerHandle))


def clTimerClusterConfigureAll():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerClusterConfigureAll()


def clTimerClusterConfigure(pTimerHandle):
    """
    arg types:
        ClTimerHandleT *pTimerHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerClusterConfigure(clUtils.byref(pTimerHandle))


def clTimerClusterSync():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clTimerClusterSync()
