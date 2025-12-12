import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils, clLib
from amf import clAmsTypes, clCpmConfigApi, clCpmApi, clAmsEntities
from ioc import clIocApi
from ipi import clCpmIpi
from ckpt import clCkptApi

import ctypes

CL_AMS_INSTANTIATE_MODE_ACTIVE = 1
CL_AMS_INSTANTIATE_MODE_STANDBY = 1<<1
CL_AMS_INSTANTIATE_USE_CHECKPOINT = 1<<2

CL_AMS_TERMINATE_MODE_GRACEFUL = 1
CL_AMS_TERMINATE_MODE_IMMEDIATE = 1<<1
CL_AMS_TERMINATE_MODE_SC_ONLY = 1<<2

CL_AMS_STATE_CHANGE_GRACEFUL = 1
CL_AMS_STATE_CHANGE_IMMEDIATE = 1<<1
CL_AMS_STATE_CHANGE_ACTIVE_TO_STANDBY = 1<<2
CL_AMS_STATE_CHANGE_STANDBY_TO_ACTIVE = 1<<3
CL_AMS_STATE_CHANGE_RESET = 1<<4
CL_AMS_STATE_CHANGE_USE_CHECKPOINT = 1<<5

class ClCpmInvocationT(ctypes.Structure):
    _fields_ = [
        ("invocation", clCommon.ClInvocationT),
        ("data", clCommon.ClPtrT),
        ("flags", clCommon.ClUint32T),
        ("createdTime", clCommon.ClTimeT)
    ]

class ClCpmMgmtCompT(ctypes.Structure):
    _fields_ = [
        ("compName", clCommon.ClCharT * clCommon.CL_MAX_NAME_LENGTH),
        ("compProperty", clAmsTypes.ClAmsCompPropertyT),
        ("compProcessRel", clCpmConfigApi.ClCpmCompProcessRelT),
        ("instantiationCMD", clCommon.ClCharT * clCommon.CL_MAX_NAME_LENGTH),
        ("argv", ctypes.POINTER(clCommon.ClCharT) * clCommon.CL_MAX_NAME_LENGTH)
    ]

ClCpmNodeLeaveT = clCommon.ClInt32T
class eClCpmNodeLeaveT(clUtils.CEnum):
    CL_CPM_NODE_LEAVING = 1,
    CL_CPM_NODE_LEFT    = 2

ClCpmComponentInstantiateT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clCommon.ClCharT),
    clCommon.ClUint64T,
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clIocApi.ClIocPhysicalAddressT),
    clCommon.ClUint32T
)

ClCpmComponentTerminateT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clIocApi.ClIocPhysicalAddressT),
    clCommon.ClUint32T
)

ClCpmComponentCleanupT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clIocApi.ClIocPhysicalAddressT),
    clCommon.ClUint32T,
    clCpmIpi.ClCpmCompRequestTypeT
)

ClCpmComponentRestartT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clIocApi.ClIocPhysicalAddressT),
    clCommon.ClUint32T
)

ClCpmComponentCSISetT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clCommon.ClCharT),
    clCommon.ClInvocationT,
    clAmsTypes.ClAmsHAStateT,
    clAmsTypes.ClAmsCSIDescriptorT
)

ClCpmComponentCSIRmvT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clCommon.ClCharT),
    ctypes.POINTER(clCommon.ClCharT),
    clCommon.ClInvocationT,
    ctypes.POINTER(clCommon.ClNameT),
    clAmsTypes.ClAmsCSIFlagsT
)

ClCpmComponentPGTrackT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clIocApi.ClIocAddressT,
    clCpmApi.ClCpmHandleT,
    clCommon.ClNameT,
    ctypes.POINTER(clAmsTypes.ClAmsPGNotificationBufferT),
    clCommon.ClUint32T,
    clCommon.ClUint32T
)

ClCpmNodeDepartureAllowedT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClNameT),
    ClCpmNodeLeaveT
)

ClCpmIocAddressForNodeGetT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClNameT),
    clIocApi.ClIocAddressT
)

ClCpmNodeNameForNodeAddressGetT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clIocApi.ClIocNodeAddressT,
    ctypes.POINTER(clCommon.ClNameT)
)

ClCpmNodeFailFastT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClNameT),
    clCommon.ClBoolT
)

ClCpmNodeFailOverT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClNameT),
    clCommon.ClBoolT
)

ClCpmNodeFailoverRestartT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClNameT),
    clCommon.ClBoolT
)

ClCpmEntityAddT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clAmsEntities.ClAmsEntityRefT)
)

