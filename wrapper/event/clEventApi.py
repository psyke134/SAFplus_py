import sys
sys.path.append("..")

from utils import clLib, clUtils
from common import clCommon

import ctypes

CL_EVENT_LOCAL_CHANNEL = (0x0)
CL_EVENT_GLOBAL_CHANNEL = (0x1)
CL_EVENT_CHANNEL_SUBSCRIBER = (0x2)
CL_EVENT_CHANNEL_PUBLISHER = (0x4)
CL_EVENT_CHANNEL_CREATE = (0x8)
CL_EVENT_HIGHEST_PRIORITY = (0x0)
CL_EVENT_LOWEST_PRIORITY = (0x3)

ClEventIdT = clCommon.ClUint64T
ClEventPriorityT = clCommon.ClUint8T
ClEventChannelOpenFlagsT = clCommon.ClUint8T
ClEventInitHandleT = clCommon.ClHandleT
ClEventHandleT = clCommon.ClHandleT
ClEventChannelHandleT = clCommon.ClHandleT
ClEventSubscriptionIdT = clCommon.ClUint32T

ClEventDeliverCallbackT = ctypes.CFUNCTYPE(
    None,
    ClEventSubscriptionIdT,
    ClEventHandleT,
    clCommon.ClSizeT
)

ClEventChannelOpenCallbackT = ctypes.CFUNCTYPE(
    None,
    clCommon.ClInvocationT,
    ClEventChannelHandleT,
    clCommon.ClRcT
)

class ClEventCallbacksT(ctypes.Structure):
    _fields_ = [
        ("clEvtChannelOpenCallback", ClEventChannelOpenCallbackT),
        ("clEvtEventDeliverCallback", ClEventDeliverCallbackT)
    ]

class ClEventVersionCallbacksT(ctypes.Structure):
    _fields_ = [
        ("version", clCommon.ClUint8T),
        ("callbacks", ClEventCallbacksT)
    ]

class ClEventPatternT(ctypes.Structure):
    _fields_ = [
        ("allocatedSize", clCommon.ClSizeT),
        ("patternSize", clCommon.ClSizeT),
        ("pPattern", ctypes.POINTER(clCommon.ClUint8T))
    ]

class ClEventPatternArrayT(ctypes.Structure):
    _fields_ = [
        ("allocatedNumber", clCommon.ClSizeT),
        ("patternsNumber", clCommon.ClSizeT),
        ("pPatterns", ctypes.POINTER(ClEventPatternT))
    ]

ClEventFilterTypeT = clCommon.ClInt32T
class eClEventFilterTypeT(clUtils.Enum):
    CL_EVENT_PREFIX_FILTER = 1
    CL_EVENT_SUFFIX_FILTER = 2
    CL_EVENT_EXACT_FILTER = 3
    CL_EVENT_PASS_ALL_FILTER = 4

class ClEventFilterT(ctypes.Structure):
    _fields_ = [
        ("filterType", ClEventFilterTypeT),
        ("filter", ClEventPatternT)
    ]

class ClEventFilterArrayT(ctypes.Structure):
    _fields_ = [
        ("filtersNumber", clCommon.ClSizeT),
        ("pFilters", ctypes.POINTER(ClEventFilterT))
    ]

def clEventInitialize(pEvtHandle, pEvtCallbacks, pVersion):
    """
    arg types:
        ClEventInitHandleT *pEvtHandle,
        ClEventCallbacksT * pEvtCallbacks,
        ClVersionT *pVersion
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventInitialize(clUtils.byref(pEvtHandle), clUtils.byref(pEvtCallbacks), clUtils.byref(pVersion))


def clEventInitializeWithVersion(pEvtHandle, pEvtCallbackTable, numCallbacks, pVersion):
    """
    arg types:
        ClEventInitHandleT *pEvtHandle,
        ClEventVersionCallbacksT *pEvtCallbackTable,
        ClUint32T numCallbacks,
        ClVersionT *pVersion
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventInitializeWithVersion(clUtils.byref(pEvtHandle), clUtils.byref(pEvtCallbackTable), numCallbacks, clUtils.byref(pVersion))


def clEventSelectionObjectGet(evtHandle, pSelectionObject):
    """
    arg types:
        ClEventInitHandleT evtHandle,
        ClSelectionObjectT * pSelectionObject
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventSelectionObjectGet(evtHandle, clUtils.byref(pSelectionObject))


def clEventDispatch(evtHandle, dispatchFlags):
    """
    arg types:
        ClEventInitHandleT evtHandle,
        ClDispatchFlagsT dispatchFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventDispatch(evtHandle, dispatchFlags)


