import clCommon
import clUtils
import clLib
import clEoConfigApi
import clAmsTypes
import clIocApi, clIocApiExt

import saAis
import saAmf

import ctypes

CL_CPM_RELEASE_CODE = 'B'
CL_CPM_MAJOR_VERSION = 0x01
CL_CPM_MINOR_VERSION = 0x01

CL_CPM_EVENT_CHANNEL_NAME = "CPM_EVENT_CHANNEL"
CL_CPM_NODE_EVENT_CHANNEL_NAME = "CPM_NODE_EVENT_CHANNEL"

CL_CPM_EO_ALIVE = 0
CL_CPM_EO_DEAD = 0xFFFFFFF

CL_CPM_IOC_SLOT_BITS = 16
CL_CPM_IOC_SLOT_BITS_HEX = 0x0000ffff

def CL_CPM_IOC_ADDRESS_GET(myCh, mySl, address):
    (address) = (myCh) << CL_CPM_IOC_SLOT_BITS
    (address) |= (mySl)
    return address

def CL_CPM_IOC_ADDRESS_SLOT_GET(address, mySl):
    (mySl) = (address) & CL_CPM_IOC_SLOT_BITS_HEX
    return mySl

def CL_CPM_IOC_ADDRESS_CHASSIS_GET(address, myCh):
    (myCh) = (address) >> CL_CPM_IOC_SLOT_BITS
    return myCh

ClCpmHandleT = clCommon.ClHandleT
ClCpmSchedFeedBackT = clEoConfigApi.ClEoSchedFeedBackT

CL_CPM_COMP_ARRIVAL_PATTERN = (1 << 0)
CL_CPM_COMP_DEPART_PATTERN = (1 << 1)
CL_CPM_COMP_DEATH_PATTERN = (1 << 2)
CL_CPM_NODE_ARRIVAL_PATTERN = (1 << 3)
CL_CPM_NODE_DEPART_PATTERN = (1 << 4)
CL_CPM_NODE_DEATH_PATTERN = (1 << 5)

ClCpmNodeEventT = saAis.SaInt32T
class eClCpmNodeEventT(clUtils.CEnum):
    CL_CPM_NODE_ARRIVAL = 1,
    CL_CPM_NODE_DEPARTURE = 2,
    CL_CPM_NODE_DEATH = 3

ClCpmCompEventT = saAis.SaInt32T
class eClCpmCompEventT(clUtils.CEnum):
    CL_CPM_COMP_ARRIVAL = 1,
    CL_CPM_COMP_DEPARTURE = 2,
    CL_CPM_COMP_DEATH = 3

def ClCpmCompEventT2Str(x):
    if x == eClCpmCompEventT.CL_CPM_COMP_ARRIVAL:
        return "CL_CPM_COMP_ARRIVAL"
    elif x == eClCpmCompEventT.CL_CPM_COMP_DEPARTURE:
        return "CL_CPM_COMP_DEPARTURE"
    elif x == eClCpmCompEventT.CL_CPM_COMP_DEATH:
        return "CL_CPM_COMP_DEATH"
    else:
        return "Invalid"

def ClHaState2Str(S):
    if S == saAmf.eSaAmfHAStateT.SA_AMF_HA_ACTIVE:
        return "Active"
    elif S == saAmf.eSaAmfHAStateT.SA_AMF_HA_STANDBY:
        return "Standby"
    elif S == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCED:
        return "Quiesced"
    elif S == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCING:
        return "Quiescing"
    else:
        return "Unknown"

class ClCpmEventPayLoadT(ctypes.Structure):
    _fields_ = [
        ("compName", clCommon.ClNameT),
        ("nodeName", clCommon.ClNameT),
        ("compId", clCommon.ClUint32T),
        ("eoId", clEoConfigApi.ClEoIdT),
        ("nodeIocAddress", clIocApi.ClIocNodeAddressT),
        ("eoIocPort", clIocApi.ClIocNodeAddressT),
    ]

class ClCpmEventNodePayLoadT(ctypes.Structure):
    _fields_ = [
        ("nodeName", clCommon.ClNameT),
        ("nodeIocAddress", clIocApi.ClIocNodeAddressT),
        ("operation", ClCpmNodeEventT),
    ]

