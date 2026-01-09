import sys
sys.path.append("..")

from common import clCommonErrors, clCommon

def CL_DEBUG_RC(ERROR_CODE):
    return clCommonErrors.CL_RC(clCommon.eClCompIdT.CL_CID_DEBUG, ERROR_CODE)

CL_DBG_ERR_CMD_NOT_FOUND = 0x100
CL_DBG_ERR_UNRECOGNIZED_CMD = 0x101
CL_DBG_ERR_INVALID_CTX = 0x102
CL_DBG_ERR_INVALID_PARAM = 0x103
CL_DBG_ERR_COMMON_ERROR = 0x104
