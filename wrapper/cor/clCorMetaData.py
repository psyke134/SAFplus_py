import sys
sys.path.append("..")

from common import clCommon, clCommonErrors
from eo import clEoApi
from utils import clUtils
from cor import clCorApi
from ioc import clIocApi
from buffer import clBufferApi

import ctypes, enum

CL_COR_WTH_COOKIE_ID =  clEoApi.eClEoServerIdT.CL_EO_COR_SERVER_COOKIE_ID+1

CL_COR_VERSION_NO =  0x0100
CL_COR_DEFAULT_MAX_SESSIONS =  5
CL_COR_DEFAULT_MAX_RETRIES =  3

CL_COR_DEFAULT_TIMEOUT =  3000

CL_COR_MAX_NAME_SZ =  clCommon.CL_MAX_NAME_LENGTH

CL_COR_NO_SAVE =  0
CL_COR_SAVE_PER_TXN =  1
CL_COR_PERIODIC_SAVE =  2
CL_COR_DELTA_SAVE =  3

CL_COR_UNKNOWN_ATTRIB =  -1

CL_COR_CLI_STR_LEN =  1024

CL_COR_VERSION_NO =  0x0100
CL_COR_HANDLE_MAX_DEPTH =  20
CL_COR_INVALID_MO_ID =  -1
CL_COR_INVALID_MO_INSTANCE =  -1
CL_COR_INVALID_SVC_ID =  -1
CL_COR_SVC_ID_DEFAULT =  0

CL_COR_CLASS_WILD_CARD =  0xFFFFFFFE

CL_COR_INSTANCE_WILD_CARD = -2

CL_COR_SVC_WILD_CARD =  0xFFFE

CL_COR_CONT_ATTR_MAX_DEPTH =  10

CL_COR_INVALID_ATTR_ID =  -1
CL_COR_INVALID_ATTR_IDX =  -1
CL_COR_ATTR_WILD_CARD =  -2
CL_COR_INDEX_WILD_CARD =  -2

CL_COR_SIMPLE_TXN =  None

CL_COR_OH_MAX_TYPES =  16
CL_COR_OH_MAX_LEVELS =  64
CL_COR_OH_MASK_END_MARKER =  0xFF

CL_COR_ATTR_CONFIG =  0x01000000
CL_COR_ATTR_RUNTIME =  0x02000000
CL_COR_ATTR_OPERATIONAL =  0x04000000
CL_COR_ATTR_WRITABLE =  0x00010000
CL_COR_ATTR_INITIALIZED =  0x00020000
CL_COR_ATTR_CACHED =  0x00000100
CL_COR_ATTR_PERSISTENT =  0x00000200

ClCorClassTypeT = clCommon.ClInt32T
ClCorAttrIdT = clCommon.ClInt32T
ClCorInstanceIdT = clCommon.ClInt32T
ClCorAttrFlagT = clCommon.ClUint32T
ClCorJobStatusT = clCommon.ClUint32T

ClCorBundleHandleT = clCommon.ClHandleT
ClCorBundleHandlePtrT = ctypes.POINTER(clCommon.ClPtrT)

ClCorTypeT = clCommon.ClInt32T
class eClCorTypeT(clUtils.Enum):
    CL_COR_INVALID_DATA_TYPE = -1
    CL_COR_VOID = 0
    CL_COR_INT8 = 1
    CL_COR_UINT8 = 2
    CL_COR_INT16 = 3
    CL_COR_UINT16 = 4
    CL_COR_INT32 = 5
    CL_COR_UINT32 = 6
    CL_COR_INT64 = 7
    CL_COR_UINT64 = 8
    CL_COR_FLOAT = 9
    CL_COR_DOUBLE = 10
    CL_COR_COUNTER32 = 11
    CL_COR_COUNTER64 = 12
    CL_COR_SEQUENCE32 = 13

