import clCommon
import saAis
import clUtils
import clOsalApi
import clIocApi

import ctypes

_clEoBasicLibArray = ctypes.c_int * 9
_clEoClientLibArray = ctypes.c_int * 13

ClEoIdT = clCommon.ClUint64T

CL_EO_MAX_NAME_LEN = 32

ClEoPollingTypeT = saAis.SaInt32T
class eClEoPollingTypeT(clUtils.CEnum):
    CL_EO_DONT_POLL    = 0,
    CL_EO_BUSY_POLL    = 1,
    CL_EO_DEFAULT_POLL = 2

class ClEoSchedFeedBackT(ctypes.Structure):
    _fields_ = [
        ("freq", ClEoPollingTypeT),
        ("status", clCommon.ClRcT)
    ]

ClEoApplicationTypeT = saAis.SaInt32T
class eClEoApplicationTypeT(clUtils.CEnum):
    CL_EO_USE_THREAD_FOR_RECV   = clCommon.CL_TRUE,
    CL_EO_USE_THREAD_FOR_APP    = clCommon.CL_FALSE

ClEoStateT = saAis.SaInt32T
class eClEoStateT(clUtils.CEnum):
    CL_EO_STATE_INIT        = 0x1,
    CL_EO_STATE_ACTIVE      = 0x2,
    CL_EO_STATE_STDBY       = 0x4,
    CL_EO_STATE_SUSPEND     = 0x8,
    CL_EO_STATE_STOP        = 0x10,
    CL_EO_STATE_KILL        = 0x20,
    CL_EO_STATE_RESUME      = 0x40,
    CL_EO_STATE_FAILED      = 0x80,
    CL_EO_STATE_THREAD_SAFE = 0x100,
    CL_EO_STATE_BITS        = 9,

ClEoAppCreateCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, clCommon.ClUint32T, ctypes.POINTER(ctypes.POINTER(clCommon.ClCharT)))
ClEoAppStateChgCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT, ClEoStateT)
ClEoAppDeleteCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT)
ClEoAppHealthCheckCallbackT = ctypes.CFUNCTYPE(clCommon.ClRcT)
ClEoCustomActionT = ctypes.CFUNCTYPE(clCommon.ClRcT, clCommon.ClCompIdT, clCommon.ClWaterMarkIdT, ctypes.POINTER(clCommon.ClWaterMarkT), clCommon.ClEoWaterMarkFlagT, clCommon.ClEoActionArgListT)

class ClEoConfigT(ctypes.Structure):
    _fields_ = [
        ("EOname", clCommon.ClCharT * CL_EO_MAX_NAME_LEN),
        ("pri", clOsalApi.ClOsalThreadPriorityT),
        ("noOfThreads", clCommon.ClUint32T),
        ("reqIocPort", clIocApi.ClIocPortT),
        ("maxNoClients", clCommon.ClUint32T),
        ("appType", ClEoApplicationTypeT),
        ("clEoCreateCallout", ClEoAppCreateCallbackT),
        ("clEoDeleteCallout", ClEoAppDeleteCallbackT),
        ("clEoStateChgCallout", ClEoAppStateChgCallbackT),
        ("clEoHealthCheckCallout", ClEoAppHealthCheckCallbackT),
        ("clEoCustomAction", ClEoCustomActionT),
        ("needSerialization", clCommon.ClBoolT)
    ]
