import clCommon
import clUtils
import saAis
import ctypes
import enum
import clLib

ClLogHandleT = clCommon.ClHandleT
ClLogStreamHandleT = clCommon.ClHandleT
ClLogFileHandleT = clCommon.ClHandleT

CL_LOG_STREAM_NAME_MAX_LENGTH = 128
CL_LOG_SLINE_MSG_LEN = 256

ClLogStreamScopeT = saAis.SaInt32T
class eClLogStreamScopeT(clUtils.CEnum):
    CL_LOG_STREAM_GLOBAL = 0,
    CL_LOG_STREAM_LOCAL  = 1

ClLogFileFullActionT = saAis.SaInt32T
class eClLogFileFullActionT(clUtils.CEnum):
    CL_LOG_FILE_FULL_ACTION_ROTATE = 0,
    CL_LOG_FILE_FULL_ACTION_WRAP   = 1,
    CL_LOG_FILE_FULL_ACTION_HALT   = 2

class ClLogStreamAttributesT(ctypes.Structure):
    _fields_ = [
        ("fileName", ctypes.c_char_p),
        ("fileLocation", ctypes.c_char_p),
        ("fileUnitSize", clCommon.ClUint32T),
        ("recordSize", clCommon.ClUint32T),
        ("haProperty", clCommon.ClBoolT),
        ("fileFullAction", ClLogFileFullActionT),
        ("maxFilesRotated", clCommon.ClUint32T),
        ("flushFreq", clCommon.ClUint32T),
        ("flushInterval", clCommon.ClTimeT),
        ("waterMark", clCommon.ClWaterMarkT),
        ("syslog", clCommon.ClBoolT),
    ]

CL_LOG_STREAM_CREATE = 0x1

ClLogStreamOpenFlagsT = clCommon.ClUint8T

class ClLogStreamInfoT(ctypes.Structure):
    _fields_ = [
        ("streamName", clCommon.ClNameT),
        ("streamScope", ClLogStreamScopeT),
        ("streamScopeNode", clCommon.ClNameT),
        ("streamId", clCommon.ClUint16T),
        ("streamAttr", ClLogStreamAttributesT)
    ]

class ClLogStreamMapT(ctypes.Structure):
    _fields_ = [
        ("streamName", clCommon.ClNameT),
        ("streamScope", ClLogStreamScopeT),
        ("nodeName", clCommon.ClNameT),
        ("streamId", clCommon.ClUint16T)
    ]

CL_LOG_HANDLER_WILL_ACK = 0x1

ClLogStreamHandlerFlagsT = clCommon.ClUint8T

ClLogSeverityT = saAis.SaInt32T
class eClLogSeverityT(clUtils.CEnum):
    CL_LOG_SEV_EMERGENCY = 1,
    CL_LOG_SEV_ALERT = 2,
    CL_LOG_SEV_CRITICAL = 3,
    CL_LOG_SEV_ERROR = 4,
    CL_LOG_SEV_WARNING = 5,
    CL_LOG_SEV_NOTICE = 6,
    CL_LOG_SEV_INFO = 7,
    CL_LOG_SEV_DEBUG = 8,
    CL_LOG_SEV_DEBUG1   =      8,
    CL_LOG_SEV_DEBUG2 = 9,
    CL_LOG_SEV_DEBUG3 = 10,
    CL_LOG_SEV_DEBUG4 = 11,
    CL_LOG_SEV_DEBUG5 = 12,
    CL_LOG_SEV_TRACE  =    12,
    CL_LOG_SEV_DEBUG6 = 13,
    CL_LOG_SEV_DEBUG7 = 14,
    CL_LOG_SEV_DEBUG8 = 15,
    CL_LOG_SEV_DEBUG9 = 16,
    CL_LOG_SEV_MAX    =    16

ClLogSeverityFilterT = clCommon.ClUint16T

