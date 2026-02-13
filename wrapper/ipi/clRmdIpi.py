import sys
sys.path.append("..")

from common import clCommon
from utils import clLib, clUtils

import ctypes

CL_RMD_CALL_ORDERED = 1<<6

class ClRmdStatsT(ctypes.Structure):
    _fields_ = [
        ("nRmdCalls", clCommon.ClUint32T),
        ("nFailedCalls", clCommon.ClUint32T),
        ("nResendRequests", clCommon.ClUint32T),
        ("nFailedResendRequests", clCommon.ClUint32T),
        ("nRmdReplies", clCommon.ClUint32T),
        ("nBadReplies", clCommon.ClUint32T),
        ("nRmdRequests", clCommon.ClUint32T),
        ("nBadRequests", clCommon.ClUint32T),
        ("nCallTimeouts", clCommon.ClUint32T),
        ("nDupRequests", clCommon.ClUint32T),
        ("nAtmostOnceCalls", clCommon.ClUint32T),
        ("nFailedAtmostOnceCalls", clCommon.ClUint32T),
        ("nReplySend", clCommon.ClUint32T),
        ("nFailedReplySend", clCommon.ClUint32T),
        ("nResendReplies", clCommon.ClUint32T),
        ("nFailedResendReplies", clCommon.ClUint32T),
        ("nRmdCallOptimized", clCommon.ClUint32T),
        ("nAtmostOnceAcksSent", clCommon.ClUint32T),
        ("nFailedAtmostOnceAcksSent", clCommon.ClUint32T),
        ("nAtmostOnceAcksRecvd", clCommon.ClUint32T),
        ("nFailedAtmostOnceAcksRecvd", clCommon.ClUint32T)
    ]

ClRmdResponseContextHandleT = clCommon.ClHandleT

def clRmdVersionVerify(pVersion):
    """
    arg types:
        ClVersionT* pVersion
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdVersionVerify(clUtils.byref(pVersion))


def clRmdObjInit(p):
    """
    arg types:
        ClRmdObjHandleT *p
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdObjInit(clUtils.byref(p))


def clRmdObjClose(p):
    """
    arg types:
        ClRmdObjHandleT p
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdObjClose(p)

def clRmdResponseDefer(pResponseCntxtHdl):
    """
    arg types:
        ClRmdResponseContextHandleT *pResponseCntxtHdl
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdResponseDefer(clUtils.byref(pResponseCntxtHdl))


def clRmdSyncResponseSend(syncSendCtnxtHdl, replyMsg, rc):
    """
    arg types:
        ClRmdResponseContextHandleT syncSendCtnxtHdl, 
        ClBufferHandleT replyMsg, 
        ClRcT rc
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdSyncResponseSend(syncSendCtnxtHdl, replyMsg, rc)

def clRmdSourceAddressGet(pSrcAddr):
    """
    arg types:
        ClIocPhysicalAddressT *pSrcAddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdSourceAddressGet(clUtils.byref(pSrcAddr))

def clRmdReceiveReply(pThis, eoRecvMsg, priority, protoType, length, srcAddr):
    """
    arg types:
        ClEoExecutionObjT* pThis,
        ClBufferHandleT eoRecvMsg, 
        ClUint8T priority,
        ClUint8T protoType,
        ClUint32T length, 
        ClIocPhysicalAddressT srcAddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdReceiveReply(clUtils.byref(pThis), eoRecvMsg, priority, protoType, length, srcAddr)


def clRmdReceiveRequest(pThis, eoRecvMsg, priority, protoType, length, srcAddr):
    """
    arg types:
        ClEoExecutionObjT* pThis,
        ClBufferHandleT eoRecvMsg, 
        ClUint8T priority,
        ClUint8T protoType,
        ClUint32T length, 
        ClIocPhysicalAddressT srcAddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdReceiveRequest(clUtils.byref(pThis), eoRecvMsg, priority, protoType, length, srcAddr)


def clRmdReceiveAsyncRequest(pThis, eoRecvMsg, priority, protoType, length, srcAddr):
    """
    arg types:
        ClEoExecutionObjT* pThis,
        ClBufferHandleT eoRecvMsg, 
        ClUint8T priority,
        ClUint8T protoType,
        ClUint32T length, 
        ClIocPhysicalAddressT srcAddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdReceiveAsyncRequest(clUtils.byref(pThis), eoRecvMsg, priority, protoType, length, srcAddr)


def clRmdReceiveAsyncReply(pThis, rmdRecvMsg, priority, protoType, length, srcAddr):
    """
    arg types:
        ClEoExecutionObjT* pThis,
        ClBufferHandleT rmdRecvMsg, 
        ClUint8T priority,
        ClUint8T protoType,
        ClUint32T length, 
        ClIocPhysicalAddressT srcAddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdReceiveAsyncReply(clUtils.byref(pThis), rmdRecvMsg, priority, protoType, length, srcAddr)


def clRmdReceiveOrderedRequest(pThis, eoRecvMsg, priority, protoType, length, srcAddr):
    """
    arg types:
        ClEoExecutionObjT* pThis,
        ClBufferHandleT eoRecvMsg, 
        ClUint8T priority,
        ClUint8T protoType,
        ClUint32T length, 
        ClIocPhysicalAddressT srcAddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdReceiveOrderedRequest(clUtils.byref(pThis), eoRecvMsg, priority, protoType, length, srcAddr)

def clRmdLibInitialize(config):
    """
    arg types:
        ClPtrT config
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdLibInitialize(config)


def clRmdLibFinalize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdLibFinalize()


def clRmdMaxPayloadSizeGet(pSize):
    """
    arg types:
        ClUint32T *pSize
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdMaxPayloadSizeGet(clUtils.byref(pSize))


def clRmdMaxNumbOfRetriesGet(pNumbOfRetries):
    """
    arg types:
        ClUint32T *pNumbOfRetries
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdMaxNumbOfRetriesGet(clUtils.byref(pNumbOfRetries))


def clRmdDumpPacketStatus(isEnable):
    """
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdDumpPacketStatus(isEnable)

def clRmdStatsReset():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdStatsReset()


def clRmdStatsGet(pStats):
    """
    arg types:
        ClRmdStatsT *pStats
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdStatsGet(clUtils.byref(pStats))

def clRmdAckReply(pThis, rmdRecvMsg, priority, protoType, length, srcAddr):
    """
    arg types: 
        ClEoExecutionObjT *pThis,
        ClBufferHandleT rmdRecvMsg, 
        ClUint8T priority,
        ClUint8T protoType, 
        ClUint32T length,
        ClIocPhysicalAddressT srcAddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdAckReply(clUtils.byref(pThis), rmdRecvMsg, priority, protoType, length, srcAddr)


def clRmdDatabaseCleanup(rmdObj, notification):
    """
    arg types:
        ClRmdObjHandleT rmdObj,
        ClIocNotificationT *notification
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRmdDatabaseCleanup(rmdObj, clUtils.byref(notification))

def rmdMetricInitialize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.rmdMetricInitialize()


def rmdMetricUpdate(status, clientId, funcId, message, response):
    """
    arg types: 
        ClRcT status,
        ClUint32T clientId, 
        ClUint32T funcId,
        ClBufferHandleT message,
        ClBoolT response
    return type:
        ClRcT
    """
    return clLib.libmw_so.rmdMetricUpdate(status, clientId, funcId, message, response)


def rmdMetricFinalize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.rmdMetricFinalize()
