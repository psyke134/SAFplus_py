import sys
sys.path.append("..")

from utils import clLib, clUtils

def clEventExtSubscribe(channelHandle, eventType, subscriptionId, pCookie):
    """
    arg types:
        ClEventChannelHandleT channelHandle,
        ClUint32T eventType,
        ClEventSubscriptionIdT subscriptionId,
        void *pCookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventExtSubscribe(channelHandle, eventType, subscriptionId, pCookie)

def clEventExtWithRbeSubscribe(channelHandle, pRbeExpr, subscriptionId, pCookie):
    """
    arg types:
        const ClEventChannelHandleT channelHandle,
        ClRuleExprT *pRbeExpr,
        ClEventSubscriptionIdT subscriptionID,
        void *pCookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventExtWithRbeSubscribe(channelHandle, clUtils.byref(pRbeExpr), subscriptionId, pCookie)

def clEventExtAttributesSet(eventHandle, eventType, priority, retentionTime, pPublisherName):
    """
    arg types:
        ClEventHandleT eventHandle,
        ClUint32T eventType,
        ClEventPriorityT priority,
        ClTimeT retentionTime,
        ClNameT *pPublisherName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventExtAttributesSet(eventHandle, eventType, priority, retentionTime, clUtils.byref(pPublisherName))

def clEventExtAttributesGet(eventHandle, pEventType, pPriority, pRetentionTime, pPublisherName, pPublishTime, pEventId):
    """
    arg types:
        ClEventHandleT eventHandle,
        ClUint32T *pEventType,
        ClEventPriorityT * pPriority,
        ClTimeT *pRetentionTime,
        ClNameT *pPublisherName,
        ClTimeT *pPublishTime,
        ClEventIdT * pEventId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventExtAttributesGet(
        eventHandle,
        clUtils.byref(pEventType),
        clUtils.byref(pPriority),
        clUtils.byref(pRetentionTime),
        clUtils.byref(pPublisherName),
        clUtils.byref(pPublishTime),
        clUtils.byref(pEventId))