CL_LOG_FILTER_ASSIGN = 0x1
CL_LOG_FILTER_MERGE_ADD = 0x2
CL_LOG_FILTER_MERGE_DELETE = 0x3

ClLogFilterFlagsT = clCommon.ClUint8T

class ClLogFilterT(ctypes.Structure):
    _fields_ = [
        ("severityFilter", ClLogSeverityFilterT),
        ("msgIdSetLength", clCommon.ClUint16T),
        ("pMsgIdSet", ctypes.POINTER(clCommon.ClUint8T)),
        ("compIdSetLength", clCommon.ClUint16T),
        ("pCompIdSet", ctypes.POINTER(clCommon.ClUint8T))
    ]

ClLogStreamOpenCallbackT = ctypes.CFUNCTYPE(None, clCommon.ClInvocationT, ClLogStreamHandleT, clCommon.ClRcT)

ClLogFilterSetCallbackT = ctypes.CFUNCTYPE(None, ClLogStreamHandleT, ClLogFilterT)

ClLogRecordDeliveryCallbackT = ctypes.CFUNCTYPE(None, ClLogStreamHandleT, clCommon.ClUint64T, clCommon.ClUint32T, clCommon.ClPtrT)

class ClLogCallbacksT(ctypes.Structure):
    _fields_ = [
        ("clLogStreamOpenCb", ClLogStreamOpenCallbackT),
        ("clLogFilterSetCb", ClLogFilterSetCallbackT),
        ("clLogRecordDeliveryCb", ClLogRecordDeliveryCallbackT)
    ]

CL_LOG_MSGID_BUFFER = 0
CL_LOG_MSGID_PRINTF_FMT = 1

CL_LOG_TAG_TERMINATE = 0
CL_LOG_TAG_BASIC_SIGNED = 1
CL_LOG_TAG_BASIC_UNSIGNED = 2
CL_LOG_TAG_STRING = 3

def clLogInitialize(phLog, pLogCallbacks, pVersion):
    """
    arg types:
        ClLogHandleT           *phLog,
        const ClLogCallbacksT  *pLogCallbacks,
        ClVersionT             *pVersion

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogInitialize(
        phLog,
        pLogCallbacks,
        pVersion
    )

def clLogFinalize(hLog):
    """
    arg types:
        ClLogHandleT  hLog

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogFinalize(hLog)

def clLogStreamOpen(hLog, streamName, streamScope, pStreamAttr, streamOpenFlags, timeout, phStream):
    """
    arg types:
        ClLogHandleT            hLog,
        ClNameT                 streamName,
        ClLogStreamScopeT       streamScope,
        ClLogStreamAttributesT  *pStreamAttr,
        ClLogStreamOpenFlagsT   streamOpenFlags,
        ClTimeT                 timeout,
        ClLogStreamHandleT      *phStream

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogStreamOpen(
        hLog,
        streamName,
        streamScope,
        pStreamAttr,
        streamOpenFlags,
        timeout,
        phStream
    )

def clLogStreamClose(hStream):
    """
    arg types:
        ClLogStreamHandleT hStream

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogStreamClose(hStream)

def clLogWriteAsync(hStream, severity, serviceId, msgId, *va_args):
    """
    Variadic function

    arg types:
        ClLogStreamHandleT   hStream,
        ClLogSeverityT       severity,
        ClUint16T            serviceId,
        ClUint16T            msgId,
        ...

    return type:
        ClRcT
    """
    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clLogWriteAsync.argtypes = [ClLogStreamHandleT, ClLogSeverityT, clCommon.ClUint16T, clCommon.ClUint16T] + argTypes
    return clLib.libmw_so.clLogWriteAsync(hStream, severity, serviceId, msgId, *cVaArgs)

