import sys
sys.path.append("..")

from utils import clLib, clUtils

def clCksm16bitCompute(pData, length, pCheckSum):
    """
    arg types:
        ClUint8T *pData,
        ClUint32T length,
        ClUint16T *pCheckSum
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCksm16bitCompute(pData, length, clUtils.byref(pCheckSum))

def clCksm32bitCompute(pData, length, pCheckSum):
    """
    arg types:
        ClUint8T *pData,
        ClUint32T length,
        ClUint32T *pCheckSum
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCksm32bitCompute(pData, length, clUtils.byref(pCheckSum))

def clCrc32bitCompute(buf, nr, cval, clen):
    """
    arg types:
        ClUint8T *buf, 
        ClInt32T nr, 
        ClUint32T *cval, 
        ClUint32T *clen
    return type:
        ClRcT
    """
    return clLib.libmw_so.clCrc32bitCompute(buf, nr, clUtils.byref(cval), clUtils.byref(clen))
