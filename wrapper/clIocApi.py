import clCommon
import ctypes
import clLib

ClIocNodeAddressT = clCommon.ClUint32T

ClIocPortT = clCommon.ClUint32T

ClIocLogicalAddressT = clCommon.ClUint64T

ClIocMulticastAddressT = clCommon.ClUint64T

class ClIocPhysicalAddressT(ctypes.Structure):
    _fields_ = [
        ("nodeAddress", ClIocNodeAddressT),
        ("portId", ClIocPortT)
    ]

class ClIocAddressT(ctypes.Union):
    _fields_ = [
        ("iocPhyAddress", ClIocPhysicalAddressT),
        ("iocLogicalAddress", ClIocLogicalAddressT),
        ("iocMulticastAddress", ClIocMulticastAddressT)
    ]

ClIocPortT = clCommon.ClUint32T

def clIocLocalAddressGet():
    """
    return type:
        ClIocNodeAddressT
    """
    return clLib.libmw_so.clIocLocalAddressGet()
