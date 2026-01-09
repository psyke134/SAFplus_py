import sys
sys.path.append("..")

from common import clCommon, clCommonErrors

import ctypes

class hashStruct(ctypes.Structure):
    pass
hashStruct._fields_ = [
    ("pNext", ctypes.POINTER(hashStruct)),
    ("ppPrev", ctypes.POINTER(ctypes.POINTER(hashStruct)))
]

# TODO: there're remaining codes in the original header file
