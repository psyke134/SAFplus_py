import sys
sys.path.append("..")

from utils import clUtils, libc, clLib
from common import saAis, clCommon

import ctypes

CL_OSAL_MIN_STACK_SIZE = 196608
CL_OSAL_NAME_MAX = 32

ClOsalSharedMutexFlagsT = clCommon.ClInt32T
class eClOsalSharedMutexFlagsT(clUtils.CEnum):
    CL_OSAL_SHARED_INVALID   = 0x0,
    CL_OSAL_SHARED_NORMAL    = 0x1,
    CL_OSAL_SHARED_SYSV_SEM  = 0x2,
    CL_OSAL_SHARED_POSIX_SEM = 0x4,
    CL_OSAL_SHARED_RECURSIVE = 0x8,
    CL_OSAL_SHARED_PROCESS   = 0x10,
    CL_OSAL_SHARED_ERROR_CHECK = 0x20

class ClSem(ctypes.Structure):
    _fields_ = [
        ("posSem", libc.sem_t),
        ("semId", ctypes.c_int),
        ("numSems", clCommon.ClInt32T)
    ]

class _shared_lock(ctypes.Union):
    _fields_ = [
        ("mutex", libc.pthread_mutex_t),
        ("sem", ClSem)
    ]

class ClOsalMutexT(ctypes.Structure):
    _fields_ = [
        ("flags", ClOsalSharedMutexFlagsT),
        ("shared_lock", _shared_lock)
    ]

ClOsalMutexAttrT = libc.pthread_mutexattr_t
ClOsalCondAttrT = libc.pthread_condattr_t

ClOsalSharedTypeT = clCommon.ClInt32T
class eClOsalSharedTypeT(clUtils.CEnum):
    CL_OSAL_PROCESS_PRIVATE = 0,
    CL_OSAL_PROCESS_SHARED = 1

ClOsalCondT = libc.pthread_cond_t

ClOsalTaskIdT = clCommon.ClUint64T

ClOsalMutexIdT = ctypes.POINTER(ClOsalMutexT)
ClOsalCondIdT = ctypes.POINTER(ClOsalCondT)
ClOsalSemIdT = clCommon.ClHandleT
ClOsalShmIdT = clCommon.ClUint32T
ClOsalPidT = clCommon.ClUint32T
ClOsalTaskDataT = clCommon.ClPtrT

ClNanoTimeT = libc.timespec

ClOsalProcessFuncT = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
ClOsalTaskKeyDeleteCallBackT = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

ClOsalSchedulePolicyT = clCommon.ClInt32T
class eClOsalSchedulePolicyT(clUtils.CEnum):
    CL_OSAL_SCHED_OTHER = 0,
    CL_OSAL_SCHED_FIFO = 1,
    CL_OSAL_SCHED_RR = 2,

ClOsalThreadPriorityT = clCommon.ClInt32T
class eClOsalThreadPriorityT(clUtils.CEnum):
    CL_OSAL_THREAD_PRI_NOT_APPLICABLE = 0,
    CL_OSAL_THREAD_PRI_HIGH = 160,
    CL_OSAL_THREAD_PRI_MEDIUM = 80,
    CL_OSAL_THREAD_PRI_LOW = 1

ClOsalProcessFlagT = clCommon.ClInt32T
class eClOsalProcessFlagT(clUtils.CEnum):
    CL_OSAL_PROCESS_WITH_NEW_SESSION = 1,
    CL_OSAL_PROCESS_WITH_NEW_GROUP = 2

ClOsalShmSecurityModeFlagT = clCommon.ClInt32T
class eClOsalShmSecurityModeFlagT(clUtils.CEnum):
    CL_OSAL_SHM_MODE_READ_USER      = 0x0100,
    CL_OSAL_SHM_MODE_READ_GROUP     = 0x0020,
    CL_OSAL_SHM_MODE_READ_OTHERS    = 0x0004,
    CL_OSAL_SHM_MODE_WRITE_USER     = 0x0080,
    CL_OSAL_SHM_MODE_WRITE_GROUP    = 0x0010,
    CL_OSAL_SHM_MODE_WRITE_OTHERS   = 0x0002

CL_OSAL_SHM_EXCEPTION_LENGTH = 2048

class ClOsalShmAreaDefT(ctypes.Structure):
    _fields_ = [
        ("exceptionInfo", clCommon.ClCharT * CL_OSAL_SHM_EXCEPTION_LENGTH)
    ]

def clOsalInitialize(pConfig):
    """
    arg types:
        ClPtrT pConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalInitialize(pConfig)


def clOsalFinalize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalFinalize()


# --- Task Management ---

def clOsalTaskCreateDetached(taskName, schedulePolicy, priority, stackSize, fpTaskFunction, pTaskFuncArgument):
    """
    arg types:
        ClCharT *taskName,
        ClOsalSchedulePolicyT schedulePolicy,
        ClUint32T priority,
        ClUint32T stackSize,
        void* (*fpTaskFunction)(void*),
        void* pTaskFuncArgument
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskCreateDetached(taskName, schedulePolicy, priority, stackSize, fpTaskFunction, pTaskFuncArgument)


