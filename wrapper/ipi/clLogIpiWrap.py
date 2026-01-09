import sys
sys.path.append("..")

from utils import clLib
from common import clCommon
from log import clLogApi
from ioc import clIocApi
from timer import clTimerApi

import ctypes

CL_LOG_EMERGENCY = 0x1
CL_LOG_ALERT = 0x2
CL_LOG_CRITICAL = 0x3
CL_LOG_ERROR = 0x4
CL_LOG_WARNING = 0x5
CL_LOG_NOTICE = 0x6
CL_LOG_INFO = 0x7
CL_LOG_INFORMATIONAL = CL_LOG_INFO
CL_LOG_DEBUG = 0x8
CL_LOG_DEBUG1 = CL_LOG_DEBUG
CL_LOG_DEBUG2 = 0x9
CL_LOG_DEBUG3 = 0xa
CL_LOG_DEBUG4 = 0xb
CL_LOG_DEBUG5 = 0xc
CL_LOG_TRACE = CL_LOG_DEBUG5
CL_LOG_DEBUG6 = 0xd
CL_LOG_DEBUG7 = 0xe
CL_LOG_DEBUG8 = 0xf
CL_LOG_DEBUG9 = 0x10
CL_LOG_MAX = 0x15
CL_LOG_END = CL_LOG_MAX


CL_LOG_MESSAGE_1_SERVICE_STARTED = "%s server fully up"
CL_LOG_MESSAGE_1_SERVICE_STOPPED = "%s server stopped"
CL_LOG_MESSAGE_0_ENV_NOT_SET = "ASP_CONFIG environment variable is not set"
CL_LOG_MESSAGE_1_INVALID_PARAMETER = "Invalid parameter passed in function [%s]"
CL_LOG_MESSAGE_2_OUT_OF_RANGE_INDEX = "Index [%d] out of range in function [%s]"
CL_LOG_MESSAGE_0_INVALID_HANDLE = "Invalid log handle [%llx]"
CL_LOG_MESSAGE_0_NULL_ARGUMENT = "NULL argument passed"
CL_LOG_MESSAGE_1_FUNC_OBSOLETE = "Function [%s] is obsolete"
CL_LOG_MESSAGE_1_XML_ERROR = "XML file [%s] not valid"
CL_LOG_MESSAGE_0_RESOURCE_NON_EXISTENT = "Requested resource does not exist"
CL_LOG_MESSAGE_0_INVALID_BUFFER = "The buffer passed is invalid"
CL_LOG_MESSAGE_0_DUPLICATE_ENTRY = "Duplicate entry"
CL_LOG_MESSAGE_0_PARAM_OUT_OF_RANGE = "Paramenter passed is out of range"
CL_LOG_MESSAGE_0_RESOURCE_UNAVAILABLE = "No resources available"
CL_LOG_MESSAGE_0_COMPONENT_INITIALIZED = "Component already initialized"
CL_LOG_MESSAGE_0_BUFFER_OVERRUN = "Buffer over run"
CL_LOG_MESSAGE_0_COMPONENT_UNINITIALIZED = "Component not initialized"
CL_LOG_MESSAGE_0_VERSION_MISMATCH = "Version mismatch"
CL_LOG_MESSAGE_0_ENTRY_ALREADY_EXISTING = "An entry is already existing"
CL_LOG_MESSAGE_0_INVALID_STATE = "Invalid State"
CL_LOG_MESSAGE_0_RESOURCE_BUSY = "Resource is in use"
CL_LOG_MESSAGE_1_COMPONENT_BUSY = "Component [%s] is busy, try again"
CL_LOG_MESSAGE_0_CALLBACK_UNAVAILABLE = "No callback available for request"
CL_LOG_MESSAGE_0_MEMORY_ALLOCATION_FAILED = "Failed to allocate memory"
CL_LOG_MESSAGE_2_COMMUNICATION_FAILED = "Failed to communicate with [%s], rc=[0x%x]"
CL_LOG_MESSAGE_2_HOST_UNREACHABLE = "Host [%s] unreachable, rc=[0x%x]"
CL_LOG_MESSAGE_2_SERVICE_START_FAILED = "Service [%s] could not be started, rc=[0x%x]"
CL_LOG_MESSAGE_2_LIBRARY_INIT_FAILED = "Library [%s] initialization failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CKPT_READ_FAILED = "Reading checkpoint data failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CKPT_WRITE_FAILED = "Unable to write Checkpoint dataset, rc=[0x%x]"
CL_LOG_MESSAGE_1_CNT_CREATE_FAILED = "Container creation failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CNT_DATA_GET_FAILED = "Container data get failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CNT_DATA_ADD_FAILED = "Container data addition failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CNT_DATA_DELETE_FAILED = "Container data delete failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_MY_EO_OBJ_GET_FAILED = "Unable to get eo object, rc=[0x%x]"
CL_LOG_MESSAGE_2_EVT_CHANNEL_OPEN_FAILED = "Opening event channel [%s] failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_EVT_SUBSCRIBE_FAILED = "Event subsription failed, rc=[0x%x]"
CL_LOG_MESSAGE_0_ASP_BINDIR_ENV_NOT_SET = "ASP_BINDIR environment variable not set"
CL_LOG_MESSAGE_1_CNT_NODE_FIND_FAILED = "Container node find failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CNT_NODE_GET_FAILED = "Container node get failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CNT_NODE_ADD_FAILED = "Container node add failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CNT_WALK_FAILED = "Container walk failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CNT_DELETE_FAILED = "Container delete failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_COR_EVT_SUBSCRIBE_FAILED = "Cor event subscribe failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_COR_OBJ_HANDLE_GET_FAILED = "Cor object handle get failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_COR_ATTR_TYPE_GET_FAILED = "Cor attribute type get failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_COR_MOID_TO_CLASS_GET_FAILED = "Cor MOID to class get failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_COR_NOTIFY_EVENT_TO_MOID_GET_FAILED = "Cor notify event to moid get failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_EVENT_COOKIE_GET_FAILED = "Event cookie get failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_COR_EVENT_TO_ATTR_PATH_GET_FAILED = "Cor event to containment attribute path get failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_COR_ATTR_GET_FAILED = "Cor object attribute get failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CNT_NODE_DELETE_FAILED = "Container node delete failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_COR_OBJ_HANDLE_TO_MOID_GET_FAILED = "Cor object handle to moid get failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_COR_TXN_COMMIT_FAILED = "Cor transaction commit failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_FUNC_NOT_IMPLEMENTED = "Function [%s] not implemented"
CL_LOG_MESSAGE_0_TIMEOUT = "Timeout"
CL_LOG_MESSAGE_1_HANDLE_CREATION_FAILED = "Handle creation failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_HANDLE_DB_CREATION_FAILED = "Handle database creation failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_HANDLE_DB_DESTROY_FAILED = "Handle database destroy failed, rc=[0x%x]"
CL_LOG_MESSAGE_2_GET_HANDLE_FAILED = "Failed to get handle for component [%s], rc=[0x%x]"
CL_LOG_MESSAGE_1_HANDLE_CHECKIN_FAILED = "Handle checkin failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_HANDLE_CHECKOUT_FAILED = "Handle checkout failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_BUFFER_MSG_CREATION_FAILED = "Message creation failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_BUFFER_MSG_READ_FAILED = "Message read failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_BUFFER_MSG_WRITE_FAILED = "Message write failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_BUFFER_MSG_DELETE_FAILED = "Message deletion failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CKPT_CREATION_FAILED = "Checkpoint creation failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CKPT_DATASET_CREATION_FAILED = "Checkpoint dataset creation failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_OSAL_MUTEX_CREATION_FAILED = "Mutex creation failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_OSAL_MUTEX_LOCK_FAILED = "Mutex could not be locked, rc=[0x%x]"
CL_LOG_MESSAGE_1_OSAL_MUTEX_UNLOCK_FAILED = "Mutex could not be unlocked, rc=[0x%x]"
CL_LOG_MESSAGE_1_RMD_CALL_FAILED = "Rmd call failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_FUNC_TABLE_INSTALL_FAILED = "Installation of function table for client failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_CALLOUT_FUNC_DELETE_FAILED = "User callout function deletion failed, rc=[0x%x]"
CL_LOG_MESSAGE_1_DBG_REGISTER_FAILED = "Registration with debug failed, rc=[0x%x]"
CL_CKPT_LOG_4_CLNT_VERSION_NACK = "%s NACK received from Node - Supported Version {'%c', 0x%x, 0x%x}",



