import clUtils
import saAis
import clCommon

import ctypes

ClAmsMgmtStateT = saAis.SaInt32T
class eClAmsMgmtStateT(clUtils.CEnum):
    CL_AMS_MGMT_STATE_NONE                      = 0,
    CL_AMS_MGMT_STATE_DISABLED                  = 1,
    CL_AMS_MGMT_STATE_ENABLED                   = 2

ClAmsAdminStateT = saAis.SaInt32T
class eClAmsAdminStateT(clUtils.CEnum):
    CL_AMS_ADMIN_STATE_NONE                     = 0,
    CL_AMS_ADMIN_STATE_UNLOCKED                 = 1,
    CL_AMS_ADMIN_STATE_LOCKED_A                 = 2,
    CL_AMS_ADMIN_STATE_LOCKED_I                 = 3,
    CL_AMS_ADMIN_STATE_SHUTTINGDOWN             = 4,
    CL_AMS_ADMIN_STATE_MAX                      = 5

ClAmsPresenceStateT = saAis.SaInt32T
class eClAmsPresenceStateT(clUtils.CEnum):
    CL_AMS_PRESENCE_STATE_NONE                  = 0,
    CL_AMS_PRESENCE_STATE_UNINSTANTIATED        = 1,
    CL_AMS_PRESENCE_STATE_INSTANTIATING         = 2,
    CL_AMS_PRESENCE_STATE_INSTANTIATED          = 3,
    CL_AMS_PRESENCE_STATE_TERMINATING           = 4,
    CL_AMS_PRESENCE_STATE_RESTARTING            = 5,
    CL_AMS_PRESENCE_STATE_INSTANTIATION_FAILED  = 6,
    CL_AMS_PRESENCE_STATE_TERMINATION_FAILED    = 7

    # The following are not defined by SAF

    CL_AMS_PRESENCE_STATE_ABSENT                = 0,
    CL_AMS_PRESENCE_STATE_FAULT                 = 8,
    CL_AMS_PRESENCE_STATE_FAULT_WTC             = 9,
    CL_AMS_PRESENCE_STATE_FAULT_WTR             = 10

ClAmsOperStateT = saAis.SaInt32T
class eClAmsOperStateT(clUtils.CEnum):
    CL_AMS_OPER_STATE_NONE                      = 0,
    CL_AMS_OPER_STATE_ENABLED                   = 1,
    CL_AMS_OPER_STATE_DISABLED                  = 2

ClAmsHAStateT = saAis.SaInt32T
class eClAmsHAStateT(clUtils.CEnum):
    CL_AMS_HA_STATE_NONE                        = 0,
    CL_AMS_HA_STATE_ACTIVE                      = 1,
    CL_AMS_HA_STATE_STANDBY                     = 2,
    CL_AMS_HA_STATE_QUIESCED                    = 3,
    CL_AMS_HA_STATE_QUIESCING                   = 4

ClAmsReadinessStateT = saAis.SaInt32T
class eClAmsReadinessStateT(clUtils.CEnum):
    CL_AMS_READINESS_STATE_NONE                 = 0,
    CL_AMS_READINESS_STATE_OUTOFSERVICE         = 1,
    CL_AMS_READINESS_STATE_INSERVICE            = 2,
    CL_AMS_READINESS_STATE_STOPPING             = 3

ClAmsServiceStateT = saAis.SaInt32T
class eClAmsServiceStateT(clUtils.CEnum):
    CL_AMS_SERVICE_STATE_NONE                   = 0,
    CL_AMS_SERVICE_STATE_RUNNING                = 1,
    CL_AMS_SERVICE_STATE_STOPPED                = 2,
    CL_AMS_SERVICE_STATE_STARTINGUP             = 3,
    CL_AMS_SERVICE_STATE_SHUTTINGDOWN           = 4,
    CL_AMS_SERVICE_STATE_UNAVAILABLE            = 5,
    CL_AMS_SERVICE_STATE_HOT_STANDBY            = 6

