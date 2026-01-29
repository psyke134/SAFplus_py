import sys
sys.path.append("..")

from common import clCommon
from utils import clUtils

ClIocProtocols = clCommon.ClInt32T
class eClIocProtocols(clUtils.Enum):
    CL_IOC_PROTO_ARP   =                0x1
    CL_IOC_PROTO_FLOWCONTROL   =        0x2
    CL_IOC_PROTO_HB     =               0x3
    CL_IOC_PROTO_CTL      =             0x4
    CL_IOC_PROTO_TL      =              0x5
    CL_IOC_PROTO_MSG    =               0x6
    CL_IOC_PROTO_ICMP       =           0x7
    CL_IOC_INTERNAL_PROTO_END  =        0xf
    CL_IOC_RMD_SYNC_REQUEST_PROTO   =   0x10
    CL_IOC_RMD_SYNC_REPLY_PROTO    =    0x11
    CL_IOC_RMD_ASYNC_REQUEST_PROTO  =   0x12
    CL_IOC_RMD_ASYNC_REPLY_PROTO    =   0x13
    CL_IOC_PORT_NOTIFICATION_PROTO   =  0x14
    CL_IOC_SYSLOG_PROTO     =           0x15
    CL_IOC_RMD_ACK_PROTO       =        0x16
    CL_IOC_RMD_ORDERED_PROTO   =        0x17
    CL_IOC_SAF_MSG_REQUEST_PROTO    =   0x18
    CL_IOC_SAF_MSG_REPLY_PROTO    =     0x19
    CL_IOC_CONFIG_CHANGE_PROTO   =      0x20
    CL_IOC_ASP_RESERVERD_PROTO_END =    0x7f
    CL_IOC_USER_PROTO_START         =   0x80
    CL_IOC_PROTO_END            =       0xfe
    CL_IOC_INVALID_PROTO         =      0xff
    CL_IOC_NUM_PROTOS            =      0x100

ClConfigChange = clCommon.ClInt32T
class eClConfigChange(clUtils.Enum):
    CL_CONFIG_TIME_ZONE = 1