class ClCpmCompCSIT(ctypes.Structure):
    _fields_ = [
        ("haState", clAmsTypes.ClAmsHAStateT),
        ("csiDescriptor", clAmsTypes.ClAmsCSIDescriptorT)
    ]

class ClCpmCompCSIRefT(ctypes.Structure):
    _fields_ = [
        ("numCSIs", clCommon.ClUint32T),
        ("pCSIList", ctypes.POINTER(ClCpmCompCSIT))
    ]

class ClCpmCompSpecInfoT(ctypes.Structure):
    _fields_ = [
        ("numArgs", clCommon.ClUint32T),
        ("args", ctypes.POINTER(ctypes.c_char_p)),
        ("period", clCommon.ClUint32T),
        ("maxDuration", clCommon.ClUint32T),
        ("recovery", clAmsTypes.ClAmsLocalRecoveryT)
    ]

ClCpmHealthCheckCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, clCommon.ClInvocationT, ctypes.POINTER(clCommon.ClNameT), ctypes.POINTER(clAmsTypes.ClAmsCompHealthcheckKeyT))

ClCpmTerminateCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, clCommon.ClInvocationT, ctypes.POINTER(clCommon.ClNameT))

ClCpmCSISetCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, clCommon.ClInvocationT, ctypes.POINTER(clCommon.ClNameT), clAmsTypes.ClAmsHAStateT, clAmsTypes.ClAmsCSIDescriptorT)

ClCpmCSIRmvCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, clCommon.ClInvocationT, ctypes.POINTER(clCommon.ClNameT), ctypes.POINTER(clCommon.ClNameT), clAmsTypes.ClAmsCSIFlagsT)

ClCpmProtectionGroupTrackCallbackT = ctypes.CFUNCTYPE(None, ctypes.POINTER(clCommon.ClNameT), ctypes.POINTER(clAmsTypes.ClAmsPGNotificationBufferT), clCommon.ClUint32T, clCommon.ClUint32T)

ClCpmProxiedComponentInstantiateCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, clCommon.ClInvocationT, ctypes.POINTER(clCommon.ClNameT))

ClCpmProxiedComponentCleanupCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, clCommon.ClInvocationT, ctypes.POINTER(clCommon.ClNameT))

ClCpmNotificationFuncT = ctypes.CFUNCTYPE(None, clIocApiExt.ClIocNotificationIdT, clCommon.ClPtrT, ctypes.POINTER(clIocApi.ClIocAddressT))

class ClCpmCallbacksT(ctypes.Structure):
    _fields_ = [
        ("appHealthCheck", ClCpmHealthCheckCallbackT),
        ("appTerminate", ClCpmTerminateCallbackT),
        ("appCSISet", ClCpmCSISetCallbackT),
        ("appCSIRmv", ClCpmCSIRmvCallbackT),
        ("appProtectionGroupTrack", ClCpmProtectionGroupTrackCallbackT),
        ("appProxiedComponentInstantiate", ClCpmProxiedComponentInstantiateCallbackT),
        ("appProxiedComponentCleanup", ClCpmProxiedComponentCleanupCallbackT),
    ]

def clCpmClientInitialize(pCpmHandle, pCallback, pVersion):
    """
    arg types:
        ClCpmHandleT *pCpmHandle,
        const ClCpmCallbacksT *pCallback,
        ClVersionT *pVersion

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmClientInitialize(pCpmHandle, pCallback, pVersion)

def clCpmClientFinalize(cpmHandle):
    """
    arg types:
        ClCpmHandleT cpmHandle

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmClientFinalize(cpmHandle)

def clCpmSelectionObjectGet(cpmHandle, pSelectionObject):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        ClSelectionObjectT *pSelectionObject

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmSelectionObjectGet(cpmHandle, pSelectionObject)

def clCpmDispatch(cpmHandle, dispatchFlags):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        ClDispatchFlagsT dispatchFlags

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmDispatch(cpmHandle, dispatchFlags)

def clCpmComponentRegister(cpmHandle, pCompName, pProxyCompName):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        const ClNameT *pCompName,
        const ClNameT *pProxyCompName

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentRegister(cpmHandle, pCompName, pProxyCompName)

def clCpmComponentUnregister(cpmHandle, pCompName, pProxyCompName):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        const ClNameT *pCompName,
        const ClNameT *pProxyCompName

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentUnregister(cpmHandle, pCompName, pProxyCompName)

def clCpmComponentNameGet(cpmHandle, pCompName):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        const ClNameT *pCompName,

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentNameGet(cpmHandle, pCompName)

def clCpmComponentDNNameGet(cpmHandle, pCompName, pDNName):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        const ClNameT *pCompName,
        const ClNameT *pDNName

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentDNNameGet(cpmHandle, pCompName, pDNName)

def clCpmResponse(cpmHandle, invocation, rc):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        ClInvocationT invocation,
        ClRcT rc

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmResponse(cpmHandle, invocation, rc)

def clCpmHAStateGet(cpmHandle, compName, csiName, haState):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        ClNameT *compName,
        ClNameT *csiName,
        ClAmsHAStateT *haState

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmHAStateGet(cpmHandle, compName, csiName, haState)

def clCpmCSIQuiescingComplete(cpmHandle, invocation, retCode):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        ClInvocationT invocation,
        ClRcT retCode

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmCSIQuiescingComplete(cpmHandle, invocation, retCode)

def clCpmComponentFailureReport(cpmHandle, pCompName, errorDetectionTime, recommendedRecovery, alarmHandle):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        const ClNameT *pCompName,
        ClTimeT errorDetectionTime,
        ClAmsLocalRecoveryT recommendedRecovery,
        ClUint32T alarmHandle

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentFailureReport(cpmHandle, pCompName, errorDetectionTime, recommendedRecovery, alarmHandle)

def clCpmComponentFailureClear(cpmHandle, pCompName):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        ClNameT *pCompName

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentFailureClear(cpmHandle, pCompName)

def clCpmHealthcheckStart(cpmHandle, pCompName, pCompHealthCheck, invocationType, recommondedRecovery):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        const ClNameT *pCompName,
        const ClAmsCompHealthcheckKeyT *pCompHealthCheck,
        ClAmsCompHealthcheckInvocationT invocationType,
        ClAmsRecoveryT recommondedRecovery

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmHealthcheckStart(cpmHandle, pCompName, pCompHealthCheck, invocationType, recommondedRecovery)

def clCpmHealthcheckConfirm(cpmHandle, pCompName, pCompHealthCheck, healthCheckResult):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        const ClNameT *pCompName,
        const ClAmsCompHealthcheckKeyT *pCompHealthCheck,
        ClRcT healthCheckResult

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmHealthcheckConfirm(cpmHandle, pCompName, pCompHealthCheck, healthCheckResult)

def clCpmHealthcheckStop(cpmHandle, pCompName, pCompHealthCheck):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        const ClNameT *pCompName,
        const ClAmsCompHealthcheckKeyT *pCompHealthCheck

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmHealthcheckStop(cpmHandle, pCompName, pCompHealthCheck)

def clCpmProtectionGroupTrack(cpmHandle, pCsiName, trackFlags, pNotificationBuffer):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        ClNameT *pCsiName,
        ClUint8T trackFlags,
        ClAmsPGNotificationBufferT *pNotificationBuffer

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmProtectionGroupTrack(cpmHandle, pCsiName, trackFlags, pNotificationBuffer)

def clCpmProtectionGroupTrackStop(cpmHandle, pCsiName):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        ClNameT *pCsiName

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmProtectionGroupTrackStop(cpmHandle, pCsiName)

def clCpmComponentIdGet(cpmHandle, pCompName, pCompId):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        ClNameT *pCompName,
        ClUint32T *pCompId

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentIdGet(cpmHandle, pCompName, pCompId)

def clCpmComponentAddressGet(nodeAddress, pCompName, pCompAddress):
    """
    arg types:
        ClIocNodeAddressT nodeAddress,
        ClNameT *pCompName,
        ClIocAddressT *pCompAddress

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentAddressGet(nodeAddress, pCompName, pCompAddress)

def clCpmComponentAddressGetFast(nodeAddress, pCompName, pCompAddress):
    """
    arg types:
        ClIocNodeAddressT nodeAddress,
        ClNameT *pCompName,
        ClIocAddressT *pCompAddress

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentAddressGetFast(nodeAddress, pCompName, pCompAddress)

