import sys
sys.path.append("..")

from utils import clLib, clUtils
from log import clLogApi
from ipi import clLogIpiWrap
from common import clCommon

CL_LOG_MAX_MSG_LEN = 1024
CL_LOG_MAX_NUM_MSGS = 992

def clLogUtilLibInitialize():
    """
    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogUtilLibInitialize()

def clLogUtilLibFinalize(logLibInit):
    """
    arg types:
        ClBoolT logLibInit
    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogUtilLibFinalize(logLibInit)

CL_LOG_AREA_UNSPECIFIED = "---"
CL_LOG_CONTEXT_UNSPECIFIED = "---"

CL_LOG_DEFAULT_SYS_SERVICE_ID = 0x01

def clLog(severity, area, context, *va_args):
    if not area:
        area = CL_LOG_AREA_UNSPECIFIED
    if not context:
        context = CL_LOG_CONTEXT_UNSPECIFIED

    (_, filename, linenumber) = clUtils.getCallerInfo()

    clLogApi.clLogMsgWrite(
        clLogIpiWrap.CL_LOG_HANDLE_SYS,
        severity,
        clCommon.ClUint16T(CL_LOG_DEFAULT_SYS_SERVICE_ID),
        area,
        context,
        filename,
        linenumber,
        *va_args
    )

def clLogDeferred(severity, area, context, *va_args):
    if not area:
        area = CL_LOG_AREA_UNSPECIFIED
    if not context:
        context = CL_LOG_CONTEXT_UNSPECIFIED

    (_, filename, linenumber) = clUtils.getCallerInfo()

    clLogApi.clLogMsgWriteDeferred(
        clLogIpiWrap.CL_LOG_HANDLE_SYS,
        severity,
        clCommon.ClUint16T(CL_LOG_DEFAULT_SYS_SERVICE_ID),
        area,
        context,
        filename,
        linenumber,
        *va_args
    )

def clLogConsole(severity, area, context, *va_args):
    if not area:
        area = CL_LOG_AREA_UNSPECIFIED
    if not context:
        context = CL_LOG_CONTEXT_UNSPECIFIED

    (_, filename, linenumber) = clUtils.getCallerInfo()

    clLogApi.clLogMsgWriteDeferred(
        clLogIpiWrap.CL_LOG_HANDLE_SYS,
        severity,
        clCommon.ClUint16T(CL_LOG_DEFAULT_SYS_SERVICE_ID),
        area,
        context,
        filename,
        linenumber,
        *va_args
    )

def clAppLog(streamHandle, severity, serviceId, area, context, *va_args):
    if not area:
        area = CL_LOG_AREA_UNSPECIFIED
    if not context:
        context = CL_LOG_CONTEXT_UNSPECIFIED

    (_, filename, linenumber) = clUtils.getCallerInfo()

    clLogApi.clLogMsgWrite(
        streamHandle,
        severity,
        serviceId,
        area,
        context,
        filename,
        linenumber,
        *va_args
    )

# TODO: there're remaining codes in the original header file
