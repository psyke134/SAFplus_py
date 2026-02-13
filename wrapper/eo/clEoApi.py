import sys
sys.path.append("..")

from utils import clLib, clUtils, clRadixTree
from common import clCommon, clVersion
from osal import clOsalApi
from event import clEventApi
from buffer import clBufferApi
from eo import clEoConfigApi
from cnt import clCntApi
from ioc import clIocApi
from rmd import clRmdApi

import ctypes, enum

CL_EO_MAX_NO_FUNC = 64

ClEOServiceInstallOrderT = clCommon.ClInt32T
class eClEOServiceInstallOrderT(clUtils.Enum):
    CL_EO_ADD_TO_FRONT  = 0
    CL_EO_ADD_TO_BACK   = 1

CL_EO_CLIENT_BIT_SHIFT = 6

CL_EO_FN_MASK = 0x3f

def CL_EO_GET_FULL_FN_NUM(cl, fn):
    _cl = cl.value
    _fn = fn.value
    return ((_cl) << CL_EO_CLIENT_BIT_SHIFT) | ((_fn) << 0)

ClEoDataT = clOsalApi.ClOsalTaskDataT

ClEoArgT = clCommon.ClUint32T

ClEoClientIdT = clCommon.ClInt32T
class eClEoClientIdT(clUtils.Enum):
    CL_EO_NATIVE_COMPONENT_TABLE_ID = 0
    CL_EO_DEFAULT_SERVICE_TABLE_ID = 1
    CL_EO_EO_MGR_CLIENT_TABLE_ID = 2
    CL_EO_COR_CLIENT_TABLE_ID = 3
    CL_EO_EVT_CLIENT_TABLE_ID = 4
    CL_CPM_MGR_CLIENT_TABLE_ID = 5
    CL_ALARM_CLIENT_TABLE_ID = 6
    CL_DEBUG_CLIENT_TABLE_ID = 7
    CL_TXN_CLIENT_TABLE_ID = 8
    CL_AMS_MGMT_SERVER_TABLE_ID = 9
    CL_AMS_MGMT_CLIENT_TABLE_ID = 10
    CL_LOG_CLIENT_TABLE_ID = 11
    CL_EO_CKPT_CLIENT_TABLE_ID = 12
    CL_EO_RMD_CLIENT_TABLE_ID = 13
    CL_AMS_ENTITY_TRIGGER_TABLE_ID = 14
    CL_CPM_MGMT_CLIENT_TABLE_ID = 15
    CL_MSG_CLIENT_TABLE_ID = 16
    CL_MSG_CLIENT_SERVER_TABLE_ID = 17
    CL_AMS_MGMT_SERVER_TABLE2_ID = 18
    CL_EO_CLOVIS_RESERVED_CLIENTID_END  = 19

CL_EO_USER_CLIENT_ID_START = eClEoClientIdT.CL_EO_CLOVIS_RESERVED_CLIENTID_END

CL_EO_SERVER_COOKIE_BIT_SIZE = 8

def CL_EO_SERVER_COOKIE_BASE(cId):
    return cId << CL_EO_SERVER_COOKIE_BIT_SIZE

CL_EO_EVENT_CHANNEL_NAME = "CL_EO_EVENT_CHANNEL_NAME"
CL_EO_EVENT_SUBSCRIBE_FLAG = clEventApi.CL_EVENT_CHANNEL_SUBSCRIBER | clEventApi.CL_EVENT_GLOBAL_CHANNEL
#define CL_EO_EVENT_DEFAULT_FILTER NULL

ClEoServerIdT = clCommon.ClInt32T
class eClEoServerIdT(clUtils.Enum):
    CL_EO_NATIVE_COMPONENT_COOKIE_BASE  = CL_EO_SERVER_COOKIE_BASE(eClEoClientIdT.CL_EO_NATIVE_COMPONENT_TABLE_ID)
    CL_EO_EO_MGR_SERVER_COOKIE_ID       = CL_EO_SERVER_COOKIE_BASE(eClEoClientIdT.CL_EO_EO_MGR_CLIENT_TABLE_ID)
    CL_EO_COR_SERVER_COOKIE_ID          = CL_EO_SERVER_COOKIE_BASE(eClEoClientIdT.CL_EO_COR_CLIENT_TABLE_ID)
    CL_EO_EVT_EVENT_DELIVERY_COOKIE_ID  = CL_EO_SERVER_COOKIE_BASE(eClEoClientIdT.CL_EO_EVT_CLIENT_TABLE_ID)
    CL_EO_DEBUG_OBJECT_COOKIE_ID        = CL_EO_SERVER_COOKIE_BASE(eClEoClientIdT.CL_DEBUG_CLIENT_TABLE_ID)
    CL_EO_RMD_CLIENT_COOKIE_ID          = CL_EO_SERVER_COOKIE_BASE(eClEoClientIdT.CL_EO_RMD_CLIENT_TABLE_ID)

