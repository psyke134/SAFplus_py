import sys
sys.path.append("..")

from common import clCommon, clCommonErrors
from utils import clLib, clUtils

import ctypes

CL_IOC_HEADER_VERSION = 1
CL_IOC_NOTIFICATION_VERSION = 1
CL_IOC_TIMEOUT_FOREVER = 0
CL_IOC_RECEIVE_TIMEOUT = 1500
CL_IOC_UNRELIABLE_MESSAGING = 0
CL_IOC_RELIABLE_MESSAGING = (1<<0)
CL_IOC_NODE_UP = 1
CL_IOC_NODE_DOWN = 0
CL_IOC_LINK_UP = 2
CL_IOC_LINK_DOWN = 3
CL_IOC_BROADCAST_ADDRESS = 0xffffffff
CL_IOC_RESERVED_ADDRESS = 0
CL_IOC_GEO_ADDR_MAX_LENGTH = 128
CL_IOC_PHYSICAL_ADDRESS_TYPE = 0
CL_IOC_LOGICAL_ADDRESS_TYPE = 1
CL_IOC_MULTICAST_ADDRESS_TYPE = 2
CL_IOC_MASTER_ADDRESS_TYPE = 3
CL_IOC_INTRANODE_ADDRESS_TYPE = 4
CL_IOC_USER_ADDRESS_TYPE = 10
CL_IOC_BROADCAST_ADDRESS_TYPE = 0xff

ClIocPriorityT = clCommon.ClInt32T
class eClIocPriorityT(clUtils.Enum):
    CL_IOC_DEFAULT_PRIORITY   = 0
    CL_IOC_HIGH_PRIORITY      = 1
    CL_IOC_LOW_PRIORITY       = 2
    CL_IOC_ORDERED_PRIORITY = 3
    CL_IOC_NOTIFICATION_PRIORITY = 4
    CL_IOC_RESERVED_PRIORITY  = 5
    CL_IOC_RESERVED_PRIORITY_USER = 6
    CL_IOC_RESERVED_PRIORITY_USER_END = 16
    CL_IOC_MAX_PRIORITIES     = CL_IOC_RESERVED_PRIORITY_USER_END + 1

ClIocNotificationActionT = clCommon.ClInt32T
class eClIocNotificationActionT(clUtils.Enum):
    CL_IOC_NOTIFICATION_DISABLE = 0
    CL_IOC_NOTIFICATION_ENABLE = 1

CL_IOC_ADDRESS_TYPE_BITS = (0x8)
CL_IOC_ADDRESS_TYPE_MASK = ((1<<CL_IOC_ADDRESS_TYPE_BITS)-1)
CL_IOC_NODE_MASK = (0 >> CL_IOC_ADDRESS_TYPE_BITS)
CL_IOC_ADDRESS_TYPE_SHIFT_WORD = (32-CL_IOC_ADDRESS_TYPE_BITS)
CL_IOC_ADDRESS_TYPE_SHIFT_DWORD = (64-CL_IOC_ADDRESS_TYPE_BITS)

def CL_IOC_ADDRESS_TYPE_GET(param):
    # param is ClIocPhysicalAddressT *
    rs = ctypes.c_int()

    p64_param = ctypes.cast(param, ctypes.POINTER(ctypes.c_long))
    rs.value = p64_param.contents.value >> CL_IOC_ADDRESS_TYPE_SHIFT_DWORD
    return rs

CL_IOC_TL_ACTIVE = 0
CL_IOC_TL_STDBY = 1

ClIocNodeAddressT = clCommon.ClUint32T

ClIocPortT = clCommon.ClUint32T

ClIocCommPortHandleT = clCommon.ClWordT

ClIocToBindHandleT = clCommon.ClHandleT

ClIocCommPortFlagsT = clCommon.ClUint32T

ClIocLogicalAddressT = clCommon.ClUint64T

ClIocMulticastAddressT = clCommon.ClUint64T

class ClIocPhysicalAddressT(ctypes.Structure):
    _fields_ = [
        ("nodeAddress", ClIocNodeAddressT),
        ("portId", ClIocPortT)
    ]

class ClIocAddressT(ctypes.Union):
    _fields_ = [
        ("iocPhyAddress", ClIocPhysicalAddressT),
        ("iocLogicalAddress", ClIocLogicalAddressT),
        ("iocMulticastAddress", ClIocMulticastAddressT)
    ]

ClIocMessageOptionT = clCommon.ClInt32T
class eClIocMessageOptionT(clUtils.Enum):
    CL_IOC_PERSISTENT_MSG = 0
    CL_IOC_NON_PERSISTENT_MSG = 1

