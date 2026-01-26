#!/usr/bin/env python3
from amf import saAmf, clCpmApi, clAmsClientNotification, clAmsUtils
from common import saAis, clCommon, clCommonErrors
from log import clLogApi
from utils import clUtils, clLib, libc
from ioc import clIocApi
from eo import clEoApi, clEoConfigApi
from osal import clOsalApi
import ctypes

CL_LOG_HANDLE_APP = clCommon.ClHandleT.in_dll(clLib.libmw_so, "CL_LOG_HANDLE_APP")

def STRING_HA_STATE(S):
    if S == saAmf.eSaAmfHAStateT.SA_AMF_HA_ACTIVE.value: return "Active"
    elif S == saAmf.eSaAmfHAStateT.SA_AMF_HA_STANDBY.value: return "Standby"
    elif S == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCED.value: return "Quiesced"
    elif S == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCING.value: return "Quiescing"
    else: return "Uknown"

def STRING_CSI_FLAGS(S):
    if S & saAmf.SA_AMF_CSI_ADD_ONE: return "Add One"
    elif S & saAmf.SA_AMF_CSI_TARGET_ONE: return "Target One"
    elif S & saAmf.SA_AMF_CSI_TARGET_ALL: return "Target All"
    else: return "Uknown"

def clprintf(severity, fmtString, *va_args):
    _, fileName, loc = clUtils.getCallerInfo()

    clLogApi.clLogMsgWrite(
        CL_LOG_HANDLE_APP,
        severity,
        10,
        clLogApi.CL_LOG_AREA_UNSPECIFIED,
        clLogApi.CL_LOG_CONTEXT_UNSPECIFIED,
        fileName,
        loc,
        fmtString,
        *va_args
    )

############################################################################
#   Component configs.
############################################################################

COMP_NAME                   = "SAFComponent0"
COMP_EO_NAME                = "SAFComponent0_EO"
COMP_EO_THREAD_PRIORITY     = clOsalApi.eClOsalThreadPriorityT.CL_OSAL_THREAD_PRI_MEDIUM
COMP_EO_NUM_THREAD          = 2
COMP_IOC_PORT               = 0
COMP_EO_USER_CLIENT_ID      = clCommon.ClUint32T(clEoApi.CL_EO_USER_CLIENT_ID_START)
COMP_EO_USE_THREAD_MODEL    = clEoConfigApi.eClEoApplicationTypeT.CL_EO_USE_THREAD_FOR_RECV

NULL_EO_CREATE_CALLOUT  = clEoConfigApi.ClEoAppCreateCallbackT()     # no arg = NULL, calling will cause seg fault
NULL_EO_DELETE_CALLOUT  = clEoConfigApi.ClEoAppDeleteCallbackT()
NULL_EO_ST_CHG_CALLOUT  = clEoConfigApi.ClEoAppStateChgCallbackT()
NULL_EO_HP_CHK_CALLOUT  = clEoConfigApi.ClEoAppHealthCheckCallbackT()
NULL_EO_CTM_ACT         = clEoConfigApi.ClEoCustomActionT()

# Component EO Basic Libraries
COMP_EO_BASICLIB_OSAL   = clCommon.CL_TRUE
COMP_EO_BASICLIB_TIMER  = clCommon.CL_TRUE
COMP_EO_BASICLIB_BUFFER = clCommon.CL_TRUE
COMP_EO_BASICLIB_IOC    = clCommon.CL_TRUE
COMP_EO_BASICLIB_RMD    = clCommon.CL_TRUE
COMP_EO_BASICLIB_EO     = clCommon.CL_TRUE
COMP_EO_BASICLIB_OM     = clCommon.CL_FALSE
COMP_EO_BASICLIB_HAL    = clCommon.CL_FALSE
COMP_EO_BASICLIB_DBAL   = clCommon.CL_FALSE

# Component EO Client Libraries
COMP_EO_CLIENTLIB_COR   = clCommon.CL_TRUE
COMP_EO_CLIENTLIB_CM    = clCommon.CL_FALSE                  
COMP_EO_CLIENTLIB_NAME  = clCommon.CL_TRUE                  
COMP_EO_CLIENTLIB_LOG   = clCommon.CL_TRUE                  
COMP_EO_CLIENTLIB_TRACE = clCommon.CL_FALSE                 
COMP_EO_CLIENTLIB_DIAG  = clCommon.CL_FALSE
COMP_EO_CLIENTLIB_TXN   = clCommon.CL_TRUE
COMP_EO_CLIENTLIB_MSO   = clCommon.CL_FALSE
COMP_EO_CLIENTLIB_PROV  = clCommon.CL_FALSE
COMP_EO_CLIENTLIB_ALARM = clCommon.CL_FALSE
COMP_EO_CLIENTLIB_DEBUG = clCommon.CL_TRUE
COMP_EO_CLIENTLIB_GMS   = clCommon.CL_FALSE
COMP_EO_CLIENTLIB_PM    = clCommon.CL_FALSE

