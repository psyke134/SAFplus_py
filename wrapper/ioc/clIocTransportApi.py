import sys
sys.path.append("..")

from common import clCommon
from buffer import clBufferApi
from ioc import clIocApi

import ctypes

CL_IOC_DEF_MAX_ALLOWED_XPORTS = 5

CL_IOC_MAX_XPORT_STRING_LENGTH = 127
CL_IOC_MAX_XPORT_ADDR_SIZE = CL_IOC_MAX_XPORT_STRING_LENGTH
CL_IOC_MAX_XPORT_NAME_LENGTH = CL_IOC_MAX_XPORT_STRING_LENGTH
CL_IOC_MIN_MTU_SIZE = 256

class ClIocTransportStatsT(ctypes.Structure):
    _fields_ = [
        ("sendMsgs", clCommon.ClUint32T),
        ("recvMsgs", clCommon.ClUint32T),
        ("sendBytes", clCommon.ClUint32T),
        ("recvBytes", clCommon.ClUint32T),
        ("badMsgs", clCommon.ClUint32T),
        ("dropMsgs", clCommon.ClUint32T)
    ]

class ClIocTransportLinkConfigT(ctypes.Structure):
    pass

ClIocCoreFuncT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clBufferApi.ClBufferHandleT,
    ctypes.POINTER(ClIocTransportLinkConfigT),
    ctypes.POINTER(clCommon.ClUint8T)
)

ClIocTransportFuncT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(ClIocTransportLinkConfigT)
)

ClIocTransportSendFuncT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clBufferApi.ClBufferHandleT,
    ctypes.POINTER(ClIocTransportLinkConfigT),
    ctypes.POINTER(clCommon.ClUint8T)
)

ClIocTransportAddrConvertFuncT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClUint8T),
    ctypes.POINTER(clCommon.ClUint8T)
)

ClIocGroupCreateFuncT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clIocApi.ClIocAddressT),
    ctypes.POINTER(clCommon.ClUint8T)
)

ClIocGroupJoinFuncT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClUint8T)
)

ClIocGroupLeaveFuncT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClUint8T)
)

ClIocGroupDeleteFuncT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ctypes.POINTER(clCommon.ClUint8T)
)

ClIocTransportLinkConfigT._fields_ = [
    ("pXportName", clCommon.ClCharT * (CL_IOC_MAX_XPORT_NAME_LENGTH + 1)),
    ("pXportLinkName", clCommon.ClCharT * (CL_IOC_MAX_XPORT_NAME_LENGTH + 1)),
    ("xportType", clCommon.ClUint8T),
    ("isChecksumReqd", clCommon.ClUint8T),
    ("addressSize", clCommon.ClUint8T),
    ("isBcastSupported", clCommon.ClUint8T),
    ("xportBcastAddress", clCommon.ClUint8T),
    ("xportAddress", clCommon.ClUint8T),
    ("mtuSize", clCommon.ClUint32T),
    ("pIocXportStats", ctypes.POINTER(ClIocTransportStatsT)),
    ("iocCoreRecvRoutine", ClIocCoreFuncT),
    ("priority", clCommon.ClUint8T),
    ("isRegistered", clCommon.ClUint8T),
    ("pXportLinkPrivData", clCommon.ClPtrT),
    ("status", clCommon.ClUint8T)
]

class ClIocTransportConfigT(ctypes.Structure):
    _fields_ = [
        ("version", clCommon.ClUint8T),
        ("pXportName", clCommon.ClCharT * (CL_IOC_MAX_XPORT_NAME_LENGTH + 1)),
        ("priority", clCommon.ClUint8T),
        ("xportType", clCommon.ClUint8T),
        ("initRoutine", ClIocTransportFuncT),
        ("sendRoutine", ClIocTransportSendFuncT),
        ("closeRoutine", ClIocTransportFuncT),
        ("addrConvertRoutine", ClIocTransportAddrConvertFuncT),
        ("addrExtractRoutine", ClIocTransportAddrConvertFuncT)
    ]