ClAmsNodeClassT = saAis.SaInt32T
class eClAmsNodeClassT(clUtils.CEnum):
    CL_AMS_NODE_CLASS_NONE                      = 0,
    CL_AMS_NODE_CLASS_A                         = 1,
    CL_AMS_NODE_CLASS_B                         = 2,
    CL_AMS_NODE_CLASS_C                         = 3,
    CL_AMS_NODE_CLASS_D                         = 4,
    CL_AMS_NODE_CLASS_MAX                       = 5

ClAmsNodeClusterMemberT = saAis.SaInt32T
class eClAmsNodeClusterMemberT(clUtils.CEnum):
    CL_AMS_NODE_IS_NOT_CLUSTER_MEMBER           = 0,
    CL_AMS_NODE_IS_CLUSTER_MEMBER               = 1,
    CL_AMS_NODE_IS_LEAVING_CLUSTER              = 2

ClAmsSGRedundancyModelT = saAis.SaInt32T
class eClAmsSGRedundancyModelT(clUtils.CEnum):
    CL_AMS_SG_REDUNDANCY_MODEL_NONE             = 0,
    CL_AMS_SG_REDUNDANCY_MODEL_NO_REDUNDANCY    = 1,
    CL_AMS_SG_REDUNDANCY_MODEL_TWO_N            = 2,
    CL_AMS_SG_REDUNDANCY_MODEL_M_PLUS_N         = 3,
    CL_AMS_SG_REDUNDANCY_MODEL_N_WAY            = 4,
    CL_AMS_SG_REDUNDANCY_MODEL_N_WAY_ACTIVE     = 5,
    CL_AMS_SG_REDUNDANCY_MODEL_CUSTOM           = 6, #user controlled redundancy mode
    CL_AMS_SG_REDUNDANCY_MODEL_MAX              = 7

ClAmsSGLoadingStrategyT = saAis.SaInt32T
class eClAmsSGLoadingStrategyT(clUtils.CEnum):
    CL_AMS_SG_LOADING_STRATEGY_NONE                 = 0,  #invalid
    CL_AMS_SG_LOADING_STRATEGY_LEAST_SI_PER_SU      = 1,  #all models
    CL_AMS_SG_LOADING_STRATEGY_LEAST_SU_ASSIGNED    = 2,  #all models
    CL_AMS_SG_LOADING_STRATEGY_LEAST_LOAD_PER_SU    = 3,  #all models
    CL_AMS_SG_LOADING_STRATEGY_BY_SI_PREFERENCE     = 4,  #n-way-* only
    CL_AMS_SG_LOADING_STRATEGY_USER_DEFINED         = 5,   #user-callout
    CL_AMS_SG_LOADING_STRATEGY_MAX                  = 6

ClAmsCompCapModelT = saAis.SaInt32T
class eClAmsCompCapModelT(clUtils.CEnum):
    CL_AMS_COMP_CAP_X_ACTIVE_AND_Y_STANDBY      = 1,
    CL_AMS_COMP_CAP_X_ACTIVE_OR_Y_STANDBY       = 2,
    CL_AMS_COMP_CAP_ONE_ACTIVE_OR_X_STANDBY     = 3,
    CL_AMS_COMP_CAP_ONE_ACTIVE_OR_ONE_STANDBY   = 4,
    CL_AMS_COMP_CAP_X_ACTIVE                    = 5,
    CL_AMS_COMP_CAP_ONE_ACTIVE                  = 6,
    CL_AMS_COMP_CAP_NON_PREINSTANTIABLE         = 7,
    CL_AMS_COMP_CAP_MAX                         = 8

def CL_AMS_COMP_CAP_ONE_HA_STATE(X):
    if X in [eClAmsCompCapModelT.CL_AMS_COMP_CAP_X_ACTIVE_OR_Y_STANDBY,
             eClAmsCompCapModelT.CL_AMS_COMP_CAP_ONE_ACTIVE_OR_ONE_STANDBY,
             eClAmsCompCapModelT.CL_AMS_COMP_CAP_ONE_ACTIVE_OR_X_STANDBY]:
        return clCommon.CL_TRUE
    return clCommon.CL_FALSE

