import sys
sys.path.append("..")

from common import clCommon, clCommonErrors
from utils import clLib, clUtils
from amf import clAmsEntities, clAmsErrors, clAmsTypes, clCpmAms
from debug import clDebugApi

import ctypes

def clAmsFormatMsg(fmt, *va_args):
    """
    Variadic function

    arg types:
        char *fmt,
        ...

    return type:
        char *
    """
    c_fmt = clUtils.toCharP(fmt)
    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clLogWriteAsync.argtypes = [ctypes.c_char_p] + argTypes
    return clLib.libmw_so.clLogWriteAsync(c_fmt, *cVaArgs)

def clAmsLogMsgClient(level, buffer):
    """
    arg types:
        ClUint32T level
        char *buffer
    """
    clLib.libmw_so.clAmsLogMsgClient(level, buffer)

def AMS_CHECK_BAD_CLNAME(name):
    if name.length > clCommon.CL_MAX_NAME_LENGTH:
        func, _, loc = clUtils.getCallerInfo()
        clAmsLogMsgClient(
            clDebugApi.CL_DEBUG_ERROR,
            clAmsFormatMsg(
                "ALERT [%s:%d] : Invalid ClNameT structure\n",
                func,
                loc
            )
        )
        return clCommonErrors.CL_ERR_BUFFER_OVERRUN
    return clCommonErrors.CL_OK

def AMS_CHECK_ENTITY_TYPE(type):
    if type > clAmsEntities.CL_AMS_ENTITY_TYPE_MAX:
        clAmsLogMsgClient(
            clDebugApi.CL_DEBUG_ERROR,
            clAmsFormatMsg(
                "ERROR: Invalid entity type = %d\n",
                type
            )
        )
        return clAmsErrors.CL_AMS_RC(clAmsErrors.CL_AMS_ERR_INVALID_ENTITY)
    return clCommonErrors.CL_OK

def AMS_CHECKPTR_SILENT(x):
    try:
        x.contents
    except ValueError:
        return clAmsErrors.CL_AMS_RC(clCommonErrors.CL_ERR_NO_MEMORY)
    return clCommonErrors.CL_OK

def AMS_MIN(x,y):
    return x if x < y else y

def AMS_MAX(x,y):
    return x if x > y else y

def clAmsFreeMemory(mPtr):
    pass


def CL_AMS_STRING_BOOLEAN(S):
    return "True" if S else "False"

def CL_AMS_STRING_SERVICE_STATE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_RUNNING: "Running",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_STOPPED: "Stopped",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_STARTINGUP: "Starting Up",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_SHUTTINGDOWN: "Shutting Down",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_UNAVAILABLE: "Unavailable",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_HOT_STANDBY: "Hot standby",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_NONE: "None"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_INSTANTIATE_MODE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value

    if S & clCpmAms.CL_AMS_INSTANTIATE_MODE_ACTIVE: return "Active Mode"
    elif S & clCpmAms.CL_AMS_INSTANTIATE_MODE_STANDBY: return "Standby Mode"
    else: return "Uknown"