def clEventFinalize(evtHandle):
    """
    arg types:
        ClEventInitHandleT evtHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventFinalize(evtHandle)

def clEventChannelOpen(evtHandle, pEvtChannelName, evtChannelOpenFlag, timeout, pChannelHandle):
    """
    arg types:
        ClEventInitHandleT evtHandle,
        ClNameT *pEvtChannelName,
        ClEventChannelOpenFlagsT evtChannelOpenFlag,
        ClTimeT timeout,
        ClEventChannelHandleT *pChannelHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventChannelOpen(evtHandle, clUtils.byref(pEvtChannelName), evtChannelOpenFlag, timeout, clUtils.byref(pChannelHandle))


def clEventChannelOpenAsync(evtHandle, invocation, pEvtChannelName, channelOpenFlags):
    """
    arg types:
        ClEventInitHandleT evtHandle,
        ClInvocationT invocation,
        ClNameT *pEvtChannelName,
        ClEventChannelOpenFlagsT channelOpenFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventChannelOpenAsync(evtHandle, invocation, clUtils.byref(pEvtChannelName), channelOpenFlags)


def clEventChannelClose(channelHandle):
    """
    arg types:
        ClEventChannelHandleT channelHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventChannelClose(channelHandle)


def clEventChannelUnlink(evtHandle, pEvtChannelName):
    """
    arg types:
        ClEventInitHandleT evtHandle,
        ClNameT *pEvtChannelName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventChannelUnlink(evtHandle, clUtils.byref(pEvtChannelName))


# --- Event Allocation/Freeing ---

def clEventAllocate(channelHandle, pEventHandle):
    """
    arg types:
        ClEventChannelHandleT channelHandle,
        ClEventHandleT *pEventHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventAllocate(channelHandle, clUtils.byref(pEventHandle))


def clEventAllocateWithVersion(channelHandle, version, pEventHandle):
    """
    arg types:
        ClEventChannelHandleT channelHandle,
        ClUint8T version,
        ClEventHandleT *pEventHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventAllocateWithVersion(channelHandle, version, clUtils.byref(pEventHandle))


def clEventFree(eventHandle):
    """
    arg types:
        ClEventHandleT eventHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventFree(eventHandle)

def clEventAttributesSet(eventHandle, pPatternArray, priority, retentionTime, pPublisherName):
    """
    arg types:
        ClEventHandleT eventHandle,
        ClEventPatternArrayT *pPatternArray,
        ClEventPriorityT priority,
        ClTimeT retentionTime,
        ClNameT *pPublisherName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventAttributesSet(eventHandle, clUtils.byref(pPatternArray), priority, retentionTime, clUtils.byref(pPublisherName))


def clEventAttributesGet(eventHandle, pPatternArray, pPriority, pRetentionTime, pPublisherName, pPublishTime, pEventId):
    """
    arg types:
        ClEventHandleT eventHandle,
        ClEventPatternArrayT *pPatternArray,
        ClEventPriorityT * pPriority,
        ClTimeT *pRetentionTime,
        ClNameT *pPublisherName,
        ClTimeT *pPublishTime,
        ClEventIdT * pEventId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventAttributesGet(
        eventHandle,
        clUtils.byref(pPatternArray),
        clUtils.byref(pPriority),
        clUtils.byref(pRetentionTime),
        clUtils.byref(pPublisherName),
        clUtils.byref(pPublishTime),
        clUtils.byref(pEventId))


def clEventDataGet(eventHandle, pEventData, pEventDataSize):
    """
    arg types:
        ClEventHandleT eventHandle,
        void *pEventData,
        ClSizeT *pEventDataSize
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventDataGet(eventHandle, pEventData, clUtils.byref(pEventDataSize))


def clEventCookieGet(eventHandle, ppCookie):
    """
    arg types:
        ClEventHandleT eventHandle,
        void **ppCookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventCookieGet(eventHandle, clUtils.byref(ppCookie))

def clEventPublish(eventHandle, pEventData, eventDataSize, pEventId):
    """
    arg types:
        ClEventHandleT eventHandle,
        void *pEventData,
        ClSizeT eventDataSize,
        ClEventIdT * pEventId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventPublish(eventHandle, pEventData, eventDataSize, clUtils.byref(pEventId))


def clEventSubscribe(channelHandle, pFilters, subscriptionId, pCookie):
    """
    arg types:
        ClEventChannelHandleT channelHandle,
        ClEventFilterArrayT *pFilters,
        ClEventSubscriptionIdT subscriptionId,
        void *pCookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventSubscribe(channelHandle, clUtils.byref(pFilters), subscriptionId, pCookie)


def clEventUnsubscribe(channelHandle, subscriptionId):
    """
    arg types:
        ClEventChannelHandleT channelHandle,
        ClEventSubscriptionIdT subscriptionId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventUnsubscribe(channelHandle, subscriptionId)


def clEventRetentionTimeClear(channelHandle, eventId):
    """
    arg types:
        ClEventChannelHandleT channelHandle,
        ClEventIdT eventId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clEventRetentionTimeClear(channelHandle, eventId)