ClAmsCompPropertyT = saAis.SaInt32T
class eClAmsCompPropertyT(clUtils.CEnum):
    CL_AMS_COMP_PROPERTY_SA_AWARE                           = 1,
    CL_AMS_COMP_PROPERTY_PROXIED_PREINSTANTIABLE            = 2,
    CL_AMS_COMP_PROPERTY_PROXIED_NON_PREINSTANTIABLE        = 3,
    CL_AMS_COMP_PROPERTY_NON_PROXIED_NON_PREINSTANTIABLE    = 4,
    CL_AMS_COMP_PROPERTY_MAX                                = 5

ClAmsCompHealthcheckInvocationT = saAis.SaInt32T
class eClAmsCompHealthcheckInvocationT(clUtils.CEnum):
    CL_AMS_COMP_HEALTHCHECK_AMF_INVOKED         = 1,
    CL_AMS_COMP_HEALTHCHECK_CLIENT_INVOKED      = 2

CL_AMS_HEALTHCHECK_KEY_MAX = 32

class ClAmsCompHealthcheckKeyT(ctypes.Structure):
    _fields_ = [
        ("key", clCommon.ClUint8T * CL_AMS_HEALTHCHECK_KEY_MAX),
        ("keyLen", clCommon.ClUint16T)
    ]

ClAmsRecoveryT = saAis.SaInt32T
class eClAmsRecoveryT(clUtils.CEnum):
    # Recommended recovery actions for local components as defined by SAF

    CL_AMS_RECOVERY_NONE                        = 0,
    CL_AMS_RECOVERY_NO_RECOMMENDATION           = 1,
    CL_AMS_RECOVERY_COMP_RESTART                = 2,
    CL_AMS_RECOVERY_COMP_FAILOVER               = 3,
    CL_AMS_RECOVERY_NODE_SWITCHOVER             = 4,
    CL_AMS_RECOVERY_NODE_FAILOVER               = 5,
    CL_AMS_RECOVERY_NODE_FAILFAST               = 6,
    CL_AMS_RECOVERY_CLUSTER_RESET               = 7,
    CL_AMS_RECOVERY_APP_RESTART                 = 8,

    # Recommeded recovery actions defined by Clovis

    CL_AMS_RECOVERY_INTERNALLY_RECOVERED        = 20,
    CL_AMS_RECOVERY_SU_RESTART                  = 21,
    CL_AMS_RECOVERY_NODE_HALT                   = 22,

    # Recommended recovery actions for external components

    CL_AMS_EXTERNAL_RECOVERY_RESET              = 30,
    CL_AMS_EXTERNAL_RECOVERY_REBOOT             = 31,
    CL_AMS_EXTERNAL_RECOVERY_POWER_ON           = 32,
    CL_AMS_EXTERNAL_RECOVERY_POWER_OFF          = 33

ClAmsLocalRecoveryT = saAis.SaInt32T

CL_AMS_CSI_FLAG_ADD_ONE = 0x1
CL_AMS_CSI_FLAG_TARGET_ONE = 0x2
CL_AMS_CSI_FLAG_TARGET_ALL = 0x4

ClAmsCSIFlagsT = clCommon.ClUint32T
ClAmsCSITypeT = clCommon.ClNameT

ClAmsCSITransitionDescriptorT = saAis.SaInt32T
class eClAmsCSITransitionDescriptorT(clUtils.CEnum):
    CL_AMS_CSI_NEW_ASSIGN                       = 1,
    CL_AMS_CSI_QUIESCED                         = 2,
    CL_AMS_CSI_NOT_QUIESCED                     = 3,
    CL_AMS_CSI_STILL_ACTIVE                     = 4