ClEoPayloadWithReplyCallbackT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ClEoDataT,
    clBufferApi.ClBufferHandleT,
    clBufferApi.ClBufferHandleT
)

class ClEoPayloadWithReplyCallbackServerT(ctypes.Structure):
    _fields_ = [
        ("fun", ClEoPayloadWithReplyCallbackT),
        ("funId", clCommon.ClUint32T),
        ("version", clCommon.ClUint32T)
    ]

class ClEoPayloadWithReplyCallbackClientT(ctypes.Structure):
    _fields_ = [
        ("funId", clCommon.ClUint32T),
        ("version", clCommon.ClUint32T)
    ]

class ClEoPayloadWithReplyCallbackTableClientT(ctypes.Structure):
    _fields_ = [
        ("clientID", clCommon.ClUint32T),
        ("funTable", ctypes.POINTER(ClEoPayloadWithReplyCallbackClientT)),
        ("funTableSize", clCommon.ClUint32T)
    ]

class ClEoPayloadWithReplyCallbackTableServerT(ctypes.Structure):
    _fields_ = [
        ("clientID", clCommon.ClUint32T),
        ("funTable", ctypes.POINTER(ClEoPayloadWithReplyCallbackServerT)),
        ("funTableSize", clCommon.ClUint32T)
    ]

_func = ctypes.CFUNCTYPE(None)
class ClEoServiceObjT(ctypes.Structure):
    pass
ClEoServiceObjT._fields_ = [
    ("func", _func),
    ("pNextServObj", ctypes.POINTER(ClEoServiceObjT))
]

class ClEoClientObjT(ctypes.Structure):
    _fields_ = [
        ("funcs", ClEoServiceObjT * CL_EO_MAX_NO_FUNC),
        ("data", ClEoDataT)
    ]

def _CLIENT_RADIX_TREE_INDEX(fun_id, version_code):
    return ((fun_id & CL_EO_FN_MASK) << clVersion.CL_VERSION_SHIFT) | ((version_code) & clVersion.CL_VERSION_MASK)

class ClEoClientTableT(ctypes.Structure):
    _fields_ = [
        ("maxClients", clCommon.ClUint32T),
        ("funTable", clRadixTree.ClRadixTreeHandleT)
    ]

class ClEoServerTableT(ctypes.Structure):
    _fields_ = [
        ("maxClients", clCommon.ClUint32T),
        ("funTable", clRadixTree.ClRadixTreeHandleT),
        ("data", ClEoDataT)
    ]

class ClEoExecutionObjT(ctypes.Structure):
    _fields_ = [
        ("name", clCommon.ClCharT * clEoConfigApi.CL_EO_MAX_NAME_LEN),
        ("eoID", clEoConfigApi.ClEoIdT),
        ("pri", clOsalApi.ClOsalThreadPriorityT),
        ("state", clEoConfigApi.ClEoStateT),
        ("threadRunning", clCommon.ClUint32T),
        ("pClient", ctypes.POINTER(ClEoClientObjT)),
        ("pClientTable", ctypes.POINTER(ClEoClientTableT)),
        ("pServerTable", ctypes.POINTER(ClEoServerTableT)),
        ("noOfThreads", clCommon.ClUint32T),
        ("pEOPrivDataHdl", clCntApi.ClCntHandleT),
        ("commObj", clIocApi.ClIocCommPortHandleT),
        ("rmdObj", clRmdApi.ClRmdObjHandleT),
        ("eoInitDone", clCommon.ClUint32T),
        ("eoSetDoneCnt", clCommon.ClUint32T),
        ("eoTaskIdInfo", clCntApi.ClCntHandleT),
        ("refCnt", clCommon.ClUint32T),
        ("eoMutex", clOsalApi.ClOsalMutexT),
        ("eoCond", clOsalApi.ClOsalCondT),
        ("eoPort", clIocApi.ClIocPortT),
        ("appType", clCommon.ClUint32T),
        ("maxNoClients", clCommon.ClUint32T),
        ("clEoCreateCallout", clEoConfigApi.ClEoAppCreateCallbackT),
        ("clEoDeleteCallout", clEoConfigApi.ClEoAppDeleteCallbackT),
        ("clEoStateChgCallout", clEoConfigApi.ClEoAppStateChgCallbackT),
        ("clEoHealthCheckCallout", clEoConfigApi.ClEoAppHealthCheckCallbackT),
    ]

