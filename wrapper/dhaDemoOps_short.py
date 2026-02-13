from common import clCommonErrors
from utils import clLib, libc
from log import clLogApi
from amf import clAmsMgmtCommon

from common.clCommon import ClHandleT, ClUint64T, ClNameT, clNameSet, clNameCopy
from utils.clUtils import getCallerInfo
from utils.clHeapApi import clHeapFree
from amf.clAmsMgmtClientApi import clAmsMgmtInitialize, clAmsMgmtCCBInitialize, clAmsMgmtFinalize, clAmsMgmtCCBFinalize,\
    clAmsMgmtEntityGetConfig, clAmsMgmtCCBEntityCreate, clAmsMgmtCCBCommit, clAmsMgmtCCBEntityDelete, clAmsMgmtCCBSetSGSUList,\
    clAmsMgmtCCBSetSGSIList, clAmsMgmtCCBEntitySetConfig, clAmsMgmtCCBSetSICSIList, clAmsMgmtCCBCSISetNVP, clAmsMgmtCCBSetNodeSUList,\
    clAmsMgmtCCBSetSUCompList, clAmsMgmtEntityLockAssignment, clAmsMgmtEntityUnlock, clAmsMgmtEntityLockInstantiation
from amf.clAmsEntities import ClAmsEntityT, ClAmsEntityConfigT, eClAmsEntityTypeT, ClAmsSGConfigT, ClAmsSIConfigT, ClAmsCSIConfigT,\
    ClAmsCSINameValuePairT, ClAmsNodeConfigT, ClAmsSUConfigT, ClAmsCompConfigT
from amf.clAmsTypes import eClAmsCompCapModelT, eClAmsRecoveryT

import ctypes

CL_LOG_HANDLE_APP = ClHandleT.in_dll(clLib.libmw_so, "CL_LOG_HANDLE_APP")

def dhaInfoPrint(fmtString, *va_args):
    _, fileName, loc = getCallerInfo()

    clLogApi.clLogMsgWrite(
        CL_LOG_HANDLE_APP,
        clLogApi.eClLogSeverityT.CL_LOG_SEV_INFO,
        11,
        "DHA",
        "DMO",
        fileName,
        loc,
        fmtString,
        *va_args
    )

def dhaErrorPrint(fmtString, *va_args):
    _, fileName, loc = getCallerInfo()

    clLogApi.clLogMsgWrite(
        CL_LOG_HANDLE_APP,
        clLogApi.eClLogSeverityT.CL_LOG_SEV_ERROR,
        11,
        "DHA",
        "DMO",
        fileName,
        loc,
        fmtString,
        *va_args
    )

WORKER0 = "WorkerI0"
WORKER1 = "WorkerI1"
NEW_COMP_PREFIX = "dynamicComp"
BASE_NAME = "dynamicTwoN"

#
# Clean up utils
#

def out(pBaseName, rc):
    if rc == clCommonErrors.CL_OK:
        dhaInfoPrint("Successfully created/deleted 2N SG [%sSG] and its entities(si, csi, su, comp, etc) dynamically", pBaseName)
    else:
        dhaErrorPrint("Error while dynamically creating 2N SG [%sSG] and its entities(si, csi, su, comp, etc)", pBaseName)

def out1(mgmtHandle, pBaseName, rc):
    dhaInfoPrint("Running MGMT finalize")
    retcode = clAmsMgmtFinalize(mgmtHandle)
    if retcode != clCommonErrors.CL_OK:
        dhaErrorPrint("MGMT finalize returned [%#x]", retcode)
    out(pBaseName, rc)

def out2(mgmtHandle, ccbHandle, pBaseName, rc):
    dhaInfoPrint("Running CCB finalize")
    retcode = clAmsMgmtCCBFinalize(ccbHandle)
    if retcode != clCommonErrors.CL_OK:
        dhaErrorPrint("CCB finalize returned [%#x]", retcode)
    out1(mgmtHandle, pBaseName, rc)

#
# Setting up
#

