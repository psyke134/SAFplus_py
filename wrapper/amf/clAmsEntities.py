import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils, clList, clHeapApi
from timer import clTimerApi
from cnt import clCntApi
from amf import clAmsTypes, clAmsSAClientApi, clCpmApi
from ioc import clIocApi
import ctypes, enum

ClAmsEntityTypeT = clCommon.ClInt32T
class eClAmsEntityTypeT(clUtils.Enum):
    CL_AMS_ENTITY_TYPE_ENTITY       = 0 # unused
    CL_AMS_ENTITY_TYPE_NODE         = 1 # A Cluster Node (system,computer)
    CL_AMS_ENTITY_TYPE_APP          = 2 # A SAF application
    CL_AMS_ENTITY_TYPE_SG           = 3 # A SAF service group
    CL_AMS_ENTITY_TYPE_SU           = 4 # A SAF service unit
    CL_AMS_ENTITY_TYPE_SI           = 5 # A SAF service instance (work assignment)
    CL_AMS_ENTITY_TYPE_COMP         = 6 # A SAF component (program)
    CL_AMS_ENTITY_TYPE_CSI          = 7 # A SAF component service instance (work assigned to a particular program)
    CL_AMS_ENTITY_TYPE_CLUSTER      = 8 # A cluster

CL_AMS_ENTITY_TYPE_MAX = 7

class ClAmsEntityOpStackT(ctypes.Structure):
    _fields_ = [
        ("numOps", clCommon.ClInt32T),
        ("opList", clList.ClListHeadT)
    ]

class ClAmsEntityConfigT(ctypes.Structure):
    _fields_ = [
        ("type", ClAmsEntityTypeT),
        ("name", clCommon.ClNameT),
        ("debugFlags", clCommon.ClUint8T)
    ]

class ClAmsEntityStatusT(ctypes.Structure):
    _fields_ = [
        ("epoch", clCommon.ClTimeT),
        ("timerCount", clCommon.ClUint32T),
        ("opStack", ClAmsEntityOpStackT)
    ]

ClAmsEntityT = ClAmsEntityConfigT

ClAmsEntityCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, ctypes.POINTER(ClAmsEntityT))
ClAmsEntityCallbackExtendedT = ctypes.CFUNCTYPE(clCommon.ClRcT, ctypes.POINTER(ClAmsEntityT), clCommon.ClPtrT)

class ClAmsEntityMethodsT(ctypes.Structure):
    _fields_ = [
        ("printOut", ClAmsEntityCallbackT),
        ("validateConfig", ClAmsEntityCallbackT),
        ("validateRelationships", ClAmsEntityCallbackT)
    ]

class ClAmsEntityOpT(ctypes.Structure):
    CL_AMS_ENTITY_OP_REMOVE_MPLUSN = 0x1
    CL_AMS_ENTITY_OP_SWAP_REMOVE_MPLUSN = 0x2
    CL_AMS_ENTITY_OP_REDUCE_REMOVE_MPLUSN = 0x4
    CL_AMS_ENTITY_OP_ACTIVE_REMOVE_MPLUSN = 0x8
    CL_AMS_ENTITY_OP_REMOVES_MPLUSN = (CL_AMS_ENTITY_OP_REMOVE_MPLUSN
                                       | CL_AMS_ENTITY_OP_SWAP_REMOVE_MPLUSN
                                       | CL_AMS_ENTITY_OP_REDUCE_REMOVE_MPLUSN)
    CL_AMS_ENTITY_OP_SWAP_ACTIVE_MPLUSN = 0x10
    CL_AMS_ENTITY_OP_SI_REASSIGN_MPLUSN = 0x20
    CL_AMS_ENTITY_OP_ACTIVE_REMOVE_REF_MPLUSN = 0x40

    _fields_ = [
        ("op", clCommon.ClUint32T),
        ("dataSize", clCommon.ClUint32T),
        ("data", clCommon.ClPtrT),
        ("list", clList.ClListHeadT)
    ]

class ClAmsEntityRemoveOpT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityT),
        ("sisRemoved", clCommon.ClInt32T),
        ("switchoverMode", clCommon.ClUint32T),
        ("error", clCommon.ClUint32T)
    ]

