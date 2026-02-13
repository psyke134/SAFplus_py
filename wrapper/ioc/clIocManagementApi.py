import sys
sys.path.append("..")

from common import clCommon
from ioc import clIocApi
from utils import clHash, clList, clLib, clUtils

import ctypes

CL_IOC_ROUTE_FLAGS_SAME_LINK = 0xff
CL_IOC_ROUTE_UP = 1
CL_IOC_ROUTE_DOWN = 0
CL_IOC_MIN_RECV_Q_SIZE = 32*1024
CL_IOC_MAX_RECV_Q_SIZE = 1024*1024
CL_IOC_STATIC_ENTRY = 1
CL_IOC_DYNAMIC_ENTRY = 0

ClIocHeartBeatLinkIndex = clCommon.ClUint32T

class ClIocRouteParamT(ctypes.Structure):
    _fields_ = [
        ("destAddr", clIocApi.ClIocNodeAddressT),
        ("nextHop", clIocApi.ClIocNodeAddressT),
        ("prefixLen", clCommon.ClUint16T),
        ("metrics", clCommon.ClUint16T),
        ("pXportName", ctypes.POINTER(clCommon.ClCharT)),
        ("pLinkName", ctypes.POINTER(clCommon.ClCharT)),
        ("flags", clCommon.ClUint8T),
        ("version", clCommon.ClUint8T),
        ("status", clCommon.ClUint8T),
        ("entryType", clCommon.ClUint8T)
    ]

class ClIocArpParamT(ctypes.Structure):
    _fields_ = [
        ("iocAddr", clIocApi.ClIocNodeAddressT),
        ("pTransportAddr", ctypes.POINTER(clCommon.ClUint8T)),
        ("addrSize", clCommon.ClUint32T),
        ("pXportName", ctypes.POINTER(clCommon.ClCharT)),
        ("pLinkName", ctypes.POINTER(clCommon.ClCharT)),
        ("status", clCommon.ClUint8T),
        ("entryType", clCommon.ClUint8T)
    ]

class ClIocHeartBeatStatusT(ctypes.Structure):
    _fields_ = [
        ("linkIndex", ClIocHeartBeatLinkIndex),
        ("status", clCommon.ClUint8T),
        ("retryCount", clCommon.ClUint8T),
        ("hash", clHash.hashStruct),
        ("list", clList.ClListHeadT)
    ]

def clIocCommPortWaterMarksGet(commPort, pLowWaterMark, pHighWaterMark):
    """
    arg types: ClUint32T commPort, ClUint64T* pLowWaterMark, ClUint64T* pHighWaterMark
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocCommPortWaterMarksGet(commPort, pLowWaterMark, pHighWaterMark)

def clIocCommPortWaterMarksSet(commPort, lowWaterMark, highWaterMark):
    """
    arg types: ClUint32T commPort, ClUint32T lowWaterMark, ClUint32T highWaterMark
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocCommPortWaterMarksSet(commPort, lowWaterMark, highWaterMark)

def clIocCommPortQueueSizeSet(portId, queueSize):
    """
    arg types: ClIocCommPortHandleT portId, ClUint32T queueSize
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocCommPortQueueSizeSet(portId, queueSize)

def clIocCommPortQueueStatsGet(portId, pQueueStats):
    """
    arg types: ClIocCommPortHandleT portId, ClIocQueueStatsT *pQueueStats
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocCommPortQueueStatsGet(portId, pQueueStats)

def clIocNodeQueueWaterMarksSet(queueId, pWM):
    """
    arg types: ClIocQueueIdT queueId, ClWaterMarkT *pWM
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocNodeQueueWaterMarksSet(queueId, pWM)

def clIocNodeQueueSizeSet(queueId, queueSize):
    """
    arg types: ClIocQueueIdT queueId, ClUint32T queueSize
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocNodeQueueSizeSet(queueId, queueSize)

def clIocNodeQueueStatsGet(pSendQStats, pRecvQStats):
    """
    arg types: ClIocQueueStatsT *pSendQStats, ClIocQueueStatsT *pRecvQStats
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocNodeQueueStatsGet(pSendQStats, pRecvQStats)

def clIocRouteInsert(pRouteInfo):
    """
    arg types: ClIocRouteParamT* pRouteInfo
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocRouteInsert(pRouteInfo)

def clIocRouteDelete(destAddr, prefixLen):
    """
    arg types: ClIocNodeAddressT destAddr, ClUint16T prefixLen
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocRouteDelete(destAddr, prefixLen)

def clIocRouteTablePrint():
    """
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocRouteTablePrint()

def clIocArpInsert(pArpInfo):
    """
    arg types: ClIocArpParamT *pArpInfo
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocArpInsert(pArpInfo)

def clIocArpDelete(iocAddr, pXportName, pLinkName):
    """
    arg types: ClIocNodeAddressT iocAddr, ClCharT *pXportName, ClCharT* pLinkName
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocArpDelete(iocAddr, pXportName, pLinkName)

def clIocArpTablePrint():
    """
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocArpTablePrint()

def clIocLinkStatusGet(pXportName, pLinkName, pStatus):
    """
    arg types: ClCharT *pXportName, ClCharT* pLinkName, ClUint8T *pStatus
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocLinkStatusGet(pXportName, pLinkName, pStatus)

def clIocLinkStatusSet(pXportName, pLinkName, status):
    """
    arg types: ClCharT *pXportName, ClCharT* pLinkName, ClUint8T status
    return type: ClRcT (DEPRECATED)
    """
    return clLib.libmw_so.clIocLinkStatusSet(pXportName, pLinkName, status)

def clIocHeartBeatInitialize(nodeRep):
    """
    arg types: ClBoolT nodeRep
    return type: ClRcT
    """
    return clLib.libmw_so.clIocHeartBeatInitialize(nodeRep)

def clIocHeartBeatFinalize(nodeRep):
    """
    arg types: ClBoolT nodeRep
    return type: ClRcT
    """
    return clLib.libmw_so.clIocHeartBeatFinalize(nodeRep)

def clIocHeartBeatStart():
    """
    return type: ClRcT
    """
    return clLib.libmw_so.clIocHeartBeatStart()

def clIocHeartBeatStop():
    """
    return type: ClRcT
    """
    return clLib.libmw_so.clIocHeartBeatStop()

def clIocHeartBeatPause():
    """
    return type: ClRcT
    """
    return clLib.libmw_so.clIocHeartBeatPause()

def clIocHeartBeatUnpause():
    """
    return type: ClRcT
    """
    return clLib.libmw_so.clIocHeartBeatUnpause()

def clIocHeartBeatIsRunning():
    """
    return type: ClBoolT
    """
    return clLib.libmw_so.clIocHeartBeatIsRunning()

def clIocHeartBeatStatusGet():
    """
    return type: const ClCharT *
    """
    return clLib.libmw_so.clIocHeartBeatStatusGet()

def clIocHearBeatHealthCheckUpdate(nodeAddr, portId, message):
    """
    arg types: ClIocNodeAddressT nodeAddr, ClUint32T portId, ClCharT *message
    return type: ClRcT
    """
    return clLib.libmw_so.clIocHearBeatHealthCheckUpdate(nodeAddr, portId, clUtils.toCharP(message))

def clIocHeartBeatMessageReqRep(commPort, destAddress, reqRep, shutdown):
    """
    arg types: ClIocCommPortHandleT commPort, ClIocAddressT *destAddress, ClUint32T reqRep, ClBoolT shutdown
    return type: ClRcT
    """
    return clLib.libmw_so.clIocHeartBeatMessageReqRep(commPort, destAddress, reqRep, shutdown)
