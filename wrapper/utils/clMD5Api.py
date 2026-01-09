import sys
sys.path.append("..")

from common import clCommon
from utils import clLib

import ctypes

class ClMD5T(ctypes.Structure):
    _fields_ = [
        ("md5sum", clCommon.ClUint8T * 16)
    ]

def clMD5Compute(data, size, result):
    """
    arg types:
        ClUint8T *data,
        ClUint32T size,
        ClUint8T result[16]
    return type:
        void
    """
    return clLib.libmw_so.clMD5Compute(data, size, result)