class ClAmsEntitySwapRemoveOpT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityT),
        ("sisRemoved", clCommon.ClInt32T),
        ("numOtherSIs", clCommon.ClUint32T),
        ("otherSIs", ctypes.POINTER(ClAmsEntityT))
    ]

class ClAmsEntityReduceRemoveOpT(ctypes.Structure):
    _fields_ = [
        ("sisRemoved", clCommon.ClInt32T)
    ]

class ClAmsEntitySwapActiveOpT(ctypes.Structure):
    _fields_ = [
        ("sisReassigned", clCommon.ClInt32T)
    ]

class ClAmsSIReassignOpT(ctypes.Structure):
    _fields_ = [
        ("su", ClAmsEntityT)
    ]

CL_AMS_SG_ADJUST_DURATION = 3000
CL_AMS_SG_ADJUST_PROBATION = CL_AMS_SG_ADJUST_DURATION
CL_AMS_SU_ASSIGNMENT_DELAY = 3000

ClAmsEntityTimerTypeT = clCommon.ClInt32T
class eClAmsEntityTimerTypeT(clUtils.Enum):
    CL_AMS_NODE_TIMER_SUFAILOVER                        = 1

    CL_AMS_SG_TIMER_INSTANTIATE                         = 10
    CL_AMS_SG_TIMER_ADJUST                              = 11
    CL_AMS_SG_TIMER_ADJUST_PROBATION                    = 12
    CL_AMS_SU_TIMER_COMPRESTART                         = 20
    CL_AMS_SU_TIMER_SURESTART                           = 21
    CL_AMS_SU_TIMER_PROBATION                           = 22
    CL_AMS_SU_TIMER_ASSIGNMENT                          = 23

    CL_AMS_COMP_TIMER_INSTANTIATE                       = 40
    CL_AMS_COMP_TIMER_TERMINATE                         = 41
    CL_AMS_COMP_TIMER_CLEANUP                           = 42
    CL_AMS_COMP_TIMER_AMSTART                           = 43
    CL_AMS_COMP_TIMER_AMSTOP                            = 44
    CL_AMS_COMP_TIMER_QUIESCINGCOMPLETE                 = 45
    CL_AMS_COMP_TIMER_CSISET                            = 46
    CL_AMS_COMP_TIMER_CSIREMOVE                         = 47
    CL_AMS_COMP_TIMER_PROXIEDCOMPINSTANTIATE            = 48
    CL_AMS_COMP_TIMER_PROXIEDCOMPCLEANUP                = 49
    CL_AMS_COMP_TIMER_INSTANTIATEDELAY                  = 50
    CL_AMS_COMP_TIMER_MAX                               = 51

class ClAmsEntityTimerT(ctypes.Structure):
    _fields_ = [
        ("type", ClAmsEntityTimerTypeT),
        ("count", clCommon.ClTimeT),
        ("handle", clTimerApi.ClTimerHandleT),
        ("entity", ctypes.POINTER(ClAmsEntityT)),
        ("currentOp", clCommon.ClUint32T),
    ]

ClAmsEntityTimerCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, ctypes.POINTER(ClAmsEntityTimerT))

class ClAmsEntityRefT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityT),
        ("ptr", ctypes.CFUNCTYPE(ClAmsEntityT)),
        ("nodeHandle", clCntApi.ClCntNodeHandleT)
    ]

ClAmsEntityRefTypeT = clCommon.ClInt32T
class eClAmsEntityRefTypeT(clUtils.Enum):
    CL_AMS_ENTITY_REF_TYPE_ENTITY   = 0
    CL_AMS_ENTITY_REF_TYPE_NODE     = 1
    CL_AMS_ENTITY_REF_TYPE_APP      = 2
    CL_AMS_ENTITY_REF_TYPE_SG       = 3
    CL_AMS_ENTITY_REF_TYPE_SU       = 4
    CL_AMS_ENTITY_REF_TYPE_SI       = 5
    CL_AMS_ENTITY_REF_TYPE_COMP     = 6
    CL_AMS_ENTITY_REF_TYPE_CSI      = 7
    CL_AMS_ENTITY_REF_TYPE_SUSI     = 8
    CL_AMS_ENTITY_REF_TYPE_SISU     = 9
    CL_AMS_ENTITY_REF_TYPE_COMPCSI  = 10
    CL_AMS_ENTITY_REF_TYPE_CSICOMP  = 11