def CL_AMS_STRING_A_STATE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsAdminStateT.CL_AMS_ADMIN_STATE_UNLOCKED: "Unlocked",
        clAmsTypes.eClAmsAdminStateT.CL_AMS_ADMIN_STATE_LOCKED_A: "Locked Assignment",
        clAmsTypes.eClAmsAdminStateT.CL_AMS_ADMIN_STATE_LOCKED_I: "Locked Instantiation",
        clAmsTypes.eClAmsAdminStateT.CL_AMS_ADMIN_STATE_SHUTTINGDOWN: "Shutting Down",
        clAmsTypes.eClAmsAdminStateT.CL_AMS_ADMIN_STATE_NONE: "None",
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_O_STATE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsOperStateT.CL_AMS_OPER_STATE_ENABLED: "Enabled",
        clAmsTypes.eClAmsOperStateT.CL_AMS_OPER_STATE_DISABLED: "Disabled",
        clAmsTypes.eClAmsOperStateT.CL_AMS_OPER_STATE_NONE: "None"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_P_STATE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_UNINSTANTIATED: "Uninstantiated",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_INSTANTIATING: "Instantiating",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_INSTANTIATED: "Instantiated",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_TERMINATING: "Terminating",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_RESTARTING: "Restarting",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_INSTANTIATION_FAILED: "Instantiation Failed",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_TERMINATION_FAILED: "Termination Failed",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_FAULT: "Fault",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_FAULT_WTR: "Fault WTR",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_FAULT_WTC: "Fault WTC",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_NONE: "None"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_R_STATE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsReadinessStateT.CL_AMS_READINESS_STATE_INSERVICE: "In Service",
        clAmsTypes.eClAmsReadinessStateT.CL_AMS_READINESS_STATE_STOPPING: "Stopping",
        clAmsTypes.eClAmsReadinessStateT.CL_AMS_READINESS_STATE_OUTOFSERVICE: "Out of Service",
        clAmsTypes.eClAmsReadinessStateT.CL_AMS_READINESS_STATE_NONE: "None"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_H_STATE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsHAStateT.CL_AMS_HA_STATE_ACTIVE: "Active",
        clAmsTypes.eClAmsHAStateT.CL_AMS_HA_STATE_STANDBY: "Standby",
        clAmsTypes.eClAmsHAStateT.CL_AMS_HA_STATE_QUIESCED: "Quiesced",
        clAmsTypes.eClAmsHAStateT.CL_AMS_HA_STATE_QUIESCING: "Quiescing",
        clAmsTypes.eClAmsHAStateT.CL_AMS_HA_STATE_NONE: "None"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_TIMER(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_NODE_TIMER_SUFAILOVER: "Node-SUFailover",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SG_TIMER_INSTANTIATE: "SG-Instantiate",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SG_TIMER_ADJUST: "SG-Adjust",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SG_TIMER_ADJUST_PROBATION: "SG-Adjust-Probation",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SU_TIMER_SURESTART: "SU-SURestart",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SU_TIMER_PROBATION: "SU-SUProbation",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SU_TIMER_COMPRESTART: "SU-CompRestart",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SU_TIMER_ASSIGNMENT: "SU-Assignment-Delay",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_INSTANTIATE: "Comp-Instantiate",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_INSTANTIATEDELAY: "Comp-InstantiateDelay",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_TERMINATE: "Comp-Terminate",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_CLEANUP: "Comp-Cleanup",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_AMSTART: "Comp-AMStart",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_AMSTOP: "Comp-AMStop",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_QUIESCINGCOMPLETE: "Comp-QuiescingComplete",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_CSISET: "Comp-CSISet",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_CSIREMOVE: "Comp-CSIRemove",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_PROXIEDCOMPINSTANTIATE: "Comp-ProxiedCompInstantiate",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_PROXIEDCOMPCLEANUP: "Comp-ProxiedCompCleanup"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_NODE_CLASSTYPE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    classLut = {
        clAmsTypes.eClAmsNodeClassT.CL_AMS_NODE_CLASS_A: "Class A",
        clAmsTypes.eClAmsNodeClassT.CL_AMS_NODE_CLASS_B: "Class B",
        clAmsTypes.eClAmsNodeClassT.CL_AMS_NODE_CLASS_C: "Class C",
        clAmsTypes.eClAmsNodeClassT.CL_AMS_NODE_CLASS_D: "Class D",
        clAmsTypes.eClAmsNodeClassT.CL_AMS_NODE_CLASS_NONE: "None"
    }

    for key, item in classLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_NODE_ISCLUSTERMEMBER(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsNodeClusterMemberT.CL_AMS_NODE_IS_CLUSTER_MEMBER: "True",
        clAmsTypes.eClAmsNodeClusterMemberT.CL_AMS_NODE_IS_LEAVING_CLUSTER: "Leaving"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "False"

def CL_AMS_STRING_SG_REDUNDANCY_MODEL(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    modelLut = {
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_NO_REDUNDANCY: "No Redundancy",
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_TWO_N: "2N (1+1)",
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_M_PLUS_N: "M + N",
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_N_WAY: "N-Way",
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_N_WAY_ACTIVE: "N-Way-Active",
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_CUSTOM: "CUSTOM"
    }

    for key, item in modelLut.items():
        if S == key:
            return item
    return "Unknown"

def CL_AMS_STRING_SG_LOADING_STRATEGY(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    startLut = {
        clAmsTypes.eClAmsSGLoadingStrategyT.CL_AMS_SG_LOADING_STRATEGY_LEAST_SI_PER_SU: "Least SI per SU",
        clAmsTypes.eClAmsSGLoadingStrategyT.CL_AMS_SG_LOADING_STRATEGY_LEAST_SU_ASSIGNED: "Least SU Assigned",
        clAmsTypes.eClAmsSGLoadingStrategyT.CL_AMS_SG_LOADING_STRATEGY_LEAST_LOAD_PER_SU: "Least Load per SU",
        clAmsTypes.eClAmsSGLoadingStrategyT.CL_AMS_SG_LOADING_STRATEGY_BY_SI_PREFERENCE: "By SI Perference",
        clAmsTypes.eClAmsSGLoadingStrategyT.CL_AMS_SG_LOADING_STRATEGY_USER_DEFINED: "User Defined"
    }

    for key, item in startLut.items():
        if S== key:
            return item
    return "Unknown"

def CL_AMS_STRING_RECOVERY(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    revLut = {
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NO_RECOMMENDATION: "No Recommendation",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_COMP_RESTART: "Component Restart",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_COMP_FAILOVER: "Component Failover",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NODE_SWITCHOVER: "Node Switchover",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NODE_FAILOVER: "Node Failover",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NODE_FAILFAST: "Node Failfast",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_APP_RESTART: "Application Restart",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_CLUSTER_RESET: "Cluster Restart",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_INTERNALLY_RECOVERED: "Internally Recovered",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_SU_RESTART: "SU Restart",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NONE: "None",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_EXTERNAL_RECOVERY_RESET: "External Component Reset",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_EXTERNAL_RECOVERY_REBOOT: "External Component Reboot",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_EXTERNAL_RECOVERY_POWER_ON: "External Component PowerOn",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_EXTERNAL_RECOVERY_POWER_OFF: "External Component PowerOff",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NODE_HALT: "Node halt"
    }

    for key, item in revLut.items():
        if S == key:
            return item
    return "Unknown"

def CL_AMS_STRING_COMP_PROPERTY(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    propLut = {
        clAmsTypes.eClAmsCompPropertyT.CL_AMS_COMP_PROPERTY_SA_AWARE: "SA Aware",
        clAmsTypes.eClAmsCompPropertyT.CL_AMS_COMP_PROPERTY_PROXIED_PREINSTANTIABLE: "Proxied Preinstantiable",
        clAmsTypes.eClAmsCompPropertyT.CL_AMS_COMP_PROPERTY_PROXIED_NON_PREINSTANTIABLE: "Proxied Non Preinstantiable",
        clAmsTypes.eClAmsCompPropertyT.CL_AMS_COMP_PROPERTY_NON_PROXIED_NON_PREINSTANTIABLE: "Non Proxied Non Preinstantiable"
    }

    for key, item in propLut.items():
        if S == key:
            return item
    return "Unknown"

def CL_AMS_STRING_COMP_CAP(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    capLut = {
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_X_ACTIVE_AND_Y_STANDBY: "X-Active AND Y-Standby",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_X_ACTIVE_OR_Y_STANDBY: "X-Active OR Y-Standby",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_ONE_ACTIVE_OR_X_STANDBY: "1-Active OR Y-Standby",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_ONE_ACTIVE_OR_ONE_STANDBY: "1-Active OR 1-Standby",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_X_ACTIVE: "X-Active",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_ONE_ACTIVE: "1-Active",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_NON_PREINSTANTIABLE: "Non Preinstantiable"
    }

    for key, item in capLut.items():
        if S == key:
            return item
    return "Unknown"

def CL_AMS_STRING_CSI_FLAGS(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    if S & clAmsTypes.CL_AMS_CSI_FLAG_ADD_ONE: return "ADD_ONE"
    elif S & clAmsTypes.CL_AMS_CSI_FLAG_TARGET_ONE: return "TARGET_ONE"
    elif S & clAmsTypes.CL_AMS_CSI_FLAG_TARGET_ALL: return "TARGET_ALL"
    else: return "Uknown"

def CL_AMS_STRING_CSI_FLAGS(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    flagLut = {
        clAmsTypes.eClAmsCSITransitionDescriptorT.CL_AMS_CSI_NEW_ASSIGN: "NEW_ASSIGN",
        clAmsTypes.eClAmsCSITransitionDescriptorT.CL_AMS_CSI_QUIESCED: "CSI_QUIESCED",
        clAmsTypes.eClAmsCSITransitionDescriptorT.CL_AMS_CSI_NOT_QUIESCED: "CSI_NOT_QUIESCED",
        clAmsTypes.eClAmsCSITransitionDescriptorT.CL_AMS_CSI_STILL_ACTIVE: "CSI_STILL_ACTIVE"
    }

    for key, item in flagLut.items():
        if S == key:
            return item
    return "Unknown"

def CL_AMS_STRING_ENTITY_TYPE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    typeLut = {
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_ENTITY: "entity",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_NODE: "node",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG: "sg",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU: "su",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI: "si",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP: "comp",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI: "csi",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CLUSTER: "cluster"
    }

    for key, item in typeLut.items():
        if S == key:
            return item
    return "Unknown"

# TODO: there're remaining codes in the original header file