ClCorAttrTypeT = clCommon.ClInt32T
class eClCorAttrTypeT(clUtils.Enum):
    CL_COR_MAX_TYPE = eClCorTypeT.CL_COR_SEQUENCE32
    CL_COR_SIMPLE_ATTR = eClCorTypeT.CL_COR_SEQUENCE32 + 1
    CL_COR_ARRAY_ATTR = eClCorTypeT.CL_COR_SEQUENCE32 + 2
    CL_COR_CONTAINMENT_ATTR = eClCorTypeT.CL_COR_SEQUENCE32 + 3
    CL_COR_ASSOCIATION_ATTR = eClCorTypeT.CL_COR_SEQUENCE32 + 4
    CL_COR_VIRTUAL_ATTR = eClCorTypeT.CL_COR_SEQUENCE32 + 5

ClCorAttrCmpFlagT = clCommon.ClInt32T
class eClCorAttrCmpFlagT(clUtils.Enum):
    CL_COR_ATTR_CMP_FLAG_INVALID = 0
    CL_COR_ATTR_CMP_FLAG_VALUE_EQUAL_TO = 1
    CL_COR_ATTR_CMP_FLAG_VALUE_LESS_THAN = 2
    CL_COR_ATTR_CMP_FLAG_VALUE_LESS_OR_EQUALS = 3
    CL_COR_ATTR_CMP_FLAG_VALUE_GREATER_THAN = 4
    CL_COR_ATTR_CMP_FLAG_VALUE_GREATER_OR_EQUALS = 5
    CL_COR_ATTR_CMP_FLAG_MAX = 6

ClCorAttrWalkOpT = clCommon.ClInt32T
class eClCorAttrWalkOpT(clUtils.Enum):
    CL_COR_ATTR_INVALID_OPTION = 0
    CL_COR_ATTR_WALK_ALL_ATTR = 1
    CL_COR_ATTR_WALK_ONLY_MATCHED_ATTR = 2
    CL_COR_ATTR_WALK_MAX = 3

class ClCorAttrValuesT(ctypes.Structure):
    _fields_ = [
        ("init", clCommon.ClInt64T),
        ("min", clCommon.ClInt64T),
        ("max", clCommon.ClInt64T)
    ]

class ClCorAttrAdditionalInfoT(ctypes.Structure):
    _fields_ = [
        ("arrDataType", ClCorTypeT),
        ("maxElement", clCommon.ClUint32T),
        ("classId", ClCorClassTypeT)
    ]

class _u(ctypes.Structure):
    _fields_ = [
        ("simpleAttrVals", ClCorAttrValuesT),
        ("attrInfo", ClCorAttrAdditionalInfoT)
    ]

class ClCorAttrDefT(ctypes.Structure):
    _fields_ = [
        ("attrId", ClCorAttrIdT),
        ("attrType", ClCorAttrTypeT),
        ("u", _u)
    ]

ClCorClassAttrWalkFunc = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ClCorClassTypeT,
    ctypes.POINTER(ClCorAttrDefT),
    clCommon.ClPtrT
)

ClCorObjTypesT = clCommon.ClInt32T
class eClCorObjTypesT(clUtils.Enum):
    CL_COR_OBJ_TYPE_SIMPLE = 0
    CL_COR_OBJ_TYPE_MO = 1
    CL_COR_OBJ_TYPE_MSO = 2

ClCorObjLockFlagsT = clCommon.ClInt32T
class eClCorObjLockFlagsT(clUtils.Enum):
    CL_COR_LOCK_OBJECT = 0
    CL_COR_LOCK_SUBTREE = 1

ClCorObjWalkFlagsT = clCommon.ClInt32T
class eClCorObjWalkFlagsT(clUtils.Enum):
    CL_COR_MOTREE_WALK = 0
    CL_COR_MO_WALK = 1
    CL_COR_MSO_WALK = 2
    CL_COR_MO_SUBTREE_WALK = 3
    CL_COR_MSO_SUBTREE_WALK = 4
    CL_COR_MO_WALK_UP = 5
    CL_COR_MSO_WALK_UP = 6