CL_AMS_ENTITY_REF_TYPE_MAX = 11

class ClAmsEntityListT(ctypes.Structure):
    _fields_ = [
        ("type", ClAmsEntityTypeT),
        ("isRankedList", clCommon.ClBoolT),
        ("isValid", clCommon.ClBoolT),
        ("numEntities", clCommon.ClUint32T),
        ("list", clCntApi.ClCntHandleT)
    ]

ClAmsEntityListTypeT = clCommon.ClInt32T
class eClAmsEntityListTypeT(clUtils.Enum):
    CL_AMS_START_LIST = 0

    #
    # Config lists
    #

    CL_AMS_CONFIG_LIST_START = 1
    CL_AMS_NODE_CONFIG_NODE_DEPENDENT_LIST = 2
    CL_AMS_NODE_CONFIG_NODE_DEPENDENCIES_LIST = 3
    CL_AMS_NODE_CONFIG_SU_LIST = 4
    CL_AMS_SG_CONFIG_SU_LIST = 5
    CL_AMS_SG_CONFIG_SI_LIST = 6
    CL_AMS_SU_CONFIG_COMP_LIST = 7
    CL_AMS_SI_CONFIG_SU_RANK_LIST = 8
    CL_AMS_SI_CONFIG_SI_DEPENDENTS_LIST = 9
    CL_AMS_SI_CONFIG_SI_DEPENDENCIES_LIST = 10
    CL_AMS_SI_CONFIG_CSI_LIST = 11
    CL_AMS_CSI_CONFIG_NVP_LIST = 12
    CL_AMS_CSI_CONFIG_CSI_DEPENDENTS_LIST = 13
    CL_AMS_CSI_CONFIG_CSI_DEPENDENCIES_LIST = 14
    CL_AMS_CONFIG_LIST_END = 15

    #
    # Status lists
    #

    CL_AMS_SG_STATUS_INSTANTIABLE_SU_LIST = 16
    CL_AMS_SG_STATUS_INSTANTIATED_SU_LIST = 17
    CL_AMS_SG_STATUS_IN_SERVICE_SPARE_SU_LIST = 18
    CL_AMS_SG_STATUS_ASSIGNED_SU_LIST = 19
    CL_AMS_SG_STATUS_FAULTY_SU_LIST = 20
    CL_AMS_SU_STATUS_SI_LIST = 21
    CL_AMS_SI_STATUS_SU_LIST = 22
    CL_AMS_COMP_STATUS_CSI_LIST = 23
    CL_AMS_CSI_STATUS_PG_LIST = 24

    #
    # Start of entity all list types.
    #

    CL_AMS_SG_LIST = 25 # List of all service groups
    CL_AMS_SI_LIST = 26 # List of all service instances (work assignment)
    CL_AMS_NODE_LIST = 27 # List of all nodes (computers)
    CL_AMS_SU_LIST = 28 # List of all service units
    CL_AMS_COMP_LIST = 29 # List of all components (program)
    CL_AMS_CSI_LIST = 30 # List of all component service instances (work assigned to one program)

    #
    # End of entity all list types.
    #

    CL_AMS_ENTITY_LIST_ALL_END = 31

    #
    # Internal entity list types.
    #

    CL_AMS_CSI_PGTRACK_CLIENT_LIST = 32
    CL_AMS_SU_STATUS_SI_EXTENDED_LIST = 33
    CL_AMS_SI_STATUS_SU_EXTENDED_LIST = 34
    CL_AMS_END_LIST = 35

ClAmsEntityRefCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, ctypes.POINTER(ClAmsEntityRefT), ClAmsEntityListTypeT)

class ClAmsEntityParamsT(ctypes.Structure):
    _fields_ = [
        ("typeString", clCommon.ClNameT),
        ("defaultConfig", clCommon.ClPtrT),
        ("configSize", clCommon.ClUint32T),
        ("defaultMethods", clCommon.ClPtrT),
        ("methodSize", clCommon.ClUint32T),
        ("entitySize", clCommon.ClUint32T)
    ]

#
# AMS NODE
#

