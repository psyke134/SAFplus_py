import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils
from amf import clAmsEntities

import ctypes

ClAmsInvocationCmdT = clCommon.ClInt32T
class eClAmsInvocationCmdT(clUtils.Enum):
    CL_AMS_TERMINATE_CALLBACK               = 1
    CL_AMS_CSI_SET_CALLBACK                 = 2
    CL_AMS_CSI_RMV_CALLBACK                 = 3
    CL_AMS_PG_TRACK_CALLBACK                = 4
    CL_AMS_INSTANTIATE_CALLBACK             = 5
    CL_AMS_PROXIED_INSTANTIATE_CALLBACK     = 6
    CL_AMS_PROXIED_CLEANUP_CALLBACK         = 7
    CL_AMS_CSI_QUIESCING_CALLBACK           = 8
    CL_AMS_INSTANTIATE_REPLAY_CALLBACK      = 9
    CL_AMS_TERMINATE_REPLAY_CALLBACK        = 10
    CL_AMS_RECOVERY_REPLAY_CALLBACK         = 11
    CL_AMS_MAX_CALLBACKS                    = 12

class ClAmsInvocationT(ctypes.Structure):
    _fields_ = [
        ("invocation", clCommon.ClInvocationT),
        ("cmd", ClAmsInvocationCmdT),
        ("compName", clCommon.ClNameT),
        ("csiTargetOne", clCommon.ClBoolT),
        ("csi", ctypes.POINTER(clAmsEntities.ClAmsCSIT)),
        ("csiName", clCommon.ClNameT),
        ("reassignCSI", clCommon.ClBoolT),
    ]
