from common import clCommon, clCommonErrors
from utils import clUtils, clLib, clHeapApi, libc
from log import clLogApi
from amf import clAmsMgmtClientApi, clAmsEntities, clAmsMgmtCommon, clAmsTypes

import ctypes

CL_LOG_HANDLE_APP = clCommon.ClHandleT.in_dll(clLib.libmw_so, "CL_LOG_HANDLE_APP")

def dhaInfoPrint(fmtString, *va_args):
    _, fileName, loc = clUtils.getCallerInfo()

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
    _, fileName, loc = clUtils.getCallerInfo()

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
    retcode = clAmsMgmtClientApi.clAmsMgmtFinalize(mgmtHandle)
    if retcode != clCommonErrors.CL_OK:
        dhaErrorPrint("MGMT finalize returned [%#x]", retcode)
    out(pBaseName, rc)

def out2(mgmtHandle, ccbHandle, pBaseName, rc):
    dhaInfoPrint("Running CCB finalize")
    retcode = clAmsMgmtClientApi.clAmsMgmtCCBFinalize(ccbHandle)
    if retcode != clCommonErrors.CL_OK:
        dhaErrorPrint("CCB finalize returned [%#x]", retcode)
    out1(mgmtHandle, pBaseName, rc)

#
# Setting up
#