class ClAmsNodeConfigT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityConfigT),
        ("adminState", clAmsTypes.ClAmsAdminStateT),
        ("id", clCommon.ClUint32T),
        ("classType", clAmsTypes.ClAmsNodeClassT),
        ("subClassType", clCommon.ClNameT),
        ("isSwappable", clCommon.ClBoolT),
        ("isRestartable", clCommon.ClBoolT),
        ("autoRepair", clCommon.ClBoolT),
        ("isASPAware", clCommon.ClBoolT),
        ("suFailoverDuration", clCommon.ClTimeT),
        ("suFailoverCountMax", clCommon.ClUint32T),
        ("nodeDependentsList", ClAmsEntityListT),
        ("nodeDependenciesList", ClAmsEntityListT),
        ("suList", ClAmsEntityListT)
    ]

class ClAmsNodeStatusT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityStatusT),
        ("presenceState", clAmsTypes.ClAmsPresenceStateT),
        ("operState", clAmsTypes.ClAmsOperStateT),
        ("isClusterMember", clAmsTypes.ClAmsNodeClusterMemberT),
        ("wasMemberBefore", clCommon.ClBoolT),
        ("recovery", clAmsTypes.ClAmsLocalRecoveryT),
        ("alarmHandle", clCommon.ClUint32T),
        ("suFailoverCount", clCommon.ClUint32T),
        ("suFailoverTimer", ClAmsEntityTimerT),
        ("numInstantiatedSUs", clCommon.ClUint32T),
        ("numAssignedSUs", clCommon.ClUint32T)
    ]

class ClAmsNodeMethodsT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityMethodsT),
        ("suFailoverTimeout", ClAmsEntityTimerCallbackT)
    ]

class ClAmsNodeT(ctypes.Structure):
    _fields_ = [
        ("config", ClAmsNodeConfigT),
        ("status", ClAmsNodeStatusT),
        ("methods", ClAmsNodeMethodsT)
    ]

#
# AMS APPLICATION
#

class ClAmsAppConfigT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityConfigT)
    ]

class ClAmsAppStatusT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityStatusT)
    ]

class ClAmsAppMethodsT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityMethodsT)
    ]

class ClAmsAppConfigT(ctypes.Structure):
    _fields_ = [
        ("config", ClAmsAppConfigT),
        ("status", ClAmsAppStatusT),
        ("methods", ClAmsAppMethodsT)
    ]

#
# AMS SERVICE GROUP
#

class ClAmsSGConfigT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityConfigT),

        ("adminState", clAmsTypes.ClAmsAdminStateT),
        ("redundancyModel", clAmsTypes.ClAmsSGRedundancyModelT),
        ("loadingStrategy", clAmsTypes.ClAmsSGLoadingStrategyT),
        ("failbackOption", clCommon.ClBoolT),
        ("autoRepair", clCommon.ClBoolT),
        ("instantiateDuration", clCommon.ClTimeT),
        ("numPrefActiveSUs", clCommon.ClUint32T),
        ("numPrefStandbySUs", clCommon.ClUint32T),
        ("numPrefInserviceSUs", clCommon.ClUint32T),
        ("numPrefAssignedSUs", clCommon.ClUint32T),
        ("numPrefActiveSUsPerSI", clCommon.ClUint32T),
        ("maxActiveSIsPerSU", clCommon.ClUint32T),
        ("maxStandbySIsPerSU", clCommon.ClUint32T),
        ("compRestartDuration", clCommon.ClTimeT),
        ("compRestartCountMax", clCommon.ClUint32T),
        ("suRestartDuration", clCommon.ClTimeT),
        ("suRestartCountMax", clCommon.ClUint32T),
        ("isCollocationAllowed", clCommon.ClBoolT),
        ("alpha", clCommon.ClUint32T),
        ("autoAdjust", clCommon.ClBoolT),
        ("autoAdjustProbation", clCommon.ClTimeT),
        ("reductionProcedure", clCommon.ClBoolT),
        ("parentApp", ClAmsEntityRefT),
        ("maxFailovers", clCommon.ClUint32T),
        ("failoverDuration", clCommon.ClTimeT),
        ("beta", clCommon.ClUint32T),
        ("suList", ClAmsEntityListT),
        ("siList", ClAmsEntityListT)
    ]

