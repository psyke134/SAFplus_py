import saAis
import ctypes
import clUtils, clLib

SaMsgHandleT = saAis.SaUint64T
SaMsgQueueHandleT = saAis.SaUint64T
SaMsgSenderIdT = saAis.SaUint64T

SA_MSG_MESSAGE_DELIVERED_ACK = 0x1

SaMsgAckFlagsT = saAis.SaUint32T

SA_MSG_QUEUE_PERSISTENT = 0x1

SaMsgQueueCreationFlagsT = saAis.SaUint32T

SA_MSG_MESSAGE_HIGHEST_PRIORITY = 0
SA_MSG_MESSAGE_LOWEST_PRIORITY = 3

class SaMsgQueueCreationAttributesT(ctypes.Structure):
    _fields_ = [
        ("creationFlags", SaMsgQueueCreationFlagsT),
        ("size", saAis.SaSizeT * (SA_MSG_MESSAGE_LOWEST_PRIORITY + 1)),
        ("retentionTime", saAis.SaTimeT)
    ]

SaMsgQueueGroupPolicyT = saAis.SaInt32T
class eSaMsgQueueGroupPolicyT(clUtils.CEnum):
    SA_MSG_QUEUE_GROUP_ROUND_ROBIN          = 1,
    SA_MSG_QUEUE_GROUP_LOCAL_ROUND_ROBIN    = 2,
    SA_MSG_QUEUE_GROUP_LOCAL_BEST_QUEUE     = 3,
    SA_MSG_QUEUE_GROUP_BROADCAST            = 4

SA_MSG_QUEUE_CREATE = 0x1
SA_MSG_QUEUE_RECEIVE_CALLBACK = 0x2
SA_MSG_QUEUE_EMPTY = 0x4

SaMsgQueueOpenFlagsT = saAis.SaUint32T

class SaMsgQueueUsageT(ctypes.Structure):
    _fields_ = [
        ("queueSize", saAis.SaSizeT),
        ("queueUsed", saAis.SaSizeT),
        ("numberOfMessages", saAis.SaUint32T)
    ]

class SaMsgQueueStatusT(ctypes.Structure):
    _fields_ = [
        ("creationFlags", SaMsgQueueCreationFlagsT),
        ("retentionTime", saAis.SaTimeT),
        ("closeTime", saAis.SaTimeT),
        ("saMsgQueueUsage", SaMsgQueueUsageT * (SA_MSG_MESSAGE_LOWEST_PRIORITY + 1))
    ]

SaMsgQueueGroupChangesT = saAis.SaInt32T
class eSaMsgQueueGroupChangesT(clUtils.CEnum):
    SA_MSG_QUEUE_GROUP_NO_CHANGE        = 1,
    SA_MSG_QUEUE_GROUP_ADDED            = 2,
    SA_MSG_QUEUE_GROUP_REMOVED          = 3,
    SA_MSG_QUEUE_GROUP_STATE_CHANGED    = 4

class SaMsgQueueGroupMemberT(ctypes.Structure):
    _fields_ = [
        ("queueName", saAis.SaNameT)
    ]
class SaMsgQueueGroupNotificationT(ctypes.Structure):
    _fields_ = [
        ("member", SaMsgQueueGroupMemberT),
        ("change", SaMsgQueueGroupChangesT)
    ]

class SaMsgQueueGroupNotificationBufferT(ctypes.Structure):
    _fields_ = [
        ("numberOfItems", saAis.SaUint32T),
        ("notification", ctypes.POINTER(SaMsgQueueGroupNotificationT)),
        ("queueGroupPolicy", SaMsgQueueGroupPolicyT)
    ]

class SaMsgMessageT(ctypes.Structure):
    _fields_ = [
        ("type", saAis.SaUint32T),
        ("version", saAis.SaVersionT),
        ("size", saAis.SaSizeT),
        ("senderName", ctypes.POINTER(saAis.SaNameT)),
        ("data", ctypes.c_void_p),
        ("priority", saAis.SaUint8T)
    ]

SaMsgQueueOpenCallbackT = ctypes.CFUNCTYPE(None, saAis.SaInvocationT, SaMsgQueueHandleT, saAis.SaAisErrorT)
SaMsgQueueGroupTrackCallbackT = ctypes.CFUNCTYPE(None, ctypes.POINTER(saAis.SaNameT), ctypes.POINTER(SaMsgQueueGroupNotificationBufferT), saAis.SaUint32T, saAis.SaAisErrorT)
SaMsgMessageDeliveredCallbackT = ctypes.CFUNCTYPE(None, saAis.SaInvocationT, saAis.SaAisErrorT)
SaMsgMessageReceivedCallbackT = ctypes.CFUNCTYPE(None, SaMsgQueueHandleT)

class SaMsgCallbacksT(ctypes.Structure):
    _fields_ = [
        ("saMsgQueueOpenCallback", SaMsgQueueOpenCallbackT),
        ("saMsgQueueGroupTrackCallback", SaMsgQueueGroupTrackCallbackT),
        ("saMsgMessageDeliveredCallback", SaMsgMessageDeliveredCallbackT),
        ("saMsgMessageReceivedCallback", SaMsgMessageReceivedCallbackT)
    ]

def saMsgInitialize(msgHandle, msgCallbacks, version):
    """
    arg types:
        SaMsgHandleT *msgHandle,
        SaMsgCallbacksT *msgCallbacks,
        SaVersionT *version
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgInitialize(msgHandle, msgCallbacks, version)

def saMsgSelectionObjectGet(msgHandle, selectionObject):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaSelectionObjectT *selectionObject
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgSelectionObjectGet(msgHandle, selectionObject)

def saMsgDispatch(msgHandle, dispatchFlags):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaDispatchFlagsT dispatchFlags
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgDispatch(msgHandle, dispatchFlags)

def saMsgFinalize(msgHandle):
    """
    arg types:
        SaMsgHandleT msgHandle
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgFinalize(msgHandle)