def clLogWriteAsyncWithHeader(hStream, severity, serviceId, msgId, *va_args):
    """
    Variadic function

    arg types:
        ClLogStreamHandleT   hStream,
        ClLogSeverityT       severity,
        ClUint16T            serviceId,
        ClUint16T            msgId,
        ...

    return type:
        ClRcT
    """
    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clLogWriteAsyncWithHeader.argtypes = [ClLogStreamHandleT, ClLogSeverityT, clCommon.ClUint16T, clCommon.ClUint16T] + argTypes
    return clLib.libmw_so.clLogWriteAsyncWithHeader(hStream, severity, serviceId, msgId, *cVaArgs)

def clLogWriteAsyncWithContextHeader(hStream, severity, pArea, pContext, serviceId, msgId, *va_args):
    """
    Variadic function

    arg types:
        ClLogStreamHandleT   hStream,
        ClLogSeverityT       severity,
        const ClCharT        *pArea,
        const ClCharT        *pContext,
        ClUint16T            serviceId,
        ClUint16T            msgId,
        ...

    return type:
        ClRcT
    """
    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clLogWriteAsyncWithContextHeader.argtypes = [ClLogStreamHandleT, ClLogSeverityT, ctypes.c_char_p, ctypes.c_char_p, clCommon.ClUint16T, clCommon.ClUint16T] + argTypes
    return clLib.libmw_so.clLogWriteAsyncWithContextHeader(hStream, severity, pArea, pContext, serviceId, msgId, *cVaArgs)

def clLogFilterSet(hStream, filterFlags, filter):
    """
    arg types:
        ClLogStreamHandleT hStream,
        ClLogFilterFlagsT   filterFlags,
        ClLogFilterT        filter

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogFilterSet(hStream, filterFlags, filter)

def clLogHandlerRegister(hLog, streamName, streamScope, nodeName, handlerFlags, phStream):
    """
    arg types:
        ClLogHandleT              hLog,
        ClNameT                   streamName, 
        ClLogStreamScopeT         streamScope,
        ClNameT                   nodeName,   
        ClLogStreamHandlerFlagsT  handlerFlags,
        ClLogHandleT              *phStream

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogHandlerRegister(hLog, streamName, streamScope, nodeName, handlerFlags, phStream)

def clLogHandlerDeregister(hStream):
    """
    arg types:
        ClLogStreamHandleT  hStream

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogHandlerDeregister(hStream)

def clLogHandlerRecordAck(hStream, sequenceNumber, numRecords):
    """
    arg types:
        ClLogStreamHandleT  hStream,
        ClUint64T           sequenceNumber,
        ClUint32T           numRecords

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogHandlerRecordAck(hStream, sequenceNumber, numRecords)

def clLogFileOpen(hLog, fileName, fileLocation, isDelete, phFile):
    """
    arg types:
        ClLogHandleT      hLog,
        ClCharT           *fileName,
        ClCharT           *fileLocation,
        ClBoolT           isDelete, 
        ClLogFileHandleT  *phFile

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogFileOpen(
        hLog,
        fileName,
        fileLocation,
        isDelete,
        phFile
    )

def clLogFileClose(hFileHdlr):
    """
    arg types:
        ClLogFileHandleT  hFileHdlr

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogFileClose(hFileHdlr)

def clLogFileMetaDataGet(hFileHdlr, pStreamAttr, pNumStreams, ppLogStreams):
    """
    arg types:
        ClLogFileHandleT        hFileHdlr,
        ClLogStreamAttributesT  *pStreamAttr,
        ClUint32T               *pNumStreams,
        ClLogStreamMapT         **ppLogStreams

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogFileMetaDataGet(
        hFileHdlr,
        pStreamAttr,
        pNumStreams,
        ppLogStreams
    )

def clLogFileRecordsGet(hFileHdlr, pStarTime, pEndTime, pNumRecords, pLogRecords):
    """
    arg types:
        ClLogFileHandleT  hFileHdlr,
        ClTimeT           *pStarTime,
        ClTimeT           *pEndTime, 
        ClUint32T         *pNumRecords,
        ClPtrT            *pLogRecords

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogFileRecordsGet(
        hFileHdlr,
        pStarTime,
        pEndTime,
        pNumRecords,
        pLogRecords
    )