def dhaMgmtInit(mgmtHandle, version):
    pBaseName = BASE_NAME
    dhaInfoPrint("Running MGMT initialize")
    rc = clAmsMgmtClientApi.clAmsMgmtInitialize(ctypes.byref(mgmtHandle), None, ctypes.byref(version))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("AmsMgmt initialize returned [%#x]", rc)
        out1(mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaMgmtCcbInit(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    dhaInfoPrint("Running MGMT CCB initialize")
    rc = clAmsMgmtClientApi.clAmsMgmtCCBInitialize(mgmtHandle, ctypes.byref(ccbHandle))
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
    entity = clAmsEntities.ClAmsEntityT()
    pEntityConfig = ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT)()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SG".format(pBaseName))
    rc = clAmsMgmtClientApi.clAmsMgmtEntityGetConfig(mgmtHandle, ctypes.byref(entity), ctypes.byref(pEntityConfig))
    clHeapApi.clHeapFree(pEntityConfig)
    
    return rc

def dhaSgCreate(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SG".format(pBaseName))
    dhaInfoPrint("Creating SG [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntityCreate(ccbHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SG create returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSiCreate(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SI".format(pBaseName))
    dhaInfoPrint("Creating SI [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntityCreate(ccbHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SI create returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaCsiCreate(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}CSI".format(pBaseName))
    dhaInfoPrint("Creating CSI [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntityCreate(ccbHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("CSI create returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSuCreate(mgmtHandle, ccbHandle, idx):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SU{1}".format(pBaseName, idx))
    dhaInfoPrint("Creating SU [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntityCreate(ccbHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SU create returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaCompCreate(mgmtHandle, ccbHandle, idx):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}{1}".format(NEW_COMP_PREFIX, idx))
    dhaInfoPrint("Creating COMP [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntityCreate(ccbHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("COMP create returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaCommit(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME

    dhaInfoPrint("CCB Commit")
    rc = clAmsMgmtClientApi.clAmsMgmtCCBCommit(ccbHandle)
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
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}{1}".format(NEW_COMP_PREFIX, idx))
    dhaInfoPrint("Delete COMP [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntityDelete(ccbHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("COMP delete returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSuDelete(mgmtHandle, ccbHandle, idx):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SU{1}".format(pBaseName, idx))
    dhaInfoPrint("Delete SU [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntityDelete(ccbHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SU delte returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaCsiDelete(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}CSI".format(pBaseName))
    dhaInfoPrint("Delete CSI [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntityDelete(ccbHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("CSI delete returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSiDelete(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SI".format(pBaseName))
    dhaInfoPrint("Delete SI [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntityDelete(ccbHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SI delete returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSgDelete(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SG".format(pBaseName))
    dhaInfoPrint("Delete SG [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntityDelete(ccbHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SG delete returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

#
# Config Filling Functions
#

def dhaSgSetSu(mgmtHandle, ccbHandle, sgEntity, suIdx):
    targetEntity = clAmsEntities.ClAmsEntityT()
    targetEntity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU.value
    clCommon.clNameSet(ctypes.byref(targetEntity.name), "{0}SU{1}".format(BASE_NAME, suIdx))
    dhaInfoPrint("SG set SU [%s]", targetEntity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBSetSGSUList(ccbHandle, ctypes.byref(sgEntity), ctypes.byref(targetEntity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SG set SU returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, BASE_NAME, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSgConfigFill(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()
    targetEntity = clAmsEntities.ClAmsEntityT()
    pEntityConfig = ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT)()

    sgConfig = clAmsEntities.ClAmsSGConfigT()
    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SG".format(pBaseName))

    dhaInfoPrint("SG config get [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityGetConfig(mgmtHandle, ctypes.byref(entity), ctypes.byref(pEntityConfig))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SG config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    libc.memcpy(ctypes.byref(sgConfig), pEntityConfig, ctypes.sizeof(sgConfig))
    clHeapApi.clHeapFree(pEntityConfig)

    # Fill SG SI list
    targetEntity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI.value
    clCommon.clNameSet(ctypes.byref(targetEntity.name), "{0}SI".format(pBaseName))
    dhaInfoPrint("SG set SI [%s]", targetEntity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBSetSGSIList(ccbHandle, ctypes.byref(entity), ctypes.byref(targetEntity))
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
    entity = clAmsEntities.ClAmsEntityT()
    targetEntity = clAmsEntities.ClAmsEntityT()
    pEntityConfig = ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT)()

    siConfig = clAmsEntities.ClAmsSIConfigT()
    bitMask = clCommon.ClUint64T(0)

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SI".format(pBaseName))
    dhaInfoPrint("SI config get [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityGetConfig(mgmtHandle, ctypes.byref(entity), ctypes.byref(pEntityConfig))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SI config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    libc.memcpy(ctypes.byref(siConfig), pEntityConfig, ctypes.sizeof(siConfig))
    clHeapApi.clHeapFree(pEntityConfig)

    siConfig.numCSIs = 1
    siConfig.numStandbyAssignments = 1

    bitMask.value |= (clAmsMgmtCommon.SI_CONFIG_NUM_CSIS
                      | clAmsMgmtCommon.SI_CONFIG_NUM_STANDBY_ASSIGNMENTS)
    dhaInfoPrint("SI config set [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntitySetConfig(ccbHandle, ctypes.byref(siConfig.entity), bitMask)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SI config set returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    # Fill SI CSI list
    targetEntity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI.value
    clCommon.clNameSet(ctypes.byref(targetEntity.name), "{0}CSI".format(pBaseName))
    dhaInfoPrint("SI set CSI [%s]", targetEntity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBSetSICSIList(ccbHandle, ctypes.byref(entity), ctypes.byref(targetEntity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SI set CSI returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    # Commit
    return dhaCommit(mgmtHandle, ccbHandle)

def dhaCsiConfigFill(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()
    pEntityConfig = ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT)()

    csiConfig = clAmsEntities.ClAmsCSIConfigT()
    bitMask = clCommon.ClUint64T(0)

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_CSI.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}CSI".format(pBaseName))
    dhaInfoPrint("CSI config get [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityGetConfig(mgmtHandle, ctypes.byref(entity), ctypes.byref(pEntityConfig))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("CSI config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    libc.memcpy(ctypes.byref(csiConfig), pEntityConfig, ctypes.sizeof(csiConfig))
    clHeapApi.clHeapFree(pEntityConfig)

    # Set CSI type
    bitMask.value |= clAmsMgmtCommon.CSI_CONFIG_TYPE
    typeName = "{0}Type".format(entity.name.__str__())
    clCommon.clNameSet(ctypes.byref(csiConfig.type), typeName)
    dhaInfoPrint("CSI type set [%s]", csiConfig.type.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntitySetConfig(ccbHandle, ctypes.byref(csiConfig.entity), bitMask)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("CSI type set returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    # Set CSI NVP list
    nvp = clAmsEntities.ClAmsCSINameValuePairT()
    clCommon.clNameSet(ctypes.byref(nvp.paramName), "model")
    clCommon.clNameSet(ctypes.byref(nvp.paramValue), "twoN")
    clCommon.clNameCopy(ctypes.byref(nvp.csiName), ctypes.byref(entity.name))

    dhaInfoPrint("CSI set nvplist")
    rc = clAmsMgmtClientApi.clAmsMgmtCCBCSISetNVP(ccbHandle, ctypes.byref(entity), ctypes.byref(nvp))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("CSI set nvplist returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    return dhaCommit(mgmtHandle, ccbHandle)

def dhaNodeSetSu(mgmtHandle, ccbHandle, nodeEntity, suIdx):
    targetEntity = clAmsEntities.ClAmsEntityT()
    targetEntity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU.value
    clCommon.clNameSet(ctypes.byref(targetEntity.name), "{0}SU{1}".format(BASE_NAME, suIdx))
    dhaInfoPrint("Node set SU [%s]", targetEntity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBSetNodeSUList(ccbHandle, ctypes.byref(nodeEntity), ctypes.byref(targetEntity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("Node set SU returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, BASE_NAME, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaNodeConfigFill(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()
    pEntityConfig = ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT)()

    nodeConfig = clAmsEntities.ClAmsNodeConfigT()
    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_NODE.value
    clCommon.clNameSet(ctypes.byref(entity.name), WORKER0)
    dhaInfoPrint("NODE config get [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityGetConfig(mgmtHandle, ctypes.byref(entity), ctypes.byref(pEntityConfig))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("NODE config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    libc.memcpy(ctypes.byref(nodeConfig), pEntityConfig, ctypes.sizeof(nodeConfig))
    clHeapApi.clHeapFree(pEntityConfig)

    # Set Node SU list with redundant SUs
    rc = dhaNodeSetSu(mgmtHandle, ccbHandle, entity, 0)
    if rc != clCommonErrors.CL_OK: return rc

    clCommon.clNameSet(ctypes.byref(entity.name), WORKER1)
    rc = dhaNodeSetSu(mgmtHandle, ccbHandle, entity, 1)
    if rc != clCommonErrors.CL_OK: return rc

    return dhaCommit(mgmtHandle, ccbHandle)

def dhaSuSetComp(mgmtHandle, ccbHandle, suConfig, bitMask, suIdx):
    pBaseName = BASE_NAME
    targetEntity = clAmsEntities.ClAmsEntityT()

    clCommon.clNameSet(ctypes.byref(suConfig.entity.name), "{0}SU{1}".format(pBaseName, suIdx))

    dhaInfoPrint("SU config set [%s]", suConfig.entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntitySetConfig(ccbHandle, ctypes.byref(suConfig.entity), bitMask)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SU config set returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    targetEntity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP.value
    clCommon.clNameSet(ctypes.byref(targetEntity.name), "{0}{1}".format(NEW_COMP_PREFIX, suIdx))
    dhaInfoPrint("SU [%s] add comp [%s]", suConfig.entity.name.value, targetEntity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBSetSUCompList(ccbHandle, ctypes.byref(suConfig.entity), ctypes.byref(targetEntity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SU add comp returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSuConfigFill(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()
    pEntityConfig = ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT)()

    suConfig = clAmsEntities.ClAmsSUConfigT()
    bitMask = clCommon.ClUint64T()
    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SU0".format(pBaseName))
    dhaInfoPrint("SU config get [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityGetConfig(mgmtHandle, ctypes.byref(entity), ctypes.byref(pEntityConfig))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("SU config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    libc.memcpy(ctypes.byref(suConfig), pEntityConfig, ctypes.sizeof(suConfig))
    clHeapApi.clHeapFree(pEntityConfig)

    suConfig.numComponents = 1
    bitMask.value |= clAmsMgmtCommon.SU_CONFIG_NUM_COMPONENTS

    rc = dhaSuSetComp(mgmtHandle, ccbHandle, suConfig, bitMask, 0)
    if rc != clCommonErrors.CL_OK: return rc
    rc = dhaSuSetComp(mgmtHandle, ccbHandle, suConfig, bitMask, 1)
    if rc != clCommonErrors.CL_OK: return rc

    return dhaCommit(mgmtHandle, ccbHandle)

def dhaCompSetConfig(mgmtHandle, ccbHandle, compConfig, bitMask, compIdx):
    pBaseName = BASE_NAME
    clCommon.clNameSet(ctypes.byref(compConfig.entity.name), "{0}{1}".format(NEW_COMP_PREFIX, compIdx))

    dhaInfoPrint("Comp config set [%s]", compConfig.entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtCCBEntitySetConfig(ccbHandle, ctypes.byref(compConfig.entity), bitMask)
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("Comp config set returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaCompConfigFill(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()
    pEntityConfig = ctypes.POINTER(clAmsEntities.ClAmsEntityConfigT)()

    compConfig = clAmsEntities.ClAmsCompConfigT()
    bitMask = clCommon.ClUint64T()
    supportedCSIType = clCommon.ClNameT("")

    clCommon.clNameSet(ctypes.byref(entity.name), "{0}0".format(NEW_COMP_PREFIX))
    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_COMP.value
    dhaInfoPrint("COMP config get [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityGetConfig(mgmtHandle, ctypes.byref(entity), ctypes.byref(pEntityConfig))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("COMP config get returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    libc.memcpy(ctypes.byref(compConfig), pEntityConfig, ctypes.sizeof(compConfig))
    clHeapApi.clHeapFree(pEntityConfig)

    bitMask.value |= (clAmsMgmtCommon.COMP_CONFIG_CAPABILITY_MODEL
                      | clAmsMgmtCommon.COMP_CONFIG_TIMEOUTS
                      | clAmsMgmtCommon.COMP_CONFIG_RECOVERY_ON_TIMEOUT)

    compConfig.capabilityModel = clAmsTypes.eClAmsCompCapModelT.CL_AMS_COMP_CAP_X_ACTIVE_OR_Y_STANDBY.value
    compConfig.timeouts.instantiate = 30000
    compConfig.timeouts.terminate = 30000
    compConfig.timeouts.cleanup = 30000
    compConfig.timeouts.quiescingComplete = 30000
    compConfig.timeouts.csiSet = 30000
    compConfig.timeouts.csiRemove = 30000
    compConfig.timeouts.instantiateDelay = 10000
    compConfig.recoveryOnTimeout = clAmsTypes.eClAmsRecoveryT.CL_AMS_RECOVERY_COMP_FAILOVER.value

    bitMask.value |= clAmsMgmtCommon.COMP_CONFIG_SUPPORTED_CSI_TYPE

    if compConfig.pSupportedCSITypes:
        clHeapApi.clHeapFree(compConfig.pSupportedCSITypes)

    compConfig.numSupportedCSITypes = 1
    compConfig.pSupportedCSITypes.contents = supportedCSIType

    clCommon.clNameSet(ctypes.byref(supportedCSIType), "{0}CSIType".format(pBaseName))

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
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SU{1}".format(pBaseName, suIdx))

    dhaInfoPrint("LockA [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityLockAssignment(mgmtHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockA returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    dhaInfoPrint("Unlock [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityUnlock(mgmtHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("Unlock returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    return clCommonErrors.CL_OK

def dhaSiUnlock(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SI".format(pBaseName))

    dhaInfoPrint("Unlock SI [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityUnlock(mgmtHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("Unlock returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    return clCommonErrors.CL_OK

def dhaSgUnlock(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SG".format(pBaseName))

    dhaInfoPrint("LockA SG [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityLockAssignment(mgmtHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockA returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc

    dhaInfoPrint("Unlock SG [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityUnlock(mgmtHandle, ctypes.byref(entity))
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
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SU.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SU{1}".format(pBaseName, suIdx))

    dhaInfoPrint("LockA [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityLockAssignment(mgmtHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockA returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    
    dhaInfoPrint("LockI [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityLockInstantiation(mgmtHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockI returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSiLockA(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SI.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SI".format(pBaseName))

    dhaInfoPrint("LockA SI [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityLockAssignment(mgmtHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockA returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    return clCommonErrors.CL_OK

def dhaSgLockI(mgmtHandle, ccbHandle):
    pBaseName = BASE_NAME
    entity = clAmsEntities.ClAmsEntityT()

    entity.type = clAmsEntities.eClAmsEntityTypeT.CL_AMS_ENTITY_TYPE_SG.value
    clCommon.clNameSet(ctypes.byref(entity.name), "{0}SG".format(pBaseName))

    dhaInfoPrint("LockA SG [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityLockAssignment(mgmtHandle, ctypes.byref(entity))
    if rc != clCommonErrors.CL_OK:
        dhaErrorPrint("LockA returned [%#x]", rc)
        out2(ccbHandle, mgmtHandle, pBaseName, rc)
        return rc
    
    dhaInfoPrint("LockI SG [%s]", entity.name.value)
    rc = clAmsMgmtClientApi.clAmsMgmtEntityLockInstantiation(mgmtHandle, ctypes.byref(entity))
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