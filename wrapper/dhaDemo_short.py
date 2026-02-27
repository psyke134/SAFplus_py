#!/usr/bin/env python3
from amf import saAmf
from utils import clLib
import ctypes

from amf.saAmf import eSaAmfHAStateT, SaAmfHandleT, SaAmfCallbacksT, SaAmfHealthcheckCallbackT,\
    SaAmfComponentTerminateCallbackT, SaAmfCSISetCallbackT, SaAmfCSIRemoveCallbackT, SaAmfProtectionGroupTrackCallbackT,\
    saAmfInitialize, saAmfSelectionObjectGet, saAmfComponentNameGet, saAmfComponentRegister, saAmfDispatch, saAmfFinalize,\
    saAmfComponentUnregister, saAmfResponse, saAmfCSIQuiescingComplete
from amf.clAmsUtils import CL_AMS_STRING_CSI_FLAGS, CL_AMS_STRING_H_STATE
from amf.clAmsTypes import ClAmsMgmtHandleT, ClAmsMgmtCCBHandleT
from common.saAis import SaNameT, SaVersionT, eSaAisErrorT, SaSelectionObjectT, eSaDispatchFlagsT
from common.clCommon import ClHandleT, ClVersionT, CL_TRUE, CL_FALSE
from common import clCommonErrors
from log.clLogApi import clLogMsgWrite, CL_LOG_AREA_UNSPECIFIED, CL_LOG_CONTEXT_UNSPECIFIED, eClLogSeverityT
from utils.clUtils import getCallerInfo
from utils.libc import fd_set, getpid, FD_ZERO, FD_SET, select, errno
from utils import clHandleApi
from ioc.clIocApi import ClIocPortT, clIocLocalAddressGet
from eo.clEoApi import clEoMyEoIocPortGet
from osal.clOsalApi import eClOsalSchedulePolicyT, eClOsalThreadPriorityT, CL_OSAL_MIN_STACK_SIZE, clOsalTaskCreateDetached

import dhaDemoOps_short

CL_LOG_HANDLE_APP = ClHandleT.in_dll(clLib.libmw_so, "CL_LOG_HANDLE_APP")

def clprintf(severity, fmtString, *va_args):
    _, fileName, loc = getCallerInfo()

    clLogMsgWrite(
        CL_LOG_HANDLE_APP,
        severity,
        10,
        CL_LOG_AREA_UNSPECIFIED,
        CL_LOG_CONTEXT_UNSPECIFIED,
        fileName,
        loc,
        fmtString,
        *va_args
    )

pid_t = ctypes.c_int

mypid = pid_t(0)
amfHandle = SaAmfHandleT(0)
appName = SaNameT("")

unblockNow = CL_FALSE


def main():
    callbacks = SaAmfCallbacksT()
    version = SaVersionT('B', 1, 1)
    iocPort = ClIocPortT(0)
    rc = eSaAisErrorT.SA_AIS_OK

    dispatch_fd = SaSelectionObjectT(0)
    read_fds = fd_set()

    global mypid
    global amfHandle
    global appName
    mypid = getpid()

    callbacks.saAmfHealthcheckCallback          = SaAmfHealthcheckCallbackT() # NULL
    callbacks.saAmfComponentTerminateCallback   = SaAmfComponentTerminateCallbackT(clCompAppTerminate)
    callbacks.saAmfCSISetCallback               = SaAmfCSISetCallbackT(clCompAppAMFCSISet)
    callbacks.saAmfCSIRemoveCallback            = SaAmfCSIRemoveCallbackT(clCompAppAMFCSIRemove)
    callbacks.saAmfProtectionGroupTrackCallback = SaAmfProtectionGroupTrackCallbackT() # NULL

    rc = saAmfInitialize(amfHandle, callbacks, version)

    if rc != eSaAisErrorT.SA_AIS_OK:
        errorexit(rc)

    FD_ZERO(read_fds)

    rc = saAmfSelectionObjectGet(amfHandle, dispatch_fd)

    if rc != eSaAisErrorT.SA_AIS_OK:
        errorexit(rc)

    FD_SET(dispatch_fd, read_fds)

    rc = saAmfComponentNameGet(amfHandle, appName)
    if rc != eSaAisErrorT.SA_AIS_OK:
        errorexit(rc)

    rc = saAmfComponentRegister(amfHandle, appName, None)
    if rc != eSaAisErrorT.SA_AIS_OK:
        errorexit(rc)

    rc = clEoMyEoIocPortGet(iocPort)

    clprintf(eClLogSeverityT.CL_LOG_SEV_INFO, "Component [%.*s] : PID [%d]. Initializing\n", appName.length, appName.__str__(), mypid)
    clprintf(eClLogSeverityT.CL_LOG_SEV_INFO, "   IOC Address             : 0x%x\n", clIocLocalAddressGet())
    clprintf(eClLogSeverityT.CL_LOG_SEV_INFO, "   IOC Port                : 0x%x\n", iocPort)

    EINTR = 4   # Interrupted system call
    while(not unblockNow):
        if select(dispatch_fd + 1, read_fds, None, None, None) < 0:
            if errno() == EINTR:
                continue
            clprintf(eClLogSeverityT.CL_LOG_SEV_ERROR, "Error in select()")
            break
        saAmfDispatch(amfHandle, eSaDispatchFlagsT.SA_DISPATCH_ALL)

    rc = saAmfFinalize(amfHandle)
    if rc != eSaAisErrorT.SA_AIS_OK:
        clprintf(eClLogSeverityT.CL_LOG_SEV_ERROR, "AMF finalization error[0x%X]", rc)
    clprintf (eClLogSeverityT.CL_LOG_SEV_INFO, "AMF Finalized")

