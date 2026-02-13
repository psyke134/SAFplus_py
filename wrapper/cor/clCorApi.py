import sys
sys.path.append("..")

from utils import clLib, clUtils

def clCorClientInitialize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClientInitialize()


def clCorClientFinalize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClientFinalize()

def clCorClassCreate(classId, superClassId):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorClassTypeT superClassId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassCreate(classId, superClassId)


def clCorClassDelete(classId):
    """
    arg types:
        ClCorClassTypeT classId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassDelete(classId)


def clCorClassAttributeCreate(classId, attrId, attrType):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorAttrIdT attrId, 
        ClCorTypeT attrType
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassAttributeCreate(classId, attrId, attrType)


def clCorClassAttributeArrayCreate(classId, attrId, attrType, arraySize):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorAttrIdT attrId, 
        ClCorTypeT attrType, 
        ClInt32T arraySize
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassAttributeArrayCreate(classId, attrId, attrType, arraySize)


def clCorClassAttributeValueSet(classId, attrId, init_val, min_val, max_val):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorAttrIdT attrId, 
        ClInt64T init, 
        ClInt64T min, 
        ClInt64T max
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassAttributeValueSet(classId, attrId, init_val, min_val, max_val)


def clCorClassAttributeUserFlagsSet(classId, attrId, flags):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorAttrIdT attrId, 
        ClUint32T flags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassAttributeUserFlagsSet(classId, attrId, flags)


def clCorClassAttributeUserFlagsGet(classId, attrId, flags):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorAttrIdT attrId, 
        ClUint32T* flags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassAttributeUserFlagsGet(classId, attrId, clUtils.byref(flags))


def clCorClassAttributeTypeGet(classId, attrId, pAttrType):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorAttrIdT attrId, 
        ClCorAttrTypeT *pAttrType
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassAttributeTypeGet(classId, attrId, clUtils.byref(pAttrType))


def clCorClassAssociationCreate(classId, attrId, associatedClass, max_val):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorAttrIdT attrId, 
        ClCorClassTypeT associatedClass, 
        ClInt32T max
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassAssociationCreate(classId, attrId, associatedClass, max_val)


def clCorClassContainmentAttributeCreate(classId, attrId, containedClass, min_val, max_val):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorAttrIdT attrId, 
        ClCorClassTypeT containedClass, 
        ClInt32T min, 
        ClInt32T max
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassContainmentAttributeCreate(classId, attrId, containedClass, min_val, max_val)


def clCorClassAttributeDelete(classId, attrId):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorAttrIdT attrId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassAttributeDelete(classId, attrId)

def clCorClassNameSet(classId, name):
    """
    arg types:
        ClCorClassTypeT classId, 
        char* name
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassNameSet(classId, clUtils.toCharP(name))


def clCorClassNameGet(classId, name, size):
    """
    arg types:
        ClCorClassTypeT classId, 
        char *name, 
        ClUint32T* size
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassNameGet(classId, clUtils.toCharP(name), clUtils.byref(size))


def clCorClassTypeFromNameGet(name, classId):
    """
    arg types:
        char *name, 
        ClCorClassTypeT *classId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassTypeFromNameGet(clUtils.toCharP(name), clUtils.byref(classId))


def clCorClassAttributeNameGet(classId, attrId, name, size):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorAttrIdT attrId, 
        char *name, 
        ClUint32T* size
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassAttributeNameGet(classId, attrId, clUtils.toCharP(name), clUtils.byref(size))


def clCorClassAttributeNameSet(classId, attrId, name):
    """
    arg types:
        ClCorClassTypeT classId, 
        ClCorAttrIdT attrId, 
        char *name
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorClassAttributeNameSet(classId, attrId, clUtils.toCharP(name))

def clCorMOClassCreate(moPath, maxInstances):
    """
    arg types:
        ClCorMOClassPathPtrT moPath, 
        ClInt32T maxInstances
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorMOClassCreate(moPath, maxInstances)


def clCorMOClassDelete(moPath):
    """
    arg types:
        ClCorMOClassPathPtrT moPath
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorMOClassDelete(moPath)


def clCorMSOClassCreate(moPath, svcId, classId):
    """
    arg types:
        ClCorMOClassPathPtrT moPath, 
        ClCorServiceIdT svcId, 
        ClCorClassTypeT classId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorMSOClassCreate(moPath, svcId, classId)


