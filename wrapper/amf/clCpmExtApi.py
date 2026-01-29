import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils, clLib

import ctypes

class ClTargetSlotInfoT(ctypes.Structure):
    _fields_ = [
        ("name", clCommon.ClCharT * 80),
        ("addr", clCommon.ClUint32T),
        ("linkname", clCommon.ClCharT * 40),
        ("arch", clCommon.ClCharT * 80),
        ("customData", clCommon.ClCharT * 256)
    ]

class ClTargetInfoT(ctypes.Structure):
    _fields_ = [
        ("version", clCommon.ClCharT * 80),
        ("trapIp", clCommon.ClCharT * 40),
        ("installPrerequisites", clCommon.ClBoolT),
        ("instantiateImages", clCommon.ClBoolT),
        ("createTarballs", clCommon.ClBoolT),
        ("tipcNetid", clCommon.ClInt32T),
        ("gmsMcastPort", clCommon.ClInt32T),
        ("numSlots", clCommon.ClUint32T)
    ]

ClCpmSlotInfoFieldIdT = clCommon.ClInt32T
class eClCpmSlotInfoFieldIdT(clUtils.Enum):
    CL_CPM_SLOT_ID = 0
    CL_CPM_IOC_ADDRESS = 1
    CL_CPM_NODE_MOID = 2
    CL_CPM_NODENAME = 3

class ClCpmNodeConfigT(ctypes.Structure):
    _fields_ = [
        ("nodeName", clCommon.ClCharT * clCommon.CL_MAX_NAME_LENGTH),
        ("nodeType", clCommon.ClNameT),
        ("nodeIdentifier", clCommon.ClNameT),
        ("nodeMoIdStr", clCommon.ClNameT),
        ("cpmType", clCommon.ClCharT * clCommon.CL_MAX_NAME_LENGTH)
    ]

ClCpmEventTypeT = clCommon.ClInt32T
class eClCpmEventTypeT(clUtils.Enum):
    CL_CPM_COMP_EVENT = 0
    CL_CPM_NODE_EVENT = 1

def clCpmEventPayLoadExtract(eventHandle, eventDataSize, cpmEventType, payLoad):
    """
    arg types:
        ClEventHandleT eventHandle,
        ClSizeT eventDataSize,
        ClCpmEventTypeT cpmEventType,
        void *payLoad
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmEventPayLoadExtract(eventHandle, eventDataSize, cpmEventType, payLoad)


def clCpmComponentPIDGet(compName, pid):
    """
    arg types:
        ClNameT *compName,
        ClUint32T *pid
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentPIDGet(compName, pid)


def clCpmComponentPIDGetBySlot(slot, compName, pid):
    """
    arg types:
        ClIocNodeAddressT slot,
        ClNameT *compName,
        ClUint32T *pid
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentPIDGetBySlot(slot, compName, pid)


def clCpmSlotInfoGet(flag, slotInfo):
    """
    arg types:
        ClCpmSlotInfoFieldIdT flag,
        ClCpmSlotInfoT *slotInfo
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmSlotInfoGet(flag, slotInfo)


def clCpmSlotGet(flag, slotInfo):
    """
    arg types:
        ClCpmSlotInfoFieldIdT flag,
        ClCpmSlotInfoT *slotInfo
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmSlotGet(flag, slotInfo)


def clCpmIocAddressForNodeGet(nodeName, pIocAddress):
    """
    arg types:
        ClNameT nodeName,
        ClIocAddressT *pIocAddress
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmIocAddressForNodeGet(nodeName, pIocAddress)


def clCpmIsCompRestarted(compName):
    """
    arg types:
        ClNameT compName
    return type:
        ClBoolT
    """
    return clLib.libmw_so.clCpmIsCompRestarted(compName)


def clCpmNodeConfigSet(nodeConfig):
    """
    arg types:
        ClCpmNodeConfigT *nodeConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmNodeConfigSet(nodeConfig)


def clCpmNodeConfigGet(nodeName, nodeConfig):
    """
    arg types:
        ClCharT *nodeName,
        ClCpmNodeConfigT *nodeConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmNodeConfigGet(nodeName, nodeConfig)


def clCpmCompConfigSet(node, name, instantiateCommand, property, mask):
    """
    arg types:
        ClIocNodeAddressT node,
        ClCharT *name,
        ClCharT *instantiateCommand,
        ClAmsCompPropertyT property,
        ClUint64T mask
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmCompConfigSet(node, name, instantiateCommand, property, mask)


def clCpmComponentFailureReportWithCookie(cpmHandle, pCompName, instantiateCookie, errorDetectionTime, recommendedRecovery, alarmHandle):
    """
    arg types:
        ClCpmHandleT cpmHandle,
        ClNameT *pCompName,
        ClUint64T instantiateCookie,
        ClTimeT errorDetectionTime,
        ClAmsLocalRecoveryT recommendedRecovery,
        ClUint32T alarmHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmComponentFailureReportWithCookie(cpmHandle, pCompName, instantiateCookie, errorDetectionTime, recommendedRecovery, alarmHandle)


def clCpmTargetSlotInfoGet(name, addr, slotInfo):
    """
    arg types:
        ClCharT *name,
        ClIocNodeAddressT addr,
        ClTargetSlotInfoT *slotInfo
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmTargetSlotInfoGet(name, addr, slotInfo)


def clCpmTargetInfoGet(targetInfo):
    """
    arg types:
        ClTargetInfoT *targetInfo
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmTargetInfoGet(targetInfo)


def clCpmTargetSlotListGet(slotInfo, numSlots):
    """
    arg types:
        ClTargetSlotInfoT *slotInfo,
        ClUint32T *numSlots
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmTargetSlotListGet(slotInfo, numSlots)


def clCpmTargetVersionGet(aspVersion, maxBytes):
    """
    arg types:
        ClCharT *aspVersion,
        ClUint32T maxBytes
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCpmTargetVersionGet(aspVersion, maxBytes)


def clCpmIsSCCapable():
    """
    arg types:
        void
    return type:
        ClBoolT
    """
    return clLib.libmw_so.clCpmIsSCCapable()