ClAmsSGConfigT_4_1_0 = ClAmsSGConfigT
ClAmsSGConfigT_5_0_0 = ClAmsSGConfigT

class ClAmsSGFailoverHistoryKeyT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityT),
        ("index", clCommon.ClUint32T)
    ]

class ClAmsSGFailoverHistoryT(ctypes.Structure):
    _fields_ = [
        ("list", clList.ClListHeadT),
        ("entity", ClAmsEntityT),
        ("index", clCommon.ClUint32T),
        ("timer", clTimerApi.ClTimerHandleT),
        ("numFailovers", clCommon.ClUint32T),
    ]

class ClAmsSGStatusT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityStatusT),
        ("isStarted", clCommon.ClBoolT),
        ("instantiateTimer", ClAmsEntityTimerT),
        ("adjustTimer", ClAmsEntityTimerT),
        ("adjustProbationTimer", ClAmsEntityTimerT),
        ("assignmentTimer", ClAmsEntityTimerT),
        ("instantiableSUList", ClAmsEntityListT),
        ("instantiatedSUList", ClAmsEntityListT),
        ("inserviceSpareSUList", ClAmsEntityListT),
        ("assignedSUList", ClAmsEntityListT),
        ("faultySUList", ClAmsEntityListT),


        ("numCurrActiveSUs", clCommon.ClUint32T),
        ("numCurrStandbySUs", clCommon.ClUint32T),
        ("failoverHistoryIndex", clCommon.ClUint32T),
        ("failoverHistoryCount", clCommon.ClInt32T),
        ("failoverHistory", clList.ClListHeadT),
    ]

ClAmsSGStatusT_4_1_0 = ClAmsSGStatusT

class ClAmsSGMethodsT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityMethodsT),

        ("instantiateTimeout", ClAmsEntityTimerCallbackT),
        ("adjustTimeout", ClAmsEntityTimerCallbackT),
        ("adjustProbationTimeout", ClAmsEntityTimerCallbackT)
    ]

class ClAmsSGT(ctypes.Structure):
    _fields_ = [
        ("config", ClAmsSGConfigT),
        ("status", ClAmsSGStatusT),
        ("methods", ClAmsSGMethodsT)
    ]

ClAmsSGT_4_1_0 = ClAmsSGT
ClAmsSGT_5_0_0 = ClAmsSGT

#
# AMS SERVICE UINT
#

class ClAmsSUSIRefT(ctypes.Structure):
    _fields_ = [
        ("entityRef", ClAmsEntityRefT),
        ("haState", clAmsTypes.ClAmsHAStateT),
        ("numActiveCSIs", clCommon.ClUint32T),
        ("numStandbyCSIs", clCommon.ClUint32T),
        ("numQuiescedCSIs", clCommon.ClUint32T),
        ("numQuiescingCSIs", clCommon.ClUint32T),
        ("rank", clCommon.ClUint32T)
    ]

class ClAmsSUSIExtendedRefT(ctypes.Structure):
    _fields_ = [
        ("entityRef", ClAmsEntityRefT),
        ("haState", clAmsTypes.ClAmsHAStateT),
        ("numActiveCSIs", clCommon.ClUint32T),
        ("numStandbyCSIs", clCommon.ClUint32T),
        ("numQuiescedCSIs", clCommon.ClUint32T),
        ("numQuiescingCSIs", clCommon.ClUint32T),
        ("numCSIs", clCommon.ClUint32T),
        ("rank", clCommon.ClUint32T),
        ("pendingInvocations", clCommon.ClUint32T)
    ]

class ClAmsSUConfigT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityConfigT),

        ("adminState", clAmsTypes.ClAmsAdminStateT),
        ("rank", clCommon.ClUint32T),
        ("numComponents", clCommon.ClUint32T),
        ("isPreinstantiable", clCommon.ClBoolT),
        ("isRestartable", clCommon.ClBoolT),

        ("isContainerSU", clCommon.ClBoolT),

        ("compList", ClAmsEntityListT),
        ("parentSG", ClAmsEntityRefT),
        ("parentNode", ClAmsEntityRefT)
    ]