# EO config variables
#clEoConfig      = clEoConfigApi.ClEoConfigT.in_dll(clLib.libmw_so, "clEoConfig")
#clEoBasicLibs   = clEoConfigApi._clEoBasicLibArray.in_dll(clLib.libmw_so, "clEoBasicLibs")
#clEoClientLibs  = clEoConfigApi._clEoClientLibArray.in_dll(clLib.libmw_so, "clEoClientLibs")

# Description of this EO
#clEoConfig.EOname                   = COMP_EO_NAME.encode("utf-8")  # EO Name
#clEoConfig.pri                      = COMP_EO_THREAD_PRIORITY       # EO Thread Priority
#clEoConfig.noOfThreads              = COMP_EO_NUM_THREAD            # No of EO thread needed
#clEoConfig.reqIocPort               = COMP_IOC_PORT                 # Required Ioc Port
#clEoConfig.maxNoClients             = COMP_EO_USER_CLIENT_ID
#clEoConfig.appType                  = COMP_EO_USE_THREAD_MODEL      # Thread Model
#clEoConfig.clEoCreateCallout        = NULL_EO_CREATE_CALLOUT        # Application Initialize Callback
#clEoConfig.clEoDeleteCallout        = NULL_EO_DELETE_CALLOUT        # Application Terminate Callback
#clEoConfig.clEoStateChgCallout      = NULL_EO_ST_CHG_CALLOUT        # Application State Change Callback
#clEoConfig.clEoHealthCheckCallout   = NULL_EO_HP_CHK_CALLOUT        # Application Health Check Callback
#clEoConfig.clEoCustomAction         = NULL_EO_CTM_ACT
#clEoConfig.needSerialization        = clCommon.CL_FALSE

# Basic libraries used by this EO. The first 6 libraries are
# mandatory, the others can be enabled or disabled by setting to
# CL_TRUE or CL_FALSE.
#clEoBasicLibs[0] = COMP_EO_BASICLIB_OSAL    #Lib: Operating System Adaptation Layer
#clEoBasicLibs[1] = COMP_EO_BASICLIB_TIMER   #Lib: Timer
#clEoBasicLibs[2] = COMP_EO_BASICLIB_BUFFER  #Lib: Buffer Management
#clEoBasicLibs[3] = COMP_EO_BASICLIB_IOC     #Lib: Intelligent Object Communication
#clEoBasicLibs[4] = COMP_EO_BASICLIB_RMD     #Lib: Remote Method Dispatch
#clEoBasicLibs[5] = COMP_EO_BASICLIB_EO      #Lib: Execution Object
#clEoBasicLibs[6] = COMP_EO_BASICLIB_OM      #Lib: Object Management
#clEoBasicLibs[7] = COMP_EO_BASICLIB_HAL     #Lib: Hardware Adaptation Layer
#clEoBasicLibs[8] = COMP_EO_BASICLIB_DBAL    #Lib: Database Adaptation Layer

# Client libraries used by this EO. All are optional and can be
# enabled or disabled by setting to CL_TRUE or CL_FALSE.
#clEoClientLibs[0] = COMP_EO_CLIENTLIB_COR       #Lib: Common Object Repository
#clEoClientLibs[1] = COMP_EO_CLIENTLIB_CM        #Lib: Chassis Management
#clEoClientLibs[2] = COMP_EO_CLIENTLIB_NAME      #Lib: Name Service
#clEoClientLibs[3] = COMP_EO_CLIENTLIB_LOG       #Lib: Log Service
#clEoClientLibs[4] = COMP_EO_CLIENTLIB_TRACE     #Lib: Trace Service
#clEoClientLibs[5] = COMP_EO_CLIENTLIB_DIAG      #Lib: Diagnostics
#clEoClientLibs[6] = COMP_EO_CLIENTLIB_TXN       #Lib: Transaction Management
#clEoClientLibs[7] = COMP_EO_CLIENTLIB_MSO       #Lib: MSO Management
#clEoClientLibs[8] = COMP_EO_CLIENTLIB_PROV      #Lib: Provisioning Management
#clEoClientLibs[9] = COMP_EO_CLIENTLIB_ALARM     #Lib: Alarm Management
#clEoClientLibs[10] = COMP_EO_CLIENTLIB_DEBUG    #Lib: Debug Service
#clEoClientLibs[11] = COMP_EO_CLIENTLIB_GMS      #Lib: Cluster/Group Membership Service
#clEoClientLibs[12] = COMP_EO_CLIENTLIB_PM       #Lib: PM Management