ClEoCallFuncCallbackT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ClEoPayloadWithReplyCallbackT,
    ClEoDataT,
    clBufferApi.ClBufferHandleT,
    clBufferApi.ClBufferHandleT
)

ClEoProtoCallbackT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(ClEoExecutionObjT),
    clBufferApi.ClBufferHandleT,
    clCommon.ClUint8T,
    clCommon.ClUint8T,
    clCommon.ClUint32T,
    clIocApi.ClIocPhysicalAddressT
)

class ClEoProtoDefT(ctypes.Structure):
    _fields_ = [
        ("protoID", clCommon.ClUint8T),
        ("name", clCommon.ClCharT * clCommon.CL_MAX_NAME_LENGTH),
        ("func", ClEoProtoCallbackT),
        ("nonblockingHandler", ClEoProtoCallbackT),
        ("flags", clCommon.ClUint32T)
    ]

# --- Client Table Management ---

def clEoClientInstallTables(pThis, table):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClEoPayloadWithReplyCallbackTableServerT *table
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoClientInstallTables(clUtils.byref(pThis), clUtils.byref(table))


def clEoClientInstallTablesWithCookie(pThis, table, data):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClEoPayloadWithReplyCallbackTableServerT *table,
        ClEoDataT data
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoClientInstallTablesWithCookie(clUtils.byref(pThis), clUtils.byref(table), data)


def clEoClientUninstallTables(pThis, table):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClEoPayloadWithReplyCallbackTableServerT *table
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoClientUninstallTables(clUtils.byref(pThis), clUtils.byref(table))


def clEoClientTableFilter(eoPort, clientID):
    """
    arg types:
        ClIocPortT eoPort,
        ClUint32T clientID
    return type:
        ClBoolT
    """
    clLib.libmw_so.clEoClientTableFilter.restype = clCommon.ClBoolT
    return clLib.libmw_so.clEoClientTableFilter(eoPort, clientID)


def clEoClientTableRegister(clientTable, clientPort):
    """
    arg types:
        ClEoPayloadWithReplyCallbackTableClientT *clientTable,
        ClIocPortT clientPort
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoClientTableRegister(clUtils.byref(clientTable), clientPort)

def clEoRefDec(eo):
    """
    Decrements the reference count of the Execution Object.
    arg types:
        ClEoExecutionObjT *eo
    return type:
        void
    """
    clLib.libmw_so.clEoRefDec(clUtils.byref(eo))


def clEoProtoInstall(def_ptr):
    """
    arg types:
        ClEoProtoDefT* def
    return type:
        void
    """
    clLib.libmw_so.clEoProtoInstall(clUtils.byref(def_ptr))


def clEoProtoUninstall(id):
    """
    arg types:
        ClUint8T id
    return type:
        void
    """
    clLib.libmw_so.clEoProtoUninstall(id)


def clEoProtoSwitch(def_ptr):
    """
    arg types:
        ClEoProtoDefT* def
    return type:
        void
    """
    clLib.libmw_so.clEoProtoSwitch(clUtils.byref(def_ptr))


# --- Execution and Traversal (Walk) ---

def clEoWalk(pThis, func, pFuncCallout, inMsgHdl, outMsgHdl):
    """
    Traverses the EO to execute a specific function.
    arg types:
        ClEoExecutionObjT *pThis,
        ClUint32T func,
        ClEoCallFuncCallbackT pFuncCallout,
        ClBufferHandleT inMsgHdl,
        ClBufferHandleT outMsgHdl
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoWalk(clUtils.byref(pThis), func, pFuncCallout, inMsgHdl, outMsgHdl)


def clEoWalkWithVersion(pThis, func, version, pFuncCallout, inMsgHdl, outMsgHdl):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClUint32T func,
        ClVersionT *version,
        ClEoCallFuncCallbackT pFuncCallout,
        ClBufferHandleT inMsgHdl,
        ClBufferHandleT outMsgHdl
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoWalkWithVersion(clUtils.byref(pThis), func, clUtils.byref(version), pFuncCallout, inMsgHdl, outMsgHdl)


# --- Client/Service Installation ---

def clEoServiceValidate(pThis, func):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClUint32T func
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoServiceValidate(clUtils.byref(pThis), func)


def clEoClientInstall(pThis, clientId, pFuncs, data, nFuncs):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClUint32T clientId,
        ClEoPayloadWithReplyCallbackT *pFuncs,
        ClEoDataT data,
        ClUint32T nFuncs
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoClientInstall(clUtils.byref(pThis), clientId, clUtils.byref(pFuncs), data, nFuncs)


