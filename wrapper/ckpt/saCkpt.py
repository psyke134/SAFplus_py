import sys
sys.path.append("..")

from common import saAis
from utils import clUtils, clLib

import ctypes

SaCkptHandleT = saAis.SaUint64T
SaCkptCheckpointHandleT = saAis.SaUint64T
SaCkptSectionIterationHandleT = saAis.SaUint64T

SA_CKPT_WR_ALL_REPLICAS = 0x1
SA_CKPT_WR_ACTIVE_REPLICA = 0x2
SA_CKPT_WR_ACTIVE_REPLICA_WEAK = 0x4
SA_CKPT_CHECKPOINT_COLLOCATED = 0x8

SaCkptCheckpointCreationFlagsT = saAis.SaUint32T

class SaCkptCheckpointCreationAttributesT(ctypes.Structure):
    _fields_ = [
        ("creationFlags", SaCkptCheckpointCreationFlagsT),
        ("checkpointSize", saAis.SaSizeT),
        ("retentionDuration", saAis.SaTimeT),
        ("maxSections", saAis.SaUint32T),
        ("maxSectionSize", saAis.SaSizeT),
        ("maxSectionIdSize", saAis.SaSizeT)
    ]

SA_CKPT_CHECKPOINT_READ = 0x1
SA_CKPT_CHECKPOINT_WRITE = 0x2
SA_CKPT_CHECKPOINT_CREATE = 0x4

SaCkptCheckpointOpenFlagsT = saAis.SaUint32T

class SaCkptSectionIdT(ctypes.Structure):
    _fields_ = [
        ("idLen", saAis.SaUint16T),
        ("id", ctypes.POINTER(saAis.SaUint8T))
    ]
    def __init__(self, idStr):
        p_id = clUtils.toUint8P(idStr)
        super(SaCkptSectionIdT, self).__init__(len(idStr), p_id)

SA_CKPT_DEFAULT_SECTION_ID = lambda: SaCkptSectionIdT(0, None)
SA_CKPT_GENERATED_SECTION_ID = lambda: SaCkptSectionIdT(0, None)

class SaCkptSectionCreationAttributesT(ctypes.Structure):
    _fields_ = [
        ("sectionId", ctypes.POINTER(SaCkptSectionIdT)),
        ("expirationTime", saAis.SaTimeT)
    ]

SaCkptSectionStateT = saAis.SaInt32T
class eSaCkptSectionStateT(clUtils.CEnum):
    SA_CKPT_SECTION_VALID = 1,
    SA_CKPT_SECTION_CORRUPTED = 2

class SaCkptSectionDescriptorT(ctypes.Structure):
    _fields_ = [
        ("sectionId", SaCkptSectionIdT),
        ("expirationTime", saAis.SaTimeT),
        ("sectionSize", saAis.SaSizeT),
        ("sectionState", SaCkptSectionStateT),
        ("lastUpdate", saAis.SaTimeT)
    ]

SaCkptSectionsChosenT = saAis.SaInt32T
class eSaCkptSectionsChosenT(clUtils.CEnum):
    SA_CKPT_SECTIONS_FOREVER = 1,
    SA_CKPT_SECTIONS_LEQ_EXPIRATION_TIME = 2,
    SA_CKPT_SECTIONS_GEQ_EXPIRATION_TIME = 3,
    SA_CKPT_SECTIONS_CORRUPTED = 4,
    SA_CKPT_SECTIONS_ANY = 5

class SaCkptIOVectorElementT(ctypes.Structure):
    _fields_ = [
        ("sectionId", SaCkptSectionIdT),
        ("dataBuffer", ctypes.c_void_p),
        ("dataSize", saAis.SaSizeT),
        ("dataOffset", saAis.SaOffsetT),
        ("readSize", saAis.SaSizeT)
    ]

class SaCkptCheckpointDescriptorT(ctypes.Structure):
    _fields_ = [
        ("checkpointCreationAttributes", SaCkptCheckpointCreationAttributesT),
        ("numberOfSections", saAis.SaUint32T),
        ("memoryUsed", saAis.SaUint32T)
    ]

