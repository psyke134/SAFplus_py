import ctypes
import os

import saAis
import saNtf
import clUtils

libClAmfClient_so = ctypes.CDLL(os.path.dirname(__file__) + os.sep + "libClAmfClient.so")

SaAmfHandleT = saAis.SaUint64T

SA_AMF_PM_ZERO_EXIT = 0x1
SA_AMF_PM_NON_ZERO_EXIT = 0x2
SA_AMF_PM_ABNORMAL_END = 0x4

SaAmfPmErrorsT = saAis.SaUint32T

SaAmfPmStopQualifierT = saAis.SaInt32T
class eSaAmfPmStopQualifierT(clUtils.CEnum):
    SA_AMF_PM_PROC = 1,
    SA_AMF_PM_PROC_AND_DESCENDENTS = 2,
    SA_AMF_PM_ALL_PROCESSES = 3

SaAmfHealthcheckInvocationT = saAis.SaInt32T
class eSaAmfHealthcheckInvocationT(clUtils.CEnum):
    SA_AMF_HEALTHCHECK_AMF_INVOKED = 1,
    SA_AMF_HEALTHCHECK_COMPONENT_INVOKED= 2

SA_AMF_HEALTHCHECK_KEY_MAX = 32

class SaAmfHealthcheckKeyT(ctypes.Structure):
    _fields_ = [
        ("key", saAis.SaUint8T * SA_AMF_HEALTHCHECK_KEY_MAX),
        ("keyLen", saAis.SaUint16T)
    ]

SaAmfHAStateT = saAis.SaInt32T
class eSaAmfHAStateT(clUtils.CEnum):
    SA_AMF_HA_ACTIVE = 1,
    SA_AMF_HA_STANDBY = 2,
    SA_AMF_HA_QUIESCED = 3,
    SA_AMF_HA_QUIESCING = 4

SA_AMF_CSI_ADD_ONE = 0X1
SA_AMF_CSI_TARGET_ONE = 0X2
SA_AMF_CSI_TARGET_ALL = 0X4

SaAmfCSIFlagsT = saAis.SaUint32T

SaAmfCSITransitionDescriptorT = saAis.SaInt32T
class eSaAmfCSITransitionDescriptorT(clUtils.CEnum):
    SA_AMF_CSI_NEW_ASSIGN = 1,
    SA_AMF_CSI_QUIESCED = 2,
    SA_AMF_CSI_NOT_QUIESCED = 3,
    SA_AMF_CSI_STILL_ACTIVE = 4

class SaAmfCSIActiveDescriptorT(ctypes.Structure):
    _fields_ = [
        ("transitionDescriptor", SaAmfCSITransitionDescriptorT),
        ("activeCompName", saAis.SaNameT)
    ]

class SaAmfCSIStandbyDescriptorT(ctypes.Structure):
    _fields_ = [
        ("activeCompName", saAis.SaNameT),
        ("standbyRank", saAis.SaUint32T)
    ]

class SaAmfCSIStateDescriptorT(ctypes.Union):
    _fields_ = [
        ("activeDescriptor", SaAmfCSIActiveDescriptorT),
        ("standbyDescriptor", SaAmfCSIStandbyDescriptorT)
    ]

class SaAmfCSIAttributeT(ctypes.Structure):
    _fields_ = [
        ("attrName", ctypes.POINTER(saAis.SaUint8T)),
        ("attrValue", ctypes.POINTER(saAis.SaUint8T))
    ]

class SaAmfCSIAttributeListT(ctypes.Structure):
    _fields_ = [
        ("attr", ctypes.POINTER(SaAmfCSIAttributeT)),
        ("number", saAis.SaUint32T)
    ]

class SaAmfCSIDescriptorT(ctypes.Structure):
    _fields_ = [
        ("csiFlags", SaAmfCSIFlagsT),
        ("csiName", saAis.SaNameT),
        ("csiStateDescriptor", SaAmfCSIStateDescriptorT),
        ("csiAttr", SaAmfCSIAttributeListT)
    ]

class SaAmfProtectionGroupMemberT(ctypes.Structure):
    _fields_ = [
        ("compName", saAis.SaNameT),
        ("haState", SaAmfHAStateT),
        ("rank", saAis.SaUint32T)
    ]

SaAmfProtectionGroupChangesT = saAis.SaInt32T
class eSaAmfProtectionGroupChangesT(clUtils.CEnum):
    SA_AMF_PROTECTION_GROUP_NO_CHANGE = 1,
    SA_AMF_PROTECTION_GROUP_ADDED = 2,
    SA_AMF_PROTECTION_GROUP_REMOVED = 3,
    SA_AMF_PROTECTION_GROUP_STATE_CHANGE = 4

class SaAmfProtectionGroupNotificationT(ctypes.Structure):
    _fields_ = [
        ("member", SaAmfProtectionGroupMemberT),
        ("change", SaAmfProtectionGroupChangesT)
    ]

