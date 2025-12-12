import sys
sys.path.append("..")

from utils import libc, clLib

import ctypes

ASP_INSTALL_KEY = "ASP_INSTALL_INFO"

def CL_AMS_NAME_LENGTH_CHECK(entity):
    if entity.name.length.value == libc.strlen(entity.name.value):
        entity.name.length.value += 1

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
    return clLib.libmw_so.clAmsMgmtInitialize(amsHandle, amsMgmtCallbacks, version)

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
    return clLib.libmw_so.clAmsMgmtEntityLockAssignment(amsHandle, entity)

def clAmsMgmtEntityLockAssignmentExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityLockAssignmentExtended(amsHandle, entity, retry)

def clAmsMgmtEntityLockInstantiation(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityLockInstantiation(amsHandle, entity)

def clAmsMgmtEntityLockInstantiationExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityLockInstantiationExtended(amsHandle, entity, retry)

def clAmsMgmtEntityForceLockInstantiation(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityForceLockInstantiation(amsHandle, entity)

def clAmsMgmtEntityForceLockInstantiationExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityForceLockInstantiationExtended(amsHandle, entity, retry)

def clAmsMgmtEntityUnlock(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUnlock(amsHandle, entity)

def clAmsMgmtEntityUnlockExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUnlockExtended(amsHandle, entity, retry)

def clAmsMgmtEntityShutdown(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityShutdown(amsHandle, entity)

def clAmsMgmtEntityShutdownExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityShutdownExtended(amsHandle, entity, retry)

def clAmsMgmtEntityRestart(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityRestart(amsHandle, entity)

def clAmsMgmtEntityRestartExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityRestartExtended(amsHandle, entity, retry)

def clAmsMgmtEntityRepaired(amsHandle, entity):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityRepaired(amsHandle, entity)

def clAmsMgmtEntityRepairedExtended(amsHandle, entity, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityRepairedExtended(amsHandle, entity, retry)

def clAmsMgmtSISwap(amsHandle, si):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClCharT *si
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtSISwap(amsHandle, si)

def clAmsMgmtSISwapExtended(amsHandle, si, retry):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClCharT *si,
        ClBoolT retry
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtSISwapExtended(amsHandle, si, retry)

def clAmsMgmtSGAdjust(amsHandle, sg, enable):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClCharT *sg,
        ClBoolT enable
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtSGAdjust(amsHandle, sg, enable)

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
    return clLib.libmw_so.clAmsMgmtSGAdjustExtended(amsHandle, sg, enable, retry)

def clAmsMgmtDebugEnable(amsHandle, entity, debugFlags):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClUint8T  debugFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDebugEnable(amsHandle, entity, debugFlags)

def clAmsMgmtDebugDisable(amsHandle, entity, debugFlags):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClUint8T  debugFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDebugDisable(amsHandle, entity, debugFlags)

def clAmsMgmtDebugGet(amsHandle, entity, debugFlags):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClUint8T *debugFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDebugGet(amsHandle, entity, debugFlags)

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
    return clLib.libmw_so.clAmsMgmtEntitySetAlphaFactor(amsHandle, entity, alphaFactor)

def clAmsMgmtEntitySetBetaFactor(amsHandle, entity, betaFactor):
    """
    arg types:
        ClAmsMgmtHandleT amsHandle,
        ClAmsEntityT *entity,
        ClUint32T betaFactor
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntitySetBetaFactor(amsHandle, entity, betaFactor)

def clAmsMgmtCCBInitialize(amlHandle, ccbHandle):
    """
    arg types:
        ClAmsMgmtHandleT amlHandle,
        ClAmsMgmtCCBHandleT *ccbHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBInitialize(amlHandle, ccbHandle)

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
    return clLib.libmw_so.clAmsMgmtCCBEntityCreate(handle, entity)

def clAmsMgmtCCBEntityDelete(handle, entity):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBEntityDelete(handle, entity)

def clAmsMgmtCCBEntitySetConfig(handle, entityConfig, bitMask):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityConfigT *entityConfig,
        ClUint64T bitMask
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBEntitySetConfig(handle, entityConfig, bitMask)

def clAmsMgmtCCBCSISetNVP(handle, csiName, nvp):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *csiName,
        ClAmsCSINVPT *nvp
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBCSISetNVP(handle, csiName, nvp)

def clAmsMgmtCCBCSIDeleteNVP(handle, csiName, nvp):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *csiName,
        ClAmsCSINVPT *nvp
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBCSIDeleteNVP(handle, csiName, nvp)

def clAmsMgmtCCBSetNodeDependency(handle, nodeName, dependencyNodeName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *dependencyNodeName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetNodeDependency(handle, nodeName, dependencyNodeName)

def clAmsMgmtCCBDeleteNodeDependency(handle, nodeName, dependencyNodeName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *dependencyNodeName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteNodeDependency(handle, nodeName, dependencyNodeName)

def clAmsMgmtCCBSetNodeSUList(handle, nodeName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetNodeSUList(handle, nodeName, suName)

def clAmsMgmtCCBDeleteNodeSUList(handle, nodeName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteNodeSUList(handle, nodeName, suName)

def clAmsMgmtCCBSetSGSUList(handle, sgName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSGSUList(handle, sgName, suName)

def clAmsMgmtCCBDeleteSGSUList(handle, sgName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSGSUList(handle, sgName, suName)

def clAmsMgmtCCBSetSGSIList(handle, sgName, siName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *siName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSGSIList(handle, sgName, siName)

def clAmsMgmtCCBDeleteSGSIList(handle, sgName, siName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *siName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSGSIList(handle, sgName, siName)

def clAmsMgmtCCBSetSUCompList(handle, suName, compName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *suName,
        ClAmsEntityT *compName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSUCompList(handle, suName, compName)

def clAmsMgmtCCBDeleteSUCompList(handle, suName, compName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *suName,
        ClAmsEntityT *compName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSUCompList(handle, suName, compName)

def clAmsMgmtCCBSetSISURankList(handle, siName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSISURankList(handle, siName, suName)

def clAmsMgmtCCBDeleteSISURankList(handle, siName, suName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSISURankList(handle, siName, suName)

def clAmsMgmtCCBSetSIDependency(handle, siName, dependencySIName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *dependencySIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSIDependency(handle, siName, dependencySIName)

def clAmsMgmtCCBDeleteSIDependency(handle, siName, dependencySIName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *dependencySIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSIDependency(handle, siName, dependencySIName)

def clAmsMgmtCCBSetCSIDependency(handle, csiName, dependencyCSIName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *csiName,
        ClAmsEntityT *dependencyCSIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetCSIDependency(handle, csiName, dependencyCSIName)

def clAmsMgmtCCBDeleteCSIDependency(handle, csiName, dependencyCSIName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *csiName,
        ClAmsEntityT *dependencyCSIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteCSIDependency(handle, csiName, dependencyCSIName)

def clAmsMgmtCCBSetSICSIList(handle, siName, csiName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *csiName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBSetSICSIList(handle, siName, csiName)

def clAmsMgmtCCBDeleteSICSIList(handle, siName, csiName):
    """
    arg types:
        ClAmsMgmtCCBHandleT handle,
        ClAmsEntityT *siName,
        ClAmsEntityT *csiName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBDeleteSICSIList(handle, siName, csiName)

def clAmsMgmtEntityGet(handle, entityRef):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityRefT *entityRef
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityGet(handle, entityRef)

def clAmsMgmtEntityGetConfig(handle, entity, entityConfig):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClAmsEntityConfigT **entityConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityGetConfig(handle, entity, entityConfig)

def clAmsMgmtNodeGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsNodeConfigT*
    """
    return clLib.libmw_so.clAmsMgmtNodeGetConfig(handle, entName)

def clAmsMgmtServiceGroupGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSGConfigT*
    """
    return clLib.libmw_so.clAmsMgmtServiceGroupGetConfig(handle, entName)

def clAmsMgmtServiceUnitGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSUConfigT*
    """
    return clLib.libmw_so.clAmsMgmtServiceUnitGetConfig(handle, entName)

def clAmsMgmtServiceInstanceGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSIConfigT*
    """
    return clLib.libmw_so.clAmsMgmtServiceInstanceGetConfig(handle, entName)

def clAmsMgmtCompServiceInstanceGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsCSIConfigT*
    """
    return clLib.libmw_so.clAmsMgmtCompServiceInstanceGetConfig(handle, entName)

def clAmsMgmtCompGetConfig(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsCompConfigT*
    """
    return clLib.libmw_so.clAmsMgmtCompGetConfig(handle, entName)

def clAmsMgmtEntityGetStatus(handle, entity, entityStatus):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClAmsEntityStatusT **entityStatus
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityGetStatus(handle, entity, entityStatus)

def clAmsMgmtNodeGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsNodeStatusT*
    """
    return clLib.libmw_so.clAmsMgmtNodeGetStatus(handle, entName)

def clAmsMgmtServiceGroupGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSGStatusT*
    """
    return clLib.libmw_so.clAmsMgmtServiceGroupGetStatus(handle, entName)

def clAmsMgmtServiceUnitGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSUStatusT*
    """
    return clLib.libmw_so.clAmsMgmtServiceUnitGetStatus(handle, entName)

def clAmsMgmtServiceInstanceGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsSIStatusT*
    """
    return clLib.libmw_so.clAmsMgmtServiceInstanceGetStatus(handle, entName)

def clAmsMgmtCompServiceInstanceGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsCSIStatusT*
    """
    return clLib.libmw_so.clAmsMgmtCompServiceInstanceGetStatus(handle, entName)

def clAmsMgmtCompGetStatus(handle, entName):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClCharT *entName
    return type:
        ClAmsCompStatusT*
    """
    return clLib.libmw_so.clAmsMgmtCompGetStatus(handle, entName)

def clAmsMgmtGetList(handle, listName, buffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityListTypeT listName,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetList(handle, listName, buffer)

def clAmsMgmtGetCSINVPList(handle, csi, nvpBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *csi,
        ClAmsCSINVPBufferT *nvpBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetCSINVPList(handle, csi, nvpBuffer)

def clAmsMgmtGetCSIDependenciesList(handle, csi, dependenciesCSIBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *csi,
        ClAmsEntityBufferT *dependenciesCSIBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetCSIDependenciesList(handle, csi, dependenciesCSIBuffer)

def clAmsMgmtGetSGList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGList(handle, entityBuffer)

def clAmsMgmtGetSIList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSIList(handle, entityBuffer)

def clAmsMgmtGetCSIList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetCSIList(handle, entityBuffer)

def clAmsMgmtGetNodeList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetNodeList(handle, entityBuffer)

def clAmsMgmtGetSUList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSUList(handle, entityBuffer)

def clAmsMgmtGetCompList(handle, entityBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityBufferT *entityBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetCompList(handle, entityBuffer)

def clAmsMgmtGetNodeDependenciesList(handle, node, dependencyBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *node,
        ClAmsEntityBufferT *dependencyBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetNodeDependenciesList(handle, node, dependencyBuffer)

def clAmsMgmtGetNodeSUList(handle, node, suBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *node,
        ClAmsEntityBufferT *suBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetNodeSUList(handle, node, suBuffer)

def clAmsMgmtGetSGSUList(handle, sg, suBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *suBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGSUList(handle, sg, suBuffer)

def clAmsMgmtGetSGSIList(handle, sg, siBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *siBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGSIList(handle, sg, siBuffer)

def clAmsMgmtGetSUCompList(handle, su, compBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *su,
        ClAmsEntityBufferT *compBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSUCompList(handle, su, compBuffer)

def clAmsMgmtGetSISURankList(handle, si, suBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *si,
        ClAmsEntityBufferT *suBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSISURankList(handle, si, suBuffer)

def clAmsMgmtGetSIDependenciesList(handle, si, dependenciesSIBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *si,
        ClAmsEntityBufferT *dependenciesSIBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSIDependenciesList(handle, si, dependenciesSIBuffer)

def clAmsMgmtGetSICSIList(handle, si, csiBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *si,
        ClAmsEntityBufferT *csiBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSICSIList(handle, si, csiBuffer)

def clAmsMgmtGetSGInstantiableSUList(handle, sg, instantiableSUBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *instantiableSUBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGInstantiableSUList(handle, sg, instantiableSUBuffer)

def clAmsMgmtGetSGInstantiatedSUList(handle, sg, instantiatedSUBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *instantiatedSUBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGInstantiatedSUList(handle, sg, instantiatedSUBuffer)

def clAmsMgmtGetSGInServiceSpareSUList(handle, sg, inserviceSpareSUBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *inserviceSpareSUBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGInServiceSpareSUList(handle, sg, inserviceSpareSUBuffer)

def clAmsMgmtGetSGAssignedSUList(handle, sg, assignedSUBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *assignedSUBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGAssignedSUList(handle, sg, assignedSUBuffer)

def clAmsMgmtGetSGFaultySUList(handle, sg, faultySUBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *sg,
        ClAmsEntityBufferT *faultySUBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSGFaultySUList(handle, sg, faultySUBuffer)

def clAmsMgmtGetSUAssignedSIsList(handle, su, siBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *su,
        ClAmsSUSIRefBufferT *siBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSUAssignedSIsList(handle, su, siBuffer)

def clAmsMgmtGetSUAssignedSIsExtendedList(handle, su, siBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *su,
        ClAmsSUSIExtendedRefBufferT *siBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSUAssignedSIsExtendedList(handle, su, siBuffer)

def clAmsMgmtGetSISUList(handle, si, suBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *si,
        ClAmsSISURefBufferT *suBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSISUList(handle, si, suBuffer)

def clAmsMgmtGetSISUExtendedList(handle, si, suBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *si,
        ClAmsSISUExtendedRefBufferT *suBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetSISUExtendedList(handle, si, suBuffer)

def clAmsMgmtGetCompCSIList(handle, comp, csiBuffer):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *comp,
        ClAmsCompCSIRefBufferT *csiBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtGetCompCSIList(handle, comp, csiBuffer)

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
    return clLib.libmw_so.clAmsMgmtGetSIHAState(handle, si, su, haState, fullyAssigned)

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
    return clLib.libmw_so.clAmsMgmtGetSUHAState(handle, su, checkAllSIs, haState, fullyAssigned)

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
    return clLib.libmw_so.clAmsMgmtMigrateSG(handle, sg, prefix, activeSUs, standbySUs, migrateList)

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
    return clLib.libmw_so.clAmsMgmtEntityUserDataSet(handle, entity, data, len)

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
    return clLib.libmw_so.clAmsMgmtEntityUserDataSetKey(handle, entity, key, data, len)

def clAmsMgmtEntityUserDataGet(handle, entity, data, len):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClCharT **data,
        ClUint32T *len
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataGet(handle, entity, data, len)

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
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataGetKey(handle, entity, key, data, len)

def clAmsMgmtEntityUserDataDelete(handle, entity):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataDelete(handle, entity)

def clAmsMgmtEntityUserDataDeleteKey(handle, entity, key):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClNameT *key
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataDeleteKey(handle, entity, key)

def clAmsMgmtEntityUserDataDeleteAll(handle, entity):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtEntityUserDataDeleteAll(handle, entity)

def clAmsMgmtSetActive(handle, entity, activeSU):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClAmsEntityT *activeSU
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtSetActive(handle, entity, activeSU)

def clAmsMgmtSIAssignSU(si, activeSU, standbySU):
    """
    arg types:
        ClCharT *si,
        ClCharT *activeSU,
        ClCharT *standbySU
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtSIAssignSU(si, activeSU, standbySU)


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
    return clLib.libmw_so.clAmsMgmtGetAspInstallInfo(handle, nodeName, aspInstallInfo, len)


def clAmsMgmtFreeCompCSIRefBuffer(buffer):
    """
    arg types:
        ClAmsCompCSIRefBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtFreeCompCSIRefBuffer(buffer)


def clAmsMgmtDBGet(db):
    """
    arg types:
        ClAmsMgmtDBHandleT *db
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGet(db)


def clAmsMgmtDBGetNodeList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetNodeList(db, buffer)


def clAmsMgmtDBGetSUList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSUList(db, buffer)


def clAmsMgmtDBGetSGList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSGList(db, buffer)


def clAmsMgmtDBGetSIList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSIList(db, buffer)


def clAmsMgmtDBGetCSIList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetCSIList(db, buffer)

def clAmsMgmtDBGetCompList(db, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetCompList(db, buffer)


def clAmsMgmtDBGetEntityConfig(db, entity, entityConfig):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityConfigT **entityConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetEntityConfig(db, entity, entityConfig)


def clAmsMgmtDBGetEntityStatus(db, entity, entityStatus):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityStatusT **entityStatus
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetEntityStatus(db, entity, entityStatus)


def clAmsMgmtDBGetNodeSUList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetNodeSUList(db, entity, buffer)


def clAmsMgmtDBGetSGSUList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSGSUList(db, entity, buffer)


def clAmsMgmtDBGetSGSIList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSGSIList(db, entity, buffer)


def clAmsMgmtDBGetSICSIList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSICSIList(db, entity, buffer)

def clAmsMgmtDBGetSUCompList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsEntityBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSUCompList(db, entity, buffer)


def clAmsMgmtDBGetSUAssignedSIsList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsSUSIExtendedRefBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSUAssignedSIsList(db, entity, buffer)


def clAmsMgmtDBGetSISUList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsSISUExtendedRefBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetSISUList(db, entity, buffer)


def clAmsMgmtDBGetCompCSIList(db, entity, buffer):
    """
    arg types:
        ClAmsMgmtDBHandleT db,
        ClAmsEntityT *entity,
        ClAmsCompCSIRefBufferT *buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetCompCSIList(db, entity, buffer)


def clAmsMgmtDBGetNodeCompList(cache, nodeName, compList):
    """
    arg types:
        ClAmsMgmtDBHandleT cache,
        ClCharT *nodeName, 
        ClAmsEntityBufferT *compList
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtDBGetNodeCompList(cache, nodeName, compList)


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
    return clLib.libmw_so.clAmsMgmtDBFinalize(db)


def clAmsMgmtComputedAdminStateGet(handle, entity, adminState):
    """
    arg types:
        ClAmsMgmtHandleT handle,
        ClAmsEntityT *entity,
        ClAmsAdminStateT *adminState
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtComputedAdminStateGet(handle, entity, adminState)

def clAmsMgmtCCBBatchInitialize(mgmtHandle, batchHandle):
    """
    arg types:
        ClAmsMgmtHandleT mgmtHandle,
        ClAmsMgmtCCBBatchHandleT *batchHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchInitialize(mgmtHandle, batchHandle)


def clAmsMgmtCCBBatchFinalize(batchHandle):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT *batchHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchFinalize(batchHandle)


def clAmsMgmtCCBBatchEntityCreate(batchHandle, entity):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchEntityCreate(batchHandle, entity)


def clAmsMgmtCCBBatchEntityDelete(batchHandle, entity):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *entity
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchEntityDelete(batchHandle, entity)


def clAmsMgmtCCBBatchEntitySetConfig(batchHandle, entityConfig, bitmask):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityConfigT *entityConfig,
        ClUint64T bitmask
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchEntitySetConfig(batchHandle, entityConfig, bitmask)


def clAmsMgmtCCBBatchCSISetNVP(batchHandle, csiName, nvp):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *csiName,
        ClAmsCSINVPT *nvp
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchCSISetNVP(batchHandle, csiName, nvp)


def clAmsMgmtCCBBatchCSIDeleteNVP(batchHandle, csiName, nvp):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *csiName,
        ClAmsCSINVPT *nvp
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchCSIDeleteNVP(batchHandle, csiName, nvp)


def clAmsMgmtCCBBatchSetNodeDependency(batchHandle, nodeName, dependencyNodeName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *dependencyNodeName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetNodeDependency(batchHandle, nodeName, dependencyNodeName)


def clAmsMgmtCCBBatchDeleteNodeDependency(batchHandle, nodeName, dependencyNodeName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *dependencyNodeName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteNodeDependency(batchHandle, nodeName, dependencyNodeName)


def clAmsMgmtCCBBatchSetNodeSUList(batchHandle, nodeName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetNodeSUList(batchHandle, nodeName, suName)


def clAmsMgmtCCBBatchDeleteNodeSUList(batchHandle, nodeName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *nodeName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteNodeSUList(batchHandle, nodeName, suName)


def clAmsMgmtCCBBatchSetSGSUList(batchHandle, sgName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSGSUList(batchHandle, sgName, suName)


def clAmsMgmtCCBBatchDeleteSGSUList(batchHandle, sgName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSGSUList(batchHandle, sgName, suName)


def clAmsMgmtCCBBatchSetSGSIList(batchHandle, sgName, siName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *siName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSGSIList(batchHandle, sgName, siName)


def clAmsMgmtCCBBatchDeleteSGSIList(batchHandle, sgName, siName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *sgName,
        ClAmsEntityT *siName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSGSIList(batchHandle, sgName, siName)


def clAmsMgmtCCBBatchSetSUCompList(batchHandle, suName, compName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *suName,
        ClAmsEntityT *compName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSUCompList(batchHandle, suName, compName)


def clAmsMgmtCCBBatchDeleteSUCompList(batchHandle, suName, compName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *suName,
        ClAmsEntityT *compName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSUCompList(batchHandle, suName, compName)


def clAmsMgmtCCBBatchSetSISURankList(batchHandle, siName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSISURankList(batchHandle, siName, suName)


def clAmsMgmtCCBBatchDeleteSISURankList(batchHandle, siName, suName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *suName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSISURankList(batchHandle, siName, suName)


def clAmsMgmtCCBBatchSetSIDependency(batchHandle, siName, dependencySIName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *dependencySIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSIDependency(batchHandle, siName, dependencySIName)


def clAmsMgmtCCBBatchDeleteSIDependency(batchHandle, siName, dependencySIName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *dependencySIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSIDependency(batchHandle, siName, dependencySIName)


def clAmsMgmtCCBBatchSetCSIDependency(batchHandle, csiName, dependencyCSIName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *csiName,
        ClAmsEntityT *dependencyCSIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetCSIDependency(batchHandle, csiName, dependencyCSIName)


def clAmsMgmtCCBBatchDeleteCSIDependency(batchHandle, csiName, dependencyCSIName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *csiName,
        ClAmsEntityT *dependencyCSIName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteCSIDependency(batchHandle, csiName, dependencyCSIName)


def clAmsMgmtCCBBatchSetSICSIList(batchHandle, siName, csiName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *csiName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchSetSICSIList(batchHandle, siName, csiName)


def clAmsMgmtCCBBatchDeleteSICSIList(batchHandle, siName, csiName):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle,
        ClAmsEntityT *siName,
        ClAmsEntityT *csiName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchDeleteSICSIList(batchHandle, siName, csiName)


def clAmsMgmtCCBBatchCommit(batchHandle):
    """
    arg types:
        ClAmsMgmtCCBBatchHandleT batchHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clAmsMgmtCCBBatchCommit(batchHandle)