def clLogStreamListGet(hLog, pNumStreams, ppLogStreams):
    """
    arg types:
        ClLogHandleT      hLog,
        ClUint32T         *pNumStreams,
        ClLogStreamInfoT  **ppLogStreams

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogStreamListGet(
        hLog,
        pNumStreams,
        ppLogStreams
    )

def clLogWriteDeferred(handle, severity, servicId, msgId, pFmtStr, *va_args):
    """
    Variadic function

    arg types:
        ClHandleT      handle,
        ClLogSeverityT severity,
        ClUint16T      servicId,
        ClUint16T      msgId,
        ClCharT        *pFmtStr,
        ...

    return type:
        ClRcT
    """
    pFmtStr = clUtils.toCharP(pFmtStr)
    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clLogWriteDeferred.argtypes = [clCommon.ClHandleT, ClLogSeverityT, clCommon.ClUint16T, clCommon.ClUint16T, ctypes.c_char_p] + argTypes
    return clLib.libmw_so.clLogWriteDeferred(handle, severity, servicId, msgId, pFmtStr, *cVaArgs)

def clLogWriteDeferredForce(handle, severity, servicId, msgId, pFmtStr, *va_args):
    """
    Variadic function

    arg types:
        ClHandleT      handle,
        ClLogSeverityT severity,
        ClUint16T      servicId,
        ClUint16T      msgId,
        ClCharT        *pFmtStr,
        ...

    return type:
        ClRcT
    """
    pFmtStr = clUtils.toCharP(pFmtStr)
    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clLogWriteDeferredForce.argtypes = [clCommon.ClHandleT, ClLogSeverityT, clCommon.ClUint16T, clCommon.ClUint16T, ctypes.c_char_p] + argTypes
    return clLib.libmw_so.clLogWriteDeferredForce(handle, severity, servicId, msgId, pFmtStr, *cVaArgs)

def clLogMsgWrite(streamHdl, severity, servicId, pArea, pContext, pFileName, lineNum, pFmtStr, *va_args):
    """
    Variadic function

    arg types:
        ClHandleT       streamHdl,
        ClLogSeverityT  severity,
        ClUint16T       serviceId,
        const ClCharT   *pArea,
        const ClCharT   *pContext,
        const ClCharT   *pFileName,
        ClUint32T       lineNum,
        const ClCharT   *pFmtStr,
        ...

    return type:
        ClRcT
    """
    pArea = clUtils.toCharP(pArea)
    pContext = clUtils.toCharP(pContext)
    pFileName = clUtils.toCharP(pFileName)
    pFmtStr = clUtils.toCharP(pFmtStr)

    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clLogMsgWrite.argtypes = [clCommon.ClHandleT, ClLogSeverityT, clCommon.ClUint16T, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, clCommon.ClUint32T, ctypes.c_char_p] + argTypes
    return clLib.libmw_so.clLogMsgWrite(streamHdl, severity, servicId, pArea, pContext, pFileName, lineNum, pFmtStr, *cVaArgs)

def clLogMsgWriteDeferred(streamHdl, severity, servicId, pArea, pContext, pFileName, lineNum, pFmtStr, *va_args):
    """
    Variadic function

    arg types:
        ClHandleT       streamHdl,
        ClLogSeverityT  severity,
        ClUint16T       serviceId,
        const ClCharT   *pArea,
        const ClCharT   *pContext,
        const ClCharT   *pFileName,
        ClUint32T       lineNum,
        const ClCharT   *pFmtStr,
        ...

    return type:
        ClRcT
    """
    pArea = clUtils.toCharP(pArea)
    pContext = clUtils.toCharP(pContext)
    pFileName = clUtils.toCharP(pFileName)
    pFmtStr = clUtils.toCharP(pFmtStr)

    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clLogMsgWriteDeferred.argtypes = [clCommon.ClHandleT, ClLogSeverityT, clCommon.ClUint16T, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, clCommon.ClUint32T, ctypes.c_char_p] + argTypes
    return clLib.libmw_so.clLogMsgWriteDeferred(streamHdl, severity, servicId, pArea, pContext, pFileName, lineNum, pFmtStr, *cVaArgs)

def clLogMsgWriteConsole(streamHdl, severity, servicId, pArea, pContext, pFileName, lineNum, pFmtStr, *va_args):
    """
    Variadic function

    arg types:
        ClHandleT       streamHdl,
        ClLogSeverityT  severity,
        ClUint16T       serviceId,
        const ClCharT   *pArea,
        const ClCharT   *pContext,
        const ClCharT   *pFileName,
        ClUint32T       lineNum,
        const ClCharT   *pFmtStr,
        ...

    return type:
        ClRcT
    """
    pArea = clUtils.toCharP(pArea)
    pContext = clUtils.toCharP(pContext)
    pFileName = clUtils.toCharP(pFileName)
    pFmtStr = clUtils.toCharP(pFmtStr)

    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clLogMsgWriteConsole.argtypes = [clCommon.ClHandleT, ClLogSeverityT, clCommon.ClUint16T, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, clCommon.ClUint32T, ctypes.c_char_p] + argTypes
    return clLib.libmw_so.clLogMsgWriteConsole(streamHdl, severity, servicId, pArea, pContext, pFileName, lineNum, pFmtStr, *cVaArgs)

CL_LOG_AREA_UNSPECIFIED = "---"
CL_LOG_CONTEXT_UNSPECIFIED = "---"
CL_LOG_DEFAULT_SYS_SERVICE_ID = 0x01

def clLogWrite(severity, libName, *va_args):
    """
    Variadic function

    arg types:
        ClLogSeverityT  severity,
        const ClCharT  *libName,
        ...
    """

    if not libName:
        libName = CL_LOG_AREA_UNSPECIFIED

    CL_LOG_HANDLE_SYS = clCommon.ClHandleT.in_dll(clLib.libmw_so, "CL_LOG_HANDLE_SYS")
    (fileName, loc) = clUtils.getCallerInfo()
    clLogMsgWrite(
        CL_LOG_HANDLE_SYS,
        severity,
        CL_LOG_DEFAULT_SYS_SERVICE_ID,
        libName,
        CL_LOG_CONTEXT_UNSPECIFIED,
        fileName,
        loc,
        *va_args
    )

def clLogFormatRecordHeader(msgHeader, maxHeaderLen, msg, consoleFlag, msgIdCnt, severity, pFileName, lineNum, pArea, pContext):
    """
    arg types:
        ClCharT *msgHeader,
        ClUint32T maxHeaderLen,
        ClCharT *msg,
        ClBoolT consoleFlag,
        ClUint32T  msgIdCnt,
        ClLogSeverityT  severity,
        const ClCharT *pFileName,
        ClUint32T lineNum,
        const ClCharT *pArea,
        const ClCharT *pContext

    return type:
        ClRcT
    """
    msgHeader = clUtils.toCharP(msgHeader)
    msg = clUtils.toCharP(msg)
    pFileName = clUtils.toCharP(pFileName)
    pArea = clUtils.toCharP(pArea)
    pContext = clUtils.toCharP(pContext)

    return clLib.libmw_so.clLogFormatRecordHeader(msgHeader, maxHeaderLen, msg, consoleFlag, msgIdCnt, severity, pFileName, lineNum, pArea, pContext)

def clLogFormatRecord(msgHeader, maxHeaderLen, msg, maxMsgLen, consoleFlag, msgIdCnt, severity, pFileName, lineNum, pArea, pContext, pFmtStr, *va_args):
    """
    Variadic function

    arg types:
        ClCharT *msgHeader,
        ClUint32T maxHeaderLen,
        ClCharT *msg,
        ClUint32T maxMsgLen,
        ClBoolT consoleFlag,
        ClUint32T  msgIdCnt,
        ClLogSeverityT  severity,
        const ClCharT *pFileName,
        ClUint32T lineNum,
        const ClCharT *pArea,
        const ClCharT *pContext,
        const ClCharT *pFmtStr,
        ...

    return type:
        ClRcT
    """
    msgHeader = clUtils.toCharP(msgHeader)
    msg = clUtils.toCharP(msg)
    pFileName = clUtils.toCharP(pFileName)
    pArea = clUtils.toCharP(pArea)
    pContext = clUtils.toCharP(pContext)
    pFmtStr = clUtils.toCharP(pFmtStr)

    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clLogFormatRecord.argtypes = [ctypes.c_char_p, clCommon.ClUint32T, ctypes.c_char_p, clCommon.ClUint32T, clCommon.ClBoolT, clCommon.ClUint32T, ClLogSeverityT, ctypes.c_char_p, clCommon.ClUint32T, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p] + argTypes
    return clLib.libmw_so.clLogFormatRecord(msgHeader, maxHeaderLen, msg, maxMsgLen, consoleFlag, msgIdCnt, severity, pFileName, lineNum, pArea, pContext, pFmtStr, *cVaArgs)

def clLogSeverityFilterToValueGet(filter, pSeverity):
    """
    arg types:
        ClLogSeverityFilterT filter,
        ClLogSeverityT* pSeverity

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogSeverityFilterToValueGet(filter, pSeverity)

