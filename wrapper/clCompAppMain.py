#!/usr/bin/env python3
import saAmf, saAis
import clCommon, clLogApi, clCpmApi, clUtils
import clLib, clIocApi, clEoApi, clEoConfigApi, clOsalApi
import ctypes
import libc

CL_LOG_HANDLE_APP = clCommon.ClHandleT.in_dll(clLib.libmw_so, "CL_LOG_HANDLE_APP")

def STRING_HA_STATE(S):
    if S == saAmf.eSaAmfHAStateT.SA_AMF_HA_ACTIVE: return "Active"
    elif S == saAmf.eSaAmfHAStateT.SA_AMF_HA_STANDBY: return "Standby"
    elif S == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCED: return "Quiesced"
    elif S == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCING: return "Quiescing"
    else: return "Uknown"

def STRING_CSI_FLAGS(S):
    if S & saAmf.SA_AMF_CSI_ADD_ONE: return "Add One"
    elif S & saAmf.SA_AMF_CSI_TARGET_ONE: return "Target One"
    elif S & saAmf.SA_AMF_CSI_TARGET_ALL: return "Target All"
    else: return "Uknown"

def clprintf(severity, fmtString, *va_args):
    fileName, loc = clUtils.getCallerInfo()

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
clEoConfig      = clEoConfigApi.ClEoConfigT.in_dll(clLib.libmw_so, "clEoConfig")
clEoBasicLibs   = clEoConfigApi._clEoBasicLibArray.in_dll(clLib.libmw_so, "clEoBasicLibs")
clEoClientLibs  = clEoConfigApi._clEoClientLibArray.in_dll(clLib.libmw_so, "clEoClientLibs")

# Description of this EO
clEoConfig.EOname                   = COMP_EO_NAME.encode("utf-8")  # EO Name
clEoConfig.pri                      = COMP_EO_THREAD_PRIORITY       # EO Thread Priority
clEoConfig.noOfThreads              = COMP_EO_NUM_THREAD            # No of EO thread needed
clEoConfig.reqIocPort               = COMP_IOC_PORT                 # Required Ioc Port
clEoConfig.maxNoClients             = COMP_EO_USER_CLIENT_ID
clEoConfig.appType                  = COMP_EO_USE_THREAD_MODEL      # Thread Model
clEoConfig.clEoCreateCallout        = NULL_EO_CREATE_CALLOUT        # Application Initialize Callback
clEoConfig.clEoDeleteCallout        = NULL_EO_DELETE_CALLOUT        # Application Terminate Callback
clEoConfig.clEoStateChgCallout      = NULL_EO_ST_CHG_CALLOUT        # Application State Change Callback
clEoConfig.clEoHealthCheckCallout   = NULL_EO_HP_CHK_CALLOUT        # Application Health Check Callback
clEoConfig.clEoCustomAction         = NULL_EO_CTM_ACT
clEoConfig.needSerialization        = clCommon.CL_FALSE

# Basic libraries used by this EO. The first 6 libraries are
# mandatory, the others can be enabled or disabled by setting to
# CL_TRUE or CL_FALSE.
clEoBasicLibs[0] = COMP_EO_BASICLIB_OSAL    #Lib: Operating System Adaptation Layer
clEoBasicLibs[1] = COMP_EO_BASICLIB_TIMER   #Lib: Timer
clEoBasicLibs[2] = COMP_EO_BASICLIB_BUFFER  #Lib: Buffer Management
clEoBasicLibs[3] = COMP_EO_BASICLIB_IOC     #Lib: Intelligent Object Communication
clEoBasicLibs[4] = COMP_EO_BASICLIB_RMD     #Lib: Remote Method Dispatch
clEoBasicLibs[5] = COMP_EO_BASICLIB_EO      #Lib: Execution Object
clEoBasicLibs[6] = COMP_EO_BASICLIB_OM      #Lib: Object Management
clEoBasicLibs[7] = COMP_EO_BASICLIB_HAL     #Lib: Hardware Adaptation Layer
clEoBasicLibs[8] = COMP_EO_BASICLIB_DBAL    #Lib: Database Adaptation Layer