def clCorMSOClassExist(moPath, svcId):
    """
    arg types:
        ClCorMOClassPathPtrT moPath, 
        ClCorServiceIdT svcId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorMSOClassExist(moPath, svcId)


def clCorMSOClassDelete(moPath, svcId):
    """
    arg types:
        ClCorMOClassPathPtrT moPath, 
        ClCorServiceIdT svcId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorMSOClassDelete(moPath, svcId)


def clCorMOClassExist(moPath):
    """
    arg types:
        ClCorMOClassPathPtrT moPath
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorMOClassExist(moPath)


def clCorMOPathToClassIdGet(pPath, svcId, pClassId):
    """
    arg types:
        ClCorMOClassPathPtrT pPath, 
        ClCorServiceIdT svcId, 
        ClCorClassTypeT* pClassId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorMOPathToClassIdGet(pPath, svcId, clUtils.byref(pClassId))

def clCorSubTreeDelete(moId):
    """
    arg types:
        ClCorMOIdT moId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorSubTreeDelete(moId)


def clCorObjectFlagsSet(moh, flags):
    """
    arg types:
        ClCorMOIdPtrT moh, 
        ClCorObjFlagsT flags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectFlagsSet(moh, flags)


def clCorObjectFlagsGet(moh, pFlags):
    """
    arg types:
        ClCorMOIdPtrT moh, 
        ClCorObjFlagsT* pFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectFlagsGet(moh, clUtils.byref(pFlags))

def clCorServiceAdd(id, mspName, comm):
    """
    arg types:
        ClCorServiceIdT id, 
        char *mspName, 
        ClCorCommInfoPtrT comm
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorServiceAdd(id, clUtils.toCharP(mspName), comm)


def clCorMoIdToComponentAddressGet(moh, addr):
    """
    arg types:
        ClCorMOIdPtrT moh, 
        ClCorAddrT* addr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorMoIdToComponentAddressGet(moh, clUtils.byref(addr))

def clCorServiceRuleDisable(moId, addr):
    """
    arg types:
        ClCorMOIdPtrT moId, 
        ClCorAddrT addr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorServiceRuleDisable(moId, addr)


def clCorServiceRuleStatusGet(moId, addr, status):
    """
    arg types:
        ClCorMOIdPtrT moId, 
        ClCorAddrT addr, 
        ClInt8T *status
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorServiceRuleStatusGet(moId, addr, clUtils.byref(status))


def clCorServiceRuleDeleteAll(srvcId, addr):
    """
    arg types:
        ClCorServiceIdT srvcId, 
        ClCorAddrT addr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorServiceRuleDeleteAll(srvcId, addr)


def clCorOIRegisterAndDisable(pMoId, addr):
    """
    arg types:
        ClCorMOIdPtrT pMoId, 
        ClCorAddrT addr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorOIRegisterAndDisable(pMoId, addr)

def clCorObjAttrInfoGet(objH, pAttrPath, attrId, attrType, arrDataType, attrSize, userFlags):
    """
    arg types:
        ClCorObjectHandleT objH, 
        ClCorAttrPathPtrT pAttrPath, 
        ClCorAttrIdT attrId,
        ClCorTypeT *attrType, 
        ClCorAttrTypeT *arrDataType, 
        ClUint32T *attrSize, 
        ClUint32T *userFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjAttrInfoGet(objH, pAttrPath, attrId, clUtils.byref(attrType), clUtils.byref(arrDataType), clUtils.byref(attrSize), clUtils.byref(userFlags))


def clCorObjectCreate(txnSessionId, moId, handle):
    """
    arg types:
        ClCorTxnSessionIdT *txnSessionId, 
        ClCorMOIdPtrT moId, 
        ClCorObjectHandleT *handle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectCreate(clUtils.byref(txnSessionId), moId, clUtils.byref(handle))


def clCorObjectAttributeSet(txnSessionId, pHandle, contAttrPath, attrId, index, value, size):
    """
    arg types:
        ClCorTxnSessionIdT *txnSessionId, 
        ClCorObjectHandleT pHandle, 
        ClCorAttrPathPtrT contAttrPath, 
        ClCorAttrIdT attrId, 
        ClUint32T index, 
        void *value, 
        ClUint32T size
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectAttributeSet(clUtils.byref(txnSessionId), pHandle, contAttrPath, attrId, index, value, size)

