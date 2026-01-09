import sys
sys.path.append("..")

from common import saAis
from utils import clUtils, clLib
import ctypes

SaEvtHandleT = saAis.SaUint64T
SaEvtEventHandleT = saAis.SaUint64T
SaEvtChannelHandleT = saAis.SaUint64T
SaEvtSubscriptionIdT = saAis.SaUint32T

SaEvtChannelOpenCallbackT = ctypes.CFUNCTYPE(
    None,
    saAis.SaInvocationT,
    SaEvtChannelHandleT,
    saAis.SaAisErrorT
)

SaEvtEventDeliverCallbackT = ctypes.CFUNCTYPE(
    None,
    SaEvtSubscriptionIdT,
    SaEvtEventHandleT,
    saAis.SaSizeT
)

class SaEvtCallbacksT(ctypes.Structure):
    _fields_ = [
        ("saEvtChannelOpenCallback", SaEvtChannelOpenCallbackT),
        ("saEvtEventDeliverCallback", SaEvtEventDeliverCallbackT)
    ]

SA_EVT_CHANNEL_PUBLISHER = 0x1
SA_EVT_CHANNEL_SUBSCRIBER = 0x2
SA_EVT_CHANNEL_CREATE = 0x4

SaEvtChannelOpenFlagsT = saAis.SaUint8T

class SaEvtEventPatternT(ctypes.Structure):
    _fields_ = [
        ("allocatedSize", saAis.SaSizeT),
        ("patternSize", saAis.SaSizeT),
        ("pattern", ctypes.POINTER(saAis.SaUint8T))
    ]

class SaEvtEventPatternArrayT(ctypes.Structure):
    _fields_ = [
        ("allocatedNumber", saAis.SaSizeT),
        ("patternsNumber", saAis.SaSizeT),
        ("patterns", ctypes.POINTER(SaEvtEventPatternT))
    ]

SA_EVT_HIGHEST_PRIORITY = 0
SA_EVT_LOWEST_PRIORITY = 3

SaEvtEventPriorityT = saAis.SaUint8T
SaEvtEventIdT = saAis.SaUint64T

SA_EVT_EVENTID_NONE = 0
SA_EVT_EVENTID_LOST = 1

SA_EVT_LOST_EVENT = "SA_EVT_LOST_EVENT_PATTERN"

SaEvtEventFilterTypeT = saAis.SaInt32T
class eSaEvtEventFilterTypeT(clUtils.CEnum):
    SA_EVT_PREFIX_FILTER = 1,
    SA_EVT_SUFFIX_FILTER = 2,
    SA_EVT_EXACT_FILTER = 3,
    SA_EVT_PASS_ALL_FILTER = 4

class SaEvtEventFilterT(ctypes.Structure):
    _fields_ = [
        ("filterType", SaEvtEventFilterTypeT),
        ("filter", SaEvtEventPatternT)
    ]

class SaEvtEventFilterArrayT(ctypes.Structure):
    _fields_ = [
        ("filtersNumber", saAis.SaSizeT),
        ("filters", ctypes.POINTER(SaEvtEventFilterT))
    ]

def saEvtInitialize(evtHandle, callbacks, version):
    """
    arg types:
        SaEvtHandleT * evtHandle,
        const SaEvtCallbacksT * callbacks,
        SaVersionT *version
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtInitialize(evtHandle, callbacks, version)


def saEvtSelectionObjectGet(evtHandle, selectionObject):
    """
    arg types:
        SaEvtHandleT evtHandle,
        SaSelectionObjectT * selectionObject
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtSelectionObjectGet(evtHandle, selectionObject)


def saEvtDispatch(evtHandle, dispatchFlags):
    """
    arg types:
        SaEvtHandleT evtHandle,
        SaDispatchFlagsT dispatchFlags
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtDispatch(evtHandle, dispatchFlags)


def saEvtFinalize(evtHandle):
    """
    arg types:
        SaEvtHandleT evtHandle
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtFinalize(evtHandle)

def saEvtChannelOpen(evtHandle, channelName, channelOpenFlags, timeout, channelHandle):
    """
    arg types:
        SaEvtHandleT evtHandle,
        const SaNameT *channelName,
        SaEvtChannelOpenFlagsT channelOpenFlags,
        SaTimeT timeout,
        SaEvtChannelHandleT *channelHandle
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtChannelOpen(evtHandle, channelName, channelOpenFlags, timeout, channelHandle)


def saEvtChannelOpenAsync(evtHandle, invocation, channelName, channelOpenFlags):
    """
    arg types:
        SaEvtHandleT evtHandle,
        SaInvocationT invocation,
        const SaNameT *channelName,
        SaEvtChannelOpenFlagsT channelOpenFlags
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtChannelOpenAsync(evtHandle, invocation, channelName, channelOpenFlags)


def saEvtChannelClose(channelHandle):
    """
    arg types:
        SaEvtChannelHandleT channelHandle
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtChannelClose(channelHandle)


def saEvtChannelUnlink(evtHandle, channelName):
    """
    arg types:
        SaEvtHandleT evtHandle,
        const SaNameT *channelName
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtChannelUnlink(evtHandle, channelName)

def saEvtEventAllocate(channelHandle, eventHandle):
    """
    arg types:
        SaEvtChannelHandleT channelHandle,
        SaEvtEventHandleT *eventHandle
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtEventAllocate(channelHandle, eventHandle)


def saEvtEventFree(eventHandle):
    """
    arg types:
        SaEvtEventHandleT eventHandle
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtEventFree(eventHandle)


def saEvtEventAttributesSet(eventHandle, patternArray, priority, retentionTime, publisherName):
    """
    arg types:
        SaEvtEventHandleT eventHandle,
        const SaEvtEventPatternArrayT *patternArray,
        SaUint8T priority,
        SaTimeT retentionTime,
        const SaNameT *publisherName
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtEventAttributesSet(eventHandle, patternArray, priority, retentionTime, publisherName)


def saEvtEventAttributesGet(eventHandle, patternArray, priority, retentionTime, publisherName, publishTime, eventId):
    """
    arg types:
        SaEvtEventHandleT eventHandle,
        SaEvtEventPatternArrayT *patternArray,
        SaUint8T *priority,
        SaTimeT * retentionTime,
        SaNameT *publisherName,
        SaTimeT * publishTime,
        SaEvtEventIdT * eventId
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtEventAttributesGet(eventHandle, patternArray, priority, retentionTime, publisherName, publishTime, eventId)


def saEvtEventDataGet(eventHandle, eventData, eventDataSize):
    """
    arg types:
        SaEvtEventHandleT eventHandle,
        void *eventData,
        SaSizeT *eventDataSize
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtEventDataGet(eventHandle, eventData, eventDataSize)

def saEvtEventPublish(eventHandle, eventData, eventDataSize, eventId):
    """
    arg types:
        SaEvtEventHandleT eventHandle,
        const void *eventData,
        SaSizeT eventDataSize,
        SaEvtEventIdT * eventId
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtEventPublish(eventHandle, eventData, eventDataSize, eventId)


def saEvtEventSubscribe(channelHandle, filters, subscriptionId):
    """
    arg types:
        SaEvtChannelHandleT channelHandle,
        const SaEvtEventFilterArrayT *filters,
        SaEvtSubscriptionIdT subscriptionId
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtEventSubscribe(channelHandle, filters, subscriptionId)


def saEvtEventUnsubscribe(channelHandle, subscriptionId):
    """
    arg types:
        SaEvtChannelHandleT channelHandle,
        SaEvtSubscriptionIdT subscriptionId
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtEventUnsubscribe(channelHandle, subscriptionId)


def saEvtEventRetentionTimeClear(channelHandle, eventId):
    """
    arg types:
        SaEvtChannelHandleT channelHandle,
        SaEvtEventIdT eventId
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saEvtEventRetentionTimeClear(channelHandle, eventId)
