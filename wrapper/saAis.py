import ctypes
import clUtils

SaInt8T = ctypes.c_char
SaInt16T = ctypes.c_short
SaInt32T = ctypes.c_int
SaInt64T = ctypes.c_longlong
SaUint8T = ctypes.c_ubyte
SaUint16T = ctypes.c_ushort
SaUint32T = ctypes.c_uint
SaUint64T = ctypes.c_ulonglong

SaFloatT = ctypes.c_float
SaDoubleT = ctypes.c_double
SaStringT = ctypes.c_char_p

SaTimeT = SaInt64T
SaInvocationT = SaUint64T
SaSizeT = SaUint64T
SaOffsetT = SaUint64T
SaSelectionObjectT = SaUint64T

SA_TIME_END = 0x7FFFFFFFFFFFFFFF
SA_TIME_BEGIN = 0x0
SA_TIME_UNKNOWN = 0x8000000000000000

SA_TIME_ONE_MICROSECOND = 1000
SA_TIME_ONE_MILLISECOND = 1000000
SA_TIME_ONE_SECOND = 1000000000
SA_TIME_ONE_MINUTE = 60000000000
SA_TIME_ONE_HOUR = 3600000000000
SA_TIME_ONE_DAY = 86400000000000
SA_TIME_MAX = SA_TIME_END

SA_MAX_NAME_LENGTH = 256

SA_TRACK_CURRENT = 0x01
SA_TRACK_CHANGES = 0x02
SA_TRACK_CHANGES_ONLY = 0x04
SA_TRACK_LOCAL = 0x08
SA_TRACK_START_STEP = 0x10
SA_TRACK_VALIDATE_STEP = 0x20

SaBoolT = SaInt32T
class eSaBoolT(clUtils.CEnum):
    SA_FALSE = 0
    SA_TRUE = 1

SaDispatchFlagsT = SaInt32T
class eSaDispatchFlagsT(clUtils.CEnum):
    A_DISPATCH_ONE = 1
    SA_DISPATCH_ALL = 2
    SA_DISPATCH_BLOCKING = 3

SaAisErrorT = SaInt32T
class eSaAisErrorT(clUtils.CEnum):
    SA_AIS_OK = 1
    SA_AIS_ERR_LIBRARY = 2
    SA_AIS_ERR_VERSION = 3
    SA_AIS_ERR_INIT = 4
    SA_AIS_ERR_TIMEOUT = 5
    SA_AIS_ERR_TRY_AGAIN = 6
    SA_AIS_ERR_INVALID_PARAM = 7
    SA_AIS_ERR_NO_MEMORY = 8
    SA_AIS_ERR_BAD_HANDLE = 9
    SA_AIS_ERR_BUSY = 10
    SA_AIS_ERR_ACCESS = 11
    SA_AIS_ERR_NOT_EXIST = 12
    SA_AIS_ERR_NAME_TOO_LONG = 13
    SA_AIS_ERR_EXIST = 14
    SA_AIS_ERR_NO_SPACE = 15
    SA_AIS_ERR_INTERRUPT =16
    SA_AIS_ERR_NAME_NOT_FOUND = 17
    SA_AIS_ERR_NO_RESOURCES = 18
    SA_AIS_ERR_NOT_SUPPORTED = 19
    SA_AIS_ERR_BAD_OPERATION = 20
    SA_AIS_ERR_FAILED_OPERATION = 21
    SA_AIS_ERR_MESSAGE_ERROR = 22
    SA_AIS_ERR_QUEUE_FULL = 23
    SA_AIS_ERR_QUEUE_NOT_AVAILABLE = 24
    SA_AIS_ERR_BAD_FLAGS = 25
    SA_AIS_ERR_TOO_BIG = 26
    SA_AIS_ERR_NO_SECTIONS = 27
    SA_AIS_ERR_NO_OP = 28
    SA_AIS_ERR_REPAIR_PENDING = 29
    SA_AIS_ERR_NO_BINDINGS = 30
    SA_AIS_ERR_UNAVAILABLE = 31
    SA_AIS_ERR_CAMPAIGN_ERROR_DETECTED = 32
    SA_AIS_ERR_CAMPAIGN_PROC_FAILED = 33
    SA_AIS_ERR_CAMPAIGN_CANCELED = 34
    SA_AIS_ERR_CAMPAIGN_FAILED = 35
    SA_AIS_ERR_CAMPAIGN_SUSPENDED = 36
    SA_AIS_ERR_CAMPAIGN_SUSPENDING = 37
    SA_AIS_ERR_ACCESS_DENIED = 38
    SA_AIS_ERR_NOT_READY = 39
    SA_AIS_ERR_DEPLOYMENT = 40

SaServicesT = SaInt32T
class eSaServicesT(clUtils.CEnum):
    SA_SVC_HPI  =  1
    SA_SVC_AMF  =  2
    SA_SVC_CLM  =  3
    SA_SVC_CKPT =  4
    SA_SVC_EVT  =  5
    SA_SVC_MSG  =  6
    SA_SVC_LCK  =  7
    SA_SVC_IMMS =  8 
    SA_SCV_LOG  =  9
    SA_SVC_NTF  =  10
    SA_SVC_NAM  =  11
    SA_SVC_TMR  =  12
    SA_SVC_SMF  =  13
    SA_SVC_SEC  =  14
    SA_SVC_PLM  =  15

class SaAnyT(ctypes.Structure):
    _fields_ = [
		("bufferSize", SaSizeT),
		("bufferAddr", SaUint8T),
	]

class SaNameT(ctypes.Structure):
    _fields_ = [
		("length", SaUint16T),
		("value", SaInt8T * SA_MAX_NAME_LENGTH),
	]
    def __init__(self, name):
        name = name.encode('utf-8')
        super(SaNameT, self).__init__(len(name), name)

    def __str__(self):
        return self.value.decode('utf-8')

class SaVersionT(ctypes.Structure):
    _fields_ = [
		("releaseCode", SaUint8T),
		("majorVersion", SaUint8T),
        ("minorVersion", SaUint8T),
	]

class eSaLimitValueT(ctypes.Structure):
    _fields_ = [
		("int64Value", SaInt64T),
		("uint64Value", SaUint64T),
        ("timeValue", SaTimeT),
        ("floatValue", SaFloatT),
        ("doubleValue", SaDoubleT),
	]