ClCorMoIdClassGetFlagsT = clCommon.ClInt32T
class eClCorMoIdClassGetFlagsT(clUtils.Enum):
    CL_COR_MO_CLASS_GET = 0
    CL_COR_MSO_CLASS_GET = 1

ClCorObjectHandleT = clCommon.ClPtrT

def CL_COR_OBJ_HANDLE_INIT(objH):
    try:
        size = clCommon.ClUint16T(0)
        tempHandle = ctypes.cast(objH, ctypes.c_void_p)
        rc = clCorApi.clCorObjectHandleSizeGet(objH, ctypes.byref(size))
        if rc != clCommonErrors.CL_OK:
            return rc
        tempHandle.value += ctypes.sizeof(clCommon.ClUint16T)
        ctypes.memset(tempHandle, 0, size.value - ctypes.sizeof(clCommon.ClUint16T))
    except ValueError:
        pass

ClCorTxnSessionIdT = clCommon.ClPtrT
ClCorTxnIdT = clCommon.ClPtrT
ClCorTxnJobIdT = clCommon.ClUint32T

ClCorOpsT = clCommon.ClInt32T
class eClCorOpsT(clUtils.Enum):
    CL_COR_OP_RESERVED = 0
    CL_COR_OP_CREATE = 0x1
    CL_COR_OP_SET =    0x2
    CL_COR_OP_DELETE = 0x4
    CL_COR_OP_GET =    0x8
    CL_COR_OP_CREATE_AND_SET = 0x10
    CL_COR_OP_ALL = (CL_COR_OP_CREATE |
                     CL_COR_OP_SET |
                     CL_COR_OP_DELETE |
                     CL_COR_OP_GET |
                     CL_COR_OP_CREATE_AND_SET)

ClCorTxnJobStatusT = clCommon.ClInt32T
class eClCorTxnJobStatusT(clUtils.Enum):
    CL_COR_TXN_JOB_PASS = 0
    CL_COR_TXN_JOB_FAIL = 1

ClCorObjFlagsT = clCommon.ClInt32T
class eClCorObjFlagsT(clUtils.Enum):
    CL_COR_OBJ_CACHE_LOCAL = 0x1
    CL_COR_OBJ_CACHE_ONLY_ON_MASTER = 0x2
    CL_COR_OBJ_CACHE_ON_MASTER = 0x4
    CL_COR_OBJ_CACHE_GLOBAL = 0x8
    CL_COR_OBJ_CACHE_MAX = CL_COR_OBJ_CACHE_GLOBAL
    CL_COR_OBJ_CACHE_MASK = 0xFF
    CL_COR_OBJ_PERSIST = 0x100
    CL_COR_OBJ_DO_NOT_PUBLISH = 0x200
    CL_COR_OBJ_ALLOW_SUB_TREE_DELETE = 0x400
    CL_COR_OBJ_FLAGS_ALL = (CL_COR_OBJ_CACHE_MASK |
                            CL_COR_OBJ_PERSIST    |
                            CL_COR_OBJ_DO_NOT_PUBLISH |
                            CL_COR_OBJ_ALLOW_SUB_TREE_DELETE)

CL_COR_OBJ_FLAGS_DEFAULT = (eClCorObjFlagsT.CL_COR_OBJ_CACHE_GLOBAL |
                            eClCorObjFlagsT.CL_COR_OBJ_PERSIST |
                            eClCorObjFlagsT.CL_COR_OBJ_ALLOW_SUB_TREE_DELETE)

ClCorBundleOperationTypeT = clCommon.ClInt32T
class eClCorBundleOperationTypeT(clUtils.Enum):
    CL_COR_BUNDLE_TRANSACTIONAL = 1
    CL_COR_BUNDLE_NON_TRANSACTIONAL = 2

ClCorAddrT = clIocApi.ClIocPhysicalAddressT
ClCorAddrPtrT = ctypes.POINTER(ClCorAddrT)

class ClCorCommInfoT(ctypes.Structure):
    _fields_ = [
        ("addr", ClCorAddrT),
        ("timeout", clCommon.ClUint32T),
        ("maxRetries", clCommon.ClUint16T),
        ("maxSessions", clCommon.ClUint16T)
    ]

