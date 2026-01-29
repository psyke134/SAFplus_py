import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils
from amf import clAmsEntities, clAmsTypes
from eo import clEoApi
from cnt import clCntApi

import ctypes, enum

ClAmsMgmtClientCallbackRmdInterfaceT = clCommon.ClInt32T
class eClAmsMgmtClientCallbackRmdInterfaceT(clUtils.Enum):
    CL_AMS_MGMT_INITIALIZE                       = 1
    CL_AMS_MGMT_FINALIZE                         = 2
    CL_AMS_MGMT_ENTITY_CREATE                   = 3
    CL_AMS_MGMT_ENTITY_DELETE                   = 4
    CL_AMS_MGMT_ENTITY_SET_CONFIG               = 5
    CL_AMS_MGMT_ENTITY_LOCK_ASSIGNMENT          = 6
    CL_AMS_MGMT_ENTITY_LOCK_INSTANTIATION       = 7
    CL_AMS_MGMT_ENTITY_UNLOCK                   = 8
    CL_AMS_MGMT_ENTITY_SHUTDOWN                 = 9
    CL_AMS_MGMT_ENTITY_RESTART                  = 10
    CL_AMS_MGMT_ENTITY_REPAIRED                 = 11
    CL_AMS_MGMT_SG_ADJUST_PREFERENCE            = 12
    CL_AMS_MGMT_SI_SWAP                         = 13
    CL_AMS_MGMT_ENTITY_LIST_ENTITY_REF_ADD      = 14
    CL_AMS_MGMT_ENTITY_SET_REF                  = 15
    CL_AMS_MGMT_CSI_SET_NVP                     = 16
    CL_AMS_MGMT_DEBUG_ENABLE                    = 17
    CL_AMS_MGMT_DEBUG_DISABLE                   = 18
    CL_AMS_MGMT_DEBUG_GET                       = 19
    CL_AMS_MGMT_DEBUG_ENABLE_LOG_TO_CONSOLE     = 20
    CL_AMS_MGMT_DEBUG_DISABLE_LOG_TO_CONSOLE    = 21

    CL_AMS_MGMT_CCB_INITIALIZE                  = 22
    CL_AMS_MGMT_CCB_FINALIZE                    = 23
    CL_AMS_MGMT_CCB_ENTITY_SET_CONFIG           = 24
    CL_AMS_MGMT_CCB_CSI_SET_NVP                 = 25
    CL_AMS_MGMT_CCB_SET_NODE_DEPENDENCY         = 26
    CL_AMS_MGMT_CCB_SET_NODE_SU_LIST            = 27
    CL_AMS_MGMT_CCB_SET_SG_SU_LIST              = 28
    CL_AMS_MGMT_CCB_SET_SG_SI_LIST              = 29
    CL_AMS_MGMT_CCB_SET_SU_COMP_LIST            = 30
    CL_AMS_MGMT_CCB_SET_SI_SU_RANK_LIST         = 31
    CL_AMS_MGMT_CCB_SET_SI_SI_DEPENDENCY        = 32
    CL_AMS_MGMT_CCB_SET_SI_CSI_LIST             = 33
    CL_AMS_MGMT_CCB_ENABLE_ENTITY               = 34
    CL_AMS_MGMT_CCB_DISABLE_ENTITY              = 35
    CL_AMS_MGMT_CCB_ENTITY_CREATE               = 36
    CL_AMS_MGMT_CCB_ENTITY_DELETE               = 37
    CL_AMS_MGMT_CCB_COMMIT                      = 38
    CL_AMS_MGMT_ENTITY_GET                      = 39
    CL_AMS_MGMT_ENTITY_GET_CONFIG               = 40
    CL_AMS_MGMT_ENTITY_GET_STATUS               = 41
    CL_AMS_MGMT_GET_CSI_NVP_LIST                = 42
    CL_AMS_MGMT_GET_ENTITY_LIST                 = 43
    CL_AMS_MGMT_GET_OL_ENTITY_LIST              = 44
    CL_AMS_MGMT_CCB_CSI_DELETE_NVP              = 45

    CL_AMS_MGMT_CCB_DELETE_NODE_DEPENDENCY         = 46
    CL_AMS_MGMT_CCB_DELETE_NODE_SU_LIST            = 47
    CL_AMS_MGMT_CCB_DELETE_SG_SU_LIST              = 48
    CL_AMS_MGMT_CCB_DELETE_SG_SI_LIST              = 49
    CL_AMS_MGMT_CCB_DELETE_SU_COMP_LIST            = 50
    CL_AMS_MGMT_CCB_DELETE_SI_SU_RANK_LIST         = 51
    CL_AMS_MGMT_CCB_DELETE_SI_SI_DEPENDENCY        = 52
    CL_AMS_MGMT_CCB_DELETE_SI_CSI_LIST             = 53

    CL_AMS_MGMT_ENTITY_SET_ALPHA_FACTOR = 54
    CL_AMS_MGMT_MIGRATE_SG = 55
    
    CL_AMS_MGMT_ENTITY_USER_DATA_SET = 56
    CL_AMS_MGMT_ENTITY_USER_DATA_SETKEY = 57
    CL_AMS_MGMT_ENTITY_USER_DATA_GET = 58
    CL_AMS_MGMT_ENTITY_USER_DATA_GETKEY = 59
    CL_AMS_MGMT_ENTITY_USER_DATA_DELETE = 60
    CL_AMS_MGMT_ENTITY_USER_DATA_DELETEKEY = 61

    CL_AMS_MGMT_CCB_SET_CSI_CSI_DEPENDENCY        = 62
    CL_AMS_MGMT_CCB_DELETE_CSI_CSI_DEPENDENCY        = 63
    CL_AMS_MGMT_SI_ASSIGN_SU_CUSTOM                 = 65
    CL_AMS_MGMT_ENTITY_SET_BETA_FACTOR = 66
    CL_AMS_MGMT_ENTITY_FORCE_LOCK     =  67
    CL_AMS_MGMT_DB_GET     =  68
    CL_AMS_MGMT_COMPUTED_ADMIN_STATE_GET     =  69
    CL_AMS_MGMT_ENTITY_FORCE_LOCK_INSTANTIATION     =  70
    CL_AMS_MGMT_CCB_BATCH_COMMIT = 71

