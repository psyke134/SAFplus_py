import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils, clLib

import ctypes

def CL_RULE_SWAP32(x):
    return (((x >> 24) & 0xFF) | 
            ((x >> 8) & 0xFF00) | 
            ((x & 0xFF00) << 8) | 
            ((x & 0xFF) << 24))

def CL_RULE_SWAP16(x):
    return (((x >> 8) & 0xFF) | 
            ((x << 8) & 0xFF00))

ClRuleExprFlagsT = clCommon.ClInt32T
class eClRuleExprFlagsT(clUtils.Enum):
    CL_RULE_LITTLE_END = 0x1
    CL_RULE_BIG_END = 0x2
    CL_RULE_NON_ZERO_MATCH = 0x4
    CL_RULE_MATCH_EXACT    = 0x8
    CL_RULE_EXPR_CHAIN_AND = 0x10
    CL_RULE_EXPR_CHAIN_GROUP_OR  = 0x40

CL_RULE_EXPR_FLAG_BITS = 2
CL_RULE_ARCH_FLAG_MASK = 0x3
CL_RULE_EXPR_FLAG_MASK = ~CL_RULE_ARCH_FLAG_MASK
CL_RULE_EXPR_FLAG_DEFAULT = eClRuleExprFlagsT.CL_RULE_NON_ZERO_MATCH | eClRuleExprFlagsT.CL_RULE_EXPR_CHAIN_AND

class _BI_u(ctypes.Union):
    _fields_ = [
        ("Byte", clCommon.ClUint8T * 1),
        ("Int", clCommon.ClUint32T * 1)
    ]

class ClRuleExprT(ctypes.Structure):
    pass
ClRuleExprT._fields_ = [
        ("flags", clCommon.ClUint8T),
        ("len", clCommon.ClUint8T),
        ("offset", clCommon.ClUint16T),
        ("next", ctypes.POINTER(ClRuleExprT)),
        ("BI_u", _BI_u)
    ]

def clRuleExprAllocate(length, ppExpr):
    """
    arg types:
        ClUint8T len,
        ClRuleExprT** ppExpr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprAllocate(length, ppExpr)


def clRuleExprDeallocate(pExpr):
    """
    arg types:
        ClRuleExprT* pExpr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprDeallocate(pExpr)


def clRuleExprAppend(pFirstExpr, pNextExpr):
    """
    arg types:
        ClRuleExprT* pFirstExpr,
        ClRuleExprT* pNextExpr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprAppend(pFirstExpr, pNextExpr)


def clRuleExprDuplicate(pSrcExpr, ppDstExpr):
    """
    arg types:
        ClRuleExprT* pSrcExpr,
        ClRuleExprT** ppDstExpr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprDuplicate(pSrcExpr, ppDstExpr)


def clRuleExprEvaluate(pExpr, pData, dataLen):
    """
    arg types:
        ClRuleExprT* pExpr,
        ClUint32T *pData,
        int dataLen
    return type:
        ClRuleResultT
    """
    return clLib.libmw_so.clRuleExprEvaluate(pExpr, pData, dataLen)


def clRuleDoubleExprEvaluate(pExpr1, pExpr2):
    """
    arg types:
        ClRuleExprT* pExpr1,
        ClRuleExprT* pExpr2
    return type:
        ClRuleResultT
    """
    return clLib.libmw_so.clRuleDoubleExprEvaluate(pExpr1, pExpr2)


def clRuleExprLocalConvert(pExpr):
    """
    arg types:
        ClRuleExprT* pExpr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprLocalConvert(pExpr)


def clRuleExprConvert(pExpr):
    """
    arg types:
        ClRuleExprT* pExpr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprConvert(pExpr)


def clRuleExprFlagsSet(pExpr, flags):
    """
    arg types:
        ClRuleExprT* pExpr,
        ClRuleExprFlagsT flags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprFlagsSet(pExpr, flags)


def clRuleExprOffsetSet(pExpr, offset):
    """
    arg types:
        ClRuleExprT* pExpr,
        ClUint16T offset
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprOffsetSet(pExpr, offset)


def clRuleExprMaskSet(pExpr, offset, mask):
    """
    arg types:
        ClRuleExprT* pExpr,
        ClUint16T offset,
        ClUint32T mask
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprMaskSet(pExpr, offset, mask)


def clRuleExprValueSet(pExpr, offset, value):
    """
    arg types:
        ClRuleExprT* pExpr,
        ClUint16T offset,
        ClUint32T value
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprValueSet(pExpr, offset, value)


def clRuleExprFlagsGet(pExpr, pFlags):
    """
    arg types:
        ClRuleExprT* pExpr,
        ClRuleExprFlagsT *pFlags
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprFlagsGet(pExpr, pFlags)


def clRuleExprOffsetGet(pExpr, pOffset):
    """
    arg types:
        ClRuleExprT* pExpr,
        ClUint16T *pOffset
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprOffsetGet(pExpr, pOffset)


def clRuleExprMaskGet(pExpr, offset, pMask):
    """
    arg types:
        ClRuleExprT* pExpr,
        ClUint16T offset,
        ClUint32T *pMask
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprMaskGet(pExpr, offset, pMask)


def clRuleExprValueGet(pExpr, offset, pValue):
    """
    arg types:
        ClRuleExprT* pExpr,
        ClUint16T offset,
        ClUint32T *pValue
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprValueGet(pExpr, offset, pValue)


def clRuleExprMemLenGet(pExpr):
    """
    arg types:
        ClRuleExprT* pExpr
    return type:
        ClUint32T
    """
    return clLib.libmw_so.clRuleExprMemLenGet(pExpr)


def clRuleExprPack(pSrcExpr, ppBuf, pLen):
    """
    arg types:
        ClRuleExprT *pSrcExpr,
        ClUint8T **ppBuf,
        ClUint32T *pLen
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprPack(pSrcExpr, ppBuf, pLen)


def clRuleExprUnpack(pBuf, length, ppDstExpr):
    """
    arg types:
        ClUint8T *pBuf,
        ClUint32T len,
        ClRuleExprT **ppDstExpr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprUnpack(pBuf, length, ppDstExpr)


def clRuleExprPrint(pExpr):
    """
    arg types:
        ClRuleExprT* pExpr
    return type:
        ClRcT
    """
    return clLib.libmw_so.clRuleExprPrint(pExpr)