class ClIocSendOptionT(ctypes.Structure):
    _fields_ = [
        ("priority", clCommon.ClUint8T),
        ("sendType", clCommon.ClUint8T),
        ("linkHandle", clCommon.ClWordT),
        ("msgOption", ClIocMessageOptionT),
        ("timeout", clCommon.ClUint32T)
    ]

class ClIocRecvParamT(ctypes.Structure):
    _fields_ = [
        ("priority", clCommon.ClUint8T),
        ("protoType", clCommon.ClUint8T),
        ("length", clCommon.ClUint32T),
        ("srcAddr", ClIocAddressT)
    ]

class ClIocRecvOptionT(ctypes.Structure):
    _fields_ = [
        ("recvTimeout", clCommon.ClUint32T)
    ]

ClIocQueueIdT = clCommon.ClInt32T
class eClIocQueueIdT(clUtils.Enum):
    CL_IOC_SENDQ = 0
    CL_IOC_RECVQ = 1
    CL_IOC_QUEUE_MAX = 2

class ClIocQueueInfoT(ctypes.Structure):
    _fields_ = [
        ("queueSize", clCommon.ClUint32T),
        ("queueWM", clCommon.ClWaterMarkT)
    ]

class ClIocQueueStatsT(ctypes.Structure):
    _fields_ = [
        ("queueInfo", ClIocQueueInfoT),
        ("queueUtilisation", clCommon.ClUint32T)
    ]

class ClIocLibConfigT(ctypes.Structure):
    _fields_ = [
        ("version", clCommon.ClUint8T),
        ("nodeAddress", ClIocNodeAddressT),
        ("iocGeoGraphicalAddress", clCommon.ClCharT * (CL_IOC_GEO_ADDR_MAX_LENGTH + 1)),
        ("iocMaxNumOfPriorities", clCommon.ClUint32T),
        ("iocReassemblyTimeOut", clCommon.ClUint32T),
        ("iocMaxNumOfXports", clCommon.ClUint32T),
        ("iocHeartbeatTimeInterval", clCommon.ClUint32T),
        ("iocTLMaxEntries", clCommon.ClUint32T),
        ("iocSendQInfo", ClIocQueueInfoT),
        ("iocRecvQInfo", ClIocQueueInfoT),
        ("iocNodeRepresentative", ClIocPortT),
        ("isNodeRepresentative", clCommon.ClBoolT)
    ]

ClIocTLContextT = clCommon.ClInt32T
class eClIocTLContextT(clUtils.Enum):
    CL_IOC_TL_GLOBAL_SCOPE = 0
    CL_IOC_TL_LOCAL_SCOPE = 1

class ClIocTLMappingT(ctypes.Structure):
    _fields_ = [
        ("haState", clCommon.ClUint32T),
        ("physicalAddr", ClIocPhysicalAddressT)
    ]

CL_IOC_TL_NO_REPLICATION = 0

class ClIocTLInfoT(ctypes.Structure):
    _fields_ = [
        ("logicalAddr", ClIocLogicalAddressT),
        ("compId", clCommon.ClUint32T),
        ("contextType", ClIocTLContextT),
        ("unused", clCommon.ClUint32T),
        ("haState", clCommon.ClUint32T),
        ("physicalAddr", ClIocPhysicalAddressT)
    ]

class ClIocMcastUserInfoT(ctypes.Structure):
    _fields_ = [
        ("mcastAddr", ClIocMulticastAddressT),
        ("physicalAddr", ClIocPhysicalAddressT)
    ]

def clIocCommPortCreate(portId, portType, pIocCommPortHdl):
    """
    arg types:
        ClIocPortT portId,
        ClIocCommPortFlagsT portType,
        ClIocCommPortHandleT * pIocCommPortHdl
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocCommPortCreate(portId, portType, clUtils.byref(pIocCommPortHdl))


def clIocCommPortDelete(iocCommPortHdl):
    """
    arg types:
        ClIocCommPortHandleT iocCommPortHdl
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocCommPortDelete(iocCommPortHdl)


def clIocCommPortFdGet(portHandle, pSd):
    """
    arg types:
        ClIocCommPortHandleT portHandle,
        ClInt32T *pSd
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocCommPortFdGet(portHandle, clUtils.byref(pSd))


def clIocCommPortGet(pIocCommPort, pPortId):
    """
    arg types:
        ClIocCommPortHandleT pIocCommPort,
        ClIocPortT * pPortId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocCommPortGet(pIocCommPort, clUtils.byref(pPortId))