ClAmsTLVTypeT = clCommon.ClInt32T
class eClAmsTLVTypeT(clUtils.Enum):
    CL_AMS_TLV_TYPE_ENTITY       = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_ENTITY
    CL_AMS_TLV_TYPE_NODE         = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_NODE
    CL_AMS_TLV_TYPE_APP          = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_APP
    CL_AMS_TLV_TYPE_SG           = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG
    CL_AMS_TLV_TYPE_SU           = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU
    CL_AMS_TLV_TYPE_SI           = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI
    CL_AMS_TLV_TYPE_COMP         = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP
    CL_AMS_TLV_TYPE_CSI          = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI
    CL_AMS_TLV_TYPE_CLUSTER      = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CLUSTER
    CL_AMS_TLV_TYPE_START_LIST   = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CLUSTER + 1
    CL_AMS_TLV_TYPE_END_LIST     = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CLUSTER + 2

ClAmsMgmtCCBOperationsT = clCommon.ClInt32T
class eClAmsMgmtCCBOperationsT(clUtils.Enum):
    CL_AMS_MGMT_CCB_OPERATION_CREATE = 1
    CL_AMS_MGMT_CCB_OPERATION_DELETE = 2
    CL_AMS_MGMT_CCB_OPERATION_SET_CONFIG = 3
    CL_AMS_MGMT_CCB_OPERATION_CSI_SET_NVP = 4
    CL_AMS_MGMT_CCB_OPERATION_SET_NODE_DEPENDENCY = 5
    CL_AMS_MGMT_CCB_OPERATION_SET_NODE_SU_LIST = 6
    CL_AMS_MGMT_CCB_OPERATION_SET_SG_SU_LIST = 7
    CL_AMS_MGMT_CCB_OPERATION_SET_SG_SI_LIST = 8
    CL_AMS_MGMT_CCB_OPERATION_SET_SU_COMP_LIST = 9
    CL_AMS_MGMT_CCB_OPERATION_SET_SI_SU_RANK_LIST = 10
    CL_AMS_MGMT_CCB_OPERATION_SET_SI_SI_DEPENDENCY_LIST = 11
    CL_AMS_MGMT_CCB_OPERATION_SET_SI_CSI_LIST = 12
    CL_AMS_MGMT_CCB_OPERATION_SET_CSI_CSI_DEPENDENCY_LIST = 13
    CL_AMS_MGMT_CCB_OPERATION_CSI_DELETE_NVP = 14
    CL_AMS_MGMT_CCB_OPERATION_DELETE_NODE_DEPENDENCY = 15
    CL_AMS_MGMT_CCB_OPERATION_DELETE_NODE_SU_LIST = 16
    CL_AMS_MGMT_CCB_OPERATION_DELETE_SG_SU_LIST = 17
    CL_AMS_MGMT_CCB_OPERATION_DELETE_SG_SI_LIST = 18
    CL_AMS_MGMT_CCB_OPERATION_DELETE_SU_COMP_LIST = 19
    CL_AMS_MGMT_CCB_OPERATION_DELETE_SI_SU_RANK_LIST = 20
    CL_AMS_MGMT_CCB_OPERATION_DELETE_SI_SI_DEPENDENCY_LIST = 21
    CL_AMS_MGMT_CCB_OPERATION_DELETE_CSI_CSI_DEPENDENCY_LIST = 22
    CL_AMS_MGMT_CCB_OPERATION_DELETE_SI_CSI_LIST = 23
    CL_AMS_MGMT_CCB_OPERATION_MAX = 24