def errorexit(rc):
    clprintf(eClLogSeverityT.CL_LOG_SEV_ERROR, "Component [%.*s] : PID [%d]. Initialization error [0x%x]\n", appName.length, appName.__str__(), mypid, rc)
    exit()

def clCompAppTerminate(invocation, compName):
    invocation = ctypes.c_ulonglong(invocation)
    rc = eSaAisErrorT.SA_AIS_OK

    clprintf(
        eClLogSeverityT.CL_LOG_SEV_INFO,
        "Component [%.*s] : PID [%d]. Terminating\n",
        compName.contents.length, compName.contents.__str__(), mypid
    )

    rc = saAmfComponentUnregister(amfHandle, compName.contents, None)
    if rc != eSaAisErrorT.SA_AIS_OK:
        clprintf(
            eClLogSeverityT.CL_LOG_SEV_ERROR,
            "Component [%.*s] : PID [%d]. Termination error [0x%x]\n",
            compName.contents.length, compName.contents.__str__(), mypid, rc
        )
        return
    
    saAmfResponse(amfHandle, invocation, eSaAisErrorT.SA_AIS_OK)

    clprintf(
        eClLogSeverityT.CL_LOG_SEV_INFO,
        "Component [%.*s] : PID [%d]. Terminated\n",
        compName.contents.length, compName.contents.__str__(), mypid
    )
    
    global unblockNow
    unblockNow = CL_TRUE

def clCompAppAMFCSISet(invocation, compName, haState, csiDescriptor):
    invocation = ctypes.c_ulonglong(invocation)

    clprintf(
        eClLogSeverityT.CL_LOG_SEV_INFO,
        "Component [%.*s] : PID [%d]. CSI Set Received\n",
        compName.contents.length, compName.contents.__str__(), mypid
    )

    clCompAppAMFPrintCSI(csiDescriptor, haState)

    if haState == eSaAmfHAStateT.SA_AMF_HA_ACTIVE:
        dhaDemoOps_short.dhaInfoPrint("Starting dynamic HA demo.")
        dhaDemoOps_short.dhaInfoPrint("It will create 2N SG : %sSG", dhaDemoOps_short.BASE_NAME)
        rc = clDhaDemoStart()
        if rc != clCommonErrors.CL_OK:
            dhaDemoOps_short.dhaErrorPrint("Failed to start dynamic HA demo.")

        saAmfResponse(amfHandle, invocation, eSaAisErrorT.SA_AIS_OK)
    elif haState == eSaAmfHAStateT.SA_AMF_HA_STANDBY:
        saAmfResponse(amfHandle, invocation, eSaAisErrorT.SA_AIS_OK)
    elif haState == eSaAmfHAStateT.SA_AMF_HA_QUIESCED:
        rc = clDhaDemoStop()
        if rc != clCommonErrors.CL_OK:
            dhaDemoOps_short.dhaErrorPrint("Failed to stop dynamic HA demo.")

        saAmfResponse(amfHandle, invocation, eSaAisErrorT.SA_AIS_OK)
    elif haState == eSaAmfHAStateT.SA_AMF_HA_QUIESCING:
        saAmfCSIQuiescingComplete(amfHandle, invocation, eSaAisErrorT.SA_AIS_OK)
    else:
        exit(0)

