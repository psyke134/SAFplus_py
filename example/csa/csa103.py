#!/usr/bin/env python3
import saAmf, saAis, saCkpt
import clCommon, clLogApi, clCpmApi, clUtils
import clLib, clIocApi, clEoApi, clEoConfigApi, clOsalApi
import ctypes
import libc
import socket, threading, time

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
COMP_EO_USER_CLIENT_ID      = clCommon.ClUint32T(clEoApi.CL_EO_USER_CLIENT_ID_START.value)
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

seq = saAis.SaUint32T(0)
ha_state = saAmf.SaAmfHAStateT(0)

############################################################################
#   Application Life Cycle Management Functions.
############################################################################

def csa103CkptActive():
    global seq
    rc = saAis.eSaAisErrorT.SA_AIS_OK

    assert ha_state.value == saAmf.eSaAmfHAStateT.SA_AMF_HA_ACTIVE.value

    clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO, "Active thread has started")

    rc = saCkpt.saCkptActiveReplicaSet(ckpt_handle)
    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR, "checkpoint_replica_activate failed [0x%x] in ActiveReplicaSet", rc)

    p_seq = ctypes.pointer(seq)
    checkpoint_read_seq(p_seq)

    while not unblockNow:
        clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,"Hello World! (seq=%d)", seq)
        seq.value += 1
        checkpoint_write_seq(seq)
        time.sleep(1)

    return saAis.eSaAisErrorT.SA_AIS_OK
        

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
    ckpt_dispatch_fd = saAis.SaSelectionObjectT(0)
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

    rc = saAmf.saAmfSelectionObjectGet(
        amfHandle,
        ctypes.byref(dispatch_fd)
    )

    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        errorexit(rc)

    #
    # Do the application specific initialization here.
    #


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

    checkpoint_initialize()

    rc = saCkpt.saCkptSelectionObjectGet(
        ckpt_lib_handle,
        ctypes.byref(ckpt_dispatch_fd)
    )

    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        errorexit(rc)

    #
    # Block on AMF dispatch file descriptor for callbacks
    #
    EINTR = 4   # Interrupted system call
    maxFd = ckpt_dispatch_fd if ckpt_dispatch_fd.value > dispatch_fd.value else dispatch_fd
    while(not unblockNow):
        libc.FD_ZERO(read_fds)
        libc.FD_SET(dispatch_fd.value, read_fds)
        libc.FD_SET(ckpt_dispatch_fd.value, read_fds)

        if libc.select(maxFd.value + 1, ctypes.byref(read_fds), None, None, None) < 0:
            if libc.errno() == EINTR:
                continue
            clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR, "Error in select()")
            break
        saAmf.saAmfDispatch(amfHandle, saAis.eSaDispatchFlagsT.SA_DISPATCH_ALL)
        saCkpt.saCkptDispatch(ckpt_lib_handle, saAis.eSaDispatchFlagsT.SA_DISPATCH_ALL)

    #
    # Do the application specific finalization here.
    #

    checkpoint_finalize()

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

    global ha_state

    if haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_ACTIVE.value:
        #
        # AMF has requested application to take the active HA state 
        # for the CSI.
        #

        clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO, "Active state requested from state %d", ha_state)

        ha_state = saAmf.eSaAmfHAStateT.SA_AMF_HA_ACTIVE

        thr = threading.Thread(target = csa103CkptActive)
        thr.start()

        saAmf.saAmfResponse(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)
    elif haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_STANDBY.value:
        #
        # AMF has requested application to take the standby HA state 
        # for this CSI.
        #
        clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO, "Standby state requested from state %d", ha_state)
        ha_state = saAmf.eSaAmfHAStateT.SA_AMF_HA_STANDBY

        saAmf.saAmfResponse(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)
    elif haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCED.value:
        #
        # AMF has requested application to quiesce the CSI currently
        # assigned the active or quiescing HA state. The application 
        # must stop work associated with the CSI immediately.
        #
        clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO, "QUIESCED")
        ha_state = saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCED

        saAmf.saAmfResponse(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)
    elif haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCING.value:
        #
        # AMF has requested application to quiesce the CSI currently
        # assigned the active HA state. The application must stop work
        # associated with the CSI gracefully and not accept any new
        # workloads while the work is being terminated.
        #
        clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO, "QUIESCING")
        ha_state = saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCING

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

CKPT_NAME = "csa103Ckpt"
ckpt_lib_handle = saCkpt.SaCkptHandleT(0)
ckpt_handle = saCkpt.SaCkptCheckpointHandleT(0)
CKPT_SID_NAME = "csa103Ckpt_sec"
ckpt_sid = saCkpt.SaCkptSectionIdT(CKPT_SID_NAME)
ckpt_callbacks = saCkpt.SaCkptCallbacksT()
seq = saAis.SaUint32T(0)
syncCount = saAis.SaInvocationT(0)

def checkpointOpenCompleted(invocation, checkpointHandle, error):
    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "Checkpoint open completed"
    )

def checkpointSynchronizeCompleted(invocation, error):
    invocation = saAis.SaUint64T(invocation)
    if ((invocation.value % 10) == 0):
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
            "Checkpoint synchronize [%llu] completed ",
            invocation
        )