def AMS_FUNC_ID(clnt, fn):
    return clEoApi.CL_EO_GET_FULL_FN_NUM(clnt, fn)

CL_AMS_RMD_DEFAULT_TIMEOUT = 10000
CL_AMS_RMD_DEFAULT_RETRIES = 3

class ClAmsTLVT(ctypes.Structure):
    _fields_ = [
        ("type", ClAmsTLVTypeT),
        ("length", clCommon.ClUint32T)
    ]

class clAmsMgmtDummyResponseT(ctypes.Structure):
    _fields_ = [
        ("handle", clCommon.ClHandleT)
    ]

class clAmsMgmtFinalizeRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT)
    ]

clAmsMgmtFinalizeResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityInstantiateRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtEntityInstantiateResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityTerminateRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtEntityTerminateResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityFindByNameRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entityRef", clAmsEntities.ClAmsEntityRefT)
    ]

class clAmsMgmtEntityFindByNameResponseT(ctypes.Structure):
    _fields_ = [
        ("entityRef", clAmsEntities.ClAmsEntityRefT)
    ]

class clAmsMgmtEntitySetConfigRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("peInstantiateFlag", clCommon.ClUint32T),
        ("entityConfig", ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT))
    ]

class clAmsMgmtEntitySetAlphaFactorRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT),
        ("alphaFactor", clCommon.ClUint32T)
    ]

class clAmsMgmtEntitySetBetaFactorRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT),
        ("betaFactor", clCommon.ClUint32T)
    ]

clAmsMgmtEntitySetAlphaFactorResponseT = clAmsMgmtDummyResponseT
clAmsMgmtEntitySetBetaFactorResponseT = clAmsMgmtDummyResponseT
clAmsMgmtEntitySetConfigResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntitySetRefRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("sourceEntity", clAmsEntities.ClAmsEntityT),
        ("targetEntity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtEntitySetRefResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCSISetNVPRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("sourceEntity", clAmsEntities.ClAmsEntityT),
        ("nvp", clAmsEntities.ClAmsCSINameValuePairT)
    ]

clAmsMgmtCSISetNVPResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityLockAssignmentRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtEntityLockAssignmentResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityForceLockRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT),
        ("lock", clCommon.ClBoolT)
    ]

clAmsMgmtEntityForceLockResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityLockInstantiationRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtEntityLockInstantiationResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityUnlockRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtEntityUnlockResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityShutdownRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtEntityShutdownResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityRestartRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtEntityRestartResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityRepairedRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtEntityRepairedResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityStartMonitoringEntityRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtEntityStartMonitoringEntityResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityStopMonitoringEntityRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtEntityStopMonitoringEntityResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtSGAdjustPreferenceRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT),
        ("enable", clCommon.ClUint32T)
    ]

clAmsMgmtSGAdjustPreferenceResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtSISwapRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtSISwapResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityListEntityRefAddRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("sourceEntity", clAmsEntities.ClAmsEntityT),
        ("targetEntity", clAmsEntities.ClAmsEntityT),
        ("entityListName", clAmsEntities.ClAmsEntityListTypeT)
    ]

clAmsMgmtEntityListEntityRefAddResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityGetEntityListRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT),
        ("entityListName", clAmsEntities.ClAmsEntityListTypeT)
    ]

class clAmsMgmtEntityGetEntityListResponseT(ctypes.Structure):
    _fields_ = [
        ("numNodes", clCommon.ClUint32T),
        ("nodeList", clCommon.ClPtrT)
    ]

ClAmsMgmtSubAreaT = clCommon.ClInt32T
class eClAmsMgmtSubAreaT(clUtils.Enum):
    CL_AMS_MGMT_SUB_AREA_MSG            = 1
    CL_AMS_MGMT_SUB_AREA_STATE_CHANGE   = 1<<1
    CL_AMS_MGMT_SUB_AREA_FN_CALL        = 1<<2
    CL_AMS_MGMT_SUB_AREA_TIMER          = 1<<3

class clAmsMgmtDebugEnableRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT),
        ("debugFlags", clCommon.ClUint8T)
    ]

clAmsMgmtDebugEnableResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtDebugDisableRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT),
        ("debugFlags", clCommon.ClUint8T)
    ]

clAmsMgmtDebugDisableResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtDebugGetRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

class clAmsMgmtDebugGetResponseT(ctypes.Structure):
    _fields_ = [
        ("debugFlags", clCommon.ClUint8T)
    ]

class clAmsMgmtDebugEnableLogToConsoleRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT)
    ]

clAmsMgmtDebugEnableLogToConsoleResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtDebugDisableLogToConsoleRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT)
    ]

clAmsMgmtDebugDisableLogToConsoleResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBT(ctypes.Structure):
    _fields_ = [
        ("ccbOpListHandle", clCntApi.ClCntHandleT)
    ]

class clAmsMgmtCCBInitializeRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT)
    ]

class clAmsMgmtCCBInitializeResponseT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT)
    ]

class clAmsMgmtCCBFinalizeRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT)
    ]

clAmsMgmtCCBFinalizeResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBCommitRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT)
    ]

clAmsMgmtCCBCommitResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBEntityCreateRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBEntityCreateResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBEntityDeleteRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBEntityDeleteResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBEntitySetConfigRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("bitmask", clCommon.ClUint64T),
        ("entityConfig", ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT))
    ]

clAmsMgmtCCBEntitySetConfigResponseT = clAmsMgmtDummyResponseT

ClAmsCSINVPT = clAmsEntities.ClAmsCSINameValuePairT

class clAmsMgmtCCBCSISetNVPRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("csiName", clAmsEntities.ClAmsEntityT),
        ("nvp", ClAmsCSINVPT)
    ]

clAmsMgmtCCBCSISetNVPResponseT = clAmsMgmtDummyResponseT

