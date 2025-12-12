import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils, clLib

import ctypes

CL_CKPT_WR_ALL_REPLICAS = 0X1
CL_CKPT_WR_ACTIVE_REPLICA = 0X2
CL_CKPT_WR_ACTIVE_REPLICA_WEAK = 0X4
CL_CKPT_CHECKPOINT_COLLOCATED = 0X8
CL_CKPT_DISTRIBUTED = 0X10
CL_CKPT_WR_ALL_SAFE = 0X20
CL_CKPT_ALL_OPEN_ARE_REPLICAS = 0x40
CL_CKPT_PEER_TO_PEER_REPLICA = 0x80
CL_CKPT_PEER_TO_PEER_CACHE_DISABLE = 0x100
CL_CKPT_CHECKPOINT_READ = 0X1
CL_CKPT_CHECKPOINT_WRITE = 0X2
CL_CKPT_CHECKPOINT_CREATE = 0X4

ClCkptSvcHdlT = clCommon.ClHandleT
ClCkptHdlT = clCommon.ClHandleT
ClCkptSecItrHdlT = clCommon.ClHandleT
ClCkptCreationFlagsT = clCommon.ClUint32T
ClCkptOpenFlagsT = clCommon.ClUint32T
ClCkptSelectionObjT = clCommon.ClUint32T

class ClCkptCheckpointCreationAttributesT(ctypes.Structure):
    _fields_ = [
        ("creationFlags", ClCkptCreationFlagsT),
        ("checkpointSize", clCommon.ClSizeT),
        ("retentionDuration", clCommon.ClTimeT),
        ("maxSections", clCommon.ClUint32T),
        ("maxSectionSize", clCommon.ClSizeT),
        ("maxSectionIdSize", clCommon.ClSizeT),
    ]

class ClCkptSectionIdT(ctypes.Structure):
    _fields_ = [
        ("idLen", clCommon.ClUint16T),
        ("id", ctypes.POINTER(clCommon.ClUint8T))
    ]

class ClCkptSectionCreationAttributesT(ctypes.Structure):
    _fields_ = [
        ("sectionId", ctypes.POINTER(ClCkptSectionIdT)),
        ("expirationTime", clCommon.ClTimeT)
    ]

ClCkptSectionStateT = clCommon.ClInt32T
class eClCkptSectionStateT(clUtils.CEnum):
    CL_CKPT_SECTION_VALID = 1,
    CL_CKPT_SECTION_CORRUPTED = 2

class ClCkptSectionDescriptorT(ctypes.Structure):
    _fields_ = [
        ("sectionId", ClCkptSectionIdT),
        ("expirationTime", clCommon.ClTimeT),
        ("sectionSize", clCommon.ClSizeT),
        ("sectionState", ClCkptSectionStateT),
        ("lastUpdate", clCommon.ClTimeT)
    ]

ClCkptSectionsChosenT = clCommon.ClInt32T
class eClCkptSectionsChosenT(clUtils.CEnum):
    CL_CKPT_SECTIONS_FOREVER = 1,
    CL_CKPT_SECTIONS_LEQ_EXPIRATION_TIME = 2,
    CL_CKPT_SECTIONS_GEQ_EXPIRATION_TIME = 3,
    CL_CKPT_SECTIONS_CORRUPTED = 4,
    CL_CKPT_SECTIONS_ANY = 5

class ClCkptIOVectorElementT(ctypes.Structure):
    _fields_ = [
        ("sectionId", ClCkptSectionIdT),
        ("dataBuffer", clCommon.ClPtrT),
        ("dataSize", clCommon.ClSizeT),
        ("dataOffset", clCommon.ClOffsetT),
        ("readSize", clCommon.ClSizeT)
    ]

class ClCkptCheckpointDescriptorT(ctypes.Structure):
    _fields_ = [
        ("checkpointCreationAttributes", ClCkptCheckpointCreationAttributesT),
        ("numberOfSections", clCommon.ClUint32T),
        ("memoryUsed", clCommon.ClUint32T)
    ]