ClCorCommInfoPtrT = ctypes.POINTER(ClCorCommInfoT)

ClCorMoPathQualifierT = clCommon.ClInt32T
class eClCorMoPathQualifierT(clUtils.Enum):
    CL_COR_MO_PATH_ABSOLUTE = 0
    CL_COR_MO_PATH_RELATIVE = 1
    CL_COR_MO_PATH_RELATIVE_TO_BASE = 2
    CL_COR_MO_PATH_QUALIFIER_MAX = CL_COR_MO_PATH_RELATIVE_TO_BASE

class ClCorMOHandleT(ctypes.Structure):
    _fields_ = [
        ("type", ClCorClassTypeT),
        ("instance", ClCorInstanceIdT)
    ]

ClCorMOHandlePtrT = ctypes.POINTER(ClCorMOHandleT)

ClCorMOServiceIdT = clCommon.ClInt16T

class ClCorMOIdT(ctypes.Structure):
    _fields_ = [
        ("node", ClCorMOHandleT * CL_COR_HANDLE_MAX_DEPTH),
        ("svcId", ClCorMOServiceIdT),
        ("depth", clCommon.ClUint16T),
        ("qualifier", ClCorMoPathQualifierT),
        ("version", clCommon.ClVersionT)
    ]

ClCorMOIdPtrT = ctypes.POINTER(ClCorMOIdT)

class ClCorAttrIdIdxPairT(ctypes.Structure):
    _fields_ = [
        ("attrId", ClCorAttrIdT),
        ("index", clCommon.ClUint32T)
    ]

ClCorAttrIdIdxPairPtr = ctypes.POINTER(ClCorAttrIdIdxPairT)

class ClCorAttrPathT(ctypes.Structure):
    _fields_ = [
        ("node", ClCorAttrIdIdxPairT * CL_COR_CONT_ATTR_MAX_DEPTH),
        ("depth", clCommon.ClUint16T),
        ("tmp", clCommon.ClUint16T)
    ]

ClCorAttrPathPtrT = ctypes.POINTER(ClCorAttrPathT)

class ClCorObjAttrWalkFilterT(ctypes.Structure):
    _fields_ = [
        ("baseAttrWalk", clCommon.ClUint8T),
        ("contAttrWalk", clCommon.ClUint8T),
        ("pAttrPath", ClCorAttrPathT),
        ("attrId", ClCorAttrIdT),
        ("index", clCommon.ClInt32T),
        ("cmpFlag", ClCorAttrCmpFlagT),
        ("attrWalkOption", ClCorAttrWalkOpT),
        ("size", clCommon.ClUint32T),
        ("value", clCommon.ClPtrT)
    ]

ClCorObjAttrWalkFuncT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ClCorAttrPathPtrT,
    ClCorAttrIdT,
    ClCorAttrTypeT,
    ClCorTypeT,
    clCommon.ClPtrT,
    clCommon.ClUint32T,
    ClCorAttrFlagT,
    clCommon.ClPtrT
)

class ClCorMOClassTreeWalkInfoT(ctypes.Structure):
    _fields_ = [
        ("classId", ClCorClassTypeT),
        ("flags", clCommon.ClUint16T),
        ("maxInstances", clCommon.ClUint32T)
    ]

ClCorMOClassTreeWalkInfoPtrT = ctypes.POINTER(ClCorMOClassTreeWalkInfoT)

class ClCorMOClassPathT(ctypes.Structure):
    _fields_ = [
        ("node", ClCorClassTypeT * CL_COR_HANDLE_MAX_DEPTH),
        ("depth", clCommon.ClUint32T),
        ("qualifier", ClCorMoPathQualifierT)
    ]

ClCorMOClassPathPtrT = ctypes.POINTER(ClCorMOClassPathT)