class ClAmsSUStatusT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityStatusT),

        ("presenceState", clAmsTypes.ClAmsPresenceStateT),
        ("operState", clAmsTypes.ClAmsOperStateT),
        ("readinessState", clAmsTypes.ClAmsReadinessStateT),
        ("recovery", clAmsTypes.ClAmsLocalRecoveryT),
        ("numActiveSIs", clCommon.ClUint32T),
        ("numStandbySIs", clCommon.ClUint32T),
        ("numQuiescedSIs", clCommon.ClUint32T),
        ("compRestartCount", clCommon.ClUint32T),
        ("compRestartTimer", ClAmsEntityTimerT),
        ("suRestartCount", clCommon.ClUint32T),
        ("suRestartTimer", ClAmsEntityTimerT),
        ("suProbationTimer", ClAmsEntityTimerT),
        ("suAssignmentTimer", ClAmsEntityTimerT),
        ("numInstantiatedComp", clCommon.ClUint32T),
        ("numPIComp", clCommon.ClUint32T),
        ("instantiateLevel", clCommon.ClUint32T),
        ("numWaitAdjustments", clCommon.ClUint32T),
        ("numDelayAssignments", clCommon.ClUint32T),
        ("siList", ClAmsEntityListT)
    ]

class ClAmsSUMethodsT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityMethodsT),

        ("suRestartTimeout", ClAmsEntityTimerCallbackT),
        ("compRestartTimeout", ClAmsEntityTimerCallbackT),
        ("suProbationTimeout", ClAmsEntityTimerCallbackT),
        ("suAssignmentTimeout", ClAmsEntityTimerCallbackT)
    ]

class ClAmsSUMethodsT(ctypes.Structure):
    _fields_ = [
        ("config", ClAmsSUConfigT),
        ("status", ClAmsSUStatusT),
        ("methods", ClAmsSUMethodsT)
    ]

#
# AMS SERVICE INSTANCE
#

class ClAmsSISURefT(ctypes.Structure):
    _fields_ = [
        ("entityRef", ClAmsEntityRefT),
        ("rank", clCommon.ClUint32T),
        ("haState", clAmsTypes.ClAmsHAStateT)
    ]

class ClAmsSISUExtendedRefT(ctypes.Structure):
    _fields_ = [
        ("entityRef", ClAmsEntityRefT),
        ("rank", clCommon.ClUint32T),
        ("haState", clAmsTypes.ClAmsHAStateT),
        ("pendingInvocations", clCommon.ClUint32T)
    ]

class ClAmsSIConfigT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityConfigT),

        ("adminState", clAmsTypes.ClAmsAdminStateT),
        ("rank", clCommon.ClUint32T),
        ("numCSIs", clCommon.ClUint32T),
        ("numStandbyAssignments", clCommon.ClUint32T),
        ("standbyAssignmentOrder", clCommon.ClUint32T),
        ("parentSG", ClAmsEntityRefT),
        ("suList", ClAmsEntityListT),
        ("siDependentsList", ClAmsEntityListT),
        ("siDependenciesList", ClAmsEntityListT),
        ("csiList", ClAmsEntityListT)
    ]

class ClAmsSIStatusT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityStatusT),

        ("operState", clAmsTypes.ClAmsOperStateT),
        ("numActiveAssignments", clCommon.ClUint32T),
        ("numStandbyAssignments", clCommon.ClUint32T),
        ("suList", ClAmsEntityListT)
    ]

class ClAmsSIMethodsT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityMethodsT)
    ]

class ClAmsSIT(ctypes.Structure):
    _fields_ = [
        ("config", ClAmsSIConfigT),
        ("status", ClAmsSIStatusT),
        ("methods", ClAmsSIMethodsT)
    ]

#
# AMS COMPONENT
#

class ClAmsCompCSIRefT(ctypes.Structure):
    _fields_ = [
        ("entityRef", ClAmsEntityRefT),
        ("haState", clAmsTypes.ClAmsHAStateT),
        ("tdescriptor", clAmsTypes.ClAmsCSITransitionDescriptorT),
        ("rank", clCommon.ClUint32T),

        ("activeComp", ctypes.POINTER(ClAmsEntityT)),
        ("pendingOp", clCommon.ClUint16T)
    ]

