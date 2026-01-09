import sys
sys.path.append("..")

from common import clCommon
from ckpt import clCkptApi
from utils import clDifferenceVector, clLib
from ioc import clIocApi

import ctypes

ClCkptSerializeT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clCommon.ClUint32T,
    ctypes.POINTER(clCommon.ClAddrT),
    ctypes.POINTER(clCommon.ClUint32T),
    clCommon.ClPtrT
    )

ClCkptDeserializeT = ctypes.CFUNCTYPE(
    clCommon.ClRcT,
    clCommon.ClUint32T,
    clCommon.ClAddrT,
    clCommon.ClUint32T,
    clCommon.ClPtrT
)

class ClCkptDataSetCallback(ctypes.Structure):
    _fields_ = [
        ("version", clCommon.ClVersionT),
        ("serialiser", ClCkptSerializeT),
        ("deSerialiser", ClCkptDeserializeT)
    ]

class ClCkptDifferenceIOVectorElementT(ctypes.Structure):
    _fields_ = [
        ("sectionId", clCkptApi.ClCkptSectionIdT),
        ("dataSize", clCommon.ClSizeT),
        ("dataOffset", clCommon.ClOffsetT),
        ("differenceVector", ctypes.POINTER(clDifferenceVector.ClDifferenceVectorT))
    ]

class ClCkptClientInfoT(ctypes.Structure):
    _fields_ = [
        ("nodeAddress", clIocApi.ClIocNodeAddressT),
        ("portId", clIocApi.ClIocPortT)
    ]

class ClCkptClientInfoListT(ctypes.Structure):
    _fields_ = [
        ("numEntries", clCommon.ClUint32T),
        ("pClientInfo", ctypes.POINTER(ClCkptClientInfoT))
    ]

def clCkptLibraryInitialize(pCkptHdl):
    """
    arg types:
        ClCkptSvcHdlT *pCkptHdl
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryInitialize(pCkptHdl)


def clCkptLibraryInitializeDB(pCkptHdl, dbName):
    """
    arg types:
        ClCkptSvcHdlT *pCkptHdl,
        const ClCharT *dbName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryInitializeDB(pCkptHdl, dbName)


def clCkptLibraryFinalize(ckptHdl):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryFinalize(ckptHdl)


def clCkptLibraryCkptCreate(ckptHdl, pCkptName):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptCreate(ckptHdl, pCkptName)


def clCkptLibraryCkptDelete(ckptHdl, pCkptName):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptDelete(ckptHdl, pCkptName)


def clCkptLibraryCkptDataSetCreate(ckptHdl, pCkptName, dsId, grpId, order, dsSerialiser, dsDeserialiser):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId,
        ClUint32T grpId,
        ClUint32T order,
        ClCkptSerializeT dsSerialiser,
        ClCkptDeserializeT dsDeserialiser
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptDataSetCreate(ckptHdl, pCkptName, dsId, grpId, order, dsSerialiser, dsDeserialiser)


def clCkptLibraryCkptDataSetVersionCreate(ckptHdl, pCkptName, dsId, grpId, order, pTable, numTableEntries):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId,
        ClUint32T grpId,
        ClUint32T order,
        ClCkptDataSetCallbackT *pTable,
        ClUint32T numTableEntries
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptDataSetVersionCreate(ckptHdl, pCkptName, dsId, grpId, order, pTable, numTableEntries)


def clCkptLibraryCkptDataSetDelete(ckptHdl, pCkptName, dsId):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptDataSetDelete(ckptHdl, pCkptName, dsId)


def clCkptLibraryCkptDataSetWrite(ckptHdl, pCkptName, dsId, cookie):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId,
        ClPtrT cookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptDataSetWrite(ckptHdl, pCkptName, dsId, cookie)


def clCkptLibraryCkptDataSetVersionWrite(ckptHdl, pCkptName, dsId, cookie, pVersion):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId,
        ClPtrT cookie,
        ClVersionT *pVersion
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptDataSetVersionWrite(ckptHdl, pCkptName, dsId, cookie, pVersion)


def clCkptLibraryCkptDataSetRead(ckptHdl, pCkptName, dsId, cookie):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId,
        ClPtrT cookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptDataSetRead(ckptHdl, pCkptName, dsId, cookie)


def clCkptLibraryDoesCkptExist(ckptHdl, pCkptName, pRetVal):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClBoolT *pRetVal
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryDoesCkptExist(ckptHdl, pCkptName, pRetVal)


def clCkptLibraryDoesDatasetExist(ckptHdl, pCkptName, dsId, pRetVal):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId,
        ClBoolT *pRetVal
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryDoesDatasetExist(ckptHdl, pCkptName, dsId, pRetVal)


def clCkptLibraryCkptElementCreate(ckptHdl, pCkptName, dsId, elemSerialiser, elemDeserialiser):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId,
        ClCkptSerializeT elemSerialiser,
        ClCkptDeserializeT elemDeserialiser
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptElementCreate(ckptHdl, pCkptName, dsId, elemSerialiser, elemDeserialiser)


def clCkptLibraryCkptElementVersionCreate(ckptHdl, pCkptName, dsId, pTable, numTableEntries):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId,
        ClCkptDataSetCallbackT *pTable,
        ClUint32T numTableEntries
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptElementVersionCreate(ckptHdl, pCkptName, dsId, pTable, numTableEntries)


def clCkptLibraryCkptElementWrite(ckptHdl, pCkptName, dsId, elemId, elemLen, cookie):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId,
        ClPtrT elemId,
        ClUint32T elemLen,
        ClPtrT cookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptElementWrite(ckptHdl, pCkptName, dsId, elemId, elemLen, cookie)


def clCkptLibraryCkptElementVersionWrite(ckptHdl, pCkptName, dsId, elemId, elemLen, cookie, pVersion):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId,
        ClPtrT elemId,
        ClUint32T elemLen,
        ClPtrT cookie,
        ClVersionT *pVersion
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptElementVersionWrite(ckptHdl, pCkptName, dsId, elemId, elemLen, cookie, pVersion)


def clCkptLibraryCkptElementDelete(ckptHdl, pCkptName, dsId, elemId, elemLen):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId,
        ClPtrT elemId,
        ClUint32T elemLen
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptElementDelete(ckptHdl, pCkptName, dsId, elemId, elemLen)


def clCkptReplicaChangeRegister(pCkptRelicaChangeCallback):
    """
    arg types:
        ClRcT (*pCkptRelicaChangeCallback)(const ClNameT *pCkptName, ClIocNodeAddressT replicaAddr)
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptReplicaChangeRegister(pCkptRelicaChangeCallback)


def clCkptReplicaChangeDeregister():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptReplicaChangeDeregister()


def clCkptSectionOverwriteVector(ckptHdl, pSectionId, dataSize, differenceVector):
    """
    arg types:
        ClCkptHdlT ckptHdl,
        const ClCkptSectionIdT *pSectionId,
        ClSizeT dataSize,
        ClDifferenceVectorT *differenceVector
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptSectionOverwriteVector(ckptHdl, pSectionId, dataSize, differenceVector)


def clCkptCheckpointReadSections(ckptHdl, ppIOVecs, pNumVecs):
    """
    arg types:
        ClCkptHdlT ckptHdl,
        ClCkptIOVectorElementT **ppIOVecs,
        ClUint32T *pNumVecs
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptCheckpointReadSections(ckptHdl, ppIOVecs, pNumVecs)


def clCkptIOVectorFree(pIOVec, numVecs):
    """
    arg types:
        ClCkptIOVectorElementT *pIOVec,
        ClUint32T numVecs
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptIOVectorFree(pIOVec, numVecs)
