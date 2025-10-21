import clLib
import clUtils
import clCommon
import saAis
import ctypes

ClEoClientIdT = saAis.SaInt32T
class eClEoClientIdT(clUtils.CEnum):
    CL_EO_NATIVE_COMPONENT_TABLE_ID = 0,
    CL_EO_DEFAULT_SERVICE_TABLE_ID = 1,
    CL_EO_EO_MGR_CLIENT_TABLE_ID = 2,
    CL_EO_COR_CLIENT_TABLE_ID = 3,
    CL_EO_EVT_CLIENT_TABLE_ID = 4,
    CL_CPM_MGR_CLIENT_TABLE_ID = 5,
    CL_ALARM_CLIENT_TABLE_ID = 6,
    CL_DEBUG_CLIENT_TABLE_ID = 7,
    CL_TXN_CLIENT_TABLE_ID = 8,
    CL_AMS_MGMT_SERVER_TABLE_ID = 9,
    CL_AMS_MGMT_CLIENT_TABLE_ID = 10,
    CL_LOG_CLIENT_TABLE_ID = 11,
    CL_EO_CKPT_CLIENT_TABLE_ID = 12,
    CL_EO_RMD_CLIENT_TABLE_ID = 13,
    CL_AMS_ENTITY_TRIGGER_TABLE_ID = 14,
    CL_CPM_MGMT_CLIENT_TABLE_ID = 15,
    CL_MSG_CLIENT_TABLE_ID = 16,
    CL_MSG_CLIENT_SERVER_TABLE_ID = 17,
    CL_AMS_MGMT_SERVER_TABLE2_ID = 18,
    CL_EO_CLOVIS_RESERVED_CLIENTID_END  = 19

CL_EO_USER_CLIENT_ID_START = eClEoClientIdT.CL_EO_CLOVIS_RESERVED_CLIENTID_END

def clEoMyEoIocPortGet(pIocPort):
    """
    arg types:
        CL_OUT ClIocPortT *pIocPort

    return type:
        ClRcT
    """
    return clLib.libmw_so.clEoMyEoIocPortGet(pIocPort)