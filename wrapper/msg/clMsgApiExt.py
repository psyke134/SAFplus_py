import sys
sys.path.append("..")

from utils import clLib, libc, clUtils
from common import clCommon, saAis

import ctypes

class ClMsgMessageIovecT(ctypes.Structure):
    _fields_ = [
        ("type", saAis.SaUint32T),
        ("version", saAis.SaVersionT),
        ("senderName", ctypes.POINTER(saAis.SaNameT)),
        ("priority", saAis.SaUint8T),
        ("pIovec", ctypes.POINTER(libc.iovec)),
        ("numIovecs", clCommon.ClUint32T)
    ]

def clMsgDispatchQueueRegister(queueHandle, callback):
    """
    arg types:
        SaMsgQueueHandleT queueHandle,
        SaMsgMessageReceivedCallbackT callback
    return type:
        ClRcT
    """
    return clLib.libmw_so.clMsgDispatchQueueRegister(queueHandle, callback)


def clMsgDispatchQueueDeregister(queueHandle):
    """
    arg types:
        SaMsgQueueHandleT queueHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clMsgDispatchQueueDeregister(queueHandle)

def clMsgQueuePersistRedundancy(queue, node):
    """
    arg types:
        const SaNameT *queue,
        const SaNameT *node
    return type:
        ClRcT
    """
    return clLib.libmw_so.clMsgQueuePersistRedundancy(clUtils.byref(queue), clUtils.byref(node))

def clMsgQueueGroupSendWithKeySynch(msgHandle, group, message, key, keylen, timeout):
    """
    arg types:
        SaMsgHandleT msgHandle,
        const SaNameT *group,
        SaMsgMessageT *message, 
        ClCharT *key,
        ClInt32T keylen,
        SaTimeT timeout
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.clMsgQueueGroupSendWithKeySynch(msgHandle, clUtils.byref(group), clUtils.byref(message), clUtils.toCharP(key), keylen, timeout)


def clMsgQueueGroupSendWithKeyAsync(msgHandle, invocation, group, message, key, keylen, ackFlags):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaInvocationT invocation,
        const SaNameT *group, 
        SaMsgMessageT *message,
        ClCharT *key,
        ClInt32T keylen,
        SaMsgAckFlagsT ackFlags
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.clMsgQueueGroupSendWithKeyAsync(msgHandle, invocation, clUtils.byref(group), clUtils.byref(message), clUtils.toCharP(key), keylen, ackFlags)

def clMsgMessageSendIovec(msgHandle, destination, message, timeout):
    """
    arg types:
        SaMsgHandleT msgHandle,
        const SaNameT *destination, 
        const ClMsgMessageIovecT *message,
        SaTimeT timeout
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.clMsgMessageSendIovec(msgHandle, clUtils.byref(destination), clUtils.byref(message), timeout)


def clMsgMessageSendAsyncIovec(msgHandle, invocation, destination, message, ackFlags):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaInvocationT invocation,
        const SaNameT *destination, 
        const ClMsgMessageIovecT *message,
        SaMsgAckFlagsT ackFlags
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.clMsgMessageSendAsyncIovec(msgHandle, invocation, clUtils.byref(destination), clUtils.byref(message), ackFlags)

def clMsgQueueGroupSendWithKeySynchIovec(msgHandle, group, message, key, keylen, timeout):
    """
    arg types:
        SaMsgHandleT msgHandle,
        const SaNameT *group,
        ClMsgMessageIovecT *message, 
        ClCharT *key,
        ClInt32T keylen,
        SaTimeT timeout
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.clMsgQueueGroupSendWithKeySynchIovec(msgHandle, clUtils.byref(group), clUtils.byref(message), clUtils.toCharP(key), keylen, timeout)

def clMsgQueueGroupSendWithKeyAsyncIovec(msgHandle, invocation, group, message, key, keylen, ackFlags):
    """
    arg types:
        SaMsgHandleT msgHandle,
        SaInvocationT invocation,
        const SaNameT *group, 
        ClMsgMessageIovecT *message,
        ClCharT *key,
        ClInt32T keylen,
        SaMsgAckFlagsT ackFlags
    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.clMsgQueueGroupSendWithKeyAsyncIovec(msgHandle, invocation, clUtils.byref(group), clUtils.byref(message), clUtils.toCharP(key), keylen, ackFlags)