class SaAmfProtectionGroupNotificationBufferT(ctypes.Structure):
    _fields_ = [
        ("numberOfItems", saAis.SaUint32T),
        ("notification", ctypes.POINTER(SaAmfProtectionGroupNotificationT))
    ]

SaAmfRecommendedRecoveryT = saAis.SaInt32T
class eSaAmfRecommendedRecoveryT(clUtils.CEnum):
    SA_AMF_NO_RECOMMENDATION = 1,
    SA_AMF_COMPONENT_RESTART = 2,
    SA_AMF_COMPONENT_FAILOVER = 3,
    SA_AMF_NODE_SWITCHOVER = 4,
    SA_AMF_NODE_FAILOVER = 5,
    SA_AMF_NODE_FAILFAST = 6,
    SA_AMF_CLUSTER_RESET =7

SaAmfHealthcheckCallbackT = ctypes.CFUNCTYPE(
    None,
    saAis.SaInvocationT,
    ctypes.POINTER(saAis.SaNameT),
    ctypes.POINTER(SaAmfHealthcheckKeyT)
)

SaAmfComponentTerminateCallbackT = ctypes.CFUNCTYPE(
    None,
    saAis.SaInvocationT,
    ctypes.POINTER(saAis.SaNameT)
)

SaAmfCSISetCallbackT = ctypes.CFUNCTYPE(
    None,
    saAis.SaInvocationT,
    ctypes.POINTER(saAis.SaNameT),
    SaAmfHAStateT,
    SaAmfCSIDescriptorT
)

SaAmfCSIRemoveCallbackT = ctypes.CFUNCTYPE(
    None,
    saAis.SaInvocationT,
    ctypes.POINTER(saAis.SaNameT),
    ctypes.POINTER(saAis.SaNameT),
    SaAmfCSIFlagsT
)

SaAmfProtectionGroupTrackCallbackT = ctypes.CFUNCTYPE(
    None,
    ctypes.POINTER(saAis.SaNameT),
    ctypes.POINTER(SaAmfProtectionGroupNotificationBufferT),
    saAis.SaUint32T,
    saAis.SaAisErrorT
)

SaAmfProxiedComponentInstantiateCallbackT = ctypes.CFUNCTYPE(
    None,
    saAis.SaInvocationT,
    ctypes.POINTER(saAis.SaNameT)
)

SaAmfProxiedComponentCleanupCallbackT = ctypes.CFUNCTYPE(
    None,
    saAis.SaInvocationT,
    ctypes.POINTER(saAis.SaNameT)
)

class SaAmfCallbacksT(ctypes.Structure):
    _fields_ = [
        ("saAmfHealthcheckCallback", SaAmfHealthcheckCallbackT),
        ("saAmfComponentTerminateCallback", SaAmfComponentTerminateCallbackT),
        ("saAmfCSISetCallback", SaAmfCSISetCallbackT),
        ("saAmfCSIRemoveCallback", SaAmfCSIRemoveCallbackT),
        ("saAmfProtectionGroupTrackCallback", SaAmfProtectionGroupTrackCallbackT),
        ("saAmfProxiedComponentInstantiateCallback", SaAmfProxiedComponentInstantiateCallbackT),
        ("saAmfProxiedComponentCleanupCallback", SaAmfProxiedComponentCleanupCallbackT),
    ]

def saAmfInitialize(amfHandle, amfCallbacks, version):
    """
    arg types:
        SaAmfHandleT *amfHandle,
        const SaAmfCallbacksT *amfCallbacks,
        SaVersionT *version

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfInitialize(
        ctypes.byref(amfHandle),
        ctypes.byref(amfCallbacks),
        ctypes.byref(version)
    )

def saAmfSelectionObjectGet(amfHandle, selectionObject):
    """
    arg types:
        SaAmfHandleT amfHandle, 
        SaSelectionObjectT *selectionObject

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfSelectionObjectGet(
        amfHandle,
        ctypes.byref(selectionObject)
    )

def saAmfDispatch(amfHandle, dispatchFlags):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaDispatchFlagsT dispatchFlags

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfDispatch(
        amfHandle,
        dispatchFlags
    )

