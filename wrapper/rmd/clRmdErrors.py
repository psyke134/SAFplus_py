import sys
sys.path.append("..")

from common import clCommonErrors, clCommon

def CL_RMD_RC(ERROR_CODE):
    return clCommonErrors.CL_RC(clCommon.eClCompIdT.CL_CID_RMD, ERROR_CODE)

CL_RMD_ERR_CONTINUE = CL_RMD_RC(clCommonErrors.CL_ERR_CONTINUE)
CL_RMD_ERR_INUSE = CL_RMD_RC(clCommonErrors.CL_ERR_INUSE)
