import sys
sys.path.append("..")

from utils import clUtils
from common import saAis

ClOsalThreadPriorityT = saAis.SaInt32T
class eClOsalThreadPriorityT(clUtils.CEnum):
    CL_OSAL_THREAD_PRI_NOT_APPLICABLE = 0,
    CL_OSAL_THREAD_PRI_HIGH = 160,
    CL_OSAL_THREAD_PRI_MEDIUM = 80,
    CL_OSAL_THREAD_PRI_LOW = 1,