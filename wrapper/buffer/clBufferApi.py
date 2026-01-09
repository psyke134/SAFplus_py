import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils, clLib, libc
from ipi import clPoolIpi

import ctypes

ClBufferSeekTypeT = clCommon.ClInt32T
class eClBufferSeekTypeT(clUtils.CEnum):
    CL_BUFFER_SEEK_SET = 0,
    CL_BUFFER_SEEK_CUR = 1,
    CL_BUFFER_SEEK_END = 2,
    CL_BUFFER_SEEK_MAX = 3

ClBufferHandleT = clCommon.ClPtrT

ClBufferModeT = clCommon.ClInt32T
class eClBufferModeT(clUtils.CEnum):
    CL_BUFFER_NATIVE_MODE = 0,
    CL_BUFFER_PREALLOCATED_MODE = 1,
    CL_BUFFER_MAX_MODE = 2

class ClBufferPoolConfigT(ctypes.Structure):
    _fields_ = [
        ("numPools", clCommon.ClUint32T),
        ("pPoolConfig", ctypes.POINTER(clPoolIpi.ClPoolConfigT)),
        ("lazy", clCommon.ClBoolT),
        ("mode", ClBufferModeT),
    ]

def clBufferInitialize(pConfig):
    """
    arg types:
        const ClBufferPoolConfigT *pConfig
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferInitialize(pConfig)


def clBufferFinalize():
    """
    arg types:
        void
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferFinalize()


def clBufferCreate(pMessageHandle):
    """
    arg types:
        ClBufferHandleT *pMessageHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferCreate(pMessageHandle)


def clBufferCreateAndAllocate(size, pMessageHandle):
    """
    arg types:
        ClUint32T size,
        ClBufferHandleT *pMessageHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferCreateAndAllocate(size, pMessageHandle)


def clBufferDelete(pMessageHandle):
    """
    arg types:
        ClBufferHandleT *pMessageHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferDelete(pMessageHandle)


def clBufferClear(messageHandle):
    """
    arg types:
        ClBufferHandleT messageHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferClear(messageHandle)


def clBufferLengthGet(messageHandle, pMessageLength):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClUint32T *pMessageLength
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferLengthGet(messageHandle, pMessageLength)


def clBufferLengthCalc(bufferHandle):
    """
    arg types:
        ClBufferHandleT bufferHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferLengthCalc(bufferHandle)


def clBufferNBytesRead(messageHandle, pByteBuffer, pNumberOfBytesToRead):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClUint8T *pByteBuffer,
        ClUint32T* pNumberOfBytesToRead
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferNBytesRead(messageHandle, pByteBuffer, pNumberOfBytesToRead)


def clBufferNBytesWrite(messageHandle, pByteBuffer, numberOfBytesToWrite):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClUint8T *pByteBuffer,
        ClUint32T numberOfBytesToWrite
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferNBytesWrite(messageHandle, pByteBuffer, numberOfBytesToWrite)


def clBufferChecksum16Compute(messageHandle, startOffset, length, pChecksum):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClUint32T startOffset,
        ClUint32T length,
        ClUint16T* pChecksum
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferChecksum16Compute(messageHandle, startOffset, length, pChecksum)


def clBufferChecksum32Compute(messageHandle, startOffset, length, pChecksum):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClUint32T startOffset,
        ClUint32T length,
        ClUint32T* pChecksum
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferChecksum32Compute(messageHandle, startOffset, length, pChecksum)


def clBufferDataPrepend(messageHandle, pByteBuffer, numberOfBytesToWrite):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClUint8T *pByteBuffer,
        ClUint32T numberOfBytesToWrite
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferDataPrepend(messageHandle, pByteBuffer, numberOfBytesToWrite)


def clBufferConcatenate(destination, pSource):
    """
    arg types:
        ClBufferHandleT destination,
        ClBufferHandleT *pSource
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferConcatenate(destination, pSource)


def clBufferReadOffsetGet(messageHandle, pReadOffset):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClUint32T *pReadOffset
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferReadOffsetGet(messageHandle, pReadOffset)