ClCpmEntityRmvT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clAmsEntities.ClAmsEntityRefT)
)

ClCpmEntitySetConfigT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT),
    clCommon.ClUint64T
)

ClCpmNodeHaltT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClNameT),
    clCommon.ClBoolT
)

ClCpmClusterResetT = ctypes.CFUNCTYPE(
    clCommon.ClRcT
)

class ClCpmAmsToCpmCallT(ctypes.Structure):
    _fields_ = [
        ("compInstantiate", ClCpmComponentInstantiateT),
        ("compTerminate", ClCpmComponentTerminateT),
        ("compCleanup", ClCpmComponentCleanupT),
        ("compRestart", ClCpmComponentRestartT),
        ("compCSISet", ClCpmComponentCSISetT),
        ("compCSIRmv", ClCpmComponentCSIRmvT),
        ("compPGTrack", ClCpmComponentPGTrackT),
        ("nodeDepartureAllowed", ClCpmNodeDepartureAllowedT),
        ("cpmIocAddressForNodeGet", ClCpmIocAddressForNodeGetT),
        ("cpmNodeNameForNodeAddressGet", ClCpmNodeNameForNodeAddressGetT),
        ("cpmNodeFailFast", ClCpmNodeFailFastT),
        ("cpmNodeFailOver", ClCpmNodeFailOverT),
        ("cpmNodeFailOverRestart", ClCpmNodeFailoverRestartT),
        ("cpmEntityAdd", ClCpmEntityAddT),
        ("cpmEntityRmv", ClCpmEntityRmvT),
        ("cpmEntitySetConfig", ClCpmEntitySetConfigT),
        ("cpmNodeHalt", ClCpmNodeHaltT),
        ("cpmClusterReset", ClCpmClusterResetT)
    ]

ClAmsCompHAStateGetT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClNameT),
    ctypes.POINTER(clCommon.ClNameT),
    ctypes.POINTER(clAmsTypes.ClAmsHAStateT)
)

ClAmsQuiescingCompleteT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clCommon.ClInvocationT,
    clCommon.ClRcT
)

ClAmsComponentErrorReportT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClNameT),
    clCommon.ClTimeT,
    clAmsTypes.ClAmsLocalRecoveryT,
    clCommon.ClUint32T,
    clCommon.ClUint32T
)

ClAmsCSIOperationResponseT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clCommon.ClInvocationT,
    clCommon.ClRcT
)

ClAmsComponentOperationResponseT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clCommon.ClNameT,
    clCpmIpi.ClCpmCompRequestTypeT,
    clCommon.ClRcT
)

ClAmsNodeJoinT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClNameT)
)

ClAmsNodeLeaveT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClNameT),
    ClCpmNodeLeaveT,
    clCommon.ClBoolT
)

ClAmsPgTrackT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clIocApi.ClIocAddressT,
    clCpmApi.ClCpmHandleT,
    ctypes.POINTER(clCommon.ClNameT),
    clCommon.ClUint8T,
    ctypes.POINTER(clAmsTypes.ClAmsPGNotificationBufferT)
)

ClAmsPgTrackStopT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clIocApi.ClIocAddressT,
    clCpmApi.ClCpmHandleT,
    ctypes.POINTER(clCommon.ClNameT)
)

ClAmsCkptServerReady = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clCkptApi.ClCkptHdlT,
    clCommon.ClUint32T
)

ClAmsSAEventServerReady = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clCommon.ClBoolT
)

ClAmsSAAmsStateChange = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clCommon.ClUint32T
)

ClAmsSANodeAdd = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClCharT)
)

ClAmsSANodeRestart = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClNameT),
    clCommon.ClBoolT
)

class ClCpmCpmToAmsCallT(ctypes.Structure):
    _fields_ = [
        ("compHAStateGet", ClAmsCompHAStateGetT),
        ("csiQuiescingComplete", ClAmsQuiescingCompleteT),
        ("compErrorReport", ClAmsComponentErrorReportT),
        ("csiOperationComplete", ClAmsCSIOperationResponseT),
        ("compOperationComplete", ClAmsComponentOperationResponseT),
        ("nodeJoin", ClAmsNodeJoinT),
        ("nodeLeave", ClAmsNodeLeaveT),
        ("pgTrack", ClAmsPgTrackT),
        ("pgTrackStop", ClAmsPgTrackStopT),
        ("ckptServerReady", ClAmsCkptServerReady),
        ("amsStateChange", ClAmsSAAmsStateChange),
        ("eventServerReady", ClAmsSAEventServerReady),
        ("nodeAdd", ClAmsSANodeAdd),
        ("nodeRestart", ClAmsSANodeRestart)
    ]