############################################################################
#   Global Variables.
############################################################################

pid_t = ctypes.c_int

mypid = pid_t(0)
amfHandle = saAmf.SaAmfHandleT(0)
appName = saAis.SaNameT("")

unblockNow = clCommon.CL_FALSE

#
#   Declare other global variables here.
#

############################################################################
#   Application Life Cycle Management Functions.
############################################################################

#
#   main
#   -------------------
#   This function is invoked when the application is to be initialized.
#

def main():
    callbacks = saAmf.SaAmfCallbacksT()
    version = saAis.SaVersionT()
    iocPort = clIocApi.ClIocPortT(0)
    rc = saAis.eSaAisErrorT.SA_AIS_OK

    dispatch_fd = saAis.SaSelectionObjectT(0)
    read_fds = libc.fd_set()

    #
    #   Declare other local variables here.
    #

    #
    #   Get the pid for the process and store it in global variable.
    #

    global mypid
    global amfHandle
    global appName
    mypid = libc.getpid()

    #
    # Initialize and register with CPM. 'version' specifies the
    # version of AMF with which this application would like to
    # interface. 'callbacks' is used to register the callbacks this
    # component expects to receive.
    #

    version.releaseCode  = ord('B')
    version.majorVersion = 1
    version.minorVersion = 1

    callbacks.saAmfHealthcheckCallback          = saAmf.SaAmfHealthcheckCallbackT() # NULL
    callbacks.saAmfComponentTerminateCallback   = saAmf.SaAmfComponentTerminateCallbackT(clCompAppTerminate)
    callbacks.saAmfCSISetCallback               = saAmf.SaAmfCSISetCallbackT(clCompAppAMFCSISet)
    callbacks.saAmfCSIRemoveCallback            = saAmf.SaAmfCSIRemoveCallbackT(clCompAppAMFCSIRemove)
    callbacks.saAmfProtectionGroupTrackCallback = saAmf.SaAmfProtectionGroupTrackCallbackT() # NULL

    #
    # Initialize AMF client library.
    #

    rc = saAmf.saAmfInitialize(
        ctypes.byref(amfHandle),
        ctypes.byref(callbacks),
        ctypes.byref(version)
    )

    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        errorexit(rc)

    libc.FD_ZERO(read_fds)

    rc = saAmf.saAmfSelectionObjectGet(
        amfHandle,
        ctypes.byref(dispatch_fd)
    )

    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        errorexit(rc)

    libc.FD_SET(dispatch_fd.value, read_fds)

    #
    # Do the application specific initialization here.
    #

    pycallback = clAmsClientNotification.ClAmsClientNotificationCallbackT(amsNotficationCallback)
    clAmsNotificationInitialize(pycallback)

    #
    # Now register the component with AMF. At this point it is
    # ready to provide service, i.e. take work assignments.
    #

    rc = saAmf.saAmfComponentNameGet(amfHandle, ctypes.byref(appName))
    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        errorexit(rc)

    rc = saAmf.saAmfComponentRegister(amfHandle, ctypes.byref(appName), None)
    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        errorexit(rc)

    #
    # Print out standard information for this component.
    #

    rc = clEoApi.clEoMyEoIocPortGet(ctypes.byref(iocPort))

    clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO, "Component [%.*s] : PID [%d]. Initializing\n", appName.length, appName.__str__(), mypid)
    clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO, "   IOC Address             : 0x%x\n", clIocApi.clIocLocalAddressGet())
    clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO, "   IOC Port                : 0x%x\n", iocPort)

    #
    # Block on AMF dispatch file descriptor for callbacks
    #
    EINTR = 4   # Interrupted system call
    while(not unblockNow):
        if libc.select(dispatch_fd.value + 1, ctypes.byref(read_fds), None, None, None) < 0:
            if libc.errno() == EINTR:
                continue
            clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR, "Error in select()")
            break
        saAmf.saAmfDispatch(amfHandle, saAis.eSaDispatchFlagsT.SA_DISPATCH_ALL)

    #
    # Do the application specific finalization here.
    #

    clAmsNotificationFinalize()

    rc = saAmf.saAmfFinalize(amfHandle)
    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR, "AMF finalization error[0x%X]", rc)
    clprintf (clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO, "AMF Finalized")