def clOsalTaskCreateAttached(taskName, schedulePolicy, priority, stackSize, fpTaskFunction, pTaskFuncArgument, pTaskId):
    """
    arg types:
        ClCharT *taskName,
        ClOsalSchedulePolicyT schedulePolicy,
        ClUint32T priority,
        ClUint32T stackSize,
        void* (*fpTaskFunction)(void*),
        void* pTaskFuncArgument,
        ClOsalTaskIdT* pTaskId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskCreateAttached(taskName, schedulePolicy, priority, stackSize, fpTaskFunction, pTaskFuncArgument, pTaskId)


def clOsalTaskJoin(taskId):
    """
    arg types:
        ClOsalTaskIdT taskId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskJoin(taskId)


def clOsalTaskDelete(taskId):
    """
    arg types:
        ClOsalTaskIdT taskId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskDelete(taskId)


def clOsalTaskKill(taskId, sig):
    """
    arg types:
        ClOsalTaskIdT taskId,
        ClInt32T sig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskKill(taskId, sig)


def clOsalTaskDetach(taskId):
    """
    arg types:
        ClOsalTaskIdT taskId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskDetach(taskId)


def clOsalSelfTaskIdGet(pTaskId):
    """
    arg types:
        ClOsalTaskIdT* pTaskId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalSelfTaskIdGet(pTaskId)


def clOsalTaskNameGet(taskId, ppTaskName):
    """
    arg types:
        ClOsalTaskIdT taskId,
        ClCharT** ppTaskName
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskNameGet(taskId, ppTaskName)


def clOsalTaskPriorityGet(taskId, pTaskPriority):
    """
    arg types:
        ClOsalTaskIdT taskId,
        ClUint32T* pTaskPriority
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskPriorityGet(taskId, pTaskPriority)


def clOsalTaskPrioritySet(taskId, taskPriority):
    """
    arg types:
        ClOsalTaskIdT taskId,
        ClUint32T taskPriority
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskPrioritySet(taskId, taskPriority)


def clOsalTaskDelay(timeOut):
    """
    arg types:
        ClTimerTimeOutT timeOut
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskDelay(timeOut)


# --- Time Functions ---

def clOsalTimeOfDayGet(pTime):
    """
    arg types:
        ClTimerTimeOutT* pTime
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTimeOfDayGet(pTime)


def clOsalNanoTimeGet(pTime):
    """
    arg types:
        ClNanoTimeT* pTime
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalNanoTimeGet(pTime)


def clOsalStopWatchTimeGet():
    """
    arg types:
        void
    return type:
        ClTimeT
    """
    return clLib.libmw_so.clOsalStopWatchTimeGet()


# --- Mutex Functions (Unshared) ---

def clOsalMutexInit(pMutex):
    """
    arg types:
        ClOsalMutexT* pMutex
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexInit(pMutex)


def clOsalMutexErrorCheckInit(pMutex):
    """
    arg types:
        ClOsalMutexT* pMutex
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexErrorCheckInit(pMutex)


def clOsalMutexValueSet(mutexId, value):
    """
    arg types:
        ClOsalMutexIdT mutexId,
        ClInt32T value
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexValueSet(mutexId, value)


def clOsalMutexValueGet(mutexId, pValue):
    """
    arg types:
        ClOsalMutexIdT mutexId,
        ClInt32T *pValue
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexValueGet(mutexId, pValue)


# --- Mutex Functions (Shared/Process Shared) ---

def clOsalProcessSharedMutexInit(pMutex, flags, pKey, keyLen, value):
    """
    arg types:
        ClOsalMutexT* pMutex,
        ClOsalSharedMutexFlagsT flags,
        ClUint8T *pKey,
        ClUint32T keyLen,
        ClInt32T value
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalProcessSharedMutexInit(pMutex, flags, pKey, keyLen, value)


def clOsalSharedMutexCreate(pMutex, flags, pKey, keyLen, value):
    """
    arg types:
        ClOsalMutexIdT* pMutex,
        ClOsalSharedMutexFlagsT flags,
        ClUint8T *pKey,
        ClUint32T keyLen,
        ClInt32T value
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalSharedMutexCreate(pMutex, flags, pKey, keyLen, value)


def clOsalRecursiveMutexInit(pMutex):
    """
    arg types:
        ClOsalMutexT* pMutex
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalRecursiveMutexInit(pMutex)


# --- Mutex ID Functions ---

def clOsalMutexCreate(pMutexId):
    """
    arg types:
        ClOsalMutexIdT* pMutexId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexCreate(pMutexId)