def clCorObjectDelete(txnSessionId, handle):
    """
    arg types:
        ClCorTxnSessionIdT *txnSessionId,
        ClCorObjectHandleT handle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectDelete(clUtils.byref(txnSessionId), handle)


def clCorObjectAttributeGet(pHandle, contAttrPath, attrId, index, value, size):
    """
    arg types:
        ClCorObjectHandleT pHandle,
        ClCorAttrPathPtrT contAttrPath,
        ClCorAttrIdT attrId,
        ClInt32T index, void *value,
        ClUint32T *size
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectAttributeGet(pHandle, contAttrPath, attrId, index, value, clUtils.byref(size))


def clCorObjectCreateAndSet(tid, pMoId, attrList, pHandle):
    """
    arg types:
        ClCorTxnSessionIdT* tid,
        ClCorMOIdPtrT pMoId,
        ClCorAttributeValueListPtrT attrList,
        ClCorObjectHandleT* pHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectCreateAndSet(clUtils.byref(tid), pMoId, attrList, clUtils.byref(pHandle))


def clCorObjectHandleGet(pMoId, objHandle):
    """
    arg types:
        ClCorMOIdPtrT pMoId,
        ClCorObjectHandleT *objHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectHandleGet(pMoId, clUtils.byref(objHandle))


def clCorObjectHandleFree(pObjH):
    """
    arg types:
        ClCorObjectHandleT* pObjH
    return type: void
    """
    return clLib.libmw_so.clCorObjectHandleFree(clUtils.byref(pObjH))


def clCorObjectHandleSizeGet(objH, pSize):
    """
    arg types:
        ClCorObjectHandleT objH,
        ClUint16T* pSize
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectHandleSizeGet(objH, clUtils.byref(pSize))

def clCorObjectWalk(moIdRoot, moIdFilter, fp, flags, cookie):
    """
    arg types:
        ClCorMOIdPtrT moIdRoot,
        ClCorMOIdPtrT moIdFilter,
        ClCorObjectWalkFunT fp,
        ClCorObjWalkFlagsT flags,
        void *cookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectWalk(moIdRoot, moIdFilter, fp, flags, cookie)


def clCorObjectAttributeWalk(objH, pFilter, fp, cookie):
    """
    arg types:
        ClCorObjectHandleT objH,
        ClCorObjAttrWalkFilterT *pFilter,
        ClCorObjAttrWalkFuncT fp,
        void * cookie
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectAttributeWalk(objH, clUtils.byref(pFilter), fp, cookie)


def clCorObjectHandleToTypeGet(pHandle, type_out):
    """
    arg types:
        ClCorObjectHandleT pHandle,
        ClCorObjTypesT* type
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectHandleToTypeGet(pHandle, clUtils.byref(type_out))


def clCorObjectHandleServiceSet(objH, svcId):
    """
    arg types: 
        ClCorObjectHandleT objH,
        ClCorServiceIdT svcId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectHandleServiceSet(objH, svcId)


def clCorObjectHandleToMoIdGet(objHandle, moId, srvcId):
    """
    arg types:
        ClCorObjectHandleT objHandle,
        ClCorMOIdPtrT moId,
        ClCorServiceIdT *srvcId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorObjectHandleToMoIdGet(objHandle, moId, clUtils.byref(srvcId))


def clCorMoIdToObjectHandleGet(pMoId, pObjH):
    """
    arg types:
        ClCorMOIdPtrT pMoId,
        ClCorObjectHandleT* pObjH
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorMoIdToObjectHandleGet(pMoId, clUtils.byref(pObjH))

def clCorMoIdToLogicalSlotGet(pMoId, logicalSlot):
    """
    arg types:
        ClCorMOIdPtrT pMoId,
        ClUint32T* logicalSlot
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorMoIdToLogicalSlotGet(pMoId, clUtils.byref(logicalSlot))


def clCorLogicalSlotToMoIdGet(logicalSlot, pMoId):
    """
    arg types:
        ClUint32T logicalSlot,
        ClCorMOIdPtrT pMoId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorLogicalSlotToMoIdGet(logicalSlot, pMoId)


def clCorMoIdToNodeNameGet(pMoId, nodeName):
    """
    arg types:
        ClCorMOIdPtrT pMoId,
        ClNameT* nodeName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorMoIdToNodeNameGet(pMoId, clUtils.byref(nodeName))