def errorexit(rc):
    clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR, "Component [%.*s] : PID [%d]. Initialization error [0x%x]\n", appName.length, appName.__str__(), mypid, rc)
    exit()

#
# clCompAppTerminate
# ------------------
# This function is invoked when the application is to be terminated.
#

def clCompAppTerminate(invocation, compName):
    invocation = ctypes.c_ulonglong(invocation)
    rc = saAis.eSaAisErrorT.SA_AIS_OK

    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "Component [%.*s] : PID [%d]. Terminating\n",
        compName.contents.length, compName.contents.__str__(), mypid
    )

    #
    # Unregister with AMF and respond to AMF saying whether the
    # termination was successful or not.
    #

    rc = saAmf.saAmfComponentUnregister(amfHandle, compName, None)
    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR,
            "Component [%.*s] : PID [%d]. Termination error [0x%x]\n",
            compName.contents.length, compName.contents.__str__(), mypid, rc
        )
        return
    
    saAmf.saAmfResponse(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)

    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "Component [%.*s] : PID [%d]. Terminated\n",
        compName.contents.length, compName.contents.__str__(), mypid
    )
    
    global unblockNow
    unblockNow = clCommon.CL_TRUE

############################################################################
#   Application Work Assignment Functions.
############################################################################

#
# clCompAppAMFCSISet
# ------------------
# This function is invoked when a CSI assignment is made or the state
# of a CSI is changed.
#

def clCompAppAMFCSISet(invocation, compName, haState, csiDescriptor):
    #
    # Print information about the CSI Set
    #
    invocation = ctypes.c_ulonglong(invocation)

    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "Component [%.*s] : PID [%d]. CSI Set Received\n",
        compName.contents.length, compName.contents.__str__(), mypid
    )

    clCompAppAMFPrintCSI(csiDescriptor, haState)

    #
    # Take appropriate action based on state
    #

    if haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_ACTIVE.value:
        #
        # AMF has requested application to take the active HA state 
        # for the CSI.
        #
        saAmf.saAmfResponse(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)
    elif haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_STANDBY.value:
        #
        # AMF has requested application to take the standby HA state 
        # for this CSI.
        #
        saAmf.saAmfResponse(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)
    elif haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCED.value:
        #
        # AMF has requested application to quiesce the CSI currently
        # assigned the active or quiescing HA state. The application 
        # must stop work associated with the CSI immediately.
        #
        saAmf.saAmfResponse(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)
    elif haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCING.value:
        #
        # AMF has requested application to quiesce the CSI currently
        # assigned the active HA state. The application must stop work
        # associated with the CSI gracefully and not accept any new
        # workloads while the work is being terminated.
        #
        saAmf.saAmfCSIQuiescingComplete(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)
    else:
        exit(0)

#
# clCompAppAMFCSIRemove
# ---------------------
# This function is invoked when a CSI assignment is to be removed.
#

def clCompAppAMFCSIRemove(invocation, compName, csiName, csiFlags):
    invocation = ctypes.c_ulonglong(invocation)
    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "Component [%.*s] : PID [%d]. CSI Remove Received\n",
        compName.contents.length, compName.contents.__str__(), mypid
    )
    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "   CSI                     : %.*s\n",
        csiName.contents.length, csiName.contents.__str__()
    )
    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "   CSI Flags               : 0x%d\n",
        csiFlags
    )

    #
    # Add application specific logic for removing the work for this CSI.
    #

    saAmf.saAmfResponse(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)

############################################################################
#   Utility functions .
############################################################################

#
# clCompAppAMFPrintCSI
# --------------------
# Print information received in a CSI set request.
#