clAmsMgmtCCBCSIDeleteNVPRequestT = clAmsMgmtCCBCSISetNVPRequestT
clAmsMgmtCCBCSIDeleteNVPResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBSetNodeDependencyRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("nodeName", clAmsEntities.ClAmsEntityT),
        ("dependencyNodeName", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBSetNodeDependencyResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBSetNodeSUListRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("nodeName", clAmsEntities.ClAmsEntityT),
        ("suName", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBSetNodeSUListResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBSetSGSUListRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("sgName", clAmsEntities.ClAmsEntityT),
        ("suName", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBSetSGSUListResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBSetSGSIListRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("sgName", clAmsEntities.ClAmsEntityT),
        ("siName", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBSetSGSIListResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBSetSUCompListRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("suName", clAmsEntities.ClAmsEntityT),
        ("compName", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBSetSUCompListResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBSetSISURankListRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("siName", clAmsEntities.ClAmsEntityT),
        ("suName", clAmsEntities.ClAmsEntityT),
        ("suRank", clCommon.ClUint32T)
    ]

clAmsMgmtCCBSetSISURankListResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBSetSISIDependencyRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("siName", clAmsEntities.ClAmsEntityT),
        ("dependencySIName", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBSetSISIDependencyResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBSetCSICSIDependencyRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("csiName", clAmsEntities.ClAmsEntityT),
        ("dependencyCSIName", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBSetCSICSIDependencyResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBSetSICSIListRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("siName", clAmsEntities.ClAmsEntityT),
        ("csiName", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBSetSICSIListResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBEnableEntityRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("entityName", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBEnableEntityResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtCCBDisableEntityRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtCCBHandleT),
        ("entityName", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtCCBDisableEntityResponseT = clAmsMgmtDummyResponseT

class clAmsMgmtEntityGetRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

class clAmsMgmtEntityGetResponseT(ctypes.Structure):
    _fields_ = [
        ("entity", ctypes.POINTER(clAmsEntities.ClAmsEntityT))
    ]

class clAmsMgmtEntityGetConfigRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

class clAmsMgmtEntityGetConfigResponseT(ctypes.Structure):
    _fields_ = [
        ("entityConfig", ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT))
    ]

class clAmsMgmtEntityGetStatusRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT)
    ]

class clAmsMgmtEntityGetStatusResponseT(ctypes.Structure):
    _fields_ = [
        ("entity", clAmsEntities.ClAmsEntityT),
        ("entityStatus", ctypes.POINTER(clAmsEntities.ClAmsEntityStatusT))
    ]

class ClAmsCSINVPBufferT(ctypes.Structure):
    _fields_ = [
        ("count", clCommon.ClUint32T),
        ("nvp", ctypes.POINTER(ClAmsCSINVPT))
    ]

class clAmsMgmtGetCSINVPListRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("csi", clAmsEntities.ClAmsEntityT)
    ]

clAmsMgmtGetCSINVPListResponseT = ClAmsCSINVPBufferT

class ClAmsEntityBufferT(ctypes.Structure):
    _fields_ = [
        ("count", clCommon.ClUint32T),
        ("entity", ctypes.POINTER(clAmsEntities.ClAmsEntityT))
    ]

class ClAmsEntityRefBufferT(ctypes.Structure):
    _fields_ = [
        ("count", clCommon.ClUint32T),
        ("entityRef", ctypes.POINTER(clAmsEntities.ClAmsEntityRefT))
    ]

class ClAmsSUSIRefBufferT(ctypes.Structure):
    _fields_ = [
        ("count", clCommon.ClUint32T),
        ("entityRef", ctypes.POINTER(clAmsEntities.ClAmsSUSIRefT))
    ]

class ClAmsSUSIExtendedRefBufferT(ctypes.Structure):
    _fields_ = [
        ("count", clCommon.ClUint32T),
        ("entityRef", ctypes.POINTER(clAmsEntities.ClAmsSUSIExtendedRefT))
    ]

class ClAmsSISURefBufferT(ctypes.Structure):
    _fields_ = [
        ("count", clCommon.ClUint32T),
        ("entityRef", ctypes.POINTER(clAmsEntities.ClAmsSISURefT))
    ]

class ClAmsSISUExtendedRefBufferT(ctypes.Structure):
    _fields_ = [
        ("count", clCommon.ClUint32T),
        ("entityRef", ctypes.POINTER(clAmsEntities.ClAmsSISUExtendedRefT))
    ]

class ClAmsCompCSIRefBufferT(ctypes.Structure):
    _fields_ = [
        ("count", clCommon.ClUint32T),
        ("entityRef", ctypes.POINTER(clAmsEntities.ClAmsCompCSIRefT))
    ]

class clAmsMgmtGetEntityListRequestT(ctypes.Structure):
    _fields_ = [
        ("handle", clAmsTypes.ClAmsMgmtHandleT),
        ("entity", clAmsEntities.ClAmsEntityT),
        ("entityListName", clAmsEntities.ClAmsEntityListTypeT)
    ]

class ClAmsMgmtMigrateListT(ctypes.Structure):
    _fields_ = [
        ("si", ClAmsEntityBufferT),
        ("csi", ClAmsEntityBufferT),
        ("node", ClAmsEntityBufferT),
        ("su", ClAmsEntityBufferT),
        ("comp", ClAmsEntityBufferT)
    ]

class ClAmsMgmtMigrateRequestT(ctypes.Structure):
    _fields_ = [
        ("sg", clCommon.ClNameT),
        ("prefix", clCommon.ClNameT),
        ("activeSUs", clCommon.ClUint32T),
        ("standbySUs", clCommon.ClUint32T)
    ]

class ClAmsMgmtMigrateResponseT(ctypes.Structure):
    _fields_ = [
        ("migrateList", ClAmsMgmtMigrateListT)
    ]

class ClAmsMgmtUserDataSetRequestT(ctypes.Structure):
    _fields_ = [
        ("entity", ctypes.POINTER(clAmsEntities.ClAmsEntityT)),
        ("key", ctypes.POINTER(clCommon.ClNameT)),
        ("data", ctypes.POINTER(clCommon.ClCharT)),
        ("len", clCommon.ClUint32T)
    ]

class ClAmsMgmtUserDataGetRequestT(ctypes.Structure):
    _fields_ = [
        ("entity", ctypes.POINTER(clAmsEntities.ClAmsEntityT)),
        ("key", ctypes.POINTER(clCommon.ClNameT)),
        ("data", ctypes.POINTER(ctypes.POINTER(clCommon.ClCharT))),
        ("len", ctypes.POINTER(clCommon.ClUint32T))
    ]

class ClAmsMgmtUserDataDeleteRequestT(ctypes.Structure):
    _fields_ = [
        ("entity", ctypes.POINTER(clAmsEntities.ClAmsEntityT)),
        ("key", ctypes.POINTER(clCommon.ClNameT)),
        ("clear", clCommon.ClBoolT)
    ]

class ClAmsMgmtSIAssignSUCustomRequestT(ctypes.Structure):
    _fields_ = [
        ("si", clAmsEntities.ClAmsEntityT),
        ("activeSU", clAmsEntities.ClAmsEntityT),
        ("standbySU", clAmsEntities.ClAmsEntityT)
    ]

class ClAmsMgmtDBGetResponseT(ctypes.Structure):
    _fields_ = [
        ("len", clCommon.ClUint32T),
        ("buffer", ctypes.POINTER(clCommon.ClUint8T))
    ]

class ClAmsMgmtCASGetRequestT(ctypes.Structure):
    _fields_ = [
        ("entity", clAmsEntities.ClAmsEntityT),
        ("computedAdminState", clAmsTypes.ClAmsAdminStateT)
    ]

clAmsMgmtGetEntityListResponseT = ClAmsEntityBufferT
clAmsMgmtGetOLEntityListRequestT = clAmsMgmtGetEntityListRequestT
clAmsMgmtGetOLEntityListResponseT = ClAmsEntityRefBufferT

CL_AMS_CONFIG_ATTR_ALL                      = 1 

NODE_CONFIG_ADMIN_STATE                     = CL_AMS_CONFIG_ATTR_ALL<<1
NODE_CONFIG_ID                              = CL_AMS_CONFIG_ATTR_ALL<<2
NODE_CONFIG_CLASS_TYPE                      = CL_AMS_CONFIG_ATTR_ALL<<3
NODE_CONFIG_SUB_CLASS_TYPE                  = CL_AMS_CONFIG_ATTR_ALL<<4
NODE_CONFIG_IS_SWAPPABLE                    = CL_AMS_CONFIG_ATTR_ALL<<5
NODE_CONFIG_IS_RESTARTABLE                  = CL_AMS_CONFIG_ATTR_ALL<<6
NODE_CONFIG_AUTO_REPAIR                     = CL_AMS_CONFIG_ATTR_ALL<<7
NODE_CONFIG_IS_ASP_AWARE                    = CL_AMS_CONFIG_ATTR_ALL<<8
NODE_CONFIG_SU_FAILOVER_DURATION            = CL_AMS_CONFIG_ATTR_ALL<<9
NODE_CONFIG_SU_FAILOVER_COUNT_MAX           = CL_AMS_CONFIG_ATTR_ALL<<10 

SG_CONFIG_ADMIN_STATE                       = CL_AMS_CONFIG_ATTR_ALL<<1
SG_CONFIG_REDUNDANCY_MODEL                  = CL_AMS_CONFIG_ATTR_ALL<<2
SG_CONFIG_LOADING_STRATEGY                  = CL_AMS_CONFIG_ATTR_ALL<<3
SG_CONFIG_FAILBACK_OPTION                   = CL_AMS_CONFIG_ATTR_ALL<<4
SG_CONFIG_AUTO_REPAIR                       = CL_AMS_CONFIG_ATTR_ALL<<5
SG_CONFIG_INSTANTIATE_DURATION              = CL_AMS_CONFIG_ATTR_ALL<<6
SG_CONFIG_NUM_PREF_ACTIVE_SUS               = CL_AMS_CONFIG_ATTR_ALL<<7
SG_CONFIG_NUM_PREF_STANDBY_SUS              = CL_AMS_CONFIG_ATTR_ALL<<8
SG_CONFIG_NUM_PREF_INSERVICE_SUS            = CL_AMS_CONFIG_ATTR_ALL<<9
SG_CONFIG_NUM_PREF_ASSIGNED_SUS             = CL_AMS_CONFIG_ATTR_ALL<<10 
SG_CONFIG_NUM_PREF_ACTIVE_SUS_PER_SI        = CL_AMS_CONFIG_ATTR_ALL<<11 
SG_CONFIG_MAX_ACTIVE_SIS_PER_SU             = CL_AMS_CONFIG_ATTR_ALL<<12 
SG_CONFIG_MAX_STANDBY_SIS_PER_SU            = CL_AMS_CONFIG_ATTR_ALL<<13 
SG_CONFIG_COMP_RESTART_DURATION             = CL_AMS_CONFIG_ATTR_ALL<<14 
SG_CONFIG_COMP_RESTART_COUNT_MAX            = CL_AMS_CONFIG_ATTR_ALL<<15 
SG_CONFIG_SU_RESTART_DURATION               = CL_AMS_CONFIG_ATTR_ALL<<16 
SG_CONFIG_SU_RESTART_COUNT_MAX              = CL_AMS_CONFIG_ATTR_ALL<<17 
SG_CONFIG_REDUCTION_PROCEDURE               = CL_AMS_CONFIG_ATTR_ALL<<18
SG_CONFIG_COLOCATION_ALLOWED                = CL_AMS_CONFIG_ATTR_ALL<<19
SG_CONFIG_AUTO_ADJUST                       = CL_AMS_CONFIG_ATTR_ALL<<20
SG_CONFIG_AUTO_ADJUST_PROBATION             = CL_AMS_CONFIG_ATTR_ALL<<21
SG_CONFIG_ALPHA_FACTOR                      = CL_AMS_CONFIG_ATTR_ALL<<22
SG_CONFIG_MAX_FAILOVERS                     = CL_AMS_CONFIG_ATTR_ALL<<23
SG_CONFIG_FAILOVER_DURATION                 = CL_AMS_CONFIG_ATTR_ALL<<24
SG_CONFIG_BETA_FACTOR                       = CL_AMS_CONFIG_ATTR_ALL<<25

SU_CONFIG_ADMIN_STATE                       = CL_AMS_CONFIG_ATTR_ALL<<1
SU_CONFIG_RANK                              = CL_AMS_CONFIG_ATTR_ALL<<2
SU_CONFIG_NUM_COMPONENTS                    = CL_AMS_CONFIG_ATTR_ALL<<3
SU_CONFIG_IS_PREINSTANTIABLE                = CL_AMS_CONFIG_ATTR_ALL<<4
SU_CONFIG_IS_RESTARTABLE                    = CL_AMS_CONFIG_ATTR_ALL<<5
SU_CONFIG_IS_CONTAINER_SU                   = CL_AMS_CONFIG_ATTR_ALL<<6

SI_CONFIG_ADMIN_STATE                       = CL_AMS_CONFIG_ATTR_ALL<<1
SI_CONFIG_RANK                              = CL_AMS_CONFIG_ATTR_ALL<<2
SI_CONFIG_NUM_CSIS                          = CL_AMS_CONFIG_ATTR_ALL<<3
SI_CONFIG_NUM_STANDBY_ASSIGNMENTS           = CL_AMS_CONFIG_ATTR_ALL<<4
SI_CONFIG_STANDBY_ASSIGNMENT_ORDER          = CL_AMS_CONFIG_ATTR_ALL<<5

COMP_CONFIG_SUPPORTED_CSI_TYPE              = CL_AMS_CONFIG_ATTR_ALL<<1 
COMP_CONFIG_PROXY_CSI_TYPE                  = CL_AMS_CONFIG_ATTR_ALL<<2 
COMP_CONFIG_CAPABILITY_MODEL                = CL_AMS_CONFIG_ATTR_ALL<<3 
COMP_CONFIG_PROPERTY                        = CL_AMS_CONFIG_ATTR_ALL<<4 
COMP_CONFIG_IS_RESTARTABLE                  = CL_AMS_CONFIG_ATTR_ALL<<5 
COMP_CONFIG_NODE_REBOOT_CLEANUP_FAIL        = CL_AMS_CONFIG_ATTR_ALL<<6 
COMP_CONFIG_INSTANTIATE_LEVEL               = CL_AMS_CONFIG_ATTR_ALL<<7 
COMP_CONFIG_NUM_MAX_INSTANTIATE             = CL_AMS_CONFIG_ATTR_ALL<<8 
COMP_CONFIG_NUM_MAX_INSTANTIATE_WITH_DELAY  = CL_AMS_CONFIG_ATTR_ALL<<9 
COMP_CONFIG_NUM_MAX_TERMINATE               = CL_AMS_CONFIG_ATTR_ALL<<10 
COMP_CONFIG_NUM_MAX_AM_START                = CL_AMS_CONFIG_ATTR_ALL<<11 
COMP_CONFIG_NUM_MAX_AM_STOP                 = CL_AMS_CONFIG_ATTR_ALL<<12 
COMP_CONFIG_NUM_MAX_ACTIVE_CSIS             = CL_AMS_CONFIG_ATTR_ALL<<13 
COMP_CONFIG_NUM_MAX_STANDBY_CSIS            = CL_AMS_CONFIG_ATTR_ALL<<14 
COMP_CONFIG_TIMEOUTS                        = CL_AMS_CONFIG_ATTR_ALL<<15 
COMP_CONFIG_RECOVERY_ON_TIMEOUT             = CL_AMS_CONFIG_ATTR_ALL<<16 
COMP_CONFIG_PARENT_SU                       = CL_AMS_CONFIG_ATTR_ALL<<17
COMP_CONFIG_INSTANTIATE_COMMAND             = CL_AMS_CONFIG_ATTR_ALL<<18

CSI_CONFIG_TYPE                             = CL_AMS_CONFIG_ATTR_ALL<<1
CSI_CONFIG_IS_PROXY_CSI                     = CL_AMS_CONFIG_ATTR_ALL<<2
CSI_CONFIG_RANK                             = CL_AMS_CONFIG_ATTR_ALL<<3
