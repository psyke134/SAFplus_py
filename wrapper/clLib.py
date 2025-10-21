import ctypes
import os

libmw_so = ctypes.CDLL(os.path.dirname(__file__) + os.sep + "libmw_py.so")