def clCompAppAMFPrintCSI(csiDescriptor, haState):
    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "CSI Flags : [%s]",
        STRING_CSI_FLAGS(csiDescriptor.csiFlags)
    )

    if csiDescriptor.csiFlags != saAmf.SA_AMF_CSI_TARGET_ALL:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
            "CSI Name : [%s]",
            csiDescriptor.csiName.__str__()
        )

    if csiDescriptor.csiFlags == saAmf.SA_AMF_CSI_ADD_ONE:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
            "Name value pairs :"
        )
        for i in range(0, csiDescriptor.csiAttr.number):
            clprintf(
                clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
                "Name : [%s]",
                csiDescriptor.csiAttr.attr[i].attrName
            )
            clprintf(
                clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
                "Value : [%s]",
                csiDescriptor.csiAttr.attr[i].attrValue
            )

    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "HA state : [%s]",
        STRING_HA_STATE(haState)
    )

    if haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_ACTIVE.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
            "Active Descriptor :"
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
            "Transition Descriptor : [%d]",
            csiDescriptor.csiStateDescriptor.activeDescriptor.transitionDescriptor
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
            "Active Component : [%s]",
            csiDescriptor.csiStateDescriptor.activeDescriptor.activeCompName.__str__()
        )
    elif haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_STANDBY.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
            "Standby Descriptor :"
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
            "Standby Rank : [%d]",
            csiDescriptor.csiStateDescriptor.standbyDescriptor.standbyRank
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
            "Active Component : [%s]",
            csiDescriptor.csiStateDescriptor.standbyDescriptor.activeCompName.__str__()
        )

#
# Insert any other utility functions here.
#

def CL_AMS_STRING_NTF(S):
    if S == clAmsClientNotification.eClAmsNotificationTypeT.CL_AMS_NOTIFICATION_SI_PARTIALLY_ASSIGNED.value:
        return "partially assigned"
    elif S == clAmsClientNotification.eClAmsNotificationTypeT.CL_AMS_NOTIFICATION_SI_FULLY_ASSIGNED.value:
        return "fully assigned"
    elif S == clAmsClientNotification.eClAmsNotificationTypeT.CL_AMS_NOTIFICATION_SI_UNASSIGNED.value:
        return "unassigned"
    else:
        "unkown"