def clEoClientInstallTable(pThis, clientId, data, pFuncs, nFuncs):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClUint32T clientId,
        ClEoDataT data,
        ClEoPayloadWithReplyCallbackServerT *pFuncs,
        ClUint32T nFuncs
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoClientInstallTable(clUtils.byref(pThis), clientId, data, clUtils.byref(pFuncs), nFuncs)


def clEoClientUninstall(pThis, clientId):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClUint32T clientId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoClientUninstall(clUtils.byref(pThis), clientId)


def clEoClientUninstallTable(pThis, clientID, pfunTable, nentries):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClUint32T clientID,
        ClEoPayloadWithReplyCallbackServerT *pfunTable,
        ClUint32T nentries
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoClientUninstallTable(clUtils.byref(pThis), clientID, clUtils.byref(pfunTable), nentries)


def clEoServiceInstall(pThis, pFunction, iFuncNum, order):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClEoPayloadWithReplyCallbackT pFunction,
        ClUint32T iFuncNum,
        ClEOServiceInstallOrderT order
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoServiceInstall(clUtils.byref(pThis), pFunction, iFuncNum, order)


def clEoServiceUninstall(pThis, pFunction, iFuncNum):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClEoPayloadWithReplyCallbackT pFunction,
        ClUint32T iFuncNum
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoServiceUninstall(clUtils.byref(pThis), pFunction, iFuncNum)


# --- Data and Port Management ---

def clEoClientDataSet(pThis, clientId, data):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClUint32T clientId,
        ClEoDataT data
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoClientDataSet(clUtils.byref(pThis), clientId, data)


def clEoClientDataGet(pThis, clientId, pData):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClUint32T clientId,
        ClEoDataT *pData
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoClientDataGet(clUtils.byref(pThis), clientId, clUtils.byref(pData))


def clEoPrivateDataSet(pThis, type_id, pData):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClUint32T type,
        void *pData
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoPrivateDataSet(clUtils.byref(pThis), type_id, pData)


def clEoPrivateDataGet(pThis, type_id, data):
    """
    arg types:
        ClEoExecutionObjT *pThis,
        ClUint32T type,
        void **data
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoPrivateDataGet(clUtils.byref(pThis), type_id, clUtils.byref(data))


def clEoMyEoIocPortSet(iocPort):
    """
    arg types:
        ClIocPortT iocPort
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoMyEoIocPortSet(iocPort)


def clEoMyEoIocPortGet(pIocPort):
    """
    arg types:
        ClIocPortT *pIocPort
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoMyEoIocPortGet(clUtils.byref(pIocPort))


def clEoMyEoObjectSet(eoObj):
    """
    arg types:
        ClEoExecutionObjT* eoObj
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoMyEoObjectSet(clUtils.byref(eoObj))


def clEoMyEoObjectGet(pEOObj):
    """
    arg types:
        ClEoExecutionObjT** pEOObj
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoMyEoObjectGet(clUtils.byref(pEOObj))


def clEoReceiveStart(pThis):
    """
    arg types:
        ClEoExecutionObjT *pThis
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoReceiveStart(clUtils.byref(pThis))

ClEoCrashReasonT = clCommon.ClInt32T
class eClEoCrashReasonT(clUtils.Enum):
    CL_EO_CRASH_DEADLOCK = 0
    CL_EO_CRASH_HUNG_SYSCALL = 1

class ClEoCrashNotificationT(ctypes.Structure):
    _fields_ = [
        ("reason", ClEoCrashReasonT),
        ("pid", ctypes.c_int),
        ("tid", clOsalApi.ClOsalTaskIdT),
        ("interval", clCommon.ClTimeT),
        ("compName", ctypes.c_char_p)
    ]

ClEoCrashDeadlockT = ClEoCrashNotificationT

class ClEoCrashHungSyscallT(ctypes.Structure):
    _TASK_SND_MASK = ctypes.c_int(1)
    _TASK_RCV_MASK = ctypes.c_int(2)

    def _IS_TASK_SND(mask):
        _mask = mask.value
        return _mask & ClEoCrashHungSyscallT._TASK_SND_MASK
    
    def _IS_TASK_RCV(mask):
        _mask = mask.value
        return _mask & ClEoCrashHungSyscallT._TASK_RCV_MASK
    
    _fields_ = [
        ("crash", ClEoCrashNotificationT),
        ("mask", clCommon.ClUint32T)
    ]

ClEoCrashNotificationCallbackT = ctypes.CFUNCTYPE(
    None,
    ctypes.POINTER(ClEoCrashNotificationT)
)

def clEoCrashNotificationRegister(callback):
    """
    arg types:
        ClEoCrashNotificationCallbackT callback
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoCrashNotificationRegister(callback)