def clBufferWriteOffsetGet(messageHandle, pWriteOffset):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClUint32T *pWriteOffset
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferWriteOffsetGet(messageHandle, pWriteOffset)


def clBufferReadOffsetSet(messageHandle, newReadOffset, seekType):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClInt32T newReadOffset,
        ClBufferSeekTypeT seekType
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferReadOffsetSet(messageHandle, newReadOffset, seekType)


def clBufferWriteOffsetSet(messageHandle, newWriteOffset, seekType):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClInt32T newWriteOffset,
        ClBufferSeekTypeT seekType
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferWriteOffsetSet(messageHandle, newWriteOffset, seekType)


def clBufferHeaderTrim(messageHandle, numberOfBytes):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClUint32T numberOfBytes
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferHeaderTrim(messageHandle, numberOfBytes)


def clBufferTrailerTrim(messageHandle, numberOfBytes):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClUint32T numberOfBytes
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferTrailerTrim(messageHandle, numberOfBytes)


def clBufferToBufferCopy(sourceMessage, sourceMessageOffset, destinationMessage, numberOfBytes):
    """
    arg types:
        ClBufferHandleT sourceMessage,
        ClUint32T sourceMessageOffset,
        ClBufferHandleT destinationMessage,
        ClUint32T numberOfBytes
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferToBufferCopy(sourceMessage, sourceMessageOffset, destinationMessage, numberOfBytes)


def clBufferDuplicate(messageHandle, pDuplicatedMessage):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClBufferHandleT *pDuplicatedMessage
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferDuplicate(messageHandle, pDuplicatedMessage)


def clBufferClone(source, pClone):
    """
    arg types:
        ClBufferHandleT source,
        ClBufferHandleT *pClone
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferClone(source, pClone)


def clBufferAppendHeap(source, buffer, size):
    """
    arg types:
        ClBufferHandleT source,
        ClUint8T *buffer,
        ClUint32T size
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferAppendHeap(source, buffer, size)


def clBufferFlatten(messageHandle, ppFlattenBuffer):
    """
    arg types:
        ClBufferHandleT messageHandle,
        ClUint8T** ppFlattenBuffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferFlatten(messageHandle, ppFlattenBuffer)


def clBufferUserToKernelCopy(userMessageHandle, pKernelMessageHandle):
    """
    arg types:
        ClBufferHandleT userMessageHandle,
        ClBufferHandleT* pKernelMessageHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferUserToKernelCopy(userMessageHandle, pKernelMessageHandle)


def clBufferKernelToUserCopy(kernelMessageHandle, userMessageHandle):
    """
    arg types:
        ClBufferHandleT kernelMessageHandle,
        ClBufferHandleT userMessageHandle
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferKernelToUserCopy(kernelMessageHandle, userMessageHandle)


def clBufferShrink(pShrinkOptions):
    """
    arg types:
        ClPoolShrinkOptionsT *pShrinkOptions
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferShrink(pShrinkOptions)


def clDbgBufferPrint(buffer):
    """
    arg types:
        ClBufferHandleT buffer
    return type:
        ClRcT
    """
    return clLib.libmw_so.clDbgBufferPrint(buffer)


def clBufferStatsGet(pBufferStats):
    """
    arg types:
        ClMemStatsT *pBufferStats
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferStatsGet(pBufferStats)


def clBufferPoolStatsGet(numPools, pPoolSize, pBufferPoolStats):
    """
    arg types:
        ClUint32T numPools,
        ClUint32T *pPoolSize,
        ClPoolStatsT *pBufferPoolStats
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferPoolStatsGet(numPools, pPoolSize, pBufferPoolStats)


def clBufferVectorize(buffer, ppIOVector, pNumVectors):
    """
    arg types:
        ClBufferHandleT buffer,
        struct iovec **ppIOVector,
        ClInt32T *pNumVectors
    return type:
        ClRcT
    """
    return clLib.libmw_so.clBufferVectorize(buffer, ppIOVector, pNumVectors)