SaCkptCheckpointOpenCallbackT = ctypes.CFUNCTYPE(
    None,
    saAis.SaInvocationT,
    SaCkptCheckpointHandleT,
    saAis.SaAisErrorT
)

SaCkptCheckpointSynchronizeCallbackT = ctypes.CFUNCTYPE(
    None,
    saAis.SaInvocationT,
    saAis.SaAisErrorT
)

class SaCkptCallbacksT(ctypes.Structure):
    _fields_ = [
        ("saCkptCheckpointOpenCallback", SaCkptCheckpointOpenCallbackT),
        ("saCkptCheckpointSynchronizeCallback", SaCkptCheckpointSynchronizeCallbackT)
    ]

def saCkptInitialize(ckptHandle, callbacks, version):
    """
    arg types:
        SaCkptHandleT *ckptHandle, 
        SaCkptCallbacksT *callbacks,
        SaVersionT *version

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptInitialize(ckptHandle, callbacks, version)

def saCkptSelectionObjectGet(ckptHandle, selectionObject):
    """
    arg types:
        SaCkptHandleT ckptHandle,
        SaSelectionObjectT *selectionObject

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptSelectionObjectGet(ckptHandle, selectionObject)

def saCkptDispatch(ckptHandle, dispatchFlags):
    """
    arg types:
        SaCkptHandleT ckptHandle, 
        SaDispatchFlagsT dispatchFlags

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptDispatch(ckptHandle, dispatchFlags)

def saCkptFinalize(ckptHandle):
    """
    arg types:
        SaCkptHandleT ckptHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptFinalize(ckptHandle)

def saCkptCheckpointOpen(ckptHandle, ckeckpointName, checkpointCreationAttributes, checkpointOpenFlags, timeout, checkpointHandle):
    """
    arg types:
        SaCkptHandleT ckptHandle,
        SaNameT *ckeckpointName,
        SaCkptCheckpointCreationAttributesT *checkpointCreationAttributes,
        SaCkptCheckpointOpenFlagsT checkpointOpenFlags,
        SaTimeT timeout,
        SaCkptCheckpointHandleT *checkpointHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptCheckpointOpen(ckptHandle, ckeckpointName, checkpointCreationAttributes, checkpointOpenFlags, timeout, checkpointHandle)

def saCkptCheckpointOpenAsync(ckptHandle, invocation, ckeckpointName, checkpointCreationAttributes, checkpointOpenFlags):
    """
    arg types:
        SaCkptHandleT ckptHandle,
        SaInvocationT invocation,
        SaNameT *ckeckpointName,
        SaCkptCheckpointCreationAttributesT *checkpointCreationAttributes,
        SaCkptCheckpointOpenFlagsT checkpointOpenFlags

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptCheckpointOpenAsync(ckptHandle, invocation, ckeckpointName, checkpointCreationAttributes, checkpointOpenFlags)

def saCkptCheckpointClose(checkpointHandle):
    """
    arg types:
        SaCkptCheckpointHandleT checkpointHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptCheckpointClose(checkpointHandle)

def saCkptCheckpointUnlink(ckptHandle, checkpointName):
    """
    arg types:
        SaCkptHandleT ckptHandle, 
        SaNameT *checkpointName

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptCheckpointUnlink(ckptHandle, checkpointName)

def saCkptCheckpointRetentionDurationSet(checkpointHandle, retentionDuration):
    """
    arg types:
        SaCkptCheckpointHandleT checkpointHandle,
        SaTimeT retentionDuration

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptCheckpointRetentionDurationSet(checkpointHandle, retentionDuration)

def saCkptActiveReplicaSet(checkpointHandle):
    """
    arg types:
        SaCkptCheckpointHandleT checkpointHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptActiveReplicaSet(checkpointHandle)

