import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils

import ctypes

CL_CPM_EO_VERSION_NO = 0x0100
CL_CPM_RESTART_FILE = "safplus_restart"
CL_CPM_REBOOT_FILE = "safplus_reboot"
CL_CPM_WATCHDOG_RESTART_FILE = "safplus_restart_watchdog"

class ClCpmFuncWalkT(ctypes.Structure):
    _fields_ = [
        ("funcno", clCommon.ClUint32T),
        ("inLen", clCommon.ClUint32T),
        ("inputArg", clCommon.ClInt8T * 1)
    ]

ClCpmCompRequestTypeT = clCommon.ClInt32T
class eClCpmCompRequestTypeT(clUtils.Enum):
    CL_CPM_REQUEST_NONE = 0
    CL_CPM_HEALTHCHECK = 1
    CL_CPM_TERMINATE = 2
    CL_CPM_PROXIED_INSTANTIATE = 3
    CL_CPM_PROXIED_CLEANUP = 4
    CL_CPM_EXTN_HEALTHCHECK = 5
    CL_CPM_INSTANTIATE = 6
    CL_CPM_CLEANUP = 7
    CL_CPM_RESTART = 8

# TODO: there're remaining codes in the original header file