def saAmfFinalize(amfHandle):
    """
    arg types:
        SaAmfHandleT amfHandle

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfFinalize(
        amfHandle
    )

def saAmfComponentRegister(amfHandle, compName, proxyCompName):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaNameT *compName,
        SaNameT *proxyCompName

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfComponentRegister(
        amfHandle,
        ctypes.byref(compName),
        ctypes.byref(proxyCompName)
    )

def saAmfComponentUnregister(amfHandle, compName, proxyCompName):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaNameT *compName,
        SaNameT *proxyCompName

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfComponentUnregister(
        amfHandle,
        ctypes.byref(compName),
        ctypes.byref(proxyCompName)
    )

def saAmfComponentNameGet(amfHandle, compName):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaNameT *compName

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfComponentNameGet(
        amfHandle,
        ctypes.byref(compName)
    )

def saAmfPmStart(amfHandle, compName, processId, descendentsTreeDepth, pmErrors, recommendedRecovery):
    """
    arg types:
        SaAmfHandleT amfHandle,
        const SaNameT *compName,
        SaUint64T processId,
        SaInt32T descendentsTreeDepth,
        SaAmfPmErrorsT pmErrors,
        SaAmfRecommendedRecoveryT recommendedRecovery

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfPmStart(
        amfHandle,
        ctypes.byref(compName),
        processId,
        descendentsTreeDepth,
        pmErrors,
        recommendedRecovery
    )

def saAmfPmStop(amfHandle, compName, stopQualifier, processId, pmErrors):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaNameT *compName,
        SaAmfPmStopQualifierT stopQualifier,
        SaInt64T processId,
        SaAmfPmErrorsT pmErrors

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfPmStop(
        amfHandle,
        ctypes.byref(compName),
        stopQualifier,
        processId,
        pmErrors
    )

def saAmfHealthcheckStart(amfHandle, compName, healthcheckKey, invocationType, recommendedRecovery):
    """
    arg types:
        SaAmfHandleT amfHandle, 
        SaNameT *compName,
        SaAmfHealthcheckKeyT *healthcheckKey,
        SaAmfHealthcheckInvocationT invocationType,
        SaAmfRecommendedRecoveryT recommendedRecovery

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfHealthcheckStart(
        amfHandle,
        ctypes.byref(compName),
        ctypes.byref(healthcheckKey),
        invocationType,
        recommendedRecovery
    )

def saAmfHealthcheckConfirm(amfHandle, compName, healthcheckKey, healthcheckResult):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaNameT *compName,
        SaAmfHealthcheckKeyT *healthcheckKey,
        SaAisErrorT healthcheckResult

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfHealthcheckConfirm(
        amfHandle,
        ctypes.byref(compName),
        ctypes.byref(healthcheckKey),
        healthcheckResult
    )

def saAmfHealthcheckStop(amfHandle, compName, healthcheckKey):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaNameT *compName,
        SaAmfHealthcheckKeyT *healthcheckKey

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfHealthcheckStop(
        amfHandle,
        ctypes.byref(compName),
        ctypes.byref(healthcheckKey)
    )

def saAmfCSIQuiescingComplete(amfHandle, invocation, error):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaInvocationT invocation,
        SaAisErrorT error

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfCSIQuiescingComplete(
        amfHandle,
        invocation,
        error
    )

def saAmfHAStateGet(amfHandle, compName, csiName, haState):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaNameT *compName,
        SaNameT *csiName,
        SaAmfHAStateT *haState

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfHAStateGet(
        amfHandle,
        ctypes.byref(compName),
        ctypes.byref(csiName),
        ctypes.byref(haState)
    )

def saAmfProtectionGroupTrack(amfHandle, csiName, trackFlags, notificationBuffer):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaNameT *csiName,
        SaUint8T trackFlags,
        SaAmfProtectionGroupNotificationBufferT *notificationBuffer

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfProtectionGroupTrack(
        amfHandle,
        ctypes.byref(csiName),
        trackFlags,
        ctypes.byref(notificationBuffer)
    )

def saAmfProtectionGroupTrackStop(amfHandle, csiName):
    """
    arg types:
        SaAmfHandleT amfHandle,
        const SaNameT *csiName

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfProtectionGroupTrackStop(
        amfHandle,
        ctypes.byref(csiName)
    )

def saAmfComponentErrorReport(amfHandle, erroneousComponent, errorDetectionTime, recommendedRecovery, ntfIdentifier):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaNameT *erroneousComponent,
        SaTimeT errorDetectionTime,
        SaAmfRecommendedRecoveryT recommendedRecovery,
        SaNtfIdentifierT ntfIdentifier

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfComponentErrorReport(
        amfHandle,
        ctypes.byref(erroneousComponent),
        errorDetectionTime,
        recommendedRecovery,
        ntfIdentifier
    )

def saAmfComponentErrorClear(amfHandle, compName, ntfIdentifier):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaNameT *compName,
        SaNtfIdentifierT ntfIdentifier

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfComponentErrorClear(
        amfHandle,
        ctypes.byref(compName),
        ntfIdentifier
    )

def saAmfResponse(amfHandle, invocation, error):
    """
    arg types:
        SaAmfHandleT amfHandle,
        SaInvocationT invocation,
        SaAisErrorT error

    return type:
        SaAisErrorT
    """
    return libClAmfClient_so.saAmfResponse(
        amfHandle,
        invocation,
        error
    )