def clIocPortNotification(port, action):
    """
    arg types:
        ClIocPortT port,
        ClIocNotificationActionT action
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocPortNotification(port, action)

def clIocSend(commPortHandle, message, protoType, pDestAddr, pSendOption):
    """
    arg types:
        ClIocCommPortHandleT commPortHandle,
        ClBufferHandleT message,
        ClUint8T protoType,
        ClIocAddressT * pDestAddr,
        ClIocSendOptionT * pSendOption
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocSend(commPortHandle, message, protoType, clUtils.byref(pDestAddr), clUtils.byref(pSendOption))


def clIocReceive(commPortHdl, pRecvOption, userMsg, pRecvParam):
    """
    arg types:
        ClIocCommPortHandleT commPortHdl,
        ClIocRecvOptionT * pRecvOption,
        ClBufferHandleT userMsg,
        ClIocRecvParamT * pRecvParam
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocReceive(commPortHdl, clUtils.byref(pRecvOption), userMsg, clUtils.byref(pRecvParam))


def clIocReceiveAsync(commPortHdl, pRecvOption, userMsg, pRecvParam):
    """
    arg types:
        ClIocCommPortHandleT commPortHdl,
        ClIocRecvOptionT * pRecvOption,
        ClBufferHandleT userMsg,
        ClIocRecvParamT * pRecvParam
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocReceiveAsync(commPortHdl, clUtils.byref(pRecvOption), userMsg, clUtils.byref(pRecvParam))


def clIocReceiveWithBuffer(commPortHdl, pRecvOption, buffer, bufSize, userMsg, pRecvParam):
    """
    arg types:
        ClIocCommPortHandleT commPortHdl,
        ClIocRecvOptionT * pRecvOption,
        ClUint8T *buffer,
        ClUint32T bufSize,
        ClBufferHandleT userMsg,
        ClIocRecvParamT * pRecvParam
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocReceiveWithBuffer(commPortHdl, clUtils.byref(pRecvOption), clUtils.byref(buffer), bufSize, userMsg, clUtils.byref(pRecvParam))


def clIocReceiveWithBufferAsync(commPortHdl, pRecvOption, buffer, bufSize, userMsg, pRecvParam):
    """
    arg types:
        ClIocCommPortHandleT commPortHdl,
        ClIocRecvOptionT * pRecvOption,
        ClUint8T *buffer,
        ClUint32T bufSize,
        ClBufferHandleT userMsg,
        ClIocRecvParamT * pRecvParam
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocReceiveWithBufferAsync(commPortHdl, clUtils.byref(pRecvOption), clUtils.byref(buffer), bufSize, userMsg, clUtils.byref(pRecvParam))


def clIocCommPortReceiverUnblock(commPortHdl):
    """
    arg types:
        ClIocCommPortHandleT commPortHdl
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocCommPortReceiverUnblock(commPortHdl)


# --- Transparency and Multicast ---

def clIocTransparencyRegister(pTLInfo):
    """
    arg types:
        ClIocTLInfoT * pTLInfo
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocTransparencyRegister(clUtils.byref(pTLInfo))


def clIocTransparencyDeregister(compId):
    """
    arg types:
        ClUint32T compId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocTransparencyDeregister(compId)


def clIocMulticastRegister(pMcastInfo):
    """
    arg types:
        ClIocMcastUserInfoT *pMcastInfo
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocMulticastRegister(clUtils.byref(pMcastInfo))


def clIocMulticastDeregister(pMcastInfo):
    """
    arg types:
        ClIocMcastUserInfoT *pMcastInfo
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocMulticastDeregister(clUtils.byref(pMcastInfo))


def clIocMulticastDeregisterAll(pMcastAddress):
    """
    arg types:
        ClIocMulticastAddressT *pMcastAddress
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocMulticastDeregisterAll(clUtils.byref(pMcastAddress))


# --- Utilities and Deprecated Functions ---

def clIocVersionCheck(pVersion):
    """
    arg types:
        ClVersionT * pVersion
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocVersionCheck(clUtils.byref(pVersion))


def clIocTransparencyLogicalToPhysicalAddrGet(logicalAddr, pPhysicalAddr, pNoEntries):
    """
    arg types:
        ClIocLogicalAddressT logicalAddr,
        ClIocTLMappingT ** pPhysicalAddr,
        ClUint32T * pNoEntries
    return type:
        ClRcT
    """
    pNoEntries.value = 0
    return clCommonErrors.CL_OK

def clIocLocalAddressGet():
    """
    return type:
        ClIocNodeAddressT
    """
    clLib.libmw_so.clIocLocalAddressGet.restype = ClIocNodeAddressT
    return clLib.libmw_so.clIocLocalAddressGet()

# TODO: there're remaining codes in the original header file