def clOsalMutexErrorCheckCreate(pMutexId):
    """
    arg types:
        ClOsalMutexIdT* pMutexId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexErrorCheckCreate(pMutexId)


def clOsalMutexCreateAndLock(pMutexId):
    """
    arg types:
        ClOsalMutexIdT* pMutexId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexCreateAndLock(pMutexId)


def clOsalMutexLock(mutexId):
    """
    arg types:
        ClOsalMutexIdT mutexId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexLock(mutexId)


def clOsalMutexLockSilent(mutexId):
    """
    arg types:
        ClOsalMutexIdT mutexId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexLockSilent(mutexId)


def clOsalMutexUnlockNonDebug(mutexId):
    """
    arg types:
        ClOsalMutexIdT mutexId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexUnlockNonDebug(mutexId)


def clOsalMutexTryLock(mutexId):
    """
    arg types:
        ClOsalMutexIdT mutexId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexTryLock(mutexId)


def clOsalMutexUnlock(mutexId):
    """
    arg types:
        ClOsalMutexIdT mutexId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexUnlock(mutexId)


def clOsalMutexUnlockSilent(mutexId):
    """
    arg types:
        ClOsalMutexIdT mutexId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexUnlockSilent(mutexId)


def clOsalMutexDelete(mutexId):
    """
    arg types:
        ClOsalMutexIdT mutexId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexDelete(mutexId)


def clOsalMutexDestroy(pMutex):
    """
    arg types:
        ClOsalMutexT *pMutex
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMutexDestroy(pMutex)


# --- Condition Variable Functions ---

def clOsalCondInit(pCond):
    """
    arg types:
        ClOsalCondT* pCond
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalCondInit(pCond)


def clOsalProcessSharedCondInit(pCond):
    """
    arg types:
        ClOsalCondT* pCond
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalProcessSharedCondInit(pCond)


def clOsalCondCreate(pConditionId):
    """
    arg types:
        ClOsalCondIdT* pConditionId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalCondCreate(pConditionId)


def clOsalCondDelete(conditionId):
    """
    arg types:
        ClOsalCondIdT conditionId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalCondDelete(conditionId)


def clOsalCondDestroy(pCond):
    """
    arg types:
        ClOsalCondT *pCond
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalCondDestroy(pCond)


def clOsalCondWait(conditionId, mutexId, time):
    """
    arg types:
        ClOsalCondIdT conditionId,
        ClOsalMutexIdT mutexId,
        ClTimerTimeOutT time
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalCondWait(conditionId, mutexId, time)


def clOsalCondBroadcast(conditionId):
    """
    arg types:
        ClOsalCondIdT conditionId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalCondBroadcast(conditionId)


def clOsalCondSignal(conditionId):
    """
    arg types:
        ClOsalCondIdT conditionId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalCondSignal(conditionId)

# --- Task/Thread-Specific Data (TSD) ---

def clOsalTaskKeyCreate(pKey, pCallbackFunc):
    """
    arg types:
        ClUint32T* pKey,
        ClOsalTaskKeyDeleteCallBackT pCallbackFunc
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskKeyCreate(pKey, pCallbackFunc)


def clOsalTaskKeyDelete(key):
    """
    arg types:
        ClUint32T key
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskKeyDelete(key)


def clOsalTaskDataSet(key, threadData):
    """
    arg types:
        ClUint32T key,
        ClOsalTaskDataT threadData
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskDataSet(key, threadData)


def clOsalTaskDataGet(key, pThreadData):
    """
    arg types:
        ClUint32T key,
        ClOsalTaskDataT* pThreadData
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalTaskDataGet(key, pThreadData)


# --- Semaphore Functions ---

def clOsalSemCreate(pName, value, pSemId):
    """
    arg types:
        ClUint8T* pName,
        ClUint32T value,
        ClOsalSemIdT* pSemId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalSemCreate(pName, value, pSemId)


def clOsalSemIdGet(pName, pSemId):
    """
    arg types:
        ClUint8T* pName,
        ClOsalSemIdT* pSemId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalSemIdGet(pName, pSemId)


def clOsalSemLock(semId):
    """
    arg types:
        ClOsalSemIdT semId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalSemLock(semId)


def clOsalSemTryLock(semId):
    """
    arg types:
        ClOsalSemIdT semId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalSemTryLock(semId)


def clOsalSemUnlock(semId):
    """
    arg types:
        ClOsalSemIdT semId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalSemUnlock(semId)


def clOsalSemValueGet(semId, pSemValue):
    """
    arg types:
        ClOsalSemIdT semId,
        ClUint32T* pSemValue
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalSemValueGet(semId, pSemValue)


def clOsalSemDelete(semId):
    """
    arg types:
        ClOsalSemIdT semId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalSemDelete(semId)


# --- Process Management ---

def clOsalProcessCreate(fpFunction, functionArg, creationFlags, pProcessId):
    """
    arg types:
        ClOsalProcessFuncT fpFunction,
        void* functionArg,
        ClOsalProcessFlagT creationFlags,
        ClOsalPidT* pProcessId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalProcessCreate(fpFunction, functionArg, creationFlags, pProcessId)


def clOsalProcessDelete(processId):
    """
    arg types:
        ClOsalPidT processId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalProcessDelete(processId)


def clOsalProcessWait(processId):
    """
    arg types:
        ClOsalPidT processId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalProcessWait(processId)


def clOsalProcessSelfIdGet(pProcessId):
    """
    arg types:
        ClOsalPidT* pProcessId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalProcessSelfIdGet(pProcessId)


# --- Shared Memory (SHM) ---

def clOsalShmCreate(pName, size, pShmId):
    """
    arg types:
        ClUint8T* pName,
        ClUint32T size,
        ClOsalShmIdT *pShmId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalShmCreate(pName, size, pShmId)


def clOsalShmIdGet(pName, pShmId):
    """
    arg types:
        ClUint8T *pName,
        ClOsalShmIdT *pShmId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalShmIdGet(pName, pShmId)


def clOsalShmDelete(shmId):
    """
    arg types:
        ClOsalShmIdT shmId
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalShmDelete(shmId)


def clOsalShmAttach(shmId, pInMem, ppOutMem):
    """
    arg types:
        ClOsalShmIdT shmId,
        void* pInMem,
        void** ppOutMem
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalShmAttach(shmId, pInMem, ppOutMem)


def clOsalShmDetach(pMem):
    """
    arg types:
        void* pMem
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalShmDetach(pMem)


def clOsalShmSecurityModeSet(shmId, mode):
    """
    arg types:
        ClOsalShmIdT shmId,
        ClUint32T mode
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalShmSecurityModeSet(shmId, mode)


def clOsalShmSecurityModeGet(shmId, pMode):
    """
    arg types:
        ClOsalShmIdT shmId,
        ClUint32T* pMode
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalShmSecurityModeGet(shmId, pMode)


def clOsalShmSizeGet(shmId, pSize):
    """
    arg types:
        ClOsalShmIdT shmId,
        ClUint32T* pSize
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalShmSizeGet(shmId, pSize)


def clOsalMmap(start, length, prot, flags, fd, offset, mmapped):
    """
    arg types:
        ClPtrT start,
        ClUint32T length,
        ClInt32T prot,
        ClInt32T flags,
        ClHandleT fd,
        ClHandleT offset,
        ClPtrT *mmapped
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMmap(start, length, prot, flags, fd, offset, mmapped)


def clOsalMunmap(start, length):
    """
    arg types:
        ClPtrT start,
        ClUint32T length
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMunmap(start, length)


def clOsalMsync(start, length, flags):
    """
    arg types:
        ClPtrT start,
        ClUint32T length,
        ClInt32T flags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMsync(start, length, flags)


def clOsalFtruncate(fd, length):
    """
    arg types:
        ClFdT fd,
        off_t length
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalFtruncate(fd, length)


def clOsalShmOpen(name, oflag, mode, fd):
    """
    arg types:
        ClCharT *name,
        ClInt32T oflag,
        ClUint32T mode,
        ClFdT *fd
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalShmOpen(name, oflag, mode, fd)


def clOsalShmClose(fd):
    """
    arg types:
        ClFdT *fd
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalShmClose(fd)


def clOsalShmUnlink(name):
    """
    arg types:
        ClCharT *name
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalShmUnlink(name)


# --- Utility Functions ---

def clOsalSigHandlerInitialize():
    """
    arg types:
        void
    return type:
        void
    """
    return clLib.libmw_so.clOsalSigHandlerInitialize()


def clOsalMaxPathGet(path, pLength):
    """
    arg types:
        ClCharT* path,
        ClInt32T* pLength
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalMaxPathGet(path, pLength)


def clOsalPageSizeGet(pSize):
    """
    arg types:
        ClInt32T* pSize
    return type:
        ClRcT
    """
    return clLib.libmw_so.clOsalPageSizeGet(pSize)

def clOsalPrintf(fmt, *va_args):
    """
    Variadic function

    arg types:
        ClCharT* fmt
        ...
    return type:
        ClRcT
    """
    cFmt = clUtils.toCharP(fmt)
    cVaArgs, argTypes = clUtils.handleVarArgs(*va_args)
    clLib.libmw_so.clOsalPrintf.argtypes = [ctypes.c_char_p] + argTypes
    return clLib.libmw_so.clOsalPrintf(cFmt, *cVaArgs)

# TODO: there're remaining codes in the original header file