class ClCorTxnInfoT(ctypes.Structure):
    _fields_ = [
        ("opType", ClCorOpsT),
        ("moId", ClCorMOIdT),
        ("attrPath", ClCorAttrPathT),
        ("attrId", ClCorAttrIdT),
        ("jobStatus", clCommon.ClUint32T)
    ]

ClCorTxnInfoPtrT = ctypes.POINTER(ClCorTxnInfoT)

ClCorTxnEntryIdT = clCommon.ClInt32T
class eClCorTxnEntryIdT(clUtils.Enum):
    CL_COR_TXN_INFO_ADD = 0
    CL_COR_TXN_INFO_FIRST_GET = 1
    CL_COR_TXN_INFO_NEXT_GET = 2
    CL_COR_TXN_INFO_CLEAN = 3

class ClCorTxnInfoStoreT(ctypes.Structure):
    _fields_ = [
        ("op", ClCorTxnEntryIdT),
        ("txnSessionId", ClCorTxnSessionIdT),
        ("txnInfo", ClCorTxnInfoT)
    ]

ClCorTxnInfoStorePtrT = ctypes.POINTER(ClCorTxnInfoStoreT)

class ClCorAttributeValueT(ctypes.Structure):
    _fields_ = [
        ("pAttrPath", ClCorAttrPathPtrT),
        ("attrId", ClCorAttrIdT),
        ("index", clCommon.ClInt32T),
        ("bufferPtr", clCommon.ClPtrT),
        ("bufferSize", clCommon.ClInt32T)
    ]

ClCorAttributeValuePtrT = ctypes.POINTER(ClCorAttributeValueT)

class ClCorAttributeValueListT(ctypes.Structure):
    _fields_ = [
        ("numOfValues", clCommon.ClUint32T),
        ("pAttributeValue", ClCorAttributeValuePtrT)
    ]

ClCorAttributeValueListPtrT = ctypes.POINTER(ClCorAttributeValueListT)

class ClCorAttrValueDescriptorT(ctypes.Structure):
    _fields_ = [
        ("pAttrPath", ClCorAttrPathPtrT),
        ("attrId", ClCorAttrIdT),
        ("index", clCommon.ClInt32T),
        ("bufferPtr", clCommon.ClPtrT),
        ("bufferSize", clCommon.ClInt32T),
        ("pJobStatus", ctypes.POINTER(ClCorJobStatusT))
    ]

ClCorAttrValueDescriptorPtrT = ctypes.POINTER(ClCorAttrValueDescriptorT)

class ClCorAttrValueDescriptorListT(ctypes.Structure):
    _fields_ = [
        ("numOfDescriptor", clCommon.ClUint32T),
        ("pAttrDescriptor", ClCorAttrValueDescriptorPtrT)
    ]

ClCorAttrValueDescriptorListPtrT = ctypes.POINTER(ClCorAttrValueDescriptorListT)

class ClCorJobDescriptorT(ctypes.Structure):
    _fields_ = [
        ("objHandle", ctypes.POINTER(ClCorObjectHandleT)),
        ("pMoId", ClCorMOIdPtrT),
        ("opType", ClCorOpsT),
        ("numOfAttrDesc", clCommon.ClUint32T),
        ("pAttrDesc", ClCorAttrValueDescriptorPtrT)
    ]

ClCorJobDescriptorPtrT = ctypes.POINTER(ClCorJobDescriptorT)

class ClCorBundleConfigT(ctypes.Structure):
    _fields_ = [
        ("bundleType", ClCorBundleOperationTypeT)
    ]

ClCorBundleConfigPtrT = ctypes.POINTER(ClCorBundleConfigT)

ClCorObjectWalkFunT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clCommon.ClPtrT,
    clCommon.ClPtrT
)

clCorXdrMarshallFP = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clCommon.ClPtrT,
    clBufferApi.ClBufferHandleT,
    clCommon.ClUint32T
)

clCorXdrUnmarshallFP = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clBufferApi.ClBufferHandleT,
    clCommon.ClPtrT
)

ClCorBundleCallbackPtrT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ClCorBundleHandleT,
    clCommon.ClPtrT
)
