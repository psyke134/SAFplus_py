import sys
sys.path.append("..")

from utils import clLib, clUtils
from common import clCommon, clCommonErrors
from ioc import clIocApi, clIocErrors
from buffer import clBufferApi

import ctypes

CL_RMD_CALL_ASYNC = (1<<0)
CL_RMD_CALL_NEED_REPLY = (1<<1)
CL_RMD_CALL_ATMOST_ONCE = (1<<2)
CL_RMD_CALL_DO_NOT_OPTIMIZE = (1<<3)
CL_RMD_CALL_NON_PERSISTENT = (1<<4)
CL_RMD_CALL_IN_SESSION = (1<<5)
CL_RMD_HEADER_VERSION = 1
CL_RMD_DEFAULT_PRIORITY = clIocApi.eClIocPriorityT.CL_IOC_DEFAULT_PRIORITY
CL_RMD_DEFAULT_TIMEOUT = 10000
CL_RMD_DEFAULT_RETRIES = 5
CL_RMD_DEFAULT_TRANSPORT_HANDLE = 0
CL_RMD_TIMEOUT_FOREVER = -1

def CL_RMD_UNREACHABLE_CHECK(ret):
    return clCommonErrors.CL_GET_ERROR_CODE(ret) == clIocErrors.CL_IOC_ERR_COMP_UNREACHABLE or clCommonErrors.CL_GET_ERROR_CODE(ret) == clIocErrors.CL_IOC_ERR_HOST_UNREACHABLE

def CL_RMD_TIMEOUT_UNREACHABLE_CHECK(ret):
    return clCommonErrors.CL_GET_ERROR_CODE(ret) == clCommonErrors.CL_ERR_TIMEOUT or CL_RMD_UNREACHABLE_CHECK(ret)

def CL_RMD_VERSION_ERROR(rc):
    err_doesnt_exist = clCommonErrors.CL_ERR_DOESNT_EXIST
    err_version_mismatch = clCommonErrors.CL_ERR_VERSION_MISMATCH
    cl_cid_eo = clCommon.eClCompIdT.CL_CID_EO
    return rc == clCommonErrors.CL_RC(cl_cid_eo, err_doesnt_exist) or rc == clCommonErrors.CL_RC(cl_cid_eo, err_version_mismatch)

ClRmdAsyncCallbackT = ctypes.CFUNCTYPE(
    None,
    clCommon.ClRcT,
    clCommon.ClPtrT,
    clBufferApi.ClBufferHandleT,
    clBufferApi.ClBufferHandleT
)

ClRmdObjHandleT = clCommon.ClPtrT

class ClRmdOptionsT(ctypes.Structure):
    _fields_ = [
        ("timeout", clCommon.ClUint32T),
        ("retries", clCommon.ClUint32T),
        ("priority", clCommon.ClUint8T),
        ("transportHandle", clIocApi.ClIocToBindHandleT)
    ]

class ClRmdAsyncOptionsT(ctypes.Structure):
    _fields_ = [
        ("pCookie", clCommon.ClPtrT),
        ("fpCallback", ClRmdAsyncCallbackT)
    ]

def clRmdWithMsg(remoteObjAddr, funcId, inMsgHdl, outMsgHdl, flags, pOptions, pAsyncOptions):
    """
    Input types:
        ClIocAddressT remoteObjAddr,
        ClUint32T funcId,
        ClBufferHandleT inMsgHdl,
        ClBufferHandleT outMsgHdl,
        ClUint32T flags,
        ClRmdOptionsT *pOptions,
        ClRmdAsyncOptionsT *pAsyncOptions
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdWithMsg(remoteObjAddr, funcId, inMsgHdl, outMsgHdl, flags, clUtils.byref(pOptions), clUtils.byref(pAsyncOptions))

def clRmdWithMsgVer(remoteObjAddr, version, funcId, inMsgHdl, outMsgHdl, flags, pOptions, pAsyncOptions):
    """
    Input types:
        ClIocAddressT remoteObjAddr,
        ClVersionT *version,
        ClUint32T funcId,
        ClBufferHandleT inMsgHdl,
        ClBufferHandleT outMsgHdl,
        ClUint32T flags,
        ClRmdOptionsT *pOptions,
        ClRmdAsyncOptionsT *pAsyncOptions
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdWithMsgVer(remoteObjAddr, clUtils.byref(version), funcId, inMsgHdl, outMsgHdl, flags, clUtils.byref(pOptions), clUtils.byref(pAsyncOptions))
