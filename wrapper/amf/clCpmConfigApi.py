import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils

import ctypes

CL_CPM_DEFAULT_MIN_FREQ = 2000

CL_CPM_DEFAULT_MAX_FREQ = 32000

ClCpmCompProcessRelT = clCommon.ClInt32T
class eClCpmCompProcessRelT(clUtils.CEnum):
    CL_CPM_COMP_NONE = 0,
    CL_CPM_COMP_MULTI_PROCESS = 1,
    CL_CPM_COMP_SINGLE_PROCESS = 2,
    CL_CPM_COMP_THREADED = 3

class ClCpmNodeClassTypeT(ctypes.Structure):
    _fields_ = [
        ("name", clCommon.ClNameT),
        ("identifier", clCommon.ClNameT)
    ]

class ClCpmSlotClassTypesT(ctypes.Structure):
    _fields_ = [
        ("numItems", clCommon.ClUint32T),
        ("nodeClassTypes", ctypes.POINTER(ClCpmNodeClassTypeT))
    ]