CL_LOG_HANDLE_SYS = clCommon.ClHandleT.in_dll(clLib.libmw_so, "CL_LOG_HANDLE_SYS")
CL_LOG_HANDLE_APP = clCommon.ClHandleT.in_dll(clLib.libmw_so, "CL_LOG_HANDLE_APP")

ClLogStreamHdlT = clCommon.ClHandleT

CL_LOG_FILENAME_LENGTH = 80
CL_LOG_FILEPATH_LENGTH = 200
CL_LOG_FORMAT_LENGTH = 50

CL_LOG_SG = 1 << 0
CL_LOG_SU = 1 << 1
CL_LOG_COMP = 1 << 2

CL_LOG_COMPNAME_LENGTH = 50
CL_LOG_MSG_LENGTH = 178

class ClLogHeaderT(ctypes.Structure):
    _fields_ = [
        ("logSeverity", clLogApi.ClLogSeverityT),
        ("streamHdl", ClLogStreamHdlT),
        ("pid", clCommon.ClUint32T),
        ("iocAddress", clIocApi.ClIocPhysicalAddressT),
        ("time", clTimerApi.ClTimerTimeOutT),
        ("compName", clCommon.ClCharT),
        ("msg", clCommon.ClCharT)
    ]

class ClLogFileConfigT(ctypes.Structure):
    _fields_ = [
        ("maxRecordSize", clCommon.ClUint32T),
        ("maxFileSize", clCommon.ClUint64T),
        ("fileName", clCommon.ClCharT),
        ("fileLoc", clCommon.ClCharT)
    ]

class ClLogFormatFileConfigT(ctypes.Structure):
    _fields_ = [
        ("format", clCommon.ClCharT * CL_LOG_FORMAT_LENGTH),
        ("fileConfig", ClLogFileConfigT)
    ]

class ClLogFilterPatternT(ctypes.Structure):
    _fields_ = [
        ("bitMap", clCommon.ClUint32T),
        ("sgName", clCommon.ClNameT),
        ("suName", clCommon.ClNameT),
        ("compName", clCommon.ClNameT)
    ]

ClLogSeverityFlagsT = clCommon.ClUint16T

def clLogLibInitialize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogLibInitialize()


def clLogLibFinalize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogLibFinalize()

def clLogOpen(handle, fileConfig):
    """
    arg types: 
        ClLogStreamHdlT *handle,
        ClLogFormatFileConfigT fileConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogOpen(handle, fileConfig)


def clLogClose(handle):
    """
    arg types:
        ClLogStreamHdlT handle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogClose(handle)

def clLogLevelSet(severity):
    """
    arg types:
        ClLogSeverityT severity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogLevelSet(severity)


def clLogLevelGet(severity):
    """
    arg types:
        ClLogSeverityT *severity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogLevelGet(severity)


# TODO: there're remaining codes in the original header file