def saMsgQueueOpen(msgHandle, queueName, creationAttributes, openFlags, timeout, queueHandle):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaNameT *queueName,
        SaMsgQueueCreationAttributesT *creationAttributes,
        SaMsgQueueOpenFlagsT openFlags,
        SaTimeT timeout,
        SaMsgQueueHandleT *queueHandle
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueOpen(msgHandle, queueName, creationAttributes, openFlags, timeout, queueHandle)

def saMsgQueueOpenAsync(msgHandle, invocation, queueName, creationAttributes, openFlags):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaInvocationT invocation,
        SaNameT *queueName,
        SaMsgQueueCreationAttributesT *creationAttributes,
        SaMsgQueueOpenFlagsT openFlags
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueOpenAsync(msgHandle, invocation, queueName, creationAttributes, openFlags)

def saMsgQueueClose(queueHandle):
    """
    arg types:
        SaMsgQueueHandleT queueHandle
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueClose(queueHandle)

def saMsgQueueStatusGet(msgHandle, queueName, queueStatus):
    """
    arg types:
        SaMsgQueueHandleT msgHandle,
        SaNameT *queueName,
        SaMsgQueueStatusT *queueStatus
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueStatusGet(msgHandle, queueName, queueStatus)

def saMsgQueueRetentionTimeSet(queueHandle, retentionTime):
    """
    arg types:
        SaMsgQueueHandleT queueHandle,
        SaTimeT *retentionTime
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueRetentionTimeSet(queueHandle, retentionTime)

def saMsgQueueUnlink(msgHandle, queueName):
    """
    arg types:
        SaMsgQueueHandleT msgHandle,
        SaNameT *queueName
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueUnlink(msgHandle, queueName)

def saMsgQueueGroupCreate(msgHandle, queueGroupName, queueGroupPolicy):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaNameT *queueGroupName,
        SaMsgQueueGroupPolicyT queueGroupPolicy
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueGroupCreate(msgHandle, queueGroupName, queueGroupPolicy)

def saMsgQueueGroupInsert(msgHandle, queueGroupName, queueName):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaNameT *queueGroupName,
        SaNameT *queueName
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueGroupInsert(msgHandle, queueGroupName, queueName)

def saMsgQueueGroupRemove(msgHandle, queueGroupName, queueName):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaNameT *queueGroupName,
        SaNameT *queueName
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueGroupRemove(msgHandle, queueGroupName, queueName)

def saMsgQueueGroupDelete(msgHandle, queueGroupName):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaNameT *queueGroupName
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueGroupDelete(msgHandle, queueGroupName)

def saMsgQueueGroupTrack(msgHandle, queueGroupName, trackFlags, notificationBuffer):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaNameT *queueGroupName,
        SaUint8T trackFlags,
        SaMsgQueueGroupNotificationBufferT *notificationBuffer
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueGroupTrack(msgHandle, queueGroupName, trackFlags, notificationBuffer)

def saMsgQueueGroupTrackStop(msgHandle, queueGroupName):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaNameT *queueGroupName
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueGroupTrackStop(msgHandle, queueGroupName)

def saMsgQueueGroupNotificationFree(msgHandle, notification):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaMsgQueueGroupNotificationT *notification
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgQueueGroupNotificationFree(msgHandle, notification)

def saMsgMessageSend(msgHandle, destination, message, timeout):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaNameT *destination,
        SaMsgMessageT *message,
        SaTimeT timeout
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgMessageSend(msgHandle, destination, message, timeout)

def saMsgMessageSendAsync(msgHandle, invocation, destination, message, ackFlags):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaInvocationT invocation,
        SaNameT *destination,
        SaMsgMessageT *message,
        SaMsgAckFlagsT ackFlags
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgMessageSendAsync(msgHandle, invocation, destination, message, ackFlags)

def saMsgMessageGet(queueHandle, message, sendTime, senderId, timeout):
    """
    arg types:
        SaMsgQueueHandleT queueHandle,
        SaMsgMessageT *message,
        SaTimeT *sendTime,
        SaMsgSenderIdT *senderId,
        SaTimeT timeout
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgMessageGet(queueHandle, message, sendTime, senderId, timeout)

def saMsgMessageDataFree(msgHandle, pData):
    """
    arg types:
        SaMsgHandleT msgHandle,
        void *pData
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgMessageDataFree(msgHandle, pData)

def saMsgMessageCancel(queueHandle):
    """
    arg types:
        SaMsgQueueHandleT queueHandle
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgMessageCancel(queueHandle)

def saMsgMessageSendReceive(msgHandle, destination, sendMessage, receiveMessage, replySendTime, timeout):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaNameT *destination,
        SaMsgMessageT *sendMessage,
        SaMsgMessageT *receiveMessage,
        SaTimeT *replySendTime,
        SaTimeT timeout
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgMessageSendReceive(msgHandle, destination, sendMessage, receiveMessage, replySendTime, timeout)

def saMsgMessageReply(msgHandle, replyMessage, senderId, timeout):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaMsgMessageT *replyMessage,
        SaMsgSenderIdT *senderId,
        SaTimeT timeout
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgMessageReply(msgHandle, replyMessage, senderId, timeout)

def saMsgMessageReplyAsync(msgHandle, invocation, replyMessage, senderId, ackFlags):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaInvocationT invocation,
        SaMsgMessageT *replyMessage,
        SaMsgSenderIdT *senderId,
        SaMsgAckFlagsT ackFlags
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saMsgMessageReplyAsync(msgHandle, invocation, replyMessage, senderId, ackFlags)