def saCkptCheckpointStatusGet(checkpointHandle, checkpointStatus):
    """
    arg types:
        SaCkptCheckpointHandleT checkpointHandle,
        SaCkptCheckpointDescriptorT *checkpointStatus

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptCheckpointStatusGet(checkpointHandle, checkpointStatus)

def saCkptSectionCreate(checkpointHandle, sectionCreationAttributes, initialData, initialDataSize):
    """
    arg types:
        SaCkptCheckpointHandleT checkpointHandle,
        SaCkptSectionCreationAttributesT *sectionCreationAttributes,
        SaUint8T *initialData,
        SaSizeT initialDataSize

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptSectionCreate(checkpointHandle, sectionCreationAttributes, initialData, initialDataSize)

def saCkptSectionDelete(checkpointHandle, sectionId):
    """
    arg types:
        SaCkptCheckpointHandleT checkpointHandle,
        SaCkptSectionIdT *sectionId

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptSectionDelete(checkpointHandle, sectionId)

def saCkptSectionExpirationTimeSet(checkpointHandle, sectionId, expirationTime):
    """
    arg types:
        SaCkptCheckpointHandleT checkpointHandle,
        SaCkptSectionIdT* sectionId,
        SaTimeT expirationTime

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptSectionExpirationTimeSet(checkpointHandle, sectionId, expirationTime)

def saCkptSectionIterationInitialize(checkpointHandle, sectionsChosen, expirationTime, sectionIterationHandle):
    """
    arg types:
        SaCkptCheckpointHandleT checkpointHandle,
        SaCkptSectionsChosenT sectionsChosen,
        SaTimeT expirationTime,
        SaCkptSectionIterationHandleT *sectionIterationHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptSectionIterationInitialize(checkpointHandle, sectionsChosen, expirationTime, sectionIterationHandle)

def saCkptSectionIterationNext(sectionIterationHandle, sectionDescriptor):
    """
    arg types:
        SaCkptSectionIterationHandleT sectionIterationHandle,
        SaCkptSectionDescriptorT *sectionDescriptor

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptSectionIterationNext(sectionIterationHandle, sectionDescriptor)

def saCkptSectionIterationFinalize(sectionIterationHandle):
    """
    arg types:
        SaCkptSectionIterationHandleT sectionIterationHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptSectionIterationFinalize(sectionIterationHandle)

def saCkptCheckpointWrite(checkpointHandle, ioVector, numberOfElements, erroneousVectorIndex):
    """
    arg types:
        SaCkptCheckpointHandleT checkpointHandle,
        SaCkptIOVectorElementT *ioVector,
        SaUint32T numberOfElements,
        SaUint32T *erroneousVectorIndex

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptCheckpointWrite(checkpointHandle, ioVector, numberOfElements, erroneousVectorIndex)

def saCkptSectionOverwrite(checkpointHandle, sectionId, dataBuffer, dataSize):
    """
    arg types:
        SaCkptCheckpointHandleT checkpointHandle,
        SaCkptSectionIdT *sectionId,
        void *dataBuffer,
        SaSizeT dataSize

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptSectionOverwrite(checkpointHandle, sectionId, dataBuffer, dataSize)

def saCkptCheckpointRead(checkpointHandle, ioVector, numberOfElements, erroneousVectorIndex):
    """
    arg types:
        SaCkptCheckpointHandleT checkpointHandle,
        SaCkptIOVectorElementT *ioVector,
        SaUint32T numberOfElements,
        SaUint32T *erroneousVectorIndex

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptCheckpointRead(checkpointHandle, ioVector, numberOfElements, erroneousVectorIndex)

def saCkptCheckpointSynchronize(checkpointHandle, timeout):
    """
    arg types:
        SaCkptCheckpointHandleT ckeckpointHandle,
        SaTimeT timeout

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptCheckpointSynchronize(checkpointHandle, timeout)

def saCkptCheckpointSynchronizeAsync(checkpointHandle, invocation):
    """
    arg types:
        SaCkptCheckpointHandleT ckeckpointHandle,
        SaInvocationT invocation

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saCkptCheckpointSynchronizeAsync(checkpointHandle, invocation)