ClCkptNotificationCallbackT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    ClCkptHdlT,
    ctypes.POINTER(clCommon.ClNameT),
    ctypes.POINTER(ClCkptIOVectorElementT),
    clCommon.ClUint32T,
    clCommon.ClPtrT
)

ClCkptCheckpointOpenCallbackT = ctypes.CFUNCTYPE(
    None,
    clCommon.ClInvocationT,
    ClCkptHdlT,
    clCommon.ClRcT
)

ClCkptCheckpointSynchronizeCallbackT = ctypes.CFUNCTYPE(
    None,
    clCommon.ClInvocationT,
    clCommon.ClRcT
)

class ClCkptCallbacksT(ctypes.Structure):
    _fields_ = [
        ("checkpointOpenCallback", ClCkptCheckpointOpenCallbackT),
        ("checkpointSynchronizeCallback", ClCkptCheckpointSynchronizeCallbackT)
    ]

def clCkptInitialize(ckptSvcHandle, callbacks, version):
    """
    arg types:
        ClCkptSvcHdlT *ckptSvcHandle,
        ClCkptCallbacksT *callbacks,
        ClVersionT *version
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptInitialize(ckptSvcHandle, callbacks, version)


def clCkptFinalize(ckptHandle):
    """
    arg types:
        ClCkptSvcHdlT ckptHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptFinalize(ckptHandle)


def clCkptCheckpointOpen(ckptHandle, ckeckpointName, checkpointCreationAttributes, checkpointOpenFlags, timeout, checkpointHandle):
    """
    arg types:
        ClCkptSvcHdlT ckptHandle,
        ClNameT *ckeckpointName,
        ClCkptCheckpointCreationAttributesT *checkpointCreationAttributes,
        ClCkptOpenFlagsT checkpointOpenFlags,
        ClTimeT timeout,
        ClCkptHdlT *checkpointHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptCheckpointOpen(ckptHandle, ckeckpointName, checkpointCreationAttributes, checkpointOpenFlags, timeout, checkpointHandle)


def clCkptCheckpointOpenAsync(ckptHandle, invocation, checkpointName, checkpoiNtCreationAttributes, checkpointOpenFlags):
    """
    arg types:
        ClCkptSvcHdlT ckptHandle,
        ClInvocationT invocation,
        ClNameT *checkpointName,
        ClCkptCheckpointCreationAttributesT *checkpoiNtCreationAttributes,
        ClCkptOpenFlagsT checkpointOpenFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptCheckpointOpenAsync(ckptHandle, invocation, checkpointName, checkpoiNtCreationAttributes, checkpointOpenFlags)


def clCkptCheckpointClose(checkpointHandle):
    """
    arg types:
        ClCkptHdlT checkpointHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptCheckpointClose(checkpointHandle)


def clCkptCheckpointDelete(ckptHandle, checkpointName):
    """
    arg types:
        ClCkptSvcHdlT ckptHandle,
        ClNameT *checkpointName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptCheckpointDelete(ckptHandle, checkpointName)


def clCkptCheckpointRetentionDurationSet(checkpointHandle, retentionDuration):
    """
    arg types:
        ClCkptHdlT checkpointHandle,
        ClTimeT retentionDuration
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptCheckpointRetentionDurationSet(checkpointHandle, retentionDuration)


def clCkptActiveReplicaSet(checkpointHandle):
    """
    arg types:
        ClCkptHdlT checkpointHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptActiveReplicaSet(checkpointHandle)


def clCkptCheckpointStatusGet(checkpointHandle, checkpointStatus):
    """
    arg types:
        ClCkptHdlT checkpointHandle,
        ClCkptCheckpointDescriptorT *checkpointStatus
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptCheckpointStatusGet(checkpointHandle, checkpointStatus)


def clCkptSectionCreate(checkpointHandle, sectionCreationAttributes, initialData, initialDataSize):
    """
    arg types:
        ClCkptHdlT checkpointHandle,
        ClCkptSectionCreationAttributesT *sectionCreationAttributes,
        ClUint8T *initialData,
        ClSizeT initialDataSize
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptSectionCreate(checkpointHandle, sectionCreationAttributes, initialData, initialDataSize)


