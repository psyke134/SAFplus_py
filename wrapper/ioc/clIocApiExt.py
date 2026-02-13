import sys
sys.path.append("..")

from utils import clUtils, clLib
from common import saAis, clCommon
from ioc import clIocApi

import ctypes

CL_IOC_NO_SESSION = 0
CL_IOC_SESSION_BASED = 1

ClIocNotificationIdT = saAis.SaInt32T
class eClIocNotificationIdT(clUtils.Enum):
    CL_IOC_NODE_ARRIVAL_NOTIFICATION = 0
    CL_IOC_NODE_LEAVE_NOTIFICATION = 1
    CL_IOC_COMP_ARRIVAL_NOTIFICATION = 2
    CL_IOC_COMP_DEATH_NOTIFICATION = 3
    CL_IOC_SENDQ_WM_NOTIFICATION = 4
    CL_IOC_COMM_PORT_WM_NOTIFICATION = 5
    CL_IOC_LOG_NOTIFICATION = 6
    CL_IOC_NODE_VERSION_NOTIFICATION = 7
    CL_IOC_NODE_VERSION_REPLY_NOTIFICATION = 8
    CL_IOC_NODE_DISCOVER_NOTIFICATION = 9
    CL_IOC_NODE_LINK_UP_NOTIFICATION = 10
    CL_IOC_NODE_LINK_DOWN_NOTIFICATION = 11
    CL_IOC_NODE_DISCOVER_PEER_NOTIFICATION = 12

class ClIocQueueNotificationT(ctypes.Structure):
    _fields_ = [
        ("wmID", clCommon.ClWaterMarkIdT),
        ("wm", clCommon.ClWaterMarkT),
        ("queueSize", clCommon.ClUint32T),
        ("messageLength", clCommon.ClUint32T)
    ]

class _sendqWMNotification(ctypes.Structure):
    _fields_ = [
        ("queueNotification", ClIocQueueNotificationT)
    ]

class _commPortWMNotification(ctypes.Structure):
    _fields_ = [
        ("queueNotification", ClIocQueueNotificationT)
    ]

class _notificationData(ctypes.Union):
    _fields_ = [
        ("sendqWMNotification", _sendqWMNotification),
        ("commPortWMNotification", _commPortWMNotification)
    ]

class ClIocNotificationT(ctypes.Structure):
    _fields_ = [
        ("id", ClIocNotificationIdT),
        ("protoVersion", clCommon.ClUint32T),
        ("nodeAddress", clIocApi.ClIocAddressT),
        ("nodeVersion", clCommon.ClUint32T),
        ("notificationData", _notificationData)
    ]

def clIocLibInitialize(pConfig):
    """
    arg types:
        ClPtrT pConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocLibInitialize(pConfig)

def clIocLibFinalize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocLibFinalize()

def clIocMaxPayloadSizeGet(pSize):
    """
    arg types:
        ClUint32T * pSize
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocMaxPayloadSizeGet(clUtils.byref(pSize))

def clIocTotalNeighborEntryGet(pNumberOfEntries):
    """
    arg types:
        ClUint32T * pNumberOfEntries
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocTotalNeighborEntryGet(clUtils.byref(pNumberOfEntries))


def clIocNeighborListGet(pNumberOfEntries, pAddrList):
    """
    arg types:
        ClUint32T * pNumberOfEntries,
        ClIocNodeAddressT * pAddrList
    return type:
        ClRcT
    """
    return clLib.libmw_so.clIocNeighborListGet(clUtils.byref(pNumberOfEntries), clUtils.byref(pAddrList))

def clConfigChange(requestType):
    """
    Notifies the system of a configuration change request.
    arg types:
        ClConfigChange requestType
    return type:
        ClRcT
    """
    return clLib.libmw_so.clConfigChange(requestType)