def checkpoint_initialize():
    global ckpt_lib_handle
    global ckpt_handle
    global ckpt_callbacks

    rc = saAis.eSaAisErrorT.SA_AIS_OK
    ckpt_version = saAis.SaVersionT(ord('B'), 1, 1)
    ckpt_name = saAis.SaNameT(CKPT_NAME)
    attrs = saCkpt.SaCkptCheckpointCreationAttributesT()

    attrs.creationFlags     = saCkpt.SA_CKPT_WR_ACTIVE_REPLICA_WEAK | saCkpt.SA_CKPT_CHECKPOINT_COLLOCATED
    attrs.checkpointSize    = ctypes.sizeof(saAis.SaUint32T)
    attrs.retentionDuration = saAis.SaTimeT(10)
    attrs.maxSections       = saAis.SaUint32T(2)
    attrs.maxSectionSize    = ctypes.sizeof(saAis.SaUint32T)
    attrs.maxSectionIdSize  = saAis.SaSizeT(64)

    ckpt_callbacks.saCkptCheckpointOpenCallback = saCkpt.SaCkptCheckpointOpenCallbackT(checkpointOpenCompleted)
    ckpt_callbacks.saCkptCheckpointSynchronizeCallback = saCkpt.SaCkptCheckpointSynchronizeCallbackT(checkpointSynchronizeCompleted)

    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "Checkpoint Initialize"
    )

    rc = saCkpt.saCkptInitialize(
        ctypes.byref(ckpt_lib_handle),
        ctypes.byref(ckpt_callbacks),
        ctypes.byref(ckpt_version)
    )

    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR,
            "Failed to initialize checkpoint service with rc [%#x]",
            rc
        )
        return rc
    
    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "Checkpoint service initialized (handle=0x%llx)",
        ckpt_lib_handle
    )

    rc = saCkpt.saCkptCheckpointOpen(
        ckpt_lib_handle,
        ctypes.byref(ckpt_name),
        ctypes.byref(attrs),
        (saCkpt.SA_CKPT_CHECKPOINT_READ | saCkpt.SA_CKPT_CHECKPOINT_WRITE | saCkpt.SA_CKPT_CHECKPOINT_CREATE),
        saAis.SaTimeT(saAis.SA_TIME_MAX),
        ctypes.byref(ckpt_handle)
    )

    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR,
            "Failed [0x%x] to open checkpoint",
            rc
        )
        return rc
    
    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "Checkpoint opened (handle=0x%llx)",
        ckpt_handle
    )
    return rc

def checkpoint_finalize():
    rc = saAis.eSaAisErrorT.SA_AIS_OK
    rc = saCkpt.saCkptCheckpointClose(ckpt_handle)
    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR,
            "Failed [0x%x] to close checkpoint handle 0x%llx",
            rc,
            ckpt_handle
        )

    rc = saCkpt.saCkptFinalize(ckpt_lib_handle)
    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR,
            "Failed [0x%x] to finalize checkpoint",
            rc
        )

def checkpoint_write_seq(seq):
    rc = saAis.eSaAisErrorT.SA_AIS_OK
    seq_no = saAis.SaUint32T(0)

    seq_no.value = socket.htonl(seq.value)

    rc = saCkpt.saCkptSectionOverwrite(
        ckpt_handle,
        ctypes.byref(ckpt_sid),
        ctypes.byref(seq_no),
        ctypes.sizeof(saAis.SaUint32T)
    )

    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        if (rc == 0x1000a) or (rc == saAis.eSaAisErrorT.SA_AIS_ERR_NOT_EXIST.value):
            p_ckpt_sid = ctypes.pointer(ckpt_sid)
            section_cr_attr = saCkpt.SaCkptSectionCreationAttributesT(
                p_ckpt_sid,
                saAis.SA_TIME_END
            )
            p_seq_no = ctypes.pointer(seq_no)
            p_data = ctypes.cast(p_seq_no, ctypes.POINTER(saAis.SaUint8T))

            rc = saCkpt.saCkptSectionCreate(
                ckpt_handle,
                ctypes.byref(section_cr_attr),
                p_data,
                ctypes.sizeof(saAis.SaUint32T)
            )

        if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
            clprintf(
                clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR,
                "Failed [0x%x] to write to section",
                rc
            )

    if rc == saAis.eSaAisErrorT.SA_AIS_OK.value:
        global syncCount
        rc = saCkpt.saCkptCheckpointSynchronizeAsync(ckpt_handle, syncCount)
        syncCount.value += 1

    return rc

def checkpoint_read_seq(seq):
    """
    arg: ClUint32T *, return: SaAisErrorT
    """
    rc = saAis.eSaAisErrorT.SA_AIS_OK
    err_idx = saAis.SaUint32T(0)
    seq_no = saAis.SaUint32T(0xFFFFFFFF)
    p_seq_no = ctypes.cast(ctypes.byref(seq_no), ctypes.c_void_p)

    iov = saCkpt.SaCkptIOVectorElementT(
        ckpt_sid,
        p_seq_no,
        ctypes.sizeof(saAis.SaUint32T),
        saAis.SaOffsetT(0),
        ctypes.sizeof(saAis.SaUint32T)
    )

    rc = saCkpt.saCkptCheckpointRead(
        ckpt_handle,
        ctypes.byref(iov),
        1,
        ctypes.byref(err_idx)
    )
    if rc != saAis.eSaAisErrorT.SA_AIS_OK.value:
        if rc != saAis.eSaAisErrorT.SA_AIS_ERR_NOT_EXIST.value:
            return saAis.eSaAisErrorT.SA_AIS_OK
        clprintf(
            clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR,
            "Error: [0x%x] from checkpoint read, err_idx = %u",
            rc, err_idx
        )

    seq.contents.value = socket.ntohl(seq_no.value) # *seq = ntohl(seq_no)
    return saAis.eSaAisErrorT.SA_AIS_OK


#
# Python entry point
#

if __name__ == "__main__":
    main()