class ClAmsCSIActiveDescriptorT(ctypes.Structure):
    _fields_ = [
        ("transitionDescriptor", ClAmsCSITransitionDescriptorT),
        ("activeCompName", clCommon.ClNameT),
    ]

class ClAmsCSIStandbyDescriptorT(ctypes.Structure):
    _fields_ = [
        ("activeCompName", clCommon.ClNameT),
        ("standbyRank", clCommon.ClUint32T),
    ]

class ClAmsCSIStateDescriptorT(ctypes.Union):
    _fields_ = [
        ("activeDescriptor", ClAmsCSIActiveDescriptorT),
        ("standbyDescriptor", ClAmsCSIStandbyDescriptorT),
    ]

class ClAmsCSIAttributeT(ctypes.Structure):
    _fields_ = [
        ("attributeName", ctypes.POINTER(clCommon.ClUint8T)),
        ("attributeValue", ctypes.POINTER(clCommon.ClUint8T)),
    ]

class ClAmsCSIAttributeListT(ctypes.Structure):
    _fields_ = [
        ("attribute", ctypes.POINTER(ClAmsCSIAttributeT)),
        ("numAttributes", clCommon.ClUint32T),
    ]

class ClAmsCSIDescriptorT(ctypes.Structure):
    _fields_ = [
        ("csiFlags", ClAmsCSIFlagsT),
        ("csiName", clCommon.ClNameT),
        ("csiStateDescriptor", ClAmsCSIStateDescriptorT),
        ("csiAttributeList", ClAmsCSIAttributeListT),
    ]

class ClAmsCSITypeDescriptorT(ctypes.Structure):
    _fields_ = [
        ("csiDescriptor", ClAmsCSIDescriptorT),
        ("csiType", ClAmsCSITypeT),
        ("compName", clCommon.ClNameT)
    ]

ClAmsPGTrackFlagT = saAis.SaInt32T
class eClAmsPGTrackFlagT(clUtils.CEnum):
    CL_AMS_PG_TRACK_CURRENT                     = 1,
    CL_AMS_PG_TRACK_CHANGES                     = 2,
    CL_AMS_PG_TRACK_CHANGES_ONLY                = 4

ClAmsPGChangeT = saAis.SaInt32T
class eClAmsPGChangeT(clUtils.CEnum):
    CL_AMS_PG_NO_CHANGE                         = 1,
    CL_AMS_PG_ADDED                             = 2,
    CL_AMS_PG_REMOVED                           = 3,
    CL_AMS_PG_STATE_CHANGE                      = 4

class ClAmsPGMemberT(ctypes.Structure):
    _fields_ = [
        ("compName", clCommon.ClNameT),
        ("haState", ClAmsHAStateT),
        ("rank", clCommon.ClUint32T)
    ]

class ClAmsPGNotificationT(ctypes.Structure):
    _fields_ = [
        ("member", ClAmsPGMemberT),
        ("change", ClAmsPGChangeT)
    ]

class ClAmsPGNotificationBufferT(ctypes.Structure):
    _fields_ = [
        ("numItems", clCommon.ClUint32T),
        ("notification", ctypes.POINTER(ClAmsPGNotificationT))
    ]

ClAmsMgmtCCBHandleT         = clCommon.ClHandleT
ClAmsMgmtHandleT            = clCommon.ClHandleT
ClAmsClientHandleT          = clCommon.ClHandleT
ClAmsEventHandleT           = clCommon.ClHandleT
ClAmsFaultHandleT           = clCommon.ClHandleT
ClAmsEntityHandleT          = clCommon.ClHandleT
ClAmsMgmtDBHandleT          = clCommon.ClPtrT
ClAmsMgmtCCBBatchHandleT    = clCommon.ClPtrT

class ClAmsSIDescriptorT(ctypes.Structure):
    _fields_ = [
        ("numberOfItems", clCommon.ClUint32T),
        ("csiDefinition", ctypes.POINTER(ClAmsCSITypeDescriptorT))
    ]