def clCompAppAMFCSIRemove(invocation, compName, csiName, csiFlags):
    invocation = ctypes.c_ulonglong(invocation)
    clprintf(
        eClLogSeverityT.CL_LOG_SEV_INFO,
        "Component [%.*s] : PID [%d]. CSI Remove Received\n",
        compName.contents.length, compName.contents.__str__(), mypid
    )
    clprintf(
        eClLogSeverityT.CL_LOG_SEV_INFO,
        "   CSI                     : %.*s\n",
        csiName.contents.length, csiName.contents.__str__()
    )
    clprintf(
        eClLogSeverityT.CL_LOG_SEV_INFO,
        "   CSI Flags               : 0x%d\n",
        csiFlags
    )

    saAmfResponse(amfHandle, invocation, eSaAisErrorT.SA_AIS_OK)

def clCompAppAMFPrintCSI(csiDescriptor, haState):
    clprintf(
        eClLogSeverityT.CL_LOG_SEV_INFO,
        "CSI Flags : [%s]",
        CL_AMS_STRING_CSI_FLAGS(csiDescriptor.csiFlags)
    )

    if csiDescriptor.csiFlags != saAmf.SA_AMF_CSI_TARGET_ALL:
        clprintf(
            eClLogSeverityT.CL_LOG_SEV_INFO,
            "CSI Name : [%s]",
            csiDescriptor.csiName.__str__()
        )

    if csiDescriptor.csiFlags == saAmf.SA_AMF_CSI_ADD_ONE:
        clprintf(
            eClLogSeverityT.CL_LOG_SEV_INFO,
            "Name value pairs :"
        )
        for i in range(0, csiDescriptor.csiAttr.number):
            clprintf(
                eClLogSeverityT.CL_LOG_SEV_INFO,
                "Name : [%s]",
                csiDescriptor.csiAttr.attr[i].attrName
            )
            clprintf(
                eClLogSeverityT.CL_LOG_SEV_INFO,
                "Value : [%s]",
                csiDescriptor.csiAttr.attr[i].attrValue
            )

    clprintf(
        eClLogSeverityT.CL_LOG_SEV_INFO,
        "HA state : [%s]",
        CL_AMS_STRING_H_STATE(haState)
    )

    if haState == eSaAmfHAStateT.SA_AMF_HA_ACTIVE:
        clprintf(
            eClLogSeverityT.CL_LOG_SEV_INFO,
            "Active Descriptor :"
        )
        clprintf(
            eClLogSeverityT.CL_LOG_SEV_INFO,
            "Transition Descriptor : [%d]",
            csiDescriptor.csiStateDescriptor.activeDescriptor.transitionDescriptor
        )
        clprintf(
            eClLogSeverityT.CL_LOG_SEV_INFO,
            "Active Component : [%s]",
            csiDescriptor.csiStateDescriptor.activeDescriptor.activeCompName.__str__()
        )
    elif haState == eSaAmfHAStateT.SA_AMF_HA_STANDBY:
        clprintf(
            eClLogSeverityT.CL_LOG_SEV_INFO,
            "Standby Descriptor :"
        )
        clprintf(
            eClLogSeverityT.CL_LOG_SEV_INFO,
            "Standby Rank : [%d]",
            csiDescriptor.csiStateDescriptor.standbyDescriptor.standbyRank
        )
        clprintf(
            eClLogSeverityT.CL_LOG_SEV_INFO,
            "Active Component : [%s]",
            csiDescriptor.csiStateDescriptor.standbyDescriptor.activeCompName.__str__()
        )