def dhaMgmtInit(mgmtHandle, version):
    pBaseName = BASE_NAME
    dhaInfoPrint("Running MGMT initialize")
    rc = clAmsMgmtInitialize(mgmtHandle, None, version)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("AmsMgmt initialize returned [%#x]", rc)
        out1(mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaMgmtCcbInit(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    dhaInfoPrint("Running MGMT CCB initialize")
    rc = clAmsMgmtCCBInitialize(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("MGMT CCB initialize returned [%#x]", rc)
        out1(mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaCleanUp(mgmtHandle, ccbHandle):
    out2(mgmtHandle, ccbHandle, BASE_NAME, clCommonErrors.CL_OK)

#
# Entity creating functions
#

def dhaSgCheck(mgmtHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()
    pEntityConfig = ClAmsSGConfigT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG
    clNameSet(entity.name, "{0}SG".format(pBaseName))
    rc = clAmsMgmtEntityGetConfig(mgmtHandle, entity, pEntityConfig)
    
    return rc

def dhaSgCreate(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG
    clNameSet(entity.name, "{0}SG".format(pBaseName))
    dhaInfoPrint("Creating SG [%s]", entity.name.value)
    rc = clAmsMgmtCCBEntityCreate(ccbHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SG create returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSiCreate(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI
    clNameSet(entity.name, "{0}SI".format(pBaseName))
    dhaInfoPrint("Creating SI [%s]", entity.name.value)
    rc = clAmsMgmtCCBEntityCreate(ccbHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SI create returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaCsiCreate(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI
    clNameSet(entity.name, "{0}CSI".format(pBaseName))
    dhaInfoPrint("Creating CSI [%s]", entity.name.value)
    rc = clAmsMgmtCCBEntityCreate(ccbHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("CSI create returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSuCreate(mgmtHandle, ccbHandle, idx):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU
    clNameSet(entity.name, "{0}SU{1}".format(pBaseName, idx))
    dhaInfoPrint("Creating SU [%s]", entity.name.value)
    rc = clAmsMgmtCCBEntityCreate(ccbHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SU create returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaCompCreate(mgmtHandle, ccbHandle, idx):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP
    clNameSet(entity.name, "{0}{1}".format(NEW_COMP_PREFIX, idx))
    dhaInfoPrint("Creating COMP [%s]", entity.name.value)
    rc = clAmsMgmtCCBEntityCreate(ccbHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("COMP create returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaCommit(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME

    dhaInfoPrint("CCB Commit")
    rc = clAmsMgmtCCBCommit(ccbHandle)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("CCB Commit returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

#
# Entity creating functions
#

def dhaCompDelete(mgmtHandle, ccbHandle, idx):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP
    clNameSet(entity.name, "{0}{1}".format(NEW_COMP_PREFIX, idx))
    dhaInfoPrint("Delete COMP [%s]", entity.name.value)
    rc = clAmsMgmtCCBEntityDelete(ccbHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("COMP delete returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSuDelete(mgmtHandle, ccbHandle, idx):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU
    clNameSet(entity.name, "{0}SU{1}".format(pBaseName, idx))
    dhaInfoPrint("Delete SU [%s]", entity.name.value)
    rc = clAmsMgmtCCBEntityDelete(ccbHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SU delte returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaCsiDelete(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI
    clNameSet(entity.name, "{0}CSI".format(pBaseName))
    dhaInfoPrint("Delete CSI [%s]", entity.name.value)
    rc = clAmsMgmtCCBEntityDelete(ccbHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("CSI delete returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSiDelete(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI
    clNameSet(entity.name, "{0}SI".format(pBaseName))
    dhaInfoPrint("Delete SI [%s]", entity.name.value)
    rc = clAmsMgmtCCBEntityDelete(ccbHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SI delete returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSgDelete(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG
    clNameSet(entity.name, "{0}SG".format(pBaseName))
    dhaInfoPrint("Delete SG [%s]", entity.name.value)
    rc = clAmsMgmtCCBEntityDelete(ccbHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SG delete returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

#
# Config Filling Functions
#

def dhaSgSetSu(mgmtHandle, ccbHandle, sgEntity, suIdx):
    targetEntity = ClAmsEntityT()
    targetEntity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU
    clNameSet(targetEntity.name, "{0}SU{1}".format(BASE_NAME, suIdx))
    dhaInfoPrint("SG set SU [%s]", targetEntity.name.value)
    rc = clAmsMgmtCCBSetSGSUList(ccbHandle, sgEntity, targetEntity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SG set SU returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, BASE_NAME, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSgConfigFill(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()
    targetEntity = ClAmsEntityT()

    sgConfig = ClAmsSGConfigT()
    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG
    clNameSet(entity.name, "{0}SG".format(pBaseName))

    dhaInfoPrint("SG config get [%s]", entity.name.value)
    rc = clAmsMgmtEntityGetConfig(mgmtHandle, entity, sgConfig)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SG config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    # Fill SG SI list
    targetEntity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI
    clNameSet(targetEntity.name, "{0}SI".format(pBaseName))
    dhaInfoPrint("SG set SI [%s]", targetEntity.name.value)
    rc = clAmsMgmtCCBSetSGSIList(ccbHandle, entity, targetEntity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SG set SI returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    # Fill SG SU list
    rc = dhaSgSetSu(mgmtHandle, ccbHandle, entity, 0)
    if rc != clCommonErrors.CL_OK: return rc
    rc = dhaSgSetSu(mgmtHandle, ccbHandle, entity, 1)
    if rc != clCommonErrors.CL_OK: return rc

    # Commit
    return dhaCommit(mgmtHandle, ccbHandle)

def dhaSiConfigFill(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()
    targetEntity = ClAmsEntityT()

    siConfig = ClAmsSIConfigT()
    bitMask = ClUint64T(0)

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI
    clNameSet(entity.name, "{0}SI".format(pBaseName))
    dhaInfoPrint("SI config get [%s]", entity.name.value)
    rc = clAmsMgmtEntityGetConfig(mgmtHandle, entity, siConfig)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SI config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc


    siConfig.numCSIs = 1
    siConfig.numStandbyAssignments = 1

    bitMask.value |= (clAmsMgmtCommon.SI_CONFIG_NUM_CSIS
                      | clAmsMgmtCommon.SI_CONFIG_NUM_STANDBY_ASSIGNMENTS)
    dhaInfoPrint("SI config set [%s]", entity.name.value)
    rc = clAmsMgmtCCBEntitySetConfig(ccbHandle, siConfig.entity, bitMask)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SI config set returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    # Fill SI CSI list
    targetEntity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI
    clNameSet(targetEntity.name, "{0}CSI".format(pBaseName))
    dhaInfoPrint("SI set CSI [%s]", targetEntity.name.value)
    rc = clAmsMgmtCCBSetSICSIList(ccbHandle, entity, targetEntity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SI set CSI returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    # Commit
    return dhaCommit(mgmtHandle, ccbHandle)

def dhaCsiConfigFill(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    csiConfig = ClAmsCSIConfigT()
    bitMask = ClUint64T(0)

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI
    clNameSet(entity.name, "{0}CSI".format(pBaseName))
    dhaInfoPrint("CSI config get [%s]", entity.name.value)
    rc = clAmsMgmtEntityGetConfig(mgmtHandle, entity, csiConfig)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("CSI config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    # Set CSI type
    bitMask.value |= clAmsMgmtCommon.CSI_CONFIG_TYPE
    typeName = "{0}Type".format(entity.name.__str__())
    clNameSet(csiConfig.type, typeName)
    dhaInfoPrint("CSI type set [%s]", csiConfig.type.value)
    rc = clAmsMgmtCCBEntitySetConfig(ccbHandle, csiConfig.entity, bitMask)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("CSI type set returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    # Set CSI NVP list
    nvp = ClAmsCSINameValuePairT()
    clNameSet(nvp.paramName, "model")
    clNameSet(nvp.paramValue, "twoN")
    clNameCopy(nvp.csiName, entity.name)

    dhaInfoPrint("CSI set nvplist")
    rc = clAmsMgmtCCBCSISetNVP(ccbHandle, entity, nvp)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("CSI set nvplist returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    return dhaCommit(mgmtHandle, ccbHandle)

def dhaNodeSetSu(mgmtHandle, ccbHandle, nodeEntity, suIdx):
    targetEntity = ClAmsEntityT()
    targetEntity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU
    clNameSet(targetEntity.name, "{0}SU{1}".format(BASE_NAME, suIdx))
    dhaInfoPrint("Node set SU [%s]", targetEntity.name.value)
    rc = clAmsMgmtCCBSetNodeSUList(ccbHandle, nodeEntity, targetEntity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("Node set SU returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, BASE_NAME, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaNodeConfigFill(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    nodeConfig = ClAmsNodeConfigT()
    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_NODE
    clNameSet(entity.name, WORKER0)
    dhaInfoPrint("NODE config get [%s]", entity.name.value)
    rc = clAmsMgmtEntityGetConfig(mgmtHandle, entity, nodeConfig)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("NODE config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    # Set Node SU list with redundant SUs
    rc = dhaNodeSetSu(mgmtHandle, ccbHandle, entity, 0)
    if rc != clCommonErrors.CL_OK: return rc

    clNameSet(entity.name, WORKER1)
    rc = dhaNodeSetSu(mgmtHandle, ccbHandle, entity, 1)
    if rc != clCommonErrors.CL_OK: return rc

    return dhaCommit(mgmtHandle, ccbHandle)

def dhaSuSetComp(mgmtHandle, ccbHandle, suConfig, bitMask, suIdx):
    pBaseName = BASE_NAME
    targetEntity = ClAmsEntityT()

    clNameSet(suConfig.entity.name, "{0}SU{1}".format(pBaseName, suIdx))

    dhaInfoPrint("SU config set [%s]", suConfig.entity.name.value)
    rc = clAmsMgmtCCBEntitySetConfig(ccbHandle, suConfig.entity, bitMask)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SU config set returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    targetEntity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP
    clNameSet(targetEntity.name, "{0}{1}".format(NEW_COMP_PREFIX, suIdx))
    dhaInfoPrint("SU [%s] add comp [%s]", suConfig.entity.name.value, targetEntity.name.value)
    rc = clAmsMgmtCCBSetSUCompList(ccbHandle, suConfig.entity, targetEntity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SU add comp returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSuConfigFill(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    suConfig = ClAmsSUConfigT()
    bitMask = ClUint64T()
    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU
    clNameSet(entity.name, "{0}SU0".format(pBaseName))
    dhaInfoPrint("SU config get [%s]", entity.name.value)
    rc = clAmsMgmtEntityGetConfig(mgmtHandle, entity, suConfig)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SU config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    suConfig.numComponents = 1
    bitMask.value |= clAmsMgmtCommon.SU_CONFIG_NUM_COMPONENTS

    rc = dhaSuSetComp(mgmtHandle, ccbHandle, suConfig, bitMask, 0)
    if rc != clCommonErrors.CL_OK: return rc
    rc = dhaSuSetComp(mgmtHandle, ccbHandle, suConfig, bitMask, 1)
    if rc != clCommonErrors.CL_OK: return rc

    return dhaCommit(mgmtHandle, ccbHandle)

def dhaCompSetConfig(mgmtHandle, ccbHandle, compConfig, bitMask, compIdx):
    pBaseName = BASE_NAME
    clNameSet(compConfig.entity.name, "{0}{1}".format(NEW_COMP_PREFIX, compIdx))

    dhaInfoPrint("Comp config set [%s]", compConfig.entity.name.value)
    rc = clAmsMgmtCCBEntitySetConfig(ccbHandle, compConfig.entity, bitMask)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("Comp config set returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaCompConfigFill(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    compConfig = ClAmsCompConfigT()
    bitMask = ClUint64T()

    clNameSet(entity.name, "{0}0".format(NEW_COMP_PREFIX))
    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP
    dhaInfoPrint("COMP config get [%s]", entity.name.value)
    rc = clAmsMgmtEntityGetConfig(mgmtHandle, entity, compConfig)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("COMP config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    bitMask.value |= (clAmsMgmtCommon.COMP_CONFIG_CAPABILITY_MODEL
                      | clAmsMgmtCommon.COMP_CONFIG_TIMEOUTS
                      | clAmsMgmtCommon.COMP_CONFIG_RECOVERY_ON_TIMEOUT)

    compConfig.capabilityModel = eClAmsCompCapModelT.CL_AMS_COMP_CAP_X_ACTIVE_OR_Y_STANDBY
    compConfig.timeouts.instantiate = 30000
    compConfig.timeouts.terminate = 30000
    compConfig.timeouts.cleanup = 30000
    compConfig.timeouts.quiescingComplete = 30000
    compConfig.timeouts.csiSet = 30000
    compConfig.timeouts.csiRemove = 30000
    compConfig.timeouts.instantiateDelay = 10000
    compConfig.recoveryOnTimeout = eClAmsRecoveryT.CL_AMS_RECOVERY_COMP_FAILOVER

    bitMask.value |= clAmsMgmtCommon.COMP_CONFIG_SUPPORTED_CSI_TYPE

    compConfig.numSupportedCSITypes = 1

    clNameSet(compConfig.pSupportedCSITypes, "{0}CSIType".format(pBaseName))

    bitMask.value |= clAmsMgmtCommon.COMP_CONFIG_INSTANTIATE_COMMAND
    compConfig.instantiateCommand = b"dummyComp"

    rc = dhaCompSetConfig(mgmtHandle, ccbHandle, compConfig, bitMask, 0)
    if rc != clCommonErrors.CL_OK: return rc
    rc = dhaCompSetConfig(mgmtHandle, ccbHandle, compConfig, bitMask, 1)
    if rc != clCommonErrors.CL_OK: return rc

    return dhaCommit(mgmtHandle, ccbHandle)

#
# AMF Operations
#

def dhaSuUnlock(mgmtHandle, ccbHandle, suIdx):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU
    clNameSet(entity.name, "{0}SU{1}".format(pBaseName, suIdx))

    dhaInfoPrint("LockA [%s]", entity.name.value)
    rc = clAmsMgmtEntityLockAssignment(mgmtHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockA returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    dhaInfoPrint("Unlock [%s]", entity.name.value)
    rc = clAmsMgmtEntityUnlock(mgmtHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("Unlock returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    return clCommonErrors.CL_OK

def dhaSiUnlock(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI
    clNameSet(entity.name, "{0}SI".format(pBaseName))

    dhaInfoPrint("Unlock SI [%s]", entity.name.value)
    rc = clAmsMgmtEntityUnlock(mgmtHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("Unlock returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    return clCommonErrors.CL_OK

def dhaSgUnlock(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG
    clNameSet(entity.name, "{0}SG".format(pBaseName))

    dhaInfoPrint("LockA SG [%s]", entity.name.value)
    rc = clAmsMgmtEntityLockAssignment(mgmtHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockA returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    dhaInfoPrint("Unlock SG [%s]", entity.name.value)
    rc = clAmsMgmtEntityUnlock(mgmtHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("Unlock returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    return clCommonErrors.CL_OK

def dhaEntitiesUnlock(mgmtHandle, ccbHandle):
    for idx in range(0, 2):
        rc = dhaSuUnlock(mgmtHandle, ccbHandle, idx)
        if rc != clCommonErrors.CL_OK: return rc

    rc = dhaSiUnlock(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return rc

    rc = dhaSgUnlock(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return rc

    return clCommonErrors.CL_OK

def dhaSuLockI(mgmtHandle, ccbHandle, suIdx):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU
    clNameSet(entity.name, "{0}SU{1}".format(pBaseName, suIdx))

    dhaInfoPrint("LockA [%s]", entity.name.value)
    rc = clAmsMgmtEntityLockAssignment(mgmtHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockA returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    
    dhaInfoPrint("LockI [%s]", entity.name.value)
    rc = clAmsMgmtEntityLockInstantiation(mgmtHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockI returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSiLockA(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI
    clNameSet(entity.name, "{0}SI".format(pBaseName))

    dhaInfoPrint("LockA SI [%s]", entity.name.value)
    rc = clAmsMgmtEntityLockAssignment(mgmtHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockA returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSgLockI(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = ClAmsEntityT()

    entity.type = eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG
    clNameSet(entity.name, "{0}SG".format(pBaseName))

    dhaInfoPrint("LockA SG [%s]", entity.name.value)
    rc = clAmsMgmtEntityLockAssignment(mgmtHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockA returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    
    dhaInfoPrint("LockI SG [%s]", entity.name.value)
    rc = clAmsMgmtEntityLockInstantiation(mgmtHandle, entity)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockI returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaEntitiesLockI(mgmtHandle, ccbHandle):
    for idx in range(0, 2):
        rc = dhaSuLockI(mgmtHandle, ccbHandle, idx)
        if rc != clCommonErrors.CL_OK: return rc

    rc = dhaSiLockA(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return rc

    rc = dhaSgLockI(mgmtHandle, ccbHandle)
    if rc != clCommonErrors.CL_OK: return rc

    return clCommonErrors.CL_OK