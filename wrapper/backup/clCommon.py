import clUtils
import saAis
import ctypes
import clLib
import enum

CL_TRUE = 1
CL_FALSE = 0

CL_YES = 1
CL_NO = 0

CL_ENABLE = 1
CL_DISABLE = 0

ClStatusT = saAis.SaInt32T
class eClStatusT(clUtils.CEnum):
    CL_STATUS_DOWN = 0,
    CL_STATUS_UP   = 1

def CL_MIN(a, b):
    return a if a < b else b

def CL_MAX(a, b):
    return a if a > b else b

def CL_ROUNDUP(val: int, base: int) -> int:
    return ((val + base - 1) // base) * base

def CL_ROUNDDOWN(val: int, base: int) -> int:
    return (val // base) * base

def CL_SIZEOF_ARRAY(array_name) -> int:
    return len(array_name)
ClUint64T = ctypes.c_ulonglong
ClInt64T = ctypes.c_longlong

ClUint32T = ctypes.c_uint
ClInt32T = ctypes.c_int
ClUint16T = ctypes.c_ushort
ClInt16T = ctypes.c_short
ClUint8T = ctypes.c_ubyte
ClInt8T = ctypes.c_byte
ClCharT = ctypes.c_char
ClFdT = ctypes.c_uint

ClWordT = ctypes.c_ulong
ClBoolT = ctypes.c_ushort
ClPidT = ctypes.c_ulong

CL_MICRO_TO_NANO = 1000
CL_MILLI_TO_MICRO = 1000
CL_SEC_TO_MILLI = 1000
CL_MILLI_TO_NANO = CL_MICRO_TO_NANO * CL_MILLI_TO_MICRO
CL_SEC_TO_NANO = CL_MILLI_TO_NANO * CL_SEC_TO_MILLI
CL_TIME_END = 0x7fffffffffffffff
CL_TIME_FOREVER = 0x7fffffffffffffff

ClTimeT = ClInt64T
ClHandleT = ClUint64T
ClSizeT = ClUint64T
ClOffsetT = ClInt64T
ClInvocationT = ClUint64T
ClSelectionObjectT = ClUint64T
ClNtfIdentifierT = ClUint64T
ClAddrT = ctypes.POINTER(ClInt8T)
ClPtrT = ctypes.c_void_p

ClRcT = ClUint32T

ClCallbackT = ctypes.CFUNCTYPE(ClRcT, ClPtrT)

class _DWord(ctypes.Structure):
    _fields_ = [
        ("high", ClUint32T),
        ("low", ClUint32T)
    ]

class ClUnion64T(ctypes.Union):
    _fields_ = [
        ("DWord", _DWord),
        ("dWords", 2 * ClUint32T),
        ("words", 4 * ClUint16T),
        ("bytes", 8 * ClInt8T)
    ]

CL_MAX_NAME_LENGTH = 256

class ClNameT(ctypes.Structure):
    _fields_ = [
        ("length", ClUint16T),
        ("value", CL_MAX_NAME_LENGTH * ClCharT)
    ]

def clNameSet(name, str):
    """
    arg types:
        ClNameT* name,
        const char* str
    """
    clLib.libmw_so.clNameSet(ctypes.byref(name), ctypes.byref(str))

def clNameCopy(nameOut, nameIn):
    """
    arg types:
        ClNameT* nameOut,
        const ClNameT *nameIn
    """
    clLib.libmw_so.clNameCopy(ctypes.byref(nameOut), ctypes.byref(nameIn))

def clNameConcat(nameOut, prefix, separator, suffix):
    """
    arg types:
        ClNameT* nameOut,
        const ClNameT *prefix,
        const char* separator,
        const ClNameT *suffix
    """
    clLib.libmw_so.clNameConcat(
        ctypes.byref(nameOut),
        ctypes.byref(prefix),
        ctypes.byref(separator),
        ctypes.byref(suffix)
    )

def clStrdup(str):
    """
    arg types:
        const ClCharT *str
    """
    clLib.libmw_so.clStrdup(ctypes.byref(str))

def clParseEnvBoolean(envvar):
    """
    arg types:
        ClCharT *envvar
    """
    clLib.libmw_so.clParseEnvBoolean(ctypes.byref(envvar))

def clParseEnvStr(envvar):
    """
    arg types:
        const ClCharT *envvar
    """
    clLib.libmw_so.clParseEnvStr(
        ctypes.byref(envvar)
    )

def clCreatePipe(fds, numMsgs, msgSize):
    """
    arg types:
        ClInt32T fds[2],
        ClUint32T numMsgs,
        ClUint32T msgSize
    """
    clLib.libmw_so.clCreatePipe(ctypes.byref(fds), numMsgs, msgSize)

def clBinaryPower(size):
    """
    arg types:
        ClUint32T size
    """
    clLib.libmw_so.clBinaryPower(size)

class ClVersionT(ctypes.Structure):
    _fields_ = [
        ("releaseCode", ClUint8T),
        ("majorVersion", ClUint8T),
        ("minorVersion", ClUint8T),
    ]

ClDispatchFlagsT = saAis.SaInt32T
class eClDispatchFlagsT(clUtils.CEnum):
    CL_DISPATCH_ONE         = 1,
    CL_DISPATCH_ALL         = 2,
    CL_DISPATCH_BLOCKING    = 3,

CL_FORCED_TO_8BITS = 0xff
CL_FORCED_TO_16BITS = 0xffff
CL_FORCED_TO_32BITS = 0xffffffff
CL_BITS_PER_BYTE = 8
def CL_BIT(X): return (0x1 << (X))

ClCompIdT = saAis.SaInt32T
class eClCompIdT(clUtils.CEnum):
    # Unspecified
    CL_CID_UNSPECIFIED  = 0x0,

    # OS Abstraction Layer    
    CL_CID_OSAL         = 0x01,
    
    # Hardware Abstraction Layer
    CL_CID_HAL          = 0x02,
    
    # Database Abstraction Layer    
    CL_CID_DBAL         = 0x03,
    
    # Execution Object    
    CL_CID_EO           = 0x04,
    
    # Intelligent Object Communication   
    CL_CID_IOC          = 0x05,
    
    # Remote Method Dispatch    
    CL_CID_RMD          = 0x06,
    
    # Name Service    
    CL_CID_NAMES        = 0x07,
    
    # Timer
    CL_CID_TIMER        = 0x08,
    
    # Shared Memory Support
    CL_CID_SHM          = 0x09,
    
    # Distributed Shared Memory
    CL_CID_DSHM         = 0x0a,
    
    # Logging
    CL_CID_LOG          = 0x0b,
    
    # Message Service
    CL_CID_MSG          = 0x0c,
    
    # Diagnostics
    CL_CID_DIAG         = 0x0d,
    
    # Debug
    CL_CID_DEBUG        = 0x0e,
    
    # Component Management
    CL_CID_CPM          = 0x0f,
    
    # Capability Management (for future use)
    CL_CID_CAP          = 0x10,
    
    # Resource Management (for future use)
    CL_CID_RES          = 0x11,
    
    # Group Membership Service
    CL_CID_GMS          = 0x12,
    
    # Event Service
    CL_CID_EVENTS       = 0x13,
    
    # Distributed Locking (for future use)    
    CL_CID_DLOCK        = 0x14,
    
    # Transactions    
    CL_CID_TXN          = 0x15,
    
    # Checkpointing Service*/    
    CL_CID_CKPT         = 0x16,
    
    # Clovis Object Registry    
    CL_CID_COR          = 0x17,
    
    # Containers    
    CL_CID_CNT          = 0x18,
    
    # Distributed Containers (for future use)    
    CL_CID_DCNT         = 0x19,
    
    # Resilient Containers (for future use)    
    CL_CID_RCNT         = 0x1a,
    
    # Alarm Manager    
    CL_CID_ALARMS       = 0x1b,
    
    # Policy Engine    
    CL_CID_POLICY       = 0x1c,
    
    # Rule Base Engine    
    CL_CID_RULE         = 0x1d,
    
    # Scripting Engine (for future use)    
    CL_CID_SCRIPTING    = 0x1e,
    
    # Chassis Manager    
    CL_CID_CM           = 0x1f,
    
    # Hardware Platform Interface    
    CL_CID_HPI          = 0x20,
    
    # Fault Management    
    CL_CID_FAULTS       = 0x21,
    
    # Availability Management Service*/    
    CL_CID_AMS          = 0x22,
    
    # Mediation Library    
    CL_CID_MED          = 0x23,
    
    # Buffer Management    
    CL_CID_BUFFER       = 0x24,
    
    # Queue Management    
    CL_CID_QUEUE        = 0x25,
    
    # Circular List Management    
    CL_CID_CLIST        = 0x26,
    
    # SNMP Agent    
    CL_CID_SNMP         = 0x27,
    
    # Name Service    
    CL_CID_NS           = 0x28,
    
    # Object Manager    
    CL_CID_OM           = 0x29,
    
    # Pool Management    
    CL_CID_POOL         = 0x2a,
    
    # Common Diagnostics (for future use)    
    CL_CID_CD           = 0x2b,
    
    # Diagnostics Manager (for future use)    
    CL_CID_DM           = 0x2c,
    
    # OAMP RT parser    
    CL_CID_OAMP_RT      = 0x2d,
    
    # Provisioning Manager        
    CL_CID_PROV         = 0x2e,
    
    # Upgrade Manager (for future use)    
    CL_CID_UM           = 0x2f,
    
    # Handle Database    
    CL_CID_HANDLE       = 0x30,
    
    # Version Checker Library    
    CL_CID_VERSION      = 0x31,
    
    # XDR Library   
    CL_CID_XDR          = 0x32,
    
    # IDL   
    CL_CID_IDL          = 0x33,
    
    # Heap Management    
    CL_CID_HEAP         = 0x34,
    
    # Memory Management        
    CL_CID_MEM          = 0x35,
    
    # Parser            
    CL_CID_PARSER       = 0x36,
    
    CL_CID_BACKING_STORAGE = 0x37,

    CL_CID_JOB          = 0x38,
    CL_CID_JOBQUEUE     = 0x38,

    CL_CID_THREADPOOL   = 0x39,
    CL_CID_TASKPOOL     = 0x39,

    # Bitmap Management    
    CL_CID_BITMAP       = 0x3a,

    
    # Add more CID here if required
    CL_CID_LEAKY_BUCKET = 0x3b,

    # Mso Services Management
    CL_CID_MSO          = 0x3c,

    # Performance Management 
    CL_CID_PM          = 0x3d,

    # SAF Notification service
    CL_CID_NF          = 0x3e,

    # This will help validate if needs to be
    CL_CID_MAX          = enum.auto()

class ClWaterMarkT(ctypes.Structure):
    _fields_ = [
        ("lowLimit", ClUint64T),
        ("highLimit", ClUint64T),
    ]

ClEoWaterMarkFlagT = saAis.SaInt32T
class eClEoWaterMarkFlagT(clUtils.CEnum):
    CL_WM_LOW_LIMIT = 0,
    CL_WM_HIGH_LIMIT = 1

ClWaterMarkIdT = saAis.SaInt32T
class eClWaterMarkIdT(clUtils.CEnum):
    CL_WM_LOW = 0,
    CL_WM_HIGH = 1,
    CL_WM_MED = 2,
    CL_WM_SENDQ = 3,
    CL_WM_RECVQ = 4,
    CL_WM_MAX = 5

#define CL_WEAK __attribute__((weak))

CL_EO_ACTION_CUSTOM = (1<<0)
CL_EO_ACTION_EVENT = (1<<1)
CL_EO_ACTION_LOG = (1<<2)
CL_EO_ACTION_NOT = (1<<3)
CL_EO_ACTION_MAX = (1<<31)     # ClUnt8T type bieng used for bitMap 

class ClEoActionInfoT(ctypes.Structure):
    _fields_ = [
        ("bitMap", ClUint32T)
    ]

ClEoActionArgListT = ctypes.POINTER(ClPtrT)

class ClStringT(ctypes.Structure):
    _fields_ = [
        ("length", ClUint32T),
        ("pValue", ctypes.c_char_p)
    ]

def clStringDup(str):
    """
    arg types:
        const ClStringT *str

    return type:
        ClStringT *
    """
    return clLib.libmw_so.clStringDup(ctypes.byref(str))

# def clNamePrintf(name, *va_args):
#     """
#     Wrapper for a macro
#     arg types:
#         const ClNameT *name

#     return type:
#         ClStringT *
#     """
#     cVarArgs, argTypes = clUtils.handleVarArgs(*va_args)
#     libc.snprintf.argtypes = [ctypes.c_char_p, ctypes.c_size_t] + argTypes
#     name.length = libc.snprintf(ctypes.byref(name.value), CL_MAX_NAME_LENGTH - 1, *cVarArgs)
#     name.value[CL_MIN(name.length, CL_MAX_NAME_LENGTH - 1)] = '\0'
    