def clCkptSectionDelete(checkpointHandle, sectionId):
    """
    arg types:
        ClCkptHdlT checkpointHandle,
        ClCkptSectionIdT *sectionId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptSectionDelete(checkpointHandle, sectionId)


def clCkptSectionExpirationTimeSet(checkpointHandle, sectionId, expirationTime):
    """
    arg types:
        ClCkptHdlT checkpointHandle,
        ClCkptSectionIdT* sectionId,
        ClTimeT expirationTime
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptSectionExpirationTimeSet(checkpointHandle, sectionId, expirationTime)


def clCkptSectionIterationInitialize(checkpointHandle, sectionsChosen, expirationTime, sectionIterationHandle):
    """
    arg types:
        ClCkptHdlT checkpointHandle,
        ClCkptSectionsChosenT sectionsChosen,
        ClTimeT expirationTime,
        ClHandleT *sectionIterationHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptSectionIterationInitialize(checkpointHandle, sectionsChosen, expirationTime, sectionIterationHandle)


def clCkptSectionIterationNext(sectionIterationHandle, sectionDescriptor):
    """
    arg types:
        ClHandleT sectionIterationHandle,
        ClCkptSectionDescriptorT *sectionDescriptor
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptSectionIterationNext(sectionIterationHandle, sectionDescriptor)


def clCkptSectionIterationFinalize(sectionIterationHandle):
    """
    arg types:
        ClHandleT sectionIterationHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptSectionIterationFinalize(sectionIterationHandle)


def clCkptCheckpointWrite(checkpointHandle, ioVector, numberOfElements, erroneousVectorIndex):
    """
    arg types:
        ClCkptHdlT checkpointHandle,
        ClCkptIOVectorElementT *ioVector,
        ClUint32T numberOfElements,
        ClUint32T *erroneousVectorIndex
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptCheckpointWrite(checkpointHandle, ioVector, numberOfElements, erroneousVectorIndex)


def clCkptSectionOverwrite(checkpointHandle, sectionId, dataBuffer, dataSize):
    """
    arg types:
        ClCkptHdlT checkpointHandle,
        ClCkptSectionIdT *sectionId,
        void *dataBuffer,
        ClSizeT dataSize
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptSectionOverwrite(checkpointHandle, sectionId, dataBuffer, dataSize)


def clCkptCheckpointRead(checkpointHandle, ioVector, numberOfElements, erroneousVectorIndex):
    """
    arg types:
        ClCkptHdlT checkpointHandle,
        ClCkptIOVectorElementT *ioVector,
        ClUint32T numberOfElements,
        ClUint32T *erroneousVectorIndex
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptCheckpointRead(checkpointHandle, ioVector, numberOfElements, erroneousVectorIndex)


def clCkptCheckpointSynchronize(ckeckpointHandle, timeout):
    """
    arg types:
        ClCkptHdlT ckeckpointHandle,
        ClTimeT timeout
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptCheckpointSynchronize(ckeckpointHandle, timeout)


def clCkptCheckpointSynchronizeAsync(checkpointHandle, invocation):
    """
    arg types:
        ClCkptHdlT checkpointHandle,
        ClInvocationT invocation
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptCheckpointSynchronizeAsync(checkpointHandle, invocation)


def clCkptImmediateConsumptionRegister(checkpointHandle, callback, pCookie):
    """
    arg types:
        ClCkptHdlT checkpointHandle,
        ClCkptNotificationCallbackT callback,
        ClPtrT pCookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptImmediateConsumptionRegister(checkpointHandle, callback, pCookie)


def clCkptSelectionObjectGet(ckptHandle, selectionObject):
    """
    arg types:
        ClCkptSvcHdlT ckptHandle,
        ClSelectionObjectT *selectionObject
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptSelectionObjectGet(ckptHandle, selectionObject)


def clCkptDispatch(ckptHandle, dispatchFlags):
    """
    arg types:
        ClCkptSvcHdlT ckptHandle,
        ClDispatchFlagsT dispatchFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptDispatch(ckptHandle, dispatchFlags)