def clDhaDemoCreate(arg):
    mgmtHandle = ClAmsMgmtHandleT(0)
    ccbHandle = ClAmsMgmtCCBHandleT(clHandleApi.CL_HANDLE_INVALID_VALUE)
    pBaseName = dhaDemoOps_short.BASE_NAME

    version = ClVersionT()
    version.releaseCode = ord('B')
    version.majorVersion = 0x1
    version.minorVersion = 0x1

    rc = dhaDemoOps_short.dhaMgmtInit(mgmtHandle, version)
    if rc != clCommonErrors.CL_OK: return None
    rc = dhaDemoOps_short.dhaMgmtCcbInit(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    rc = dhaDemoOps_short.dhaSgCheck(mgmtHandle)
    if rc == clCommonErrors.CL_OK:
        dhaDemoOps_short.dhaInfoPrint("Not creating SG[%sSG], it already exist", pBaseName)
        dhaDemoOps_short.dhaCleanUp(mgmtHandle, ccbHandle)
        return None
    
    dhaDemoOps_short.dhaInfoPrint("Creating 2N SG [%sSG] and other entities(si, csi, su, comp, etc)", pBaseName)

    rc = dhaDemoOps_short.dhaSgCreate(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    rc = dhaDemoOps_short.dhaSiCreate(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    rc = dhaDemoOps_short.dhaCsiCreate(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    for idx in range(0, 2):
        rc = dhaDemoOps_short.dhaSuCreate(mgmtHandle, ccbHandle, idx)
        if rc != clCommonErrors.CL_OK: return None

    for idx in range(0, 2):
        rc = dhaDemoOps_short.dhaCompCreate(mgmtHandle, ccbHandle, idx)
        if rc != clCommonErrors.CL_OK: return None

    rc = dhaDemoOps_short.dhaCommit(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    dhaDemoOps_short.dhaInfoPrint("Fill SG config")
    rc = dhaDemoOps_short.dhaSgConfigFill(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    dhaDemoOps_short.dhaInfoPrint("Fill SI config")
    rc = dhaDemoOps_short.dhaSiConfigFill(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    dhaDemoOps_short.dhaInfoPrint("Fill CSI config")
    rc = dhaDemoOps_short.dhaCsiConfigFill(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    dhaDemoOps_short.dhaInfoPrint("Fill SU config")
    rc = dhaDemoOps_short.dhaSuConfigFill(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    dhaDemoOps_short.dhaInfoPrint("Fill NODE config")
    rc = dhaDemoOps_short.dhaNodeConfigFill(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    dhaDemoOps_short.dhaInfoPrint("Fill COMP config")
    rc = dhaDemoOps_short.dhaCompConfigFill(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    dhaDemoOps_short.dhaInfoPrint("Unlock AMS entities")
    rc = dhaDemoOps_short.dhaEntitiesUnlock(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    dhaDemoOps_short.dhaCleanUp(mgmtHandle, ccbHandle)
    return None

_TaskRoutineT = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)
demoCreateRoutine = _TaskRoutineT(clDhaDemoCreate)
def clDhaDemoStart():
    rc = clOsalTaskCreateDetached(
        "dhaDemoCreate",
        eClOsalSchedulePolicyT.CL_OSAL_SCHED_OTHER,
        eClOsalThreadPriorityT.CL_OSAL_THREAD_PRI_NOT_APPLICABLE,
        CL_OSAL_MIN_STACK_SIZE,
        demoCreateRoutine,
        None
    )
    return rc

def clDhaDemoDelete(arg):
    mgmtHandle = ClAmsMgmtHandleT(0)
    ccbHandle = ClAmsMgmtCCBHandleT(clHandleApi.CL_HANDLE_INVALID_VALUE)
    pBaseName = dhaDemoOps_short.BASE_NAME

    version = ClVersionT()
    version.releaseCode = ord('B')
    version.majorVersion = 0x1
    version.minorVersion = 0x1

    rc = dhaDemoOps_short.dhaMgmtInit(mgmtHandle, version)
    if rc != clCommonErrors.CL_OK: return None
    rc = dhaDemoOps_short.dhaMgmtCcbInit(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    rc = dhaDemoOps_short.dhaSgCheck(mgmtHandle)
    if rc != clCommonErrors.CL_OK:
        dhaDemoOps_short.dhaInfoPrint("Not deleting SG[%sSG], it doesn't exist", pBaseName)
        dhaDemoOps_short.dhaCleanUp(mgmtHandle, ccbHandle)
        return None
    
    dhaDemoOps_short.dhaInfoPrint("Deleting SG [%sSG] and other entities(si, csi, su, comp, etc)", pBaseName)

    rc = dhaDemoOps_short.dhaEntitiesLockI(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    for idx in range(0, 2):
        rc = dhaDemoOps_short.dhaCompDelete(mgmtHandle, ccbHandle, idx)
        if rc != clCommonErrors.CL_OK: return None

    for idx in range(0, 2):
        rc = dhaDemoOps_short.dhaSuDelete(mgmtHandle, ccbHandle, idx)
        if rc != clCommonErrors.CL_OK: return None

    rc = dhaDemoOps_short.dhaCsiDelete(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    rc = dhaDemoOps_short.dhaSiDelete(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    rc = dhaDemoOps_short.dhaSgDelete(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    rc = dhaDemoOps_short.dhaCommit(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return None

    dhaDemoOps_short.dhaCleanUp(mgmtHandle, ccbHandle)
    return None

demoDeleteRoutine = _TaskRoutineT(clDhaDemoDelete)
def clDhaDemoStop():
    rc = clOsalTaskCreateDetached(
        "dhaDemoDelete",
        eClOsalSchedulePolicyT.CL_OSAL_SCHED_OTHER,
        eClOsalThreadPriorityT.CL_OSAL_THREAD_PRI_NOT_APPLICABLE,
        CL_OSAL_MIN_STACK_SIZE,
        demoDeleteRoutine,
        None
    )
    return rc

if __name__ == "__main__":
    main()
