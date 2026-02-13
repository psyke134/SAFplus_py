import sys
sys.path.append("..")

from common import clCommon
from utils import clLib, clUtils

import ctypes

CL_HANDLE_INVALID_VALUE = 0x0
CL_HDL_IDX_MASK = 0x00000000FFFFFFFF

def CL_HDL_IDX(hdl):
    return clCommon.ClUint32T(hdl.value & CL_HDL_IDX_MASK)

CL_HDL_NODE_ADDR_MASK = 0xFFF0000000000000
CL_HDL_PORT_ADDR_MASK = 0x000FFF0000000000
CL_HDL_DB_ADDR_MASK = 0x000000FF00000000

def CL_HDL_NODE_ADDR(hdl):
    return clCommon.ClUint64T((hdl.value & CL_HDL_NODE_ADDR_MASK) >> 52)

def CL_HDL_PORT_ADDR(hdl):
    return clCommon.ClUint64T((hdl.value & CL_HDL_PORT_ADDR_MASK) >> 40)

def CL_HDL_DB_ADDR(hdl):
    return clCommon.ClUint64T((hdl.value & CL_HDL_DB_ADDR_MASK) >> 32)

ClHandleDatabaseHandleT = clCommon.ClPtrT

def clHandleDatabaseCreate(destructor, databaseHandle):
    """
    arg types: 
        void (*destructor)(void*), 
        ClHandleDatabaseHandleT *databaseHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHandleDatabaseCreate(destructor, clUtils.byref(databaseHandle))

def clHandleDatabaseDestroy(databaseHandle):
    """
    arg types:
        ClHandleDatabaseHandleT databaseHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHandleDatabaseDestroy(databaseHandle)

def clHandleCreate(databaseHandle, instanceSize, handle):
    """
    arg types: 
        ClHandleDatabaseHandleT databaseHandle, 
        ClInt32T instanceSize, 
        ClHandleT *handle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHandleCreate(databaseHandle, instanceSize, clUtils.byref(handle))

def clHandleWithAddressCreate(databaseHandle, instance_size, compAddr, handle_out):
    """
    arg types: 
        ClHandleDatabaseHandleT databaseHandle, 
        ClInt32T instance_size, 
        ClIocPhysicalAddressT compAddr, 
        ClHandleT *handle_out
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHandleWithAddressCreate(databaseHandle, instance_size, compAddr, clUtils.byref(handle_out))

def clHandleDestroy(databaseHandle, handle):
    """
    arg types:
        ClHandleDatabaseHandleT databaseHandle,
        ClHandleT handle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHandleDestroy(databaseHandle, handle)

def clHandleCheckout(databaseHandle, handle, instance):
    """
    arg types: 
        ClHandleDatabaseHandleT databaseHandle, 
        ClHandleT handle, 
        void **instance
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHandleCheckout(databaseHandle, handle, clUtils.byref(instance))

def clHandleCheckin(databaseHandle, handle):
    """
    arg types:
        ClHandleDatabaseHandleT databaseHandle,
        ClHandleT handle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHandleCheckin(databaseHandle, handle)

def clHandleMove(databaseHandle, oldHandle, newHandle):
    """
    arg types: 
        ClHandleDatabaseHandleT databaseHandle, 
        ClHandleT oldHandle, 
        ClHandleT newHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clHandleMove(databaseHandle, oldHandle, newHandle)


def clHandleGetDatabaseId(databaseHandle):
    """
    arg types:
        ClHandleDatabaseHandleT *databaseHandle
    return type:
        ClWordT
    """
    clLib.libmw_so.clHandleGetDatabaseId.restype = clCommon.ClWordT
    return clLib.libmw_so.clHandleGetDatabaseId(clUtils.byref(databaseHandle))