class ClAmsCompTimerDurationsT(ctypes.Structure):
    _fields_ = [
        ("instantiate", clCommon.ClTimeT),
        ("terminate", clCommon.ClTimeT),
        ("cleanup", clCommon.ClTimeT),
        ("amStart", clCommon.ClTimeT),
        ("amStop", clCommon.ClTimeT),
        ("quiescingComplete", clCommon.ClTimeT),
        ("csiSet", clCommon.ClTimeT),
        ("csiRemove", clCommon.ClTimeT),
        ("proxiedCompInstantiate", clCommon.ClTimeT),
        ("proxiedCompCleanup", clCommon.ClTimeT),
        ("instantiateDelay", clCommon.ClTimeT)
    ]

class ClAmsCompTimersT(ctypes.Structure):
    _fields_ = [
        ("instantiate", ClAmsEntityTimerT),
        ("terminate", ClAmsEntityTimerT),
        ("cleanup", ClAmsEntityTimerT),
        ("amStart", ClAmsEntityTimerT),
        ("amStop", ClAmsEntityTimerT),
        ("quiescingComplete", ClAmsEntityTimerT),
        ("csiSet", ClAmsEntityTimerT),
        ("csiRemove", ClAmsEntityTimerT),
        ("proxiedCompInstantiate", ClAmsEntityTimerT),
        ("proxiedCompCleanup", ClAmsEntityTimerT),
        ("instantiateDelay", ClAmsEntityTimerT)
    ]

class ClAmsCompConfigT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityConfigT),
        ("numSupportedCSITypes", clCommon.ClUint32T),
        ("pSupportedCSITypes", ctypes.POINTER(clCommon.ClNameT)),
        ("proxyCSIType", clCommon.ClNameT),
        ("capabilityModel", clAmsTypes.ClAmsCompCapModelT),
        ("property", clAmsTypes.ClAmsCompPropertyT),
        ("isRestartable", clCommon.ClBoolT),
        ("nodeRebootCleanupFail", clCommon.ClBoolT),
        ("instantiateLevel", clCommon.ClUint32T),
        ("numMaxInstantiate", clCommon.ClUint32T),
        ("numMaxInstantiateWithDelay", clCommon.ClUint32T),
        ("numMaxTerminate", clCommon.ClUint32T),
        ("numMaxAmStart", clCommon.ClUint32T),
        ("numMaxAmStop", clCommon.ClUint32T),
        ("numMaxActiveCSIs", clCommon.ClUint32T),
        ("numMaxStandbyCSIs", clCommon.ClUint32T),
        ("timeouts", ClAmsCompTimerDurationsT),
        ("recoveryOnTimeout", clAmsTypes.ClAmsLocalRecoveryT),
        ("parentSU", ClAmsEntityRefT),
        ("instantiateCommand", clCommon.ClCharT * clCommon.CL_MAX_NAME_LENGTH)
    ]

    def __init__(self, *args, **kw):
        self._c_owned = False
        super().__init__(*args, **kw)

    def _freeSpCsiTypes(self):
        if self.pSupportedCSITypes and self._c_owned:    #valid ptr and not python-owned
            clHeapApi.clHeapFree(self.pSupportedCSITypes)

    def __setattr__(self, name, value):
        if name == "pSupportedCSITypes":
            self._freeSpCsiTypes()
            self._c_owned = False
        return super().__setattr__(name, value)

    def __del__(self):
        self._freeSpCsiTypes()

class ClAmsCompStatusT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityStatusT),
        ("presenceState", clAmsTypes.ClAmsPresenceStateT),
        ("operState", clAmsTypes.ClAmsOperStateT),
        ("readinessState", clAmsTypes.ClAmsLocalRecoveryT),
        ("recovery", clCommon.ClUint32T),
        ("alarmHandle", clCommon.ClUint32T),
        ("numActiveCSIs", clCommon.ClUint32T),
        ("numStandbyCSIs", clCommon.ClUint32T),
        ("numQuiescingCSIs", clCommon.ClUint32T),
        ("numQuiescedCSIs", clCommon.ClUint32T),
        ("restartCount", clCommon.ClUint32T),
        ("failoverCount", clCommon.ClUint32T),
        ("instantiateCount", clCommon.ClUint32T),
        ("instantiateDelayCount", clCommon.ClUint32T),
        ("amStartCount", clCommon.ClUint32T),
        ("amStopCount", clCommon.ClUint32T),
        ("instantiateCookie", clCommon.ClUint64T),
        ("timers", ClAmsCompTimersT),
        ("proxyComp", ctypes.POINTER(ClAmsEntityT)),
        ("csiList", ClAmsEntityListT),
        ("clientCallbacks", clAmsSAClientApi.ClAmsSAClientCallbacksT)
    ]