def amsNotficationCallback(notification):
    """
        ClAmsNotificationInfoT *notification
        return: ClRcT
    """

    ntfObj = notification.contents
    ntfType = ntfObj.type
    if (ntfType == clAmsClientNotification.eClAmsNotificationTypeT.CL_AMS_NOTIFICATION_SI_PARTIALLY_ASSIGNED.value
        or ntfType == clAmsClientNotification.eClAmsNotificationTypeT.CL_AMS_NOTIFICATION_SI_UNASSIGNED.value):
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "Received SI [%s] event",
            CL_AMS_STRING_NTF(ntfType)
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "SI name : [%.*s]",
            ntfObj.amsNotificationInfo.amsStateInfo.siName.length,
            ntfObj.amsNotificationInfo.amsStateInfo.siName.value,
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "SU name : [%.*s]",
            ntfObj.amsNotificationInfo.amsStateInfo.suName.length,
            ntfObj.amsNotificationInfo.amsStateInfo.suName.value,
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "Last HA State : [%s]",
            clAmsUtils.CL_AMS_STRING_H_STATE(ntfObj.amsNotificationInfo.amsStateInfo.lastHAState),
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "New HA State : [%s]",
            clAmsUtils.CL_AMS_STRING_H_STATE(ntfObj.amsNotificationInfo.amsStateInfo.newHAState),
        )
    elif ntfType == clAmsClientNotification.eClAmsNotificationTypeT.CL_AMS_NOTIFICATION_SU_HA_STATE_CHANGE.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "Received SU HA state change event"
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "SU name : [%.*s]",
            ntfObj.amsNotificationInfo.amsStateInfo.suName.length,
            ntfObj.amsNotificationInfo.amsStateInfo.suName.value,
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "SI name : [%.*s]",
            ntfObj.amsNotificationInfo.amsStateInfo.siName.length,
            ntfObj.amsNotificationInfo.amsStateInfo.siName.value,
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "Last HA State : [%s]",
            clAmsUtils.CL_AMS_STRING_H_STATE(ntfObj.amsNotificationInfo.amsStateInfo.lastHAState),
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "New HA State : [%s]",
            clAmsUtils.CL_AMS_STRING_H_STATE(ntfObj.amsNotificationInfo.amsStateInfo.newHAState),
        )
    elif ntfType == clAmsClientNotification.eClAmsNotificationTypeT.CL_AMS_NOTIFICATION_OPER_STATE_CHANGE.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "Received operational state [%s - %s] notification for type [%s] entity [%.*s]",
            clAmsUtils.CL_AMS_STRING_O_STATE(ntfObj.amsNotificationInfo.amsStateInfo.lastOperState),
            clAmsUtils.CL_AMS_STRING_O_STATE(ntfObj.amsNotificationInfo.amsStateInfo.newOperState),
            clAmsUtils.CL_AMS_STRING_ENTITY_TYPE(ntfObj.amsNotificationInfo.amsStateInfo.entityType),
            ntfObj.amsNotificationInfo.amsStateInfo.entityName.length,
            ntfObj.amsNotificationInfo.amsStateInfo.entityName.value,
        )
    elif ntfType == clAmsClientNotification.eClAmsNotificationTypeT.CL_AMS_NOTIFICATION_ADMIN_STATE_CHANGE.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "Received admin state [%s - %s] notification for type [%s] entity [%.*s]",
            clAmsUtils.CL_AMS_STRING_O_STATE(ntfObj.amsNotificationInfo.amsStateInfo.lastAdminState),
            clAmsUtils.CL_AMS_STRING_O_STATE(ntfObj.amsNotificationInfo.amsStateInfo.newAdminState),
            clAmsUtils.CL_AMS_STRING_ENTITY_TYPE(ntfObj.amsNotificationInfo.amsStateInfo.entityType),
            ntfObj.amsNotificationInfo.amsStateInfo.entityName.length,
            ntfObj.amsNotificationInfo.amsStateInfo.entityName.value,
        )
    elif ntfType == clAmsClientNotification.eClAmsNotificationTypeT.CL_AMS_NOTIFICATION_COMP_ARRIVAL.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "Component arrival for [%.*s]",
            ntfObj.amsNotificationInfo.amsCompInfo.compName.length,
            ntfObj.amsNotificationInfo.amsCompInfo.compName.value,
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "Comp node [%.*s]",
            ntfObj.amsNotificationInfo.amsCompInfo.nodeName.length,
            ntfObj.amsNotificationInfo.amsCompInfo.nodeName.value,
        )
    elif ntfType == clAmsClientNotification.eClAmsNotificationTypeT.CL_AMS_NOTIFICATION_COMP_DEPARTURE.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "Component [%s] for [%.*s]",
            "death" if ntfObj.amsNotificationInfo.amsCompInfo.operation == clCpmApi.eClCpmCompEventT.CL_CPM_COMP_DEATH.value else "departure",
            ntfObj.amsNotificationInfo.amsCompInfo.compName.length,
            ntfObj.amsNotificationInfo.amsCompInfo.compName.value,
        )
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
            "Comp node [%.*s]",
            ntfObj.amsNotificationInfo.amsCompInfo.nodeName.length,
            ntfObj.amsNotificationInfo.amsCompInfo.nodeName.value,
        )
    elif ntfType == clAmsClientNotification.eClAmsNotificationTypeT.CL_AMS_NOTIFICATION_NODE_DEPARTURE.value:
        operation = ntfObj.amsNotificationInfo.amsNodeInfo.operation
        if (operation == clCpmApi.eClCpmNodeEventT.CL_CPM_NODE_DEPARTURE.value
            or operation == clCpmApi.eClCpmNodeEventT.CL_CPM_NODE_DEATH.value):
            clprintf(
                clLogApi.eClLogSeverityT.CL_LOG_SEV_NOTICE,
                "Node [%s] for [%.*s], address [%d]",
                "death" if operation == clCpmApi.eClCpmNodeEventT.CL_CPM_NODE_DEATH.value else "departure",
                ntfObj.amsNotificationInfo.amsNodeInfo.nodeName.length,
                ntfObj.amsNotificationInfo.amsNodeInfo.nodeName.value,
                ntfObj.amsNotificationInfo.amsNodeInfo.nodeIocAddress
            )

    return clCommonErrors.CL_OK

def clAmsNotificationInitialize(callback):
    rc = clAmsClientNotification.clAmsClientNotificationInitialize(callback)
    if rc != clCommonErrors.CL_OK:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_WARNING,
            "AMF notification initialize returned with [%#x]",
            rc
        )
    return rc

def clAmsNotificationFinalize():
    clAmsClientNotification.clAmsClientNotificationFinalize()

#
# Python entry point
#

if __name__ == "__main__":
    main()