# Client libraries used by this EO. All are optional and can be
# enabled or disabled by setting to CL_TRUE or CL_FALSE.
clEoClientLibs[0] = COMP_EO_CLIENTLIB_COR       #Lib: Common Object Repository
clEoClientLibs[1] = COMP_EO_CLIENTLIB_CM        #Lib: Chassis Management
clEoClientLibs[2] = COMP_EO_CLIENTLIB_NAME      #Lib: Name Service
clEoClientLibs[3] = COMP_EO_CLIENTLIB_LOG       #Lib: Log Service
clEoClientLibs[4] = COMP_EO_CLIENTLIB_TRACE     #Lib: Trace Service
clEoClientLibs[5] = COMP_EO_CLIENTLIB_DIAG      #Lib: Diagnostics
clEoClientLibs[6] = COMP_EO_CLIENTLIB_TXN       #Lib: Transaction Management
clEoClientLibs[7] = COMP_EO_CLIENTLIB_MSO       #Lib: MSO Management
clEoClientLibs[8] = COMP_EO_CLIENTLIB_PROV      #Lib: Provisioning Management
clEoClientLibs[9] = COMP_EO_CLIENTLIB_ALARM     #Lib: Alarm Management
clEoClientLibs[10] = COMP_EO_CLIENTLIB_DEBUG    #Lib: Debug Service
clEoClientLibs[11] = COMP_EO_CLIENTLIB_GMS      #Lib: Cluster/Group Membership Service
clEoClientLibs[12] = COMP_EO_CLIENTLIB_PM       #Lib: PM Management

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

    if rc != saAis.eSaAisErrorT.SA_AIS_OK:
        errorexit(rc)

    libc.FD_ZERO(read_fds)

    rc = saAmf.saAmfSelectionObjectGet(
        amfHandle,
        ctypes.byref(dispatch_fd)
    )

    if rc != saAis.eSaAisErrorT.SA_AIS_OK:
        errorexit(rc)

    libc.FD_SET(dispatch_fd, read_fds)

    #
    # Do the application specific initialization here.
    #


    #
    # Now register the component with AMF. At this point it is
    # ready to provide service, i.e. take work assignments.
    #

    rc = saAmf.saAmfComponentNameGet(amfHandle, ctypes.byref(appName))
    if rc != saAis.eSaAisErrorT.SA_AIS_OK:
        errorexit(rc)

    rc = saAmf.saAmfComponentRegister(amfHandle, ctypes.byref(appName), None)
    if rc != saAis.eSaAisErrorT.SA_AIS_OK:
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
        if libc.select(dispatch_fd + 1, ctypes.byref(read_fds), None, None, None) < 0:
            if libc.errno() == EINTR:
                continue
            clprintf(clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR, "Error in select()")
            break
        saAmf.saAmfDispatch(amfHandle, saAis.eSaDispatchFlagsT.SA_DISPATCH_ALL)

    #
    # Do the application specific finalization here.
    #

    rc = saAmf.saAmfFinalize(amfHandle)
    if rc != saAis.eSaAisErrorT.SA_AIS_OK:
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
    if rc != saAis.eSaAisErrorT.SA_AIS_OK:
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

    clprintf(
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        "Component [%.*s] : PID [%d]. CSI Set Received\n",
        compName.contents.length, compName.contents.__str__(), mypid
    )

    clCompAppAMFPrintCSI(csiDescriptor, haState)

    #
    # Take appropriate action based on state
    #

    if haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_ACTIVE:
        #
        # AMF has requested application to take the active HA state 
        # for the CSI.
        #
        saAmf.saAmfResponse(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)
    elif haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_STANDBY:
        #
        # AMF has requested application to take the standby HA state 
        # for this CSI.
        #
        saAmf.saAmfResponse(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)
    elif haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCED:
        #
        # AMF has requested application to quiesce the CSI currently
        # assigned the active or quiescing HA state. The application 
        # must stop work associated with the CSI immediately.
        #
        saAmf.saAmfResponse(amfHandle, invocation, saAis.eSaAisErrorT.SA_AIS_OK)
    elif haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_QUIESCING:
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
        for i in range(0, csiDescriptor.csiAttr.number.value):
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

    if haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_ACTIVE:
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
    elif haState == saAmf.eSaAmfHAStateT.SA_AMF_HA_STANDBY:
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


#
# Python entry point
#

if __name__ == "__main__":
    main()
