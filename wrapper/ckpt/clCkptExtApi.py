import sys
sys.path.append("..")

from common import clCommon
from ckpt import clCkptApi
from utils import clDifferenceVector, clLib, clUtils, libc, clHeapApi
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
    return clLib.libmw_so.clCkptLibraryInitialize(clUtils.byref(pCkptHdl))


def clCkptLibraryInitializeDB(pCkptHdl, dbName):
    """
    arg types:
        ClCkptSvcHdlT *pCkptHdl,
        const ClCharT *dbName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryInitializeDB(clUtils.byref(pCkptHdl), clUtils.toCharP(dbName))


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
    return clLib.libmw_so.clCkptLibraryCkptCreate(ckptHdl, clUtils.byref(pCkptName))


def clCkptLibraryCkptDelete(ckptHdl, pCkptName):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptDelete(ckptHdl, clUtils.byref(pCkptName))


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
    return clLib.libmw_so.clCkptLibraryCkptDataSetCreate(ckptHdl, clUtils.byref(pCkptName), dsId, grpId, order, dsSerialiser, dsDeserialiser)


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
    return clLib.libmw_so.clCkptLibraryCkptDataSetVersionCreate(ckptHdl, clUtils.byref(pCkptName), dsId, grpId, order, clUtils.byref(pTable), numTableEntries)


def clCkptLibraryCkptDataSetDelete(ckptHdl, pCkptName, dsId):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClUint32T dsId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryCkptDataSetDelete(ckptHdl, clUtils.byref(pCkptName), dsId)


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
    return clLib.libmw_so.clCkptLibraryCkptDataSetWrite(ckptHdl, clUtils.byref(pCkptName), dsId, cookie)


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
    return clLib.libmw_so.clCkptLibraryCkptDataSetVersionWrite(ckptHdl, clUtils.byref(pCkptName), dsId, cookie, clUtils.byref(pVersion))


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
    return clLib.libmw_so.clCkptLibraryCkptDataSetRead(ckptHdl, clUtils.byref(pCkptName), dsId, cookie)


def clCkptLibraryDoesCkptExist(ckptHdl, pCkptName, pRetVal):
    """
    arg types:
        ClCkptSvcHdlT ckptHdl,
        ClNameT *pCkptName,
        ClBoolT *pRetVal
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptLibraryDoesCkptExist(ckptHdl, clUtils.byref(pCkptName), clUtils.byref(pRetVal))


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
    return clLib.libmw_so.clCkptLibraryDoesDatasetExist(ckptHdl, clUtils.byref(pCkptName), dsId, clUtils.byref(pRetVal))


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
    return clLib.libmw_so.clCkptLibraryCkptElementCreate(ckptHdl, clUtils.byref(pCkptName), dsId, elemSerialiser, elemDeserialiser)


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
    return clLib.libmw_so.clCkptLibraryCkptElementVersionCreate(ckptHdl, clUtils.byref(pCkptName), dsId, clUtils.byref(pTable), numTableEntries)


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
    return clLib.libmw_so.clCkptLibraryCkptElementWrite(ckptHdl, clUtils.byref(pCkptName), dsId, elemId, elemLen, cookie)


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
    return clLib.libmw_so.clCkptLibraryCkptElementVersionWrite(ckptHdl, clUtils.byref(pCkptName), dsId, elemId, elemLen, cookie, clUtils.byref(pVersion))


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
    return clLib.libmw_so.clCkptLibraryCkptElementDelete(ckptHdl, clUtils.byref(pCkptName), dsId, elemId, elemLen)

CkptRelicaChangeCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, ctypes.POINTER(clCommon.ClNameT), clIocApi.ClIocNodeAddressT)

def clCkptReplicaChangeRegister(pCkptRelicaChangeCallback):
    """
    arg types:
        CkptRelicaChangeCallbackT pCkptRelicaChangeCallback
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
    return clLib.libmw_so.clCkptSectionOverwriteVector(ckptHdl, clUtils.byref(pSectionId), dataSize, clUtils.byref(differenceVector))


def clCkptCheckpointReadSections(ckptHdl, ppIOVecs, pNumVecs):
    """
    arg types:
        ClCkptHdlT ckptHdl,
        ClCkptIOVectorElementT **ppIOVecs,
        ClUint32T *pNumVecs
    return type:
        ClRcT
    """
    temp = ctypes.POINTER(libc.iovec)()
    rc = clLib.libmw_so.clCkptCheckpointReadSections(ckptHdl, clUtils.byref(temp), clUtils.byref(pNumVecs))
    if temp:
        ctypes.memmove(clUtils.byref(ppIOVecs), temp, ctypes.sizeof(libc.iovec))
        clCkptIOVectorFree(temp, clUtils.byref(pNumVecs))
        clHeapApi.clHeapFree(temp)
    return rc

def clCkptIOVectorFree(pIOVec, numVecs):
    """
    arg types:
        ClCkptIOVectorElementT *pIOVec,
        ClUint32T numVecs
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCkptIOVectorFree(pIOVec, numVecs)