ClAmsCompStatusT_5_1_0 = ClAmsCompStatusT

class ClAmsCompMethodsT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityMethodsT),

        ("instantiateTimeout", ClAmsEntityTimerCallbackT),
        ("terminateTimeout", ClAmsEntityTimerCallbackT),
        ("cleanupTimeout", ClAmsEntityTimerCallbackT),
        ("amStartTimeout", ClAmsEntityTimerCallbackT),
        ("amStopTimeout", ClAmsEntityTimerCallbackT),
        ("quiescingCompleteTimeout", ClAmsEntityTimerCallbackT),
        ("csiSetTimeout", ClAmsEntityTimerCallbackT),
        ("csiRemoveTimeout", ClAmsEntityTimerCallbackT),
        ("proxiedCompInstantiateTimeout", ClAmsEntityTimerCallbackT),
        ("proxiedCompCleanupTimeout", ClAmsEntityTimerCallbackT),
        ("instantiateDelayTimeout", ClAmsEntityTimerCallbackT)
    ]

class ClAmsCompT(ctypes.Structure):
    _fields_ = [
        ("config", ClAmsCompConfigT),
        ("status", ClAmsCompStatusT),
        ("methods", ClAmsCompMethodsT)
    ]

ClAmsCompT_5_1_0 = ClAmsCompT

#
# AMS COMPONENT SERVICE INSTANCE
#

class ClAmsCSICompRefT(ctypes.Structure):
    _fields_ = [
        ("entityRef", ClAmsEntityRefT),
        ("haState", clAmsTypes.ClAmsHAStateT),
        ("rank", clCommon.ClUint32T)
    ]

class ClAmsCSIPGTrackClientT(ctypes.Structure):
    _fields_ = [
        ("address", clIocApi.ClIocAddressT),
        ("trackFlags", clAmsTypes.ClAmsPGTrackFlagT),
        ("cpmHandle", clCpmApi.ClCpmHandleT)
    ]

class ClAmsCSINameValuePairT(ctypes.Structure):
    _fields_ = [
        ("csiName", clCommon.ClNameT),
        ("paramName", clCommon.ClNameT),
        ("paramValue", clCommon.ClNameT)
    ]

class ClAmsCSIConfigT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityConfigT),

        ("type", clCommon.ClNameT),
        ("isProxyCSI", clCommon.ClBoolT),

        ("rank", clCommon.ClUint32T),
        ("nameValuePairList", clCntApi.ClCntHandleT),
        ("parentSI", ClAmsEntityRefT),
        ("csiDependentsList", ClAmsEntityListT),
        ("csiDependenciesList", ClAmsEntityListT)
    ]

class ClAmsCSIStatusT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityStatusT),
        ("pgList", ClAmsEntityListT),
        ("pgTrackList", clCntApi.ClCntHandleT)
    ]

class ClAmsCSIMethodsT(ctypes.Structure):
    _fields_ = [
        ("entity", ClAmsEntityMethodsT)
    ]

class ClAmsCSIT(ctypes.Structure):
    _fields_ = [
        ("config", ClAmsCSIConfigT),
        ("status", ClAmsCSIStatusT),
        ("methods", ClAmsCSIMethodsT)
    ]

class ClAmsSUReassignOpT(ctypes.Structure):
    _fields_ = [
        ("numSIs", clCommon.ClInt32T),
        ("sis", ctypes.POINTER(ClAmsEntityT))
    ]

class ClAmsSIReassignEntryT(ctypes.Structure):
    _fields_ = [
        ("si", ctypes.POINTER(ClAmsSIT)),
        ("list", clList.ClListHeadT)
    ]

def CL_AMS_TIMER_CONVERT(x,y):
    y.tsSec = x / 1000
    y.tsMilliSec = x % 1000

# TODO: there're remaining codes in the original header file
