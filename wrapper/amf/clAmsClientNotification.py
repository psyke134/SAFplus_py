import sys
sys.path.append("..")

from common import clCommon, saAis
from utils import clUtils, clLib
from amf import clAmsEntities, clAmsTypes, saAmf, clCpmApi
import ctypes, enum

CL_AMS_EVENT_CHANNEL_NAME   = "AMS_EVENT_CHANNEL"
CL_AMS_EVENT_PATTERN        = "AMS_NOTIFICATION"
CL_AMS_EVENT_PUBLISHER_NAME = "AMS_NOTIFICATION_MANAGER"
CL_AMS_EVENT_VERSION        = "B.01.01"

ClAmsNotificationTypeT = clCommon.ClInt32T
class eClAmsNotificationTypeT(clUtils.Enum):
    CL_AMS_NOTIFICATION_NONE                        = 0
    CL_AMS_NOTIFICATION_FAULT                       = 1
    CL_AMS_NOTIFICATION_SU_INSTANTIATION_FAILURE    = 2
    CL_AMS_NOTIFICATION_SU_HA_STATE_CHANGE          = 3
    CL_AMS_NOTIFICATION_SI_FULLY_ASSIGNED           = 4
    CL_AMS_NOTIFICATION_SI_PARTIALLY_ASSIGNED       = 5
    CL_AMS_NOTIFICATION_SI_UNASSIGNED               = 6
    CL_AMS_NOTIFICATION_COMP_ARRIVAL                = 7
    CL_AMS_NOTIFICATION_COMP_DEPARTURE              = 8
    CL_AMS_NOTIFICATION_NODE_ARRIVAL                = 9
    CL_AMS_NOTIFICATION_NODE_DEPARTURE              = 10
    CL_AMS_NOTIFICATION_ENTITY_CREATE               = 11
    CL_AMS_NOTIFICATION_ENTITY_DELETE               = 12
    CL_AMS_NOTIFICATION_OPER_STATE_CHANGE           = 13   
    CL_AMS_NOTIFICATION_ADMIN_STATE_CHANGE          = 14
    CL_AMS_NOTIFICATION_NODE_SWITCHOVER             = 15
    CL_AMS_NOTIFICATION_NODE_FAILOVER               = 16
    CL_AMS_NOTIFICATION_COMP_HA_STATE_CHANGE        = 17
    CL_AMS_NOTIFICATION_MAX                         = 18

class ClAmsNotificationDescriptorT(ctypes.Structure):
    _fields_ = [
        ("type", ClAmsNotificationTypeT),
        ("entityType", clAmsEntities.ClAmsEntityTypeT),
        ("entityName", saAis.SaNameT),
        ("faultyCompName", saAis.SaNameT),
        ("siName", saAis.SaNameT),
        ("suName", saAis.SaNameT),
        ("lastHAState", saAmf.SaAmfHAStateT),
        ("newHAState", saAmf.SaAmfHAStateT),
        ("recoveryActionTaken", saAmf.SaAmfRecommendedRecoveryT),
        ("repairNecessary", clCommon.ClBoolT),
        ("lastOperState", clAmsTypes.ClAmsOperStateT),
        ("newOperState", clAmsTypes.ClAmsOperStateT),
        ("lastAdminState", clAmsTypes.ClAmsAdminStateT),
        ("newAdminState", clAmsTypes.ClAmsAdminStateT)
    ]

class _amsNotificationInfo(ctypes.Union):
    _fields_ = [
        ("amsStateInfo", ClAmsNotificationDescriptorT),
        ("amsCompInfo", clCpmApi.ClCpmEventPayLoadT),
        ("amsNodeInfo", clCpmApi.ClCpmEventNodePayLoadT),
    ]

class ClAmsNotificationInfoT(ctypes.Structure):
    _fields_ = [
        ("type", ClAmsNotificationTypeT),
        ("amsNotificationInfo", _amsNotificationInfo)
    ]

    def __setattr__(self, name, value):
        if name == "amsStateNotification":
            self.amsNotificationInfo.amsStateInfo = value
        elif name == "amsCompNotification":
            self.amsNotificationInfo.amsCompInfo = value
        elif name == "amsNodeNotification":
            self.amsNotificationInfo.amsNodeInfo = value
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name == "amsStateNotification":
            return self.amsNotificationInfo.amsStateInfo
        elif name == "amsCompNotification":
            return self.amsNotificationInfo.amsCompInfo
        elif name == "amsNodeNotification":
            return self.amsNotificationInfo.amsNodeInfo
        else:
            return self._data[name]

ClAmsClientNotificationCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, ctypes.POINTER(ClAmsNotificationInfoT))

def clAmsClientNotificationInitialize(callback):
    """
    arg types:
        ClAmsClientNotificationCallbackT callback
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsClientNotificationInitialize(callback)

def clAmsClientNotificationFinalize():
    """
    arg types:

    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsClientNotificationFinalize()

def clAmsNotificationEventPayloadExtract(eventHandle, eventDataSize, payLoad):
    """
    arg types:
        ClEventHandleT eventHandle,
        ClSizeT eventDataSize,
        void *payLoad
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsNotificationEventPayloadExtract(eventHandle, eventDataSize, payLoad)
