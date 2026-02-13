import sys
sys.path.append("..")

from utils import clUtils, clLib
from common import clCommon
from amf import clAmsEntities

import ctypes

ClAmsMgmtAdminOperT = clCommon.ClInt32T
class eClAmsMgmtAdminOperT(clUtils.Enum):
    CL_AMS_MGMT_ADMIN_OPER_UNLOCK = 0
    CL_AMS_MGMT_ADMIN_OPER_LOCKA = 1
    CL_AMS_MGMT_ADMIN_OPER_LOCKI = 2
    CL_AMS_MGMT_ADMIN_OPER_SHUTDOWN = 3
    CL_AMS_MGMT_ADMIN_OPER_RESTART = 4
    CL_AMS_MGMT_ADMIN_OPER_REPAIRED = 5
    CL_AMS_MGMT_ADMIN_OPER_SI_SWAP = 6
    CL_AMS_MGMT_ADMIN_OPER_MAX = 7

class ClAmsMgmtEntityAdminResponseT(ctypes.Structure):
    _fields_ = [
        ("mgmtHandle", clCommon.ClHandleT),
        ("clientHandle", clCommon.ClHandleT),
        ("oper", ClAmsMgmtAdminOperT),
        ("type", clAmsEntities.ClAmsEntityTypeT),
        ("retCode", clCommon.ClUint32T)
    ]

def clAmsMgmtEntityForceLock(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityForceLock(amsHandle, clUtils.byref(entity))

def clAmsMgmtEntityForceLockExtended(amsHandle, entity, lockFlags):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClUint32T lockFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityForceLockExtended(amsHandle, clUtils.byref(entity), lockFlags)