def clCorNodeNameToMoIdGet(nodeName, pMoId):
    """
    arg types:
        ClNameT nodeName,
        ClCorMOIdPtrT pMoId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorNodeNameToMoIdGet(nodeName, pMoId)


def clCorServiceRuleAdd(moh, addr):
    """
    arg types:
        ClCorMOIdPtrT moh,
        ClCorAddrT addr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorServiceRuleAdd(moh, addr)


def clCorServiceRuleDelete(moh, addr):
    """
    arg types:
        ClCorMOIdPtrT moh,
        ClCorAddrT addr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorServiceRuleDelete(moh, addr)

def clCorOIRegister(pMoId, pCompAaddr):
    """
    arg types:
        const ClCorMOIdPtrT pMoId,
        const ClCorAddrPtrT pCompAaddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorOIRegister(pMoId, pCompAaddr)


def clCorOIUnregister(pMoId, pCompAddr):
    """
    arg types:
        const ClCorMOIdPtrT pMoId,
        const ClCorAddrPtrT pCompAddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorOIUnregister(pMoId, pCompAddr)


def clCorPrimaryOISet(pMoId, pCompAddr):
    """
    arg types:
        const ClCorMOIdPtrT pMoId,
        const ClCorAddrPtrT pCompAddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorPrimaryOISet(pMoId, pCompAddr)


def clCorNIPrimaryOISet(pResource):
    """
    arg types:
        const ClCharT *pResource
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorNIPrimaryOISet(clUtils.byref(pResource))


def clCorPrimaryOIClear(pMoId, pCompAddr):
    """
    arg types:
        const ClCorMOIdPtrT pMoId,
        const ClCorAddrPtrT pCompAddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorPrimaryOIClear(pMoId, pCompAddr)


def clCorNIPrimaryOIClear(pResource):
    """
    arg types:
        const ClCharT *pResource
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorNIPrimaryOIClear(clUtils.toCharP(pResource))


def clCorPrimaryOIGet(pMoId, pCompAddr):
    """
    arg types:
        const ClCorMOIdPtrT pMoId,
        ClCorAddrPtrT pCompAddr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorPrimaryOIGet(pMoId, pCompAddr)

def clCorBundleInitialize(pBundleHandle, pBundleConfig):
    """
    arg types:
        ClCorBundleHandlePtrT pBundleHandle,
        ClCorBundleConfigPtrT pBundleConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorBundleInitialize(pBundleHandle, pBundleConfig)


def clCorBundleApplyAsync(bundleHandle, funcPtr, userArg):
    """
    arg types:
        ClCorBundleHandleT bundleHandle,
        ClCorBundleCallbackPtrT funcPtr,
        ClPtrT userArg
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorBundleApplyAsync(bundleHandle, funcPtr, userArg)


def clCorBundleApply(bundleHandle):
    """
    arg types:
        ClCorBundleHandleT bundleHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorBundleApply(bundleHandle)


def clCorBundleApplySync(bundleHandle):
    """
    arg types:
        ClCorBundleHandleT bundleHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorBundleApplySync(bundleHandle)


def clCorBundleFinalize(bundleHandle):
    """
    arg types:
        ClCorBundleHandleT bundleHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorBundleFinalize(bundleHandle)


def clCorBundleAttrValueSet(txnId, jobId, pValue):
    """
    arg types:
        ClCorTxnIdT txnId,
        ClCorTxnJobIdT jobId,
        ClPtrT *pValue
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorBundleAttrValueSet(txnId, jobId, clUtils.byref(pValue))


def clCorBundleObjectGet(bundleHandle, pObjectHandle, pAttrList):
    """
    arg types:
        ClCorBundleHandleT bundleHandle,
        const ClCorObjectHandleT *pObjectHandle,
        ClCorAttrValueDescriptorListPtrT pAttrList
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorBundleObjectGet(bundleHandle, clUtils.byref(pObjectHandle), pAttrList)

def clCorVersionCheck(version):
    """
    arg types:
        ClVersionT *version
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorVersionCheck(clUtils.byref(version))


def clCorNIAttrIdGet(classId, name, attrId):
    """
    arg types:
        ClCorClassTypeT classId,
        char *name,
        ClCorAttrIdT *attrId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCorNIAttrIdGet(classId, clUtils.toCharP(name), clUtils.byref(attrId))