def clCpmComponentStatusGet(pCompName, pNodeName, pPresenceState, pOperationalState):
    """
    arg types:
        ClNameT *pCompName,
        ClNameT *pNodeName,
        ClAmsPresenceStateT *pPresenceState,
        ClAmsOperStateT *pOperationalState

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentStatusGet(pCompName, pNodeName, pPresenceState, pOperationalState)

def clCpmMasterAddressGet(pIocAddress):
    """
    arg types:
        ClIocNodeAddressT *pIocAddress

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmMasterAddressGet(pIocAddress)

def clCpmMasterAddressGetExtended(pIocAddress, numRetries, pDelay):
    """
    arg types:
        ClIocNodeAddressT *pIocAddress,
        ClInt32T numRetries, 
        ClTimerTimeOutT *pDelay

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmMasterAddressGetExtended(pIocAddress, numRetries, pDelay)

def clCpmIsMaster():
    """
    return type:
        ClUint32T
    """
    return clLib.libmw_so.clCpmIsMaster()

def clCpmNodeShutDown(iocNodeAddress):
    """
    arg types:
        ClIocNodeAddressT iocNodeAddress

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmNodeShutDown(iocNodeAddress)

def clCpmNodeRestart(iocNodeAddress, graceful):
    """
    arg types:
        ClIocNodeAddressT iocNodeAddress,
        ClBoolT graceful

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmNodeRestart(iocNodeAddress, graceful)

def clCpmNodeSwitchover(iocNodeAddress):
    """
    arg types:
        ClIocNodeAddressT iocNodeAddress

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmNodeSwitchover(iocNodeAddress)

def clCpmMiddlewareRestart(iocNodeAddress, graceful, nodeReset):
    """
    arg types:
        ClIocNodeAddressT iocNodeAddress,
        ClBoolT graceful,
        ClBoolT nodeReset

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmMiddlewareRestart(iocNodeAddress, graceful, nodeReset)

def clCpmLocalNodeNameGet(nodeName):
    """
    arg types:
        ClNameT *nodeName

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmLocalNodeNameGet(nodeName)

def clCpmCompStatusGet(compAddr, pStatus):
    """
    arg types:
        ClIocAddressT compAddr,
        ClStatusT *pStatus

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmCompStatusGet(compAddr, pStatus)

def clCpmNodeStatusGet(nodeAddr, pStatus):
    """
    arg types:
        ClIocNodeAddressT nodeAddr,
        ClStatusT *pStatus

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmNodeStatusGet(nodeAddr, pStatus)

def clCpmNotificationCallbackInstall(compAddr, pFunc, pArg, pHandle):
    """
    arg types:
        ClIocPhysicalAddressT compAddr,
        ClCpmNotificationFuncT pFunc,
        ClPtrT pArg,
        ClHandleT *pHandle

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmNotificationCallbackInstall(compAddr, pFunc, pArg, pHandle)

def clCpmNotificationCallbackUninstall(pHandle):
    """
    arg types:
        ClHandleT *pHandle

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmNotificationCallbackUninstall(pHandle)

def clCpmCompCSIList(pCompName, pCSIRef):
    """
    arg types:
        const ClNameT *pCompName,
        ClCpmCompCSIRefT *pCSIRef

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmCompCSIList(pCompName, pCSIRef)

def clCpmIsSC():
    """
    return type:
        ClBoolT
    """
    return clLib.libmw_so.clCpmIsSC()

def clCpmCompInfoGet(pCompName, nodeAddress, compInfo):
    """
    arg types:
        const ClNameT *compName,
        const ClIocNodeAddressT nodeAddress,
        ClCpmCompSpecInfoT *compInfo

    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmCompInfoGet(pCompName, nodeAddress, compInfo)

clCpmHandle = ClCpmHandleT.in_dll(clLib.libmw_so, "clCpmHandle")
