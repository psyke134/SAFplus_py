import sys
sys.path.append("..")

from utils import libc, clLib, clUtils, clHeapApi
from amf import clAmsEntities
from common import clCommonErrors

import ctypes

ASP_INSTALL_KEY = "ASP_INSTALL_INFO"

def CL_AMS_NAME_LENGTH_CHECK(entity):
    if entity.name.length == libc.strlen(entity.name.value):
        entity.name.length += 1

class ClAmsMgmtCallbacksT(ctypes.Structure):
    _fields_ = [
        ("nothingForNow", ctypes.c_int)
    ]

def clAmsMgmtInitialize(amsHandle, amsMgmtCallbacks, version):
    """
    arg types:
        ClAmsMgmtHandleT  *amsHandle,
        ClAmsMgmtCallbacksT  *amsMgmtCallbacks,
        ClVersionT  *version
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtInitialize(clUtils.byref(amsHandle), clUtils.byref(amsMgmtCallbacks), clUtils.byref(version))

def clAmsMgmtFinalize(amsHandle):
    """
    arg types:
        ClAmsMgmtHandleT  amsHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtFinalize(amsHandle)

def clAmsMgmtEntityLockAssignment(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityLockAssignment(amsHandle, clUtils.byref(entity))

def clAmsMgmtEntityLockAssignmentExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityLockAssignmentExtended(amsHandle, entity, clUtils.byref(retry))

def clAmsMgmtEntityLockInstantiation(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityLockInstantiation(amsHandle, clUtils.byref(entity))

def clAmsMgmtEntityLockInstantiationExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityLockInstantiationExtended(amsHandle, entity, clUtils.byref(retry))

def clAmsMgmtEntityForceLockInstantiation(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityForceLockInstantiation(amsHandle, clUtils.byref(entity))

def clAmsMgmtEntityForceLockInstantiationExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityForceLockInstantiationExtended(amsHandle, clUtils.byref(entity), retry)

def clAmsMgmtEntityUnlock(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUnlock(amsHandle, clUtils.byref(entity))

def clAmsMgmtEntityUnlockExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUnlockExtended(amsHandle, entity, clUtils.byref(retry))

def clAmsMgmtEntityShutdown(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityShutdown(amsHandle, clUtils.byref(entity))

def clAmsMgmtEntityShutdownExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityShutdownExtended(amsHandle, clUtils.byref(entity), retry)

def clAmsMgmtEntityRestart(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityRestart(amsHandle, clUtils.byref(entity))

def clAmsMgmtEntityRestartExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityRestartExtended(amsHandle, clUtils.byref(entity), retry)

def clAmsMgmtEntityRepaired(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityRepaired(amsHandle, clUtils.byref(entity))

def clAmsMgmtEntityRepairedExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityRepairedExtended(amsHandle, clUtils.byref(entity), retry)

def clAmsMgmtSISwap(amsHandle, si):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClCharT *si
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtSISwap(amsHandle, clUtils.toCharP(si))

def clAmsMgmtSISwapExtended(amsHandle, si, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClCharT *si,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtSISwapExtended(amsHandle, clUtils.toCharP(si), retry)

def clAmsMgmtSGAdjust(amsHandle, sg, enable):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClCharT *sg,
        ClBoolT enable
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtSGAdjust(amsHandle, clUtils.toCharP(sg), enable)

def clAmsMgmtSGAdjustExtended(amsHandle, sg, enable, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClCharT *sg,
        ClBoolT enable,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtSGAdjustExtended(amsHandle, clUtils.toCharP(sg), enable, retry)

def clAmsMgmtDebugEnable(amsHandle, entity, debugFlags):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClUint8T  debugFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDebugEnable(amsHandle, clUtils.byref(entity), debugFlags)

def clAmsMgmtDebugDisable(amsHandle, entity, debugFlags):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClUint8T  debugFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDebugDisable(amsHandle, clUtils.byref(entity), debugFlags)

def clAmsMgmtDebugGet(amsHandle, entity, debugFlags):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClUint8T *debugFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDebugGet(amsHandle, clUtils.byref(entity), clUtils.byref(debugFlags))

def clAmsMgmtDebugEnableLogToConsole(amsHandle):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDebugEnableLogToConsole(amsHandle)

def clAmsMgmtDebugDisableLogToConsole(amsHandle):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDebugDisableLogToConsole(amsHandle)

def clAmsMgmtEntitySetAlphaFactor(amsHandle, entity, alphaFactor):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClUint32T alphaFactor
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntitySetAlphaFactor(amsHandle, clUtils.byref(entity), alphaFactor)

def clAmsMgmtEntitySetBetaFactor(amsHandle, entity, betaFactor):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClUint32T betaFactor
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntitySetBetaFactor(amsHandle, clUtils.byref(entity), betaFactor)

def clAmsMgmtCCBInitialize(amlHandle, ccbHandle):
    """
    arg types:
        ClAmsMgmtHandleT amlHandle,
        ClAmsMgmtCCBHandleT *ccbHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBInitialize(amlHandle, clUtils.byref(ccbHandle))

def clAmsMgmtCCBFinalize(ccbHandle):
    """
    arg types:
        ClAmsMgmtCCBHandleT ccbHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBFinalize(ccbHandle)

def clAmsMgmtCCBCommit(ccbHandle):
    """
    arg types:
        ClAmsMgmtCCBHandleT ccbHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBCommit(ccbHandle)

def clAmsMgmtCCBEntityCreate(handle, entity):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBEntityCreate(handle, clUtils.byref(entity))

def clAmsMgmtCCBEntityDelete(handle, entity):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBEntityDelete(handle, clUtils.byref(entity))

def clAmsMgmtCCBEntitySetConfig(handle, entityConfig, bitMask):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityConfigT *entityConfig,
        ClUint64T bitMask
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBEntitySetConfig(handle, clUtils.byref(entityConfig), bitMask)

def clAmsMgmtCCBCSISetNVP(handle, csiName, nvp):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *csiName,
        ClAmsCSINVPT *nvp
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBCSISetNVP(handle, clUtils.byref(csiName), clUtils.byref(nvp))

def clAmsMgmtCCBCSIDeleteNVP(handle, csiName, nvp):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *csiName,
        ClAmsCSINVPT *nvp
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBCSIDeleteNVP(handle, clUtils.byref(csiName), clUtils.byref(nvp))

def clAmsMgmtCCBSetNodeDependency(handle, nodeName, dependencyNodeName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *dependencyNodeName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetNodeDependency(handle, clUtils.byref(nodeName), clUtils.byref(dependencyNodeName))

def clAmsMgmtCCBDeleteNodeDependency(handle, nodeName, dependencyNodeName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *dependencyNodeName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteNodeDependency(handle, clUtils.byref(nodeName), clUtils.byref(dependencyNodeName))

def clAmsMgmtCCBSetNodeSUList(handle, nodeName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetNodeSUList(handle, clUtils.byref(nodeName), clUtils.byref(suName))

def clAmsMgmtCCBDeleteNodeSUList(handle, nodeName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteNodeSUList(handle, clUtils.byref(nodeName), clUtils.byref(suName))

def clAmsMgmtCCBSetSGSUList(handle, sgName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSGSUList(handle, clUtils.byref(sgName), clUtils.byref(suName))

def clAmsMgmtCCBDeleteSGSUList(handle, sgName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSGSUList(handle, clUtils.byref(sgName), clUtils.byref(suName))

def clAmsMgmtCCBSetSGSIList(handle, sgName, siName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *siName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSGSIList(handle, clUtils.byref(sgName), clUtils.byref(siName))

def clAmsMgmtCCBDeleteSGSIList(handle, sgName, siName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *siName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSGSIList(handle, clUtils.byref(sgName), clUtils.byref(siName))

def clAmsMgmtCCBSetSUCompList(handle, suName, compName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *suName,
        ClAmsEntityT *compName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSUCompList(handle, clUtils.byref(suName), clUtils.byref(compName))

def clAmsMgmtCCBDeleteSUCompList(handle, suName, compName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *suName,
        ClAmsEntityT *compName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSUCompList(handle, clUtils.byref(suName), clUtils.byref(compName))

def clAmsMgmtCCBSetSISURankList(handle, siName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSISURankList(handle, clUtils.byref(siName), clUtils.byref(suName))

def clAmsMgmtCCBDeleteSISURankList(handle, siName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSISURankList(handle, clUtils.byref(siName), clUtils.byref(suName))

def clAmsMgmtCCBSetSIDependency(handle, siName, dependencySIName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *dependencySIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSIDependency(handle, clUtils.byref(siName), clUtils.byref(dependencySIName))

def clAmsMgmtCCBDeleteSIDependency(handle, siName, dependencySIName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *dependencySIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSIDependency(handle, clUtils.byref(siName), clUtils.byref(dependencySIName))

def clAmsMgmtCCBSetCSIDependency(handle, csiName, dependencyCSIName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *csiName,
        ClAmsEntityT *dependencyCSIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetCSIDependency(handle, clUtils.byref(csiName), clUtils.byref(dependencyCSIName))

def clAmsMgmtCCBDeleteCSIDependency(handle, csiName, dependencyCSIName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *csiName,
        ClAmsEntityT *dependencyCSIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteCSIDependency(handle, clUtils.byref(csiName), clUtils.byref(dependencyCSIName))

def clAmsMgmtCCBSetSICSIList(handle, siName, csiName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *csiName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSICSIList(handle, clUtils.byref(siName), clUtils.byref(csiName))

def clAmsMgmtCCBDeleteSICSIList(handle, siName, csiName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *csiName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSICSIList(handle, clUtils.byref(siName), clUtils.byref(csiName))

def clAmsMgmtEntityGet(handle, entityRef):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityRefT *entityRef
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityGet(handle, clUtils.byref(entityRef))

def clAmsMgmtEntityGetConfig(handle, entity, entityConfig):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClAmsEntityConfigT **entityConfig
    return type:
        ClRcT
    """
    typeClassLut = {
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_NODE: clAmsEntities.ClAmsNodeConfigT,
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG: clAmsEntities.ClAmsSGConfigT,
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU: clAmsEntities.ClAmsSUConfigT,
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI: clAmsEntities.ClAmsSIConfigT,
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI: clAmsEntities.ClAmsCSIConfigT,
        clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP: clAmsEntities.ClAmsCompConfigT
    }

    expectedType = typeClassLut[entity.type.value]
    if not isinstance(entityConfig, expectedType):
        return clCommonErrors.CL_ERR_INVALID_PARAMETER

    pTemp = ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT)()
    rc = clLib.libmw_so.clAmsMgmtEntityGetConfig(handle, clUtils.byref(entity), clUtils.byref(pTemp))
    if pTemp:
        ctypes.memmove(ctypes.byref(entityConfig), pTemp, ctypes.sizeof(expectedType))
        clHeapApi.clHeapFree(pTemp)
    return rc

def clAmsMgmtNodeGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsNodeConfigT*
    """
    clLib.libmw_so.clAmsMgmtNodeGetConfig.restype = ctypes.POINTER(clAmsEntities.ClAmsNodeConfigT)
    return clLib.libmw_so.clAmsMgmtNodeGetConfig(handle, clUtils.toCharP(entName))

def clAmsMgmtServiceGroupGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSGConfigT*
    """
    clLib.libmw_so.clAmsMgmtServiceGroupGetConfig.restype = ctypes.POINTER(clAmsEntities.ClAmsSGConfigT)
    return clLib.libmw_so.clAmsMgmtServiceGroupGetConfig(handle, clUtils.toCharP(entName))

def clAmsMgmtServiceUnitGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSUConfigT*
    """
    clLib.libmw_so.clAmsMgmtServiceUnitGetConfig.restype = ctypes.POINTER(clAmsEntities.ClAmsSUConfigT)
    return clLib.libmw_so.clAmsMgmtServiceUnitGetConfig(handle, clUtils.toCharP(entName))

def clAmsMgmtServiceInstanceGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSIConfigT*
    """
    clLib.libmw_so.clAmsMgmtServiceInstanceGetConfig.restype = ctypes.POINTER(clAmsEntities.ClAmsSIConfigT)
    return clLib.libmw_so.clAmsMgmtServiceInstanceGetConfig(handle, clUtils.toCharP(entName))

def clAmsMgmtCompServiceInstanceGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsCSIConfigT*
    """
    clLib.libmw_so.clAmsMgmtCompServiceInstanceGetConfig.restype = ctypes.POINTER(clAmsEntities.ClAmsCSIConfigT)
    return clLib.libmw_so.clAmsMgmtCompServiceInstanceGetConfig(handle, clUtils.toCharP(entName))

def clAmsMgmtCompGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsCompConfigT*
    """
    clLib.libmw_so.clAmsMgmtCompGetConfig.restype = ctypes.POINTER(clAmsEntities.ClAmsCompConfigT)
    return clLib.libmw_so.clAmsMgmtCompGetConfig(handle, clUtils.toCharP(entName))

def clAmsMgmtEntityGetStatus(handle, entity, entityStatus):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClAmsEntityStatusT **entityStatus
    return type:
        ClRcT
    """
    pTemp = ctypes.POINTER(clAmsEntities.ClAmsEntityStatusT)()
    rc = clLib.libmw_so.clAmsMgmtEntityGetStatus(handle, clUtils.byref(entity), clUtils.byref(pTemp))
    if pTemp:
        ctypes.memmove(ctypes.byref(entityStatus), pTemp, ctypes.sizeof(clAmsEntities.ClAmsEntityStatusT))
        clHeapApi.clHeapFree(pTemp)
    return rc

def clAmsMgmtNodeGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsNodeStatusT*
    """
    clLib.libmw_so.clAmsMgmtNodeGetStatus.restype = ctypes.POINTER(clAmsEntities.ClAmsNodeStatusT)
    return clLib.libmw_so.clAmsMgmtNodeGetStatus(handle, clUtils.toCharP(entName))

def clAmsMgmtServiceGroupGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSGStatusT*
    """
    clLib.libmw_so.clAmsMgmtServiceGroupGetStatus.restype = ctypes.POINTER(clAmsEntities.ClAmsSGStatusT)
    return clLib.libmw_so.clAmsMgmtServiceGroupGetStatus(handle, clUtils.toCharP(entName))

def clAmsMgmtServiceUnitGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSUStatusT*
    """
    clLib.libmw_so.clAmsMgmtServiceUnitGetStatus.restype = ctypes.POINTER(clAmsEntities.ClAmsSUStatusT)
    return clLib.libmw_so.clAmsMgmtServiceUnitGetStatus(handle, clUtils.toCharP(entName))

def clAmsMgmtServiceInstanceGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSIStatusT*
    """
    clLib.libmw_so.clAmsMgmtServiceInstanceGetStatus.restype = ctypes.POINTER(clAmsEntities.ClAmsSIStatusT)
    return clLib.libmw_so.clAmsMgmtServiceInstanceGetStatus(handle, clUtils.toCharP(entName))

def clAmsMgmtCompServiceInstanceGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsCSIStatusT*
    """
    clLib.libmw_so.clAmsMgmtCompServiceInstanceGetStatus.restype = ctypes.POINTER(clAmsEntities.ClAmsCSIStatusT)
    return clLib.libmw_so.clAmsMgmtCompServiceInstanceGetStatus(handle, clUtils.toCharP(entName))

def clAmsMgmtCompGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsCompStatusT*
    """
    clLib.libmw_so.clAmsMgmtCompGetStatus.restype = ctypes.POINTER(clAmsEntities.ClAmsCompStatusT)
    return clLib.libmw_so.clAmsMgmtCompGetStatus(handle, clUtils.toCharP(entName))

def clAmsMgmtGetList(handle, listName, buffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityListTypeT listName,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetList(handle, listName, clUtils.byref(buffer))

def clAmsMgmtGetCSINVPList(handle, csi, nvpBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *csi,
        ClAmsCSINVPBufferT *nvpBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetCSINVPList(handle, clUtils.byref(csi), clUtils.byref(nvpBuffer))

def clAmsMgmtGetCSIDependenciesList(handle, csi, dependenciesCSIBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *csi,
        ClAmsEntityBufferT *dependenciesCSIBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetCSIDependenciesList(handle, clUtils.byref(csi), clUtils.byref(dependenciesCSIBuffer))

def clAmsMgmtGetSGList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGList(handle, clUtils.byref(entityBuffer))

def clAmsMgmtGetSIList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSIList(handle, clUtils.byref(entityBuffer))

def clAmsMgmtGetCSIList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetCSIList(handle, clUtils.byref(entityBuffer))

def clAmsMgmtGetNodeList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetNodeList(handle, clUtils.byref(entityBuffer))

def clAmsMgmtGetSUList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSUList(handle, clUtils.byref(entityBuffer))

def clAmsMgmtGetCompList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetCompList(handle, clUtils.byref(entityBuffer))

def clAmsMgmtGetNodeDependenciesList(handle, node, dependencyBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *node,
        ClAmsEntityBufferT *dependencyBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetNodeDependenciesList(handle, clUtils.byref(node), clUtils.byref(dependencyBuffer))

def clAmsMgmtGetNodeSUList(handle, node, suBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *node,
        ClAmsEntityBufferT *suBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetNodeSUList(handle, clUtils.byref(node), clUtils.byref(suBuffer))

def clAmsMgmtGetSGSUList(handle, sg, suBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *suBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGSUList(handle, clUtils.byref(sg), clUtils.byref(suBuffer))

def clAmsMgmtGetSGSIList(handle, sg, siBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *siBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGSIList(handle, clUtils.byref(sg), clUtils.byref(siBuffer))

def clAmsMgmtGetSUCompList(handle, su, compBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *su,
        ClAmsEntityBufferT *compBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSUCompList(handle, clUtils.byref(su), clUtils.byref(compBuffer))

def clAmsMgmtGetSISURankList(handle, si, suBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *si,
        ClAmsEntityBufferT *suBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSISURankList(handle, clUtils.byref(si), clUtils.byref(suBuffer))

def clAmsMgmtGetSIDependenciesList(handle, si, dependenciesSIBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *si,
        ClAmsEntityBufferT *dependenciesSIBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSIDependenciesList(handle, clUtils.byref(si), clUtils.byref(dependenciesSIBuffer))

def clAmsMgmtGetSICSIList(handle, si, csiBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *si,
        ClAmsEntityBufferT *csiBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSICSIList(handle, clUtils.byref(si), clUtils.byref(csiBuffer))

def clAmsMgmtGetSGInstantiableSUList(handle, sg, instantiableSUBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *instantiableSUBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGInstantiableSUList(handle, clUtils.byref(sg), clUtils.byref(instantiableSUBuffer))

def clAmsMgmtGetSGInstantiatedSUList(handle, sg, instantiatedSUBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *instantiatedSUBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGInstantiatedSUList(handle, clUtils.byref(sg), clUtils.byref(instantiatedSUBuffer))

def clAmsMgmtGetSGInServiceSpareSUList(handle, sg, inserviceSpareSUBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *inserviceSpareSUBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGInServiceSpareSUList(handle, clUtils.byref(sg), clUtils.byref(inserviceSpareSUBuffer))

def clAmsMgmtGetSGAssignedSUList(handle, sg, assignedSUBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *assignedSUBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGAssignedSUList(handle, clUtils.byref(sg), clUtils.byref(assignedSUBuffer))

def clAmsMgmtGetSGFaultySUList(handle, sg, faultySUBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *faultySUBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGFaultySUList(handle, clUtils.byref(sg), clUtils.byref(faultySUBuffer))

def clAmsMgmtGetSUAssignedSIsList(handle, su, siBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *su,
        ClAmsSUSIRefBufferT *siBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSUAssignedSIsList(handle, clUtils.byref(su), clUtils.byref(siBuffer))

def clAmsMgmtGetSUAssignedSIsExtendedList(handle, su, siBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *su,
        ClAmsSUSIExtendedRefBufferT *siBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSUAssignedSIsExtendedList(handle, clUtils.byref(su), clUtils.byref(siBuffer))

def clAmsMgmtGetSISUList(handle, si, suBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *si,
        ClAmsSISURefBufferT *suBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSISUList(handle, clUtils.byref(si), clUtils.byref(suBuffer))

def clAmsMgmtGetSISUExtendedList(handle, si, suBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *si,
        ClAmsSISUExtendedRefBufferT *suBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSISUExtendedList(handle, clUtils.byref(si), clUtils.byref(suBuffer))

def clAmsMgmtGetCompCSIList(handle, comp, csiBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *comp,
        ClAmsCompCSIRefBufferT *csiBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetCompCSIList(handle, clUtils.byref(comp), clUtils.byref(csiBuffer))

def clAmsMgmtGetSIHAState(handle, si, su, haState, fullyAssigned):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *si,
        ClCharT *su,
        ClAmsHAStateT *haState,
        ClBoolT *fullyAssigned
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSIHAState(handle, clUtils.toCharP(si), clUtils.toCharP(su), haState, clUtils.byref(fullyAssigned))

def clAmsMgmtGetSUHAState(handle, su, checkAllSIs, haState, fullyAssigned):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *su,
        ClBoolT checkAllSIs,
        ClAmsHAStateT *haState,
        ClBoolT *fullyAssigned
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSUHAState(handle, clUtils.toCharP(su), checkAllSIs, clUtils.byref(haState), clUtils.byref(fullyAssigned))

def clAmsMgmtMigrateSG(handle, sg, prefix, activeSUs, standbySUs, migrateList):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *sg,
        ClCharT *prefix,
        ClUint32T activeSUs,
        ClUint32T standbySUs,
        ClAmsMgmtMigrateListT *migrateList
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtMigrateSG(handle, clUtils.toCharP(sg), clUtils.toCharP(prefix), activeSUs, standbySUs, clUtils.byref(migrateList))

def clAmsMgmtEntityUserDataSet(handle, entity, data, len):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClCharT *data,
        ClUint32T len
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataSet(handle, clUtils.byref(entity), clUtils.toCharP(data), len)

def clAmsMgmtEntityUserDataSetKey(handle, entity, key, data, len):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClNameT *key,
        ClCharT *data,
        ClUint32T len
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataSetKey(handle, clUtils.byref(entity), clUtils.byref(key), clUtils.toCharP(data), len)

def clAmsMgmtEntityUserDataGet(handle, entity, data, len):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClCharT **data,
        ClUint32T *len
    return type:
        ClRcT
    Note: free data later using clHeapFree()
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataGet(handle, clUtils.byref(entity), clUtils.byref(data), clUtils.byref(len))

def clAmsMgmtEntityUserDataGetKey(handle, entity, key, data, len):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClNameT *key,
        ClCharT **data,
        ClUint32T *len
    return type:
        ClRcT
    Note: free data later using clHeapFree()
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataGetKey(handle, clUtils.byref(entity), clUtils.byref(key), clUtils.byref(data), clUtils.byref(len))

def clAmsMgmtEntityUserDataDelete(handle, entity):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataDelete(handle, clUtils.byref(entity))

def clAmsMgmtEntityUserDataDeleteKey(handle, entity, key):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClNameT *key
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataDeleteKey(handle, clUtils.byref(entity), clUtils.byref(key))

def clAmsMgmtEntityUserDataDeleteAll(handle, entity):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataDeleteAll(handle, clUtils.byref(entity))

def clAmsMgmtSetActive(handle, entity, activeSU):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClAmsEntityT *activeSU
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtSetActive(handle, clUtils.byref(entity), clUtils.byref(activeSU))

def clAmsMgmtSIAssignSU(si, activeSU, standbySU):
    """
    arg types:
        ClCharT *si,
        ClCharT *activeSU,
        ClCharT *standbySU
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtSIAssignSU(clUtils.toCharP(si), clUtils.toCharP(activeSU), clUtils.toCharP(standbySU))


def clAmsMgmtGetAspInstallInfo(handle, nodeName, aspInstallInfo, len):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *nodeName,
        ClCharT *aspInstallInfo,
        ClUint32T len
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetAspInstallInfo(handle, clUtils.toCharP(nodeName), clUtils.toCharP(aspInstallInfo), len)


def clAmsMgmtFreeCompCSIRefBuffer(buffer):
    """
    arg types:
        ClAmsCompCSIRefBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtFreeCompCSIRefBuffer(clUtils.byref(buffer))


def clAmsMgmtDBGet(db):
    """
    arg types:
        ClAmsMgmtDBHandleT *db
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGet(clUtils.byref(db))


def clAmsMgmtDBGetNodeList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetNodeList(db, clUtils.byref(buffer))


def clAmsMgmtDBGetSUList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSUList(db, clUtils.byref(buffer))


def clAmsMgmtDBGetSGList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSGList(db, clUtils.byref(buffer))


def clAmsMgmtDBGetSIList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSIList(db, clUtils.byref(buffer))


def clAmsMgmtDBGetCSIList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetCSIList(db, clUtils.byref(buffer))

def clAmsMgmtDBGetCompList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetCompList(db, clUtils.byref(buffer))


def clAmsMgmtDBGetEntityConfig(db, entity, entityConfig):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityConfigT **entityConfig
    return type:
        ClRcT
    """
    pTemp = ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT)()
    rc = clLib.libmw_so.clAmsMgmtDBGetEntityConfig(db, clUtils.byref(entity), clUtils.byref(pTemp))
    if pTemp:
        ctypes.memmove(ctypes.byref(entityConfig), pTemp, ctypes.sizeof(clAmsEntities.ClAmsEntityConfigT))
        clHeapApi.clHeapFree(pTemp)
    return rc


def clAmsMgmtDBGetEntityStatus(db, entity, entityStatus):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityStatusT **entityStatus
    return type:
        ClRcT
    """
    pTemp = ctypes.POINTER(clAmsEntities.ClAmsEntityStatusT)()
    rc = clLib.libmw_so.clAmsMgmtDBGetEntityStatus(db, clUtils.byref(entity), clUtils.byref(pTemp))
    if pTemp:
        ctypes.memmove(ctypes.byref(entityStatus), pTemp, ctypes.sizeof(clAmsEntities.ClAmsEntityStatusT))
        clHeapApi.clHeapFree(pTemp)
    return rc


def clAmsMgmtDBGetNodeSUList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetNodeSUList(db, clUtils.byref(entity), clUtils.byref(buffer))


def clAmsMgmtDBGetSGSUList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSGSUList(db, clUtils.byref(entity), clUtils.byref(buffer))


def clAmsMgmtDBGetSGSIList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSGSIList(db, clUtils.byref(entity), clUtils.byref(buffer))


def clAmsMgmtDBGetSICSIList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSICSIList(db, clUtils.byref(entity), clUtils.byref(buffer))

def clAmsMgmtDBGetSUCompList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSUCompList(db, clUtils.byref(entity), clUtils.byref(buffer))


def clAmsMgmtDBGetSUAssignedSIsList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsSUSIExtendedRefBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSUAssignedSIsList(db, clUtils.byref(entity), clUtils.byref(buffer))


def clAmsMgmtDBGetSISUList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsSISUExtendedRefBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSISUList(db, clUtils.byref(entity), clUtils.byref(buffer))


def clAmsMgmtDBGetCompCSIList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsCompCSIRefBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetCompCSIList(db, clUtils.byref(entity), clUtils.byref(buffer))


def clAmsMgmtDBGetNodeCompList(cache, nodeName, compList):
    """
    arg types:
        ClAmsMgmtDBHandleT cache,
        ClCharT *nodeName, 
        ClAmsEntityBufferT *compList
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetNodeCompList(cache, clUtils.byref(nodeName), clUtils.byref(compList))


def clAmsMgmtDBCacheDump(db):
    """
    arg types:
        ClAmsMgmtDBHandleT db
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBCacheDump(db)


def clAmsMgmtDBFinalize(db):
    """
    arg types:
        ClAmsMgmtDBHandleT *db
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBFinalize(clUtils.byref(db))


def clAmsMgmtComputedAdminStateGet(handle, entity, adminState):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClAmsAdminStateT *adminState
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtComputedAdminStateGet(handle, clUtils.byref(entity), clUtils.byref(adminState))

def clAmsMgmtCCBBatchInitialize(mgmtHandle, batchHandle):
    """
    arg types:
        ClAmsMgmtHandleT mgmtHandle,
        ClAmsMgmtCCBBatchHandleT *batchHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchInitialize(mgmtHandle, clUtils.byref(batchHandle))


def clAmsMgmtCCBBatchFinalize(batchHandle):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT *batchHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchFinalize(clUtils.byref(batchHandle))


def clAmsMgmtCCBBatchEntityCreate(batchHandle, entity):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchEntityCreate(batchHandle, clUtils.byref(entity))


def clAmsMgmtCCBBatchEntityDelete(batchHandle, entity):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchEntityDelete(batchHandle, clUtils.byref(entity))


def clAmsMgmtCCBBatchEntitySetConfig(batchHandle, entityConfig, bitmask):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityConfigT *entityConfig,
        ClUint64T bitmask
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchEntitySetConfig(batchHandle, clUtils.byref(entityConfig), bitmask)


def clAmsMgmtCCBBatchCSISetNVP(batchHandle, csiName, nvp):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *csiName,
        ClAmsCSINVPT *nvp
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchCSISetNVP(batchHandle, clUtils.byref(csiName), clUtils.byref(nvp))


def clAmsMgmtCCBBatchCSIDeleteNVP(batchHandle, csiName, nvp):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *csiName,
        ClAmsCSINVPT *nvp
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchCSIDeleteNVP(batchHandle, clUtils.byref(csiName), clUtils.byref(nvp))


def clAmsMgmtCCBBatchSetNodeDependency(batchHandle, nodeName, dependencyNodeName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *dependencyNodeName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetNodeDependency(batchHandle, clUtils.byref(nodeName), clUtils.byref(dependencyNodeName))


def clAmsMgmtCCBBatchDeleteNodeDependency(batchHandle, nodeName, dependencyNodeName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *dependencyNodeName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteNodeDependency(batchHandle, clUtils.byref(nodeName), clUtils.byref(dependencyNodeName))


def clAmsMgmtCCBBatchSetNodeSUList(batchHandle, nodeName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetNodeSUList(batchHandle, clUtils.byref(nodeName), clUtils.byref(suName))


def clAmsMgmtCCBBatchDeleteNodeSUList(batchHandle, nodeName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteNodeSUList(batchHandle, clUtils.byref(nodeName), clUtils.byref(suName))


def clAmsMgmtCCBBatchSetSGSUList(batchHandle, sgName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSGSUList(batchHandle, clUtils.byref(sgName), clUtils.byref(suName))


def clAmsMgmtCCBBatchDeleteSGSUList(batchHandle, sgName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSGSUList(batchHandle, clUtils.byref(sgName), clUtils.byref(suName))


def clAmsMgmtCCBBatchSetSGSIList(batchHandle, sgName, siName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *siName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSGSIList(batchHandle, clUtils.byref(sgName), clUtils.byref(siName))


def clAmsMgmtCCBBatchDeleteSGSIList(batchHandle, sgName, siName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *siName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSGSIList(batchHandle, clUtils.byref(sgName), clUtils.byref(siName))


def clAmsMgmtCCBBatchSetSUCompList(batchHandle, suName, compName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *suName,
        ClAmsEntityT *compName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSUCompList(batchHandle, clUtils.byref(suName), clUtils.byref(compName))


def clAmsMgmtCCBBatchDeleteSUCompList(batchHandle, suName, compName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *suName,
        ClAmsEntityT *compName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSUCompList(batchHandle, clUtils.byref(suName), clUtils.byref(compName))


def clAmsMgmtCCBBatchSetSISURankList(batchHandle, siName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSISURankList(batchHandle, clUtils.byref(siName), clUtils.byref(suName))


def clAmsMgmtCCBBatchDeleteSISURankList(batchHandle, siName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSISURankList(batchHandle, clUtils.byref(siName), clUtils.byref(suName))


def clAmsMgmtCCBBatchSetSIDependency(batchHandle, siName, dependencySIName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *dependencySIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSIDependency(batchHandle, clUtils.byref(siName), clUtils.byref(dependencySIName))


def clAmsMgmtCCBBatchDeleteSIDependency(batchHandle, siName, dependencySIName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *dependencySIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSIDependency(batchHandle, clUtils.byref(siName), clUtils.byref(dependencySIName))


def clAmsMgmtCCBBatchSetCSIDependency(batchHandle, csiName, dependencyCSIName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *csiName,
        ClAmsEntityT *dependencyCSIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetCSIDependency(batchHandle, clUtils.byref(csiName), clUtils.byref(dependencyCSIName))


def clAmsMgmtCCBBatchDeleteCSIDependency(batchHandle, csiName, dependencyCSIName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *csiName,
        ClAmsEntityT *dependencyCSIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteCSIDependency(batchHandle, clUtils.byref(csiName), clUtils.byref(dependencyCSIName))


def clAmsMgmtCCBBatchSetSICSIList(batchHandle, siName, csiName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *csiName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSICSIList(batchHandle, clUtils.byref(siName), clUtils.byref(csiName))


def clAmsMgmtCCBBatchDeleteSICSIList(batchHandle, siName, csiName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *csiName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSICSIList(batchHandle, clUtils.byref(siName), clUtils.byref(csiName))


def clAmsMgmtCCBBatchCommit(batchHandle):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchCommit(batchHandle)
