import sys
sys.path.append("..")

from utils import clLib

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
    return clLib.libmw_so.clEventExtWithRbeSubscribe(channelHandle, pRbeExpr, subscriptionId, pCookie)

def clEventExtAttributesSet(eventHandle, eventType, priority, retentionTime, pPublisherName):
    """
    arg types:
        const ClEventChannelHandleT channelHandle,
        ClRuleExprT *pRbeExpr,
        ClEventSubscriptionIdT subscriptionID,
        void *pCookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventExtAttributesSet(eventHandle, eventType, priority, retentionTime, pPublisherName)

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
    return clLib.libmw_so.clEventExtAttributesGet(eventHandle, pEventType, pPriority, pRetentionTime, pPublisherName, pPublishTime, pEventId)