def cpmInvocationAdd(cbType, data, invocationId, flags):
    """
    arg types:
        ClUint32T cbType,
        void *data,
        ClInvocationT *invocationId,
        ClUint32T flags
    return type:
        ClRcT
    """
    return clLib.libmw_so.cpmInvocationAdd(cbType, data, invocationId, flags)


def cpmInvocationAddKey(cbType, data, invocationId, flags):
    """
    arg types:
        ClUint32T cbType,
        void *data,
        ClInvocationT invocationId,
        ClUint32T flags
    return type:
        ClRcT
    """
    return clLib.libmw_so.cpmInvocationAddKey(cbType, data, invocationId, flags)


def cpmInvocationGet(invocationId, cbType, data):
    """
    arg types:
        ClInvocationT invocationId,
        ClUint32T *cbType,
        void **data
    return type:
        ClRcT
    """
    return clLib.libmw_so.cpmInvocationGet(invocationId, cbType, data)


def cpmHBInvocationGet(compName, invocation, createdTime, eoPort):
    """
    arg types:
        ClNameT *compName,
        ClInvocationT *invocation,
        ClTimeT *createdTime,
        ClIocPortT *eoPort
    return type:
        ClRcT
    """
    return clLib.libmw_so.cpmHBInvocationGet(compName, invocation, createdTime, eoPort)


def cpmInvocationGetWithLock(invocationId, cbType, data):
    """
    arg types:
        ClInvocationT invocationId,
        ClUint32T *cbType,
        void **data
    return type:
        ClRcT
    """
    return clLib.libmw_so.cpmInvocationGetWithLock(invocationId, cbType, data)


def cpmInvocationClearCompInvocation(compName):
    """
    arg types:
        ClNameT *compName
    return type:
        ClRcT
    """
    return clLib.libmw_so.cpmInvocationClearCompInvocation(compName)


def cpmInvocationDeleteInvocation(invocationId):
    """
    arg types:
        ClInvocationT invocationId
    return type:
        ClRcT
    """
    return clLib.libmw_so.cpmInvocationDeleteInvocation(invocationId)


def cpmReplayInvocationAdd(cbType, pComp, pNode, pResponsePending):
    """
    arg types:
        ClUint32T cbType,
        ClCharT *pComp,
        ClCharT *pNode,
        ClBoolT *pResponsePending
    return type:
        ClRcT
    """
    return clLib.libmw_so.cpmReplayInvocationAdd(cbType, pComp, pNode, pResponsePending)


def cpmReplayInvocationsGet(ppInvocations, pNumInvocations, canDelete):
    """
    arg types:
        ClAmsInvocationT ***ppInvocations,
        ClUint32T *pNumInvocations,
        ClBoolT canDelete
    return type:
        ClRcT
    """
    return clLib.libmw_so.cpmReplayInvocationsGet(ppInvocations, pNumInvocations, canDelete)


def cpmReplayInvocations(canDelete):
    """
    arg types:
        ClBoolT canDelete
    return type:
        ClRcT
    """
    return clLib.libmw_so.cpmReplayInvocations(canDelete)


def _cpmComponentCSIRmv(compName, proxyCompName, nodeName, invocation, csiName, csiFlags):
    """
    arg types:
        ClCharT *compName,
        ClCharT *proxyCompName,
        ClCharT *nodeName,
        ClInvocationT invocation,
        ClNameT *csiName,
        ClAmsCSIFlagsT csiFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so._cpmComponentCSIRmv(compName, proxyCompName, nodeName, invocation, csiName, csiFlags)


def _cpmComponentCSISet(compName, proxyCompName, nodeName, invocation, haState, csiDescriptor):
    """
    arg types:
        ClCharT *compName,
        ClCharT *proxyCompName,
        ClCharT *nodeName,
        ClInvocationT invocation,
        ClAmsHAStateT haState,
        ClAmsCSIDescriptorT csiDescriptor
    return type:
        ClRcT
    """
    return clLib.libmw_so._cpmComponentCSISet(compName, proxyCompName, nodeName, invocation, haState, csiDescriptor)


def clCpmAmsToCpmInitialize(callback):
    """
    arg types:
        ClCpmAmsToCpmCallT **callback
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmAmsToCpmInitialize(callback)


def clCpmAmsToCpmFree(callback):
    """
    arg types:
        ClCpmAmsToCpmCallT *callback
    return type:
        void
    """
    return clLib.libmw_so.clCpmAmsToCpmFree(callback)
