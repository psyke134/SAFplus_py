import sys
sys.path.append("..")

from common import clCommon
from amf import clAmsTypes

import ctypes

ClAmsSACSISetCallbackT = ctypes.CFUNCTYPE(
    None,
    clCommon.ClInvocationT,
    ctypes.POINTER(clCommon.ClNameT),
    clAmsTypes.ClAmsHAStateT,
    clAmsTypes.ClAmsCSIDescriptorT
)

ClAmsSACSIRemoveCallbackT = ctypes.CFUNCTYPE(
    None,
    clCommon.ClInvocationT,
    ctypes.POINTER(clCommon.ClNameT),
    ctypes.POINTER(clCommon.ClNameT),
    clAmsTypes.ClAmsCSIFlagsT
)

ClAmsSAPGTrackCallbackT = ctypes.CFUNCTYPE(
    None,
    ctypes.POINTER(clCommon.ClNameT),
    clAmsTypes.ClAmsPGNotificationBufferT,
    clCommon.ClUint32T,
    clCommon.ClRcT
)

ClAmsSACompHealthcheckCallbackT = ctypes.CFUNCTYPE(
    None,
    clCommon.ClInvocationT,
    ctypes.POINTER(clCommon.ClNameT),
    clAmsTypes.ClAmsCompHealthcheckKeyT
)

ClAmsSACompTerminateCallbackT = ctypes.CFUNCTYPE(
    None,
    clCommon.ClInvocationT,
    ctypes.POINTER(clCommon.ClNameT)
)

ClAmsSAProxiedCompInstantiateCallbackT = ctypes.CFUNCTYPE(
    None,
    clCommon.ClInvocationT,
    ctypes.POINTER(clCommon.ClNameT)
)

ClAmsSAProxiedCompCleanupCallbackT = ctypes.CFUNCTYPE(
    None,
    clCommon.ClInvocationT,
    ctypes.POINTER(clCommon.ClNameT)
)

class ClAmsSAClientCallbacksT(ctypes.Structure):
    _fields_ = [
        ("healthcheckCallback", ClAmsSACompHealthcheckCallbackT),
        ("compTerminateCallback", ClAmsSACompTerminateCallbackT),
        ("csiSetCallback", ClAmsSACSISetCallbackT),
        ("csiRemoveCallback", ClAmsSACSIRemoveCallbackT),
        ("pgTrackCallback", ClAmsSAPGTrackCallbackT),
        ("proxiedCompInstantiateCallback", ClAmsSAProxiedCompInstantiateCallbackT),
        ("proxiedCompCleanupCallback", ClAmsSAProxiedCompCleanupCallbackT)
    ]

# TODO: there're remaining codes in the original header file
