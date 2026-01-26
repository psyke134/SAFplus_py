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
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_RUNNING.value: "Running",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_STOPPED.value: "Stopped",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_STARTINGUP.value: "Starting Up",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_SHUTTINGDOWN.value: "Shutting Down",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_UNAVAILABLE.value: "Unavailable",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_HOT_STANDBY.value: "Hot standby",
        clAmsTypes.eClAmsServiceStateT.CL_AMS_SERVICE_STATE_NONE.value: "None"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_INSTANTIATE_MODE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    modeLut = {
        clCpmAms.CL_AMS_INSTANTIATE_MODE_ACTIVE: "Active Mode",
        clCpmAms.CL_AMS_INSTANTIATE_MODE_STANDBY: "Standby Mode"
    }

    for key, item in modeLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_A_STATE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsAdminStateT.CL_AMS_ADMIN_STATE_UNLOCKED.value: "Unlocked",
        clAmsTypes.eClAmsAdminStateT.CL_AMS_ADMIN_STATE_LOCKED_A.value: "Locked Assignment",
        clAmsTypes.eClAmsAdminStateT.CL_AMS_ADMIN_STATE_LOCKED_I.value: "Locked Instantiation",
        clAmsTypes.eClAmsAdminStateT.CL_AMS_ADMIN_STATE_SHUTTINGDOWN.value: "Shutting Down",
        clAmsTypes.eClAmsAdminStateT.CL_AMS_ADMIN_STATE_NONE.value: "None",
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_O_STATE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsOperStateT.CL_AMS_OPER_STATE_ENABLED.value: "Enabled",
        clAmsTypes.eClAmsOperStateT.CL_AMS_OPER_STATE_DISABLED.value: "Disabled",
        clAmsTypes.eClAmsOperStateT.CL_AMS_OPER_STATE_NONE.value: "None"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_P_STATE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_UNINSTANTIATED.value: "Uninstantiated",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_INSTANTIATING.value: "Instantiating",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_INSTANTIATED.value: "Instantiated",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_TERMINATING.value: "Terminating",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_RESTARTING.value: "Restarting",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_INSTANTIATION_FAILED.value: "Instantiation Failed",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_TERMINATION_FAILED.value: "Termination Failed",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_FAULT.value: "Fault",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_FAULT_WTR.value: "Fault WTR",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_FAULT_WTC.value: "Fault WTC",
        clAmsTypes.eClAmsPresenceStateT.CL_AMS_PRESENCE_STATE_NONE.value: "None"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_R_STATE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsReadinessStateT.CL_AMS_READINESS_STATE_INSERVICE.value: "In Service",
        clAmsTypes.eClAmsReadinessStateT.CL_AMS_READINESS_STATE_STOPPING.value: "Stopping",
        clAmsTypes.eClAmsReadinessStateT.CL_AMS_READINESS_STATE_OUTOFSERVICE.value: "Out of Service",
        clAmsTypes.eClAmsReadinessStateT.CL_AMS_READINESS_STATE_NONE.value: "None"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_H_STATE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsHAStateT.CL_AMS_HA_STATE_ACTIVE.value: "Active",
        clAmsTypes.eClAmsHAStateT.CL_AMS_HA_STATE_STANDBY.value: "Standby",
        clAmsTypes.eClAmsHAStateT.CL_AMS_HA_STATE_QUIESCED.value: "Quiesced",
        clAmsTypes.eClAmsHAStateT.CL_AMS_HA_STATE_QUIESCING.value: "Quiescing",
        clAmsTypes.eClAmsHAStateT.CL_AMS_HA_STATE_NONE.value: "None"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_TIMER(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_NODE_TIMER_SUFAILOVER.value: "Node-SUFailover",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SG_TIMER_INSTANTIATE.value: "SG-Instantiate",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SG_TIMER_ADJUST.value: "SG-Adjust",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SG_TIMER_ADJUST_PROBATION.value: "SG-Adjust-Probation",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SU_TIMER_SURESTART.value: "SU-SURestart",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SU_TIMER_PROBATION.value: "SU-SUProbation",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SU_TIMER_COMPRESTART.value: "SU-CompRestart",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_SU_TIMER_ASSIGNMENT.value: "SU-Assignment-Delay",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_INSTANTIATE.value: "Comp-Instantiate",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_INSTANTIATEDELAY.value: "Comp-InstantiateDelay",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_TERMINATE.value: "Comp-Terminate",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_CLEANUP.value: "Comp-Cleanup",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_AMSTART.value: "Comp-AMStart",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_AMSTOP.value: "Comp-AMStop",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_QUIESCINGCOMPLETE.value: "Comp-QuiescingComplete",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_CSISET.value: "Comp-CSISet",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_CSIREMOVE.value: "Comp-CSIRemove",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_PROXIEDCOMPINSTANTIATE.value: "Comp-ProxiedCompInstantiate",
        clAmsEntities.eClAmsEntityTimerTypeT.CL_AMS_COMP_TIMER_PROXIEDCOMPCLEANUP.value: "Comp-ProxiedCompCleanup"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_NODE_CLASSTYPE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    classLut = {
        clAmsTypes.eClAmsNodeClassT.CL_AMS_NODE_CLASS_A.value: "Class A",
        clAmsTypes.eClAmsNodeClassT.CL_AMS_NODE_CLASS_B.value: "Class B",
        clAmsTypes.eClAmsNodeClassT.CL_AMS_NODE_CLASS_C.value: "Class C",
        clAmsTypes.eClAmsNodeClassT.CL_AMS_NODE_CLASS_D.value: "Class D",
        clAmsTypes.eClAmsNodeClassT.CL_AMS_NODE_CLASS_NONE.value: "None"
    }

    for key, item in classLut.items():
        if S == key:
            return item
    return "Uknown"

def CL_AMS_STRING_NODE_ISCLUSTERMEMBER(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    stateLut = {
        clAmsTypes.eClAmsNodeClusterMemberT.CL_AMS_NODE_IS_CLUSTER_MEMBER.value: "True",
        clAmsTypes.eClAmsNodeClusterMemberT.CL_AMS_NODE_IS_LEAVING_CLUSTER.value: "Leaving"
    }

    for key, item in stateLut.items():
        if S == key:
            return item
    return "False"

def CL_AMS_STRING_SG_REDUNDANCY_MODEL(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    modelLut = {
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_NO_REDUNDANCY.value: "No Redundancy",
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_TWO_N.value: "2N (1+1)",
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_M_PLUS_N.value: "M + N",
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_N_WAY.value: "N-Way",
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_N_WAY_ACTIVE.value: "N-Way-Active",
        clAmsTypes.eClAmsSGRedundancyModelT.CL_AMS_SG_REDUNDANCY_MODEL_CUSTOM.value: "CUSTOM"
    }

    for key, item in modelLut.items():
        if S == key:
            return item
    return "Unknown"

def CL_AMS_STRING_SG_LOADING_STRATEGY(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    startLut = {
        clAmsTypes.eClAmsSGLoadingStrategyT.CL_AMS_SG_LOADING_STRATEGY_LEAST_SI_PER_SU.value: "Least SI per SU",
        clAmsTypes.eClAmsSGLoadingStrategyT.CL_AMS_SG_LOADING_STRATEGY_LEAST_SU_ASSIGNED.value: "Least SU Assigned",
        clAmsTypes.eClAmsSGLoadingStrategyT.CL_AMS_SG_LOADING_STRATEGY_LEAST_LOAD_PER_SU.value: "Least Load per SU",
        clAmsTypes.eClAmsSGLoadingStrategyT.CL_AMS_SG_LOADING_STRATEGY_BY_SI_PREFERENCE.value: "By SI Perference",
        clAmsTypes.eClAmsSGLoadingStrategyT.CL_AMS_SG_LOADING_STRATEGY_USER_DEFINED.value: "User Defined"
    }

    for key, item in startLut.items():
        if S== key:
            return item
    return "Unknown"

def CL_AMS_STRING_RECOVERY(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    revLut = {
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NO_RECOMMENDATION.value: "No Recommendation",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_COMP_RESTART.value: "Component Restart",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_COMP_FAILOVER.value: "Component Failover",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NODE_SWITCHOVER.value: "Node Switchover",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NODE_FAILOVER.value: "Node Failover",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NODE_FAILFAST.value: "Node Failfast",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_APP_RESTART.value: "Application Restart",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_CLUSTER_RESET.value: "Cluster Restart",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_INTERNALLY_RECOVERED.value: "Internally Recovered",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_SU_RESTART.value: "SU Restart",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NONE.value: "None",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_EXTERNAL_RECOVERY_RESET.value: "External Component Reset",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_EXTERNAL_RECOVERY_REBOOT.value: "External Component Reboot",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_EXTERNAL_RECOVERY_POWER_ON.value: "External Component PowerOn",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_EXTERNAL_RECOVERY_POWER_OFF.value: "External Component PowerOff",
        clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_NODE_HALT.value: "Node halt"
    }

    for key, item in revLut.items():
        if S == key:
            return item
    return "Unknown"

def CL_AMS_STRING_COMP_PROPERTY(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    propLut = {
        clAmsTypes.eClAmsCompPropertyT.CL_AMS_COMP_PROPERTY_SA_AWARE.value: "SA Aware",
        clAmsTypes.eClAmsCompPropertyT.CL_AMS_COMP_PROPERTY_PROXIED_PREINSTANTIABLE.value: "Proxied Preinstantiable",
        clAmsTypes.eClAmsCompPropertyT.CL_AMS_COMP_PROPERTY_PROXIED_NON_PREINSTANTIABLE.value: "Proxied Non Preinstantiable",
        clAmsTypes.eClAmsCompPropertyT.CL_AMS_COMP_PROPERTY_NON_PROXIED_NON_PREINSTANTIABLE.value: "Non Proxied Non Preinstantiable"
    }

    for key, item in propLut.items():
        if S == key:
            return item
    return "Unknown"

def CL_AMS_STRING_COMP_CAP(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    capLut = {
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_X_ACTIVE_AND_Y_STANDBY.value: "X-Active AND Y-Standby",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_X_ACTIVE_OR_Y_STANDBY.value: "X-Active OR Y-Standby",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_ONE_ACTIVE_OR_X_STANDBY.value: "1-Active OR Y-Standby",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_ONE_ACTIVE_OR_ONE_STANDBY.value: "1-Active OR 1-Standby",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_X_ACTIVE.value: "X-Active",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_ONE_ACTIVE.value: "1-Active",
        clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_NON_PREINSTANTIABLE.value: "Non Preinstantiable"
    }

    for key, item in capLut.items():
        if S == key:
            return item
    return "Unknown"

def CL_AMS_STRING_CSI_FLAGS(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    flagLut = {
        clAmsTypes.CL_AMS_CSI_FLAG_ADD_ONE: "ADD_ONE",
        clAmsTypes.CL_AMS_CSI_FLAG_TARGET_ONE: "TARGET_ONE",
        clAmsTypes.CL_AMS_CSI_FLAG_TARGET_ALL: "TARGET_ALL"
    }

    for key, item in flagLut.items():
        if S == key:
            return item
    return "Unknown"

def CL_AMS_STRING_CSI_FLAGS(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    flagLut = {
        clAmsTypes.eClAmsCSITransitionDescriptorT.CL_AMS_CSI_NEW_ASSIGN.value: "NEW_ASSIGN",
        clAmsTypes.eClAmsCSITransitionDescriptorT.CL_AMS_CSI_QUIESCED.value: "CSI_QUIESCED",
        clAmsTypes.eClAmsCSITransitionDescriptorT.CL_AMS_CSI_NOT_QUIESCED.value: "CSI_NOT_QUIESCED",
        clAmsTypes.eClAmsCSITransitionDescriptorT.CL_AMS_CSI_STILL_ACTIVE.value: "CSI_STILL_ACTIVE"
    }

    for key, item in flagLut.items():
        if S == key:
            return item
    return "Unknown"

def CL_AMS_STRING_ENTITY_TYPE(S):
    if isinstance(S, clCommon.ClInt32T):
        S = S.value
    typeLut = {
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_ENTITY.value: "entity",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_NODE.value: "node",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG.value: "sg",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU.value: "su",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI.value: "si",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP.value: "comp",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI.value: "csi",
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CLUSTER.value: "cluster"
    }

    for key, item in typeLut.items():
        if S == key:
            return item
    return "Unknown"

# TODO: there're remaining codes in the original header file