def clLogSeverityValueToFilterGet(severity, pFilter):
    """
    arg types:
        ClLogSeverityT severity,
        ClLogSeverityFilterT* pFilter

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogSeverityValueToFilterGet(severity, pFilter)

def clLogStreamFilterSet(pStreamName, streamScope, pStreamScopeNode, filterFlags, filter):
    """
    arg types:
        ClNameT             *pStreamName, 
        ClLogStreamScopeT   streamScope,
        ClNameT             *pStreamScopeNode,
        ClLogFilterFlagsT   filterFlags,
        ClLogFilterT        filter

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogStreamFilterSet(pStreamName, streamScope, pStreamScopeNode, filterFlags, filter)

def clLogStreamFilterGet(pStreamName, streamScope, pStreamScopeNode, pFilter):
    """
    arg types:
        ClNameT             *pStreamName, 
        ClLogStreamScopeT   streamScope,
        ClNameT             *pStreamScopeNode,
        ClLogFilterT        *pFilter

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogStreamFilterGet(pStreamName, streamScope, pStreamScopeNode, pFilter)

def clLogSeverityGet(pSevName):
    """
    arg types:
        const ClCharT  *pSevName

    return type:
        ClLogSeverityT
    """
    return clLib.libmw_so.clLogSeverityGet(pSevName)

def clLogTimeGet(pStrTime, maxBytes):
    """
    arg types:
        ClCharT   *pStrTime,
        ClUint32T maxBytes

    return type:
        ClRcT
    """
    return clLib.libmw_so.clLogTimeGet(pStrTime, maxBytes)

# extern ClBoolT          gClLogCodeLocationEnable;
#define CL_LOG_PRNT_FMT_STR               "%-26s [%s:%d] (%.*s.%d : %s.%3s.%3s"
#define CL_LOG_PRNT_FMT_STR_CONSOLE       "%-26s [%s:%d] (%.*s.%d : %s.%3s.%3s.%05d : %6s) "

#define CL_LOG_PRNT_FMT_STR_WO_FILE         "%-26s (%.*s.%d : %s.%3s.%3s"
#define CL_LOG_PRNT_FMT_STR_WO_FILE_CONSOLE "%-26s (%.*s.%d : %s.%3s.%3s.%05d : %6s) "
