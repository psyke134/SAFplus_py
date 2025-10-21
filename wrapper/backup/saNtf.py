import ctypes
import enum
import clUtils
import saAis
import clLib

import os

SaNtfHandleT = saAis.SaUint64T
SaNtfNotificationHandleT = saAis.SaUint64T
SaNtfNotificationFilterHandleT = saAis.SaUint64T
SaNtfReadHandleT = saAis.SaUint64T

SaNtfNotificationTypeT = saAis.SaInt32T
class eSaNtfNotificationTypeT(clUtils.CEnum):
    SA_NTF_TYPE_OBJECT_CREATE_DELETE    = 0x1000
    SA_NTF_TYPE_ATTRIBUTE_CHANGE        = 0x2000
    SA_NTF_TYPE_STATE_CHANGE            = 0x3000
    SA_NTF_TYPE_ALARM                   = 0x4000
    SA_NTF_TYPE_SECURITY_ALARM          = 0x5000
    SA_NTF_TYPE_MISCELLANEOUS           = 0x6000

SA_NTF_NOTIFICATIONS_TYPE_MASK = 0xF000

SaNtfEventTypeT = saAis.SaInt32T
class eSaNtfEventTypeT(clUtils.CEnum):
    SA_NTF_OBJECT_NOTIFICATIONS_START = eSaNtfNotificationTypeT.SA_NTF_TYPE_OBJECT_CREATE_DELETE.value
    SA_NTF_OBJECT_CREATION              = enum.auto()
    SA_NTF_OBJECT_DELETION              = enum.auto()

    SA_NTF_ATTRIBUTE_NOTIFICATIONS_START = eSaNtfNotificationTypeT.SA_NTF_TYPE_ATTRIBUTE_CHANGE.value
    SA_NTF_ATTRIBUTE_ADDED              = enum.auto()
    SA_NTF_ATTRIBUTE_REMOVED            = enum.auto()
    SA_NTF_ATTRIBUTE_CHANGED            = enum.auto()
    SA_NTF_ATTRIBUTE_RESET              = enum.auto()

    SA_NTF_STATE_CHANGE_NOTIFICATIONS_START = eSaNtfNotificationTypeT.SA_NTF_TYPE_STATE_CHANGE.value
    SA_NTF_OBJECT_STATE_CHANGE          = enum.auto()

    SA_NTF_ALARM_NOTIFICATIONS_START = eSaNtfNotificationTypeT.SA_NTF_TYPE_ALARM.value
    SA_NTF_ALARM_COMMUNICATION          = enum.auto()
    SA_NTF_ALARM_QOS                    = enum.auto()
    SA_NTF_ALARM_PROCESSING             = enum.auto()
    SA_NTF_ALARM_EQUIPMENT              = enum.auto()
    SA_NTF_ALARM_ENVIRONMENT            = enum.auto()

    SA_NTF_SECURITY_ALARM_NOTIFICATIONS_START = eSaNtfNotificationTypeT.SA_NTF_TYPE_SECURITY_ALARM.value
    SA_NTF_INTEGRITY_VIOLATION          = enum.auto()
    SA_NTF_OPERATION_VIOLATION          = enum.auto()
    SA_NTF_PHYSICAL_VIOLATION           = enum.auto()
    SA_NTF_SECURITY_SERVICE_VIOLATION   = enum.auto()
    SA_NTF_TIME_VIOLATION               = enum.auto()

    SA_NTF_MISCELLANEOUS_NOTIFICATIONS_START = eSaNtfNotificationTypeT.SA_NTF_TYPE_MISCELLANEOUS.value
    SA_NTF_APPLICATION_EVENT            = enum.auto()
    SA_NTF_ADMIN_OPERATION_START        = enum.auto()
    SA_NTF_ADMIN_OPERATION_END          = enum.auto()
    SA_NTF_CONFIG_UPDATE_START          = enum.auto()
    SA_NTF_CONFIG_UPDATE_END            = enum.auto()
    SA_NTF_ERROR_REPORT                 = enum.auto()
    SA_NTF_ERROR_CLEAR                  = enum.auto()
    SA_NTF_HPI_EVENT_RESOURCE           = enum.auto()
    SA_NTF_HPI_EVENT_SENSOR             = enum.auto()
    SA_NTF_HPI_EVENT_WATCHDOG           = enum.auto()
    SA_NTF_HPI_EVENT_DIMI               = enum.auto()
    SA_NTF_HPI_EVENT_FUMI               = enum.auto()
    SA_NTF_HPI_EVENT_OTHER              = enum.auto()

SaNtfNotificationTypeBitsT = saAis.SaInt32T
class eSaNtfNotificationTypeBitsT(clUtils.CEnum):
    SA_NTF_TYPE_OBJECT_CREATE_DELETE_BIT    = 0x0001
    SA_NTF_TYPE_ATTRIBUTE_CHANGE_BIT        = 0x0002
    SA_NTF_TYPE_STATE_CHANGE_BIT            = 0x0004
    SA_NTF_TYPE_ALARM_BIT                   = 0x0008
    SA_NTF_TYPE_SECURITY_ALARM_BIT          = 0x0010

SA_NTF_OBJECT_CREATION_BIT              = 0x01
SA_NTF_OBJECT_DELETION_BIT              = 0x02
SA_NTF_ATTRIBUTE_ADDED_BIT              = 0x04
SA_NTF_ATTRIBUTE_REMOVED_BIT            = 0x08
SA_NTF_ATTRIBUTE_CHANGED_BIT            = 0x10
SA_NTF_ATTRIBUTE_RESET_BIT              = 0x20
SA_NTF_OBJECT_STATE_CHANGE_BIT          = 0x40
SA_NTF_ALARM_COMMUNICATION_BIT          = 0x80
SA_NTF_ALARM_QOS_BIT                    = 0x100
SA_NTF_ALARM_PROCESSING_BIT             = 0x200
SA_NTF_ALARM_EQUIPMENT_BIT              = 0x400
SA_NTF_ALARM_ENVIRONMENT_BIT            = 0x800
SA_NTF_INTEGRITY_VIOLATION_BIT          = 0x1000
SA_NTF_OPERATION_VIOLATION_BIT          = 0x2000
SA_NTF_PHYSICAL_VIOLATION_BIT           = 0x4000
SA_NTF_SECURITY_SERVICE_VIOLATION_BIT   = 0x8000
SA_NTF_TIME_VIOLATION_BIT               = 0x10000
SA_NTF_ADMIN_OPERATION_START_BIT        = 0x20000
SA_NTF_ADMIN_OPERATION_END_BIT          = 0x40000
SA_NTF_CONFIG_UPDATE_START_BIT          = 0x80000
SA_NTF_CONFIG_UPDATE_END_BIT            = 0x100000
SA_NTF_ERROR_REPORT_BIT                 = 0x200000
SA_NTF_ERROR_CLEAR_BIT                  = 0x400000
SA_NTF_HPI_EVENT_RESOURCE_BIT           = 0x800000
SA_NTF_HPI_EVENT_SENSOR_BIT             = 0x1000000
SA_NTF_HPI_EVENT_WATCHDOG_BIT           = 0x2000000
SA_NTF_HPI_EVENT_DIMI_BIT               = 0x4000000
SA_NTF_HPI_EVENT_FUMI_BIT               = 0x8000000
SA_NTF_HPI_EVENT_OTHER_BIT              = 0x10000000
SA_NTF_APPLICATION_EVENT_BIT            = 0x100000000000

SaNtfEventTypeBitmapT = saAis.SaUint64T

class SaNtfClassIdT(ctypes.Structure):
    _fields_ = [
		("vendorId", saAis.SaUint32T),
		("majorId", saAis.SaUint16T),
        ("minorId", saAis.SaUint16T),
	]

SA_NTF_VENDOR_ID_SAF = 18568

SaNtfElementIdT = saAis.SaUint16T
SaNtfIdentifierT = saAis.SaUint64T

SA_NTF_IDENTIFIER_UNUSED = 0

class SaNtfCorrelationIdsT(ctypes.Structure):
    _fields_ = [
		("rootCorrelationId", SaNtfIdentifierT),
		("parentCorrelationId", SaNtfIdentifierT),
        ("notificationId", SaNtfIdentifierT),
	]

SaNtfValueTypeT = saAis.SaInt32T
class eSaNtfValueTypeT(clUtils.CEnum):
    SA_NTF_VALUE_UINT8      = 1
    SA_NTF_VALUE_INT8       = enum.auto()
    SA_NTF_VALUE_UINT16     = enum.auto()
    SA_NTF_VALUE_INT16      = enum.auto()
    SA_NTF_VALUE_UINT32     = enum.auto()
    SA_NTF_VALUE_INT32      = enum.auto()
    SA_NTF_VALUE_FLOAT      = enum.auto()
    SA_NTF_VALUE_UINT64     = enum.auto()
    SA_NTF_VALUE_INT64      = enum.auto()
    SA_NTF_VALUE_DOUBLE     = enum.auto()
    SA_NTF_VALUE_LDAP_NAME  = enum.auto()
    SA_NTF_VALUE_STRING     = enum.auto()
    SA_NTF_VALUE_IPADDRESS  = enum.auto()
    SA_NTF_VALUE_BINARY     = enum.auto()
    SA_NTF_VALUE_ARRAY      = enum.auto()

class _ptrVal(ctypes.Structure):
    _fields_ = [
		("dataOffset", saAis.SaUint16T),
		("dataSize", saAis.SaUint16T),
	]
class _arrayVal(ctypes.Structure):
    _fields_ = [
		("arrayOffset", saAis.SaUint16T),
		("numElements", saAis.SaUint16T),
        ("elementSize", saAis.SaUint16T),
	]

class SaNtfValueT(ctypes.Union):
    _fields_ = [
		("uint8Val", SaNtfIdentifierT),
		("int8Val", SaNtfIdentifierT),
        ("uint16Val", SaNtfIdentifierT),
        ("int16Val", SaNtfIdentifierT),
        ("uint32Val", SaNtfIdentifierT),
        ("int32Val", SaNtfIdentifierT),
        ("floatVal", SaNtfIdentifierT),
        ("uint64Val", SaNtfIdentifierT),
        ("int64Val", SaNtfIdentifierT),
        ("doubleVal", SaNtfIdentifierT),
        ("ptrVal", _ptrVal),
        ("arrayVal", _arrayVal),
	]

class SaNtfAdditionalInfoT(ctypes.Union):
    _fields_ = [
		("infoId", SaNtfElementIdT),
		("infoType", SaNtfValueTypeT),
        ("infoValue", SaNtfValueT),
	]

class SaNtfNotificationHeaderT(ctypes.Structure):
    _fields_ = [
        ("eventType", ctypes.POINTER(SaNtfEventTypeT)),
        ("notificationObject", ctypes.POINTER(saAis.SaNameT)),
        ("notifyingObject", ctypes.POINTER(saAis.SaNameT)),
        ("notificationClassId", ctypes.POINTER(SaNtfClassIdT)),
        ("eventTime", ctypes.POINTER(saAis.SaTimeT)),
        ("numCorrelatedNotifications", saAis.SaUint16T),
        ("lengthAdditionalText", saAis.SaUint16T),
        ("numAdditionalInfo", saAis.SaUint16T),
        ("notificationId", ctypes.POINTER(SaNtfIdentifierT)),
        ("correlatedNotifications", ctypes.POINTER(SaNtfIdentifierT)),
        ("additionalText", saAis.SaStringT),
        ("additionalInfo", ctypes.POINTER(SaNtfAdditionalInfoT)),
    ]

class SaNtfSourceIndicatorT(ctypes.Structure):
    SA_NTF_OBJECT_OPERATION = 0
    SA_NTF_UNKNOWN_OPERATION = 1
    SA_NTF_MANAGEMENT_OPERATION = 2

class SaNtfAttributeChangeT(ctypes.Structure):
    _fields_ = [
        ("attributeId", SaNtfElementIdT),
        ("attributeType", SaNtfValueTypeT),
        ("oldAttributePresent", saAis.SaBoolT),
        ("oldAttributeValue", SaNtfValueT),
        ("newAttributeValue", SaNtfValueT),
    ]

class SaNtfAttributeChangeNotificationT(ctypes.Structure):
    _fields_ = [
        ("notificationHandle", SaNtfNotificationHandleT),
        ("notificationHeader", SaNtfNotificationHeaderT),
        ("numAttributes", saAis.SaUint16T),
        ("sourceIndicator", ctypes.POINTER(SaNtfSourceIndicatorT)),
        ("changedAttributes", ctypes.POINTER(SaNtfAttributeChangeT)),
    ]

class SaNtfAttributeT(ctypes.Structure):
    _fields_ = [
        ("attributeId", SaNtfElementIdT),
        ("attributeType", SaNtfValueTypeT),
        ("attributeValue", SaNtfValueT),
    ]

class SaNtfObjectCreateDeleteNotificationT(ctypes.Structure):
    _fields_ = [
        ("notificationHandle", SaNtfNotificationHandleT),
        ("notificationHeader", SaNtfNotificationHeaderT),
        ("numAttributes", saAis.SaUint16T),
        ("sourceIndicator", ctypes.POINTER(SaNtfSourceIndicatorT)),
        ("objectAttributes", ctypes.POINTER(SaNtfAttributeT)),
    ]

class SaNtfStateChangeT(ctypes.Structure):
    _fields_ = [
        ("stateId", SaNtfElementIdT),
        ("oldStatePresent", saAis.SaBoolT),
        ("oldState", saAis.SaUint16T),
        ("newState", saAis.SaUint16T),
    ]

class SaNtfStateChangeNotificationT(ctypes.Structure):
    _fields_ = [
        ("notificationHandle", SaNtfNotificationHandleT),
        ("notificationHeader", SaNtfNotificationHeaderT),
        ("numStateChanges", saAis.SaUint16T),
        ("sourceIndicator", ctypes.POINTER(SaNtfSourceIndicatorT)),
        ("changedStates", ctypes.POINTER(SaNtfStateChangeT)),
    ]

SaNtfProbableCauseT = saAis.SaInt32T
class eSaNtfProbableCauseT(clUtils.CEnum):
    SA_NTF_ADAPTER_ERROR                                    = 0
    SA_NTF_APPLICATION_SUBSYSTEM_FAILURE                    = enum.auto()
    SA_NTF_BANDWIDTH_REDUCED                                = enum.auto()
    SA_NTF_CALL_ESTABLISHMENT_ERROR                         = enum.auto()
    SA_NTF_COMMUNICATIONS_PROTOCOL_ERROR                    = enum.auto()
    SA_NTF_COMMUNICATIONS_SUBSYSTEM_FAILURE                 = enum.auto()
    SA_NTF_CONFIGURATION_OR_CUSTOMIZATION_ERROR             = enum.auto()
    SA_NTF_CONGESTION                                       = enum.auto()
    SA_NTF_CORRUPT_DATA                                     = enum.auto()
    SA_NTF_CPU_CYCLES_LIMIT_EXCEEDED                        = enum.auto()
    SA_NTF_DATASET_OR_MODEM_ERROR                           = enum.auto()
    SA_NTF_DEGRADED_SIGNAL                                  = enum.auto()
    SA_NTF_D_T_E                                            = enum.auto()
    SA_NTF_ENCLOSURE_DOOR_OPEN                              = enum.auto()
    SA_NTF_EQUIPMENT_MALFUNCTION                            = enum.auto()
    SA_NTF_EXCESSIVE_VIBRATION                              = enum.auto()
    SA_NTF_FILE_ERROR                                       = enum.auto()
    SA_NTF_FIRE_DETECTED                                    = enum.auto()
    SA_NTF_FLOOD_DETECTED                                   = enum.auto()
    SA_NTF_FRAMING_ERROR                                    = enum.auto()
    SA_NTF_HEATING_OR_VENTILATION_OR_COOLING_SYSTEM_PROBLEM = enum.auto()
    SA_NTF_HUMIDITY_UNACCEPTABLE                            = enum.auto()
    SA_NTF_INPUT_OUTPUT_DEVICE_ERROR                        = enum.auto()
    SA_NTF_INPUT_DEVICE_ERROR                               = enum.auto()
    SA_NTF_L_A_N_ERROR                                      = enum.auto()
    SA_NTF_LEAK_DETECTED                                    = enum.auto()
    SA_NTF_LOCAL_NODE_TRANSMISSION_ERROR                    = enum.auto()
    SA_NTF_LOSS_OF_FRAME                                    = enum.auto()
    SA_NTF_LOSS_OF_SIGNAL                                   = enum.auto()
    SA_NTF_MATERIAL_SUPPLY_EXHAUSTED                        = enum.auto()
    SA_NTF_MULTIPLEXER_PROBLEM                              = enum.auto()
    SA_NTF_OUT_OF_MEMORY                                    = enum.auto()
    SA_NTF_OUTPUT_DEVICE_ERROR                              = enum.auto()
    SA_NTF_PERFORMANCE_DEGRADED                             = enum.auto()
    SA_NTF_POWER_PROBLEM                                    = enum.auto()
    SA_NTF_PRESSURE_UNACCEPTABLE                            = enum.auto()
    SA_NTF_PROCESSOR_PROBLEM                                = enum.auto()
    SA_NTF_PUMP_FAILURE                                     = enum.auto()
    SA_NTF_QUEUE_SIZE_EXCEEDED                              = enum.auto()
    SA_NTF_RECEIVE_FAILURE                                  = enum.auto()
    SA_NTF_RECEIVER_FAILURE                                 = enum.auto()
    SA_NTF_REMOTE_NODE_TRANSMISSION_ERROR                   = enum.auto()
    SA_NTF_RESOURCE_AT_OR_NEARING_CAPACITY                  = enum.auto()
    SA_NTF_RESPONSE_TIME_EXCESSIVE                          = enum.auto()
    SA_NTF_RETRANSMISSION_RATE_EXCESSIVE                    = enum.auto()
    SA_NTF_SOFTWARE_ERROR                                   = enum.auto()
    SA_NTF_SOFTWARE_PROGRAM_ABNORMALLY_TERMINATED           = enum.auto()
    SA_NTF_SOFTWARE_PROGRAM_ERROR                           = enum.auto()
    SA_NTF_STORAGE_CAPACITY_PROBLEM                         = enum.auto()
    SA_NTF_TEMPERATURE_UNACCEPTABLE                         = enum.auto()
    SA_NTF_THRESHOLD_CROSSED                                = enum.auto()
    SA_NTF_TIMING_PROBLEM                                   = enum.auto()
    SA_NTF_TOXIC_LEAK_DETECTED                              = enum.auto()
    SA_NTF_TRANSMIT_FAILURE                                 = enum.auto()
    SA_NTF_TRANSMITTER_FAILURE                              = enum.auto()
    SA_NTF_UNDERLYING_RESOURCE_UNAVAILABLE                  = enum.auto()
    SA_NTF_VERSION_MISMATCH                                 = enum.auto()
    SA_NTF_AUTHENTICATION_FAILURE                           = enum.auto()
    SA_NTF_BREACH_OF_CONFIDENTIALITY                        = enum.auto()
    SA_NTF_CABLE_TAMPER                                     = enum.auto()
    SA_NTF_DELAYED_INFORMATION                              = enum.auto()
    SA_NTF_DENIAL_OF_SERVICE                                = enum.auto()
    SA_NTF_DUPLICATE_INFORMATION                            = enum.auto()
    SA_NTF_INFORMATION_MISSING                              = enum.auto()
    SA_NTF_INFORMATION_MODIFICATION_DETECTED                = enum.auto()
    SA_NTF_INFORMATION_OUT_OF_SEQUENCE                      = enum.auto()
    SA_NTF_INTRUSION_DETECTION                              = enum.auto()
    SA_NTF_KEY_EXPIRED                                      = enum.auto()
    SA_NTF_NON_REPUDIATION_FAILURE                          = enum.auto()
    SA_NTF_OUT_OF_HOURS_ACTIVITY                            = enum.auto()
    SA_NTF_OUT_OF_SERVICE                                   = enum.auto()
    SA_NTF_PROCEDURAL_ERROR                                 = enum.auto()
    SA_NTF_UNAUTHORIZED_ACCESS_ATTEMPT                      = enum.auto()
    SA_NTF_UNEXPECTED_INFORMATION                           = enum.auto()
    SA_NTF_UNSPECIFIED_REASON                               = enum.auto()

class SaNtfSpecificProblemT(ctypes.Structure):
    _fields_ = [
        ("problemId", SaNtfElementIdT),
        ("problemClassId", SaNtfClassIdT),
        ("problemType", SaNtfValueTypeT),
        ("problemValue", SaNtfValueT),
    ]

SaNtfSeverityT = saAis.SaInt32T
class eSaNtfSeverityT(clUtils.CEnum):
    SA_NTF_SEVERITY_CLEARED = 0
    SA_NTF_SEVERITY_INDETERMINATE = enum.auto()
    SA_NTF_SEVERITY_WARNING = enum.auto()
    SA_NTF_SEVERITY_MINOR = enum.auto()
    SA_NTF_SEVERITY_MAJOR = enum.auto()
    SA_NTF_SEVERITY_CRITICAL = enum.auto()

SaNtfSeverityTrendT = saAis.SaInt32T
class eSaNtfSeverityTrendT(clUtils.CEnum):
    SA_NTF_TREND_MORE_SEVERE = 0
    SA_NTF_TREND_NO_CHANGE = enum.auto()
    SA_NTF_TREND_LESS_SEVERE = enum.auto()

class SaNtfThresholdInformationT(ctypes.Structure):
    _fields_ = [
        ("thresholdId", SaNtfElementIdT),
        ("thresholdValueType", SaNtfValueTypeT),
        ("thresholdValue", SaNtfValueT),
        ("thresholdHysteresis", SaNtfValueT),
        ("observedValue", SaNtfValueT),
        ("armTime", saAis.SaTimeT),
    ]

class SaNtfProposedRepairActionT(ctypes.Structure):
    _fields_ = [
        ("actionId", SaNtfElementIdT),
        ("actionValueType", SaNtfValueTypeT),
        ("actionValue", SaNtfValueT),
    ]

class SaNtfAlarmNotificationT(ctypes.Structure):
    _fields_ = [
        ("notificationHandle", SaNtfNotificationHandleT),
        ("notificationHeader", SaNtfNotificationHeaderT),
        ("numSpecificProblems", saAis.SaUint16T),
        ("numMonitoredAttributes", saAis.SaUint16T),
        ("numProposedRepairActions", saAis.SaUint16T),
        ("probableCause", ctypes.POINTER(SaNtfProbableCauseT)),
        ("specificProblems", ctypes.POINTER(SaNtfSpecificProblemT)),
        ("perceivedSeverity", ctypes.POINTER(SaNtfSeverityT)),
        ("trend", ctypes.POINTER(SaNtfSeverityTrendT)),
        ("thresholdInformation", ctypes.POINTER(SaNtfThresholdInformationT)),
        ("monitoredAttributes", ctypes.POINTER(SaNtfAttributeT)),
        ("proposedRepairActions", ctypes.POINTER(SaNtfProposedRepairActionT)),
    ]

class SaNtfSecurityAlarmDetectorT(ctypes.Structure):
    _fields_ = [
        ("valueType", SaNtfValueTypeT),
        ("value", SaNtfValueT),
    ]

class SaNtfServiceUserT(ctypes.Structure):
    _fields_ = [
        ("valueType", SaNtfValueTypeT),
        ("value", SaNtfValueT),
    ]

class SaNtfSecurityAlarmNotificationT(ctypes.Structure):
    _fields_ = [
        ("notificationHandle", SaNtfNotificationHandleT),
        ("notificationHeader", SaNtfNotificationHeaderT),
        ("probableCause", ctypes.POINTER(SaNtfProbableCauseT)),
        ("severity", ctypes.POINTER(SaNtfSeverityT)),
        ("securityAlarmDetector", ctypes.POINTER(SaNtfSecurityAlarmDetectorT)),
        ("serviceUser", ctypes.POINTER(SaNtfServiceUserT)),
        ("serviceProvider", ctypes.POINTER(SaNtfServiceUserT)),
    ]

class SaNtfMiscellaneousNotificationT(ctypes.Structure):
    _fields_ = [
        ("notificationHandle", SaNtfNotificationHandleT),
        ("notificationHeader", SaNtfNotificationHeaderT),
    ]

SA_NTF_ALLOC_SYSTEM_LIMIT = -1

SaNtfSubscriptionIdT = saAis.SaUint32T

class SaNtfNotificationFilterHeaderT(ctypes.Structure):
    _fields_ = [
        ("numEventTypes", saAis.SaUint16T),
        ("eventTypes", ctypes.POINTER(SaNtfEventTypeT)),
        ("numNotificationObjects", saAis.SaUint16T),
        ("notificationObjects", ctypes.POINTER(saAis.SaNameT)),
        ("numNotifyingObjects", saAis.SaUint16T),
        ("notifyingObjects", ctypes.POINTER(saAis.SaNameT)),
        ("numNotificationClassIds", saAis.SaUint16T),
        ("notificationClassIds", ctypes.POINTER(SaNtfClassIdT)),
    ]

class SaNtfObjectCreateDeleteNotificationFilterT(ctypes.Structure):
    _fields_ = [
        ("notificationFilterHandle", SaNtfNotificationFilterHandleT),
        ("notificationFilterHeader", SaNtfNotificationFilterHeaderT),
        ("numSourceIndicators", saAis.SaUint16T),
        ("sourceIndicators", ctypes.POINTER(SaNtfSourceIndicatorT)),
    ]

class SaNtfAttributeChangeNotificationFilterT(ctypes.Structure):
    _fields_ = [
        ("notificationFilterHandle", SaNtfNotificationFilterHandleT),
        ("notificationFilterHeader", SaNtfNotificationFilterHeaderT),
        ("numSourceIndicators", saAis.SaUint16T),
        ("sourceIndicators", ctypes.POINTER(SaNtfSourceIndicatorT)),
    ]

class SaNtfStateChangeNotificationFilterT(ctypes.Structure):
    _fields_ = [
        ("notificationFilterHandle", SaNtfNotificationFilterHandleT),
        ("notificationFilterHeader", SaNtfNotificationFilterHeaderT),
        ("numSourceIndicators", saAis.SaUint16T),
        ("sourceIndicators", ctypes.POINTER(SaNtfSourceIndicatorT)),
        ("numStateChanges", saAis.SaUint16T),
        ("changedStates", ctypes.POINTER(SaNtfStateChangeT)),
    ]

class SaNtfStateChangeNotificationFilterT_2(ctypes.Structure):
    _fields_ = [
        ("notificationFilterHandle", SaNtfNotificationFilterHandleT),
        ("notificationFilterHeader", SaNtfNotificationFilterHeaderT),
        ("numSourceIndicators", saAis.SaUint16T),
        ("sourceIndicators", ctypes.POINTER(SaNtfSourceIndicatorT)),
        ("numStateChanges", saAis.SaUint16T),
        ("stateId", ctypes.POINTER(SaNtfElementIdT)),
    ]

class SaNtfAlarmNotificationFilterT(ctypes.Structure):
    _fields_ = [
        ("notificationFilterHandle", SaNtfNotificationFilterHandleT),
        ("notificationFilterHeader", SaNtfNotificationFilterHeaderT),
        ("numProbableCauses", saAis.SaUint16T),
        ("numPerceivedSeverities", saAis.SaUint16T),
        ("numTrends", saAis.SaUint16T),
        ("probableCauses", ctypes.POINTER(SaNtfProbableCauseT)),
        ("perceivedSeverities", ctypes.POINTER(SaNtfSeverityT)),
        ("trends", ctypes.POINTER(SaNtfSeverityTrendT)),
    ]

class SaNtfSecurityAlarmNotificationFilterT(ctypes.Structure):
    _fields_ = [
        ("notificationFilterHandle", SaNtfNotificationFilterHandleT),
        ("notificationFilterHeader", SaNtfNotificationFilterHeaderT),
        ("numProbableCauses", saAis.SaUint16T),
        ("numSeverities", saAis.SaUint16T),
        ("numSecurityAlarmDetectors", saAis.SaUint16T),
        ("numServiceUsers", saAis.SaUint16T),
        ("numServiceProviders", saAis.SaUint16T),
        ("probableCauses", ctypes.POINTER(SaNtfProbableCauseT)),
        ("severities", ctypes.POINTER(SaNtfSeverityT)),
        ("securityAlarmDetectors", ctypes.POINTER(SaNtfSecurityAlarmDetectorT)),
        ("serviceUsers", ctypes.POINTER(SaNtfServiceUserT)),
        ("serviceProviders", ctypes.POINTER(SaNtfServiceUserT)),
    ]

class SaNtfMiscellaneousNotificationFilterT(ctypes.Structure):
    _fields_ = [
        ("notificationFilterHandle", SaNtfNotificationFilterHandleT),
        ("notificationFilterHeader", SaNtfNotificationFilterHeaderT),
    ]

SaNtfSearchModeT = saAis.SaInt32T
class eSaNtfSearchModeT(clUtils.CEnum):
    SA_NTF_SEARCH_BEFORE_OR_AT_TIME = 1
    SA_NTF_SEARCH_AT_TIME = 2
    SA_NTF_SEARCH_AT_OR_AFTER_TIME = 3
    SA_NTF_SEARCH_BEFORE_TIME = 4
    SA_NTF_SEARCH_AFTER_TIME = 5
    SA_NTF_SEARCH_NOTIFICATION_ID = 6
    SA_NTF_SEARCH_ONLY_FILTER = 7

class SaNtfSearchCriteriaT(ctypes.Structure):
    _fields_ = [
        ("searchMode", SaNtfSearchModeT),
        ("eventTime", saAis.SaTimeT),
        ("notificationId", SaNtfIdentifierT),
    ]

SaNtfSearchDirectionT = saAis.SaInt32T
class eSaNtfSearchDirectionT(clUtils.CEnum):
    SA_NTF_SEARCH_OLDER = 1,
    SA_NTF_SEARCH_YOUNGER = 2

class SaNtfNotificationTypeFilterHandlesT(ctypes.Structure):
    _fields_ = [
        ("objectCreateDeleteFilterHandle", SaNtfNotificationFilterHandleT),
        ("attributeChangeFilterHandle", SaNtfNotificationFilterHandleT),
        ("stateChangeFilterHandle", SaNtfNotificationFilterHandleT),
        ("alarmFilterHandle", SaNtfNotificationFilterHandleT),
        ("securityAlarmFilterHandle", SaNtfNotificationFilterHandleT),
    ]

class SaNtfNotificationTypeFilterHandlesT_3(ctypes.Structure):
    _fields_ = [
        ("objectCreateDeleteFilterHandle", SaNtfNotificationFilterHandleT),
        ("attributeChangeFilterHandle", SaNtfNotificationFilterHandleT),
        ("stateChangeFilterHandle", SaNtfNotificationFilterHandleT),
        ("alarmFilterHandle", SaNtfNotificationFilterHandleT),
        ("securityAlarmFilterHandle", SaNtfNotificationFilterHandleT),
        ("miscellaneousFilterHandle", SaNtfNotificationFilterHandleT),
    ]

SA_NTF_FILTER_HANDLE_NULL = 0

class _notification(ctypes.Union):
    _fields_ = [
		("objectCreateDeleteNotification", SaNtfObjectCreateDeleteNotificationT),
		("attributeChangeNotification", SaNtfAttributeChangeNotificationT),
        ("stateChangeNotification", SaNtfStateChangeNotificationT),
        ("alarmNotification", SaNtfAlarmNotificationT),
        ("securityAlarmNotification", SaNtfSecurityAlarmNotificationT),
	]

class SaNtfNotificationsT(ctypes.Structure):
    _fields_ = [
        ("notificationType", SaNtfNotificationTypeT),
        ("notification", _notification),
    ]

SaNtfStateT = saAis.SaInt32T
class eSaNtfStateT(clUtils.CEnum):
    SA_NTF_STATIC_FILTER_STATE = 1
    SA_NTF_SUBSCRIBER_STATE = 2

SaNtfStaticFilterStateT = saAis.SaInt32T
class eSaNtfStaticFilterStateT(clUtils.CEnum):
    SA_NTF_STATIC_FILTER_STATE_INACTIVE = 1
    SA_NTF_STATIC_FILTER_STATE_ACTIVE = 2

SaNtfSubscriberStateT = saAis.SaInt32T
class eSaNtfSubscriberStateT(clUtils.CEnum):
    SA_NTF_SUBSCRIBER_STATE_FORWARD_NOT_OK = 1
    SA_NTF_SUBSCRIBER_STATE_FORWARD_OK = 2

SaNtfNotificationMinorIdT = saAis.SaInt32T
class eSaNtfNotificationMinorIdT(clUtils.CEnum):
    SA_NTF_NTFID_STATIC_FILTER_ACTIVATED = 0x065
    SA_NTF_NTFID_STATIC_FILTER_DEACTIVATED = 0x066
    SA_NTF_NTFID_CONSUMER_SLOW = 0x067
    SA_NTF_NTFID_CONSUMER_FAST_ENOUGH = 0x068

SaNtfNotificationCallbackT = ctypes.CFUNCTYPE(
    None,
    SaNtfSubscriptionIdT,
    ctypes.POINTER(SaNtfNotificationsT)
)

SaNtfNotificationDiscardedCallbackT = ctypes.CFUNCTYPE(
    None,
    SaNtfSubscriptionIdT,
    SaNtfNotificationTypeT,
    saAis.SaUint32T,
    ctypes.POINTER(SaNtfIdentifierT)
)

class SaNtfCallbacksT(ctypes.Structure):
    _fields_ = [
        ("saNtfNotificationCallback", SaNtfNotificationCallbackT),
        ("saNtfNotificationDiscardedCallback", SaNtfNotificationDiscardedCallbackT),
    ]

def saNtfInitialize(ntfHandle, ntfCallbacks, version):
    """
    arg types:
        SaNtfHandleT *ntfHandle,
        SaNtfCallbacksT *ntfCallbacks,
        SaVersionT *version

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfInitialize(
        ctypes.byref(ntfHandle),
        ctypes.byref(ntfCallbacks),
        ctypes.byref(version)
    )

def saNtfLocalizedMessageFree(message):
    """
    arg types:
        SaStringT message

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfLocalizedMessageFree(message)

def saNtfStateChangeNotificationFilterAllocate(
    ntfHandle,
    notificationFilter,
    numEventTypes,
    numNotificationObjects,
    numNotifyingObjects,
    numNotificationClassIds,
    numSourceIndicators,
    numChangedStates
):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfStateChangeNotificationFilterT *notificationFilter,
        SaUint16T numEventTypes,
        SaUint16T numNotificationObjects,
        SaUint16T numNotifyingObjects,
        SaUint16T numNotificationClassIds,
        SaUint32T numSourceIndicators,
        SaUint32T numChangedStates

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfStateChangeNotificationFilterAllocate(
        ntfHandle,
        ctypes.byref(notificationFilter),
        numEventTypes,
        numNotificationObjects,
        numNotifyingObjects,
        numNotificationClassIds,
        numSourceIndicators,
        numChangedStates
    )

def saNtfNotificationUnsubscribe(subscriptionId):
    """
    arg types:
        SaNtfSubscriptionIdT subscriptionId

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationUnsubscribe(subscriptionId)

def saNtfNotificationReadInitialize(searchCriteria, notificationFilterHandles, readHandle):
    """
    arg types:
        SaNtfSearchCriteriaT searchCriteria,
        SaNtfNotificationTypeFilterHandlesT *notificationFilterHandles,
        SaNtfReadHandleT *readHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationReadInitialize(
        searchCriteria,
        ctypes.byref(notificationFilterHandles),
        ctypes.byref(readHandle)
    )

SaNtfStaticSuppressionFilterSetCallbackT = ctypes.CFUNCTYPE(None, SaNtfHandleT, saAis.SaUint16T)

class SaNtfCallbacksT_2(ctypes.Structure):
    _fields_ = [
        ("saNtfNotificationCallback", SaNtfNotificationCallbackT),
        ("saNtfNotificationDiscardedCallback", SaNtfNotificationDiscardedCallbackT),
        ("saNtfStaticSuppressionFilterSetCallback", SaNtfStaticSuppressionFilterSetCallbackT),
    ]

def saNtfInitialize_2(ntfHandle, ntfCallbacks, version):
    """
    arg types:
        SaNtfHandleT *ntfHandle,
        SaNtfCallbacksT_2 *ntfCallbacks,
        SaVersionT *version

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfInitialize_2(
        ctypes.byref(ntfHandle),
        ctypes.byref(ntfCallbacks),
        ctypes.byref(version)
    )

def saNtfNotificationReadInitialize_2(searchCriteria, notificationFilterHandles, readHandle):
    """
    arg types:
        SaNtfSearchCriteriaT *searchCriteria,
        SaNtfNotificationTypeFilterHandlesT *notificationFilterHandles,
        SaNtfReadHandleT *readHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationReadInitialize_2(
        ctypes.byref(searchCriteria),
        ctypes.byref(notificationFilterHandles),
        ctypes.byref(readHandle)
    )

def saNtfNotificationSubscribe(notificationFilterHandles, subscriptionId):
    """
    arg types:
        SaNtfNotificationTypeFilterHandlesT *notificationFilterHandles,
        SaNtfSubscriptionIdT subscriptionId

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationSubscribe(
        ctypes.byref(notificationFilterHandles),
        subscriptionId
    )

SaNtfStaticSuppressionFilterSetCallbackT_3 = ctypes.CFUNCTYPE(None, SaNtfHandleT, SaNtfEventTypeBitmapT)

class SaNtfCallbacksT_3(ctypes.Structure):
    _fields_ = [
        ("saNtfNotificationCallback", SaNtfNotificationCallbackT),
        ("saNtfNotificationDiscardedCallback", SaNtfNotificationDiscardedCallbackT),
        ("saNtfStaticSuppressionFilterSetCallback", SaNtfStaticSuppressionFilterSetCallbackT_3),
    ]

def saNtfInitialize_3(ntfHandle, ntfCallbacks, version):
    """
    arg types:
        SaNtfHandleT *ntfHandle,
        SaNtfCallbacksT_3 *ntfCallbacks,
        SaVersionT *version

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfInitialize_3(
        ctypes.byref(ntfHandle),
        ctypes.byref(ntfCallbacks),
        ctypes.byref(version)
    )

def saNtfSelectionObjectGet(ntfHandle, selectionObject):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaSelectionObjectT *selectionObject

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfSelectionObjectGet(
        ntfHandle,
        ctypes.byref(selectionObject)
    )

def saNtfDispatch(ntfHandle, dispatchFlags):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaDispatchFlagsT dispatchFlags)

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfDispatch(ntfHandle, dispatchFlags)

def saNtfFinalize(ntfHandle):
    """
    arg types:
        SaNtfHandleT ntfHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfFinalize(ntfHandle)

def saNtfObjectCreateDeleteNotificationAllocate(
    ntfHandle,
    notification,
    numCorrelatedNotifications,
    lengthAdditionalText,
    numAdditionalInfo,
    numAttributes,
    variableDataSize
):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfObjectCreateDeleteNotificationT *notification,
        SaUint16T numCorrelatedNotifications,
        SaUint16T lengthAdditionalText,
        SaUint16T numAdditionalInfo,
        SaUint16T numAttributes,
        SaInt16T variableDataSize

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfObjectCreateDeleteNotificationAllocate(
        ntfHandle,
        ctypes.byref(notification),
        numCorrelatedNotifications,
        lengthAdditionalText,
        numAdditionalInfo,
        numAttributes,
        variableDataSize
    )

def saNtfAttributeChangeNotificationAllocate(
    ntfHandle,
    notification,
    numCorrelatedNotifications,
    lengthAdditionalText,
    numAdditionalInfo,
    numAttributes,
    variableDataSize
):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfAttributeChangeNotificationT *notification,
        SaUint16T numCorrelatedNotifications,
        SaUint16T lengthAdditionalText,
        SaUint16T numAdditionalInfo,
        SaUint16T numAttributes,
        SaInt16T variableDataSize

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfAttributeChangeNotificationAllocate(
        ntfHandle,
        ctypes.byref(notification),
        numCorrelatedNotifications,
        lengthAdditionalText,
        numAdditionalInfo,
        numAttributes,
        variableDataSize
    )

def saNtfStateChangeNotificationAllocate(
    ntfHandle,
    notification,
    numCorrelatedNotifications,
    lengthAdditionalText,
    numAdditionalInfo,
    numStateChanges,
    variableDataSize
):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfStateChangeNotificationT *notification,
        SaUint16T numCorrelatedNotifications,
        SaUint16T lengthAdditionalText,
        SaUint16T numAdditionalInfo,
        SaUint16T numStateChanges,
        SaInt16T variableDataSize

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfStateChangeNotificationAllocate(
        ntfHandle,
        ctypes.byref(notification),
        numCorrelatedNotifications,
        lengthAdditionalText,
        numAdditionalInfo,
        numStateChanges,
        variableDataSize
    )

def saNtfAlarmNotificationAllocate(
    ntfHandle,
    notification,
    numCorrelatedNotifications,
    lengthAdditionalText,
    numAdditionalInfo,
    numSpecificProblems,
    numMonitoredAttributes,
    numProposedRepairActions,
    variableDataSize
):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfAlarmNotificationT *notification,
        SaUint16T numCorrelatedNotifications,
        SaUint16T lengthAdditionalText,
        SaUint16T numAdditionalInfo,
        SaUint16T numSpecificProblems,
        SaUint16T numMonitoredAttributes,
        SaUint16T numProposedRepairActions,
        SaInt16T variableDataSize

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfAlarmNotificationAllocate(
        ntfHandle,
        ctypes.byref(notification),
        numCorrelatedNotifications,
        lengthAdditionalText,
        numAdditionalInfo,
        numSpecificProblems,
        numMonitoredAttributes,
        numProposedRepairActions,
        variableDataSize
    )

def saNtfSecurityAlarmNotificationAllocate(
    ntfHandle,
    notification,
    numCorrelatedNotifications,
    lengthAdditionalText,
    numAdditionalInfo,
    variableDataSize
):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfSecurityAlarmNotificationT *notification,
        SaUint16T numCorrelatedNotifications,
        SaUint16T lengthAdditionalText,
        SaUint16T numAdditionalInfo,
        SaInt16T variableDataSize

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfSecurityAlarmNotificationAllocate(
        ntfHandle,
        ctypes.byref(notification),
        numCorrelatedNotifications,
        lengthAdditionalText,
        numAdditionalInfo,
        variableDataSize
    )

def saNtfPtrValAllocate(notificationHandle, dataSize, dataPtr, value):
    """
    arg types:
        SaNtfNotificationHandleT notificationHandle,
        SaUint16T dataSize,
        void **dataPtr,
        SaNtfValueT *value

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfPtrValAllocate(
        notificationHandle,
        dataSize,
        ctypes.byref(dataPtr),
        ctypes.byref(value)
    )

def saNtfArrayValAllocate(notificationHandle, numElements, elementSize, arrayPtr, value):
    """
    arg types:
        SaNtfNotificationHandleT notificationHandle,
        SaUint16T numElements,
        SaUint16T elementSize,
        void **arrayPtr,
        SaNtfValueT *value

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfArrayValAllocate(
        notificationHandle,
        numElements,
        elementSize,
        ctypes.byref(arrayPtr),
        ctypes.byref(value)
    )

def saNtfNotificationSend(notificationHandle):
    """
    arg types:
        SaNtfNotificationHandleT notificationHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationSend(notificationHandle)

def saNtfNotificationFree(notificationHandle):
    """
    arg types:
        SaNtfNotificationHandleT notificationHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationFree(notificationHandle)

def saNtfVariableDataSizeGet(notificationHandle, variableDataSpaceAvailable):
    """
    arg types:
        SaNtfNotificationHandleT notificationHandle,
        SaUint16T *variableDataSpaceAvailable

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfVariableDataSizeGet(
        notificationHandle,
        ctypes.byref(variableDataSpaceAvailable)
    )

def saNtfLocalizedMessageGet(notificationHandle, message):
    """
    arg types:
        SaNtfNotificationHandleT notificationHandle,
        SaStringT *message

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfLocalizedMessageGet(
        notificationHandle,
        ctypes.byref(message)
    )

def saNtfLocalizedMessageFree_2(ntfHandle, message):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaStringT message

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfLocalizedMessageFree_2(ntfHandle, message)

def saNtfPtrValGet(notificationHandle, value, dataPtr, dataSize):
    """
    arg types:
        SaNtfNotificationHandleT notificationHandle,
        SaNtfValueT *value,
        void **dataPtr,
        SaUint16T *dataSize

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfPtrValGet(
        notificationHandle,
        ctypes.byref(value),
        ctypes.byref(dataPtr),
        ctypes.byref(dataSize)
    )

def saNtfArrayValGet(notificationHandle, value, arrayPtr, numElements, elementSize):
    """
    arg types:
        SaNtfNotificationHandleT notificationHandle,
        SaNtfValueT *value,
        void **arrayPtr,
        SaUint16T *numElements,
        SaUint16T *elementSize

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfArrayValGet(
        notificationHandle,
        ctypes.byref(value),
        ctypes.byref(arrayPtr),
        ctypes.byref(numElements),
        ctypes.byref(elementSize)
    )

def saNtfObjectCreateDeleteNotificationFilterAllocate(
    ntfHandle,
    notificationFilter,
    numEventTypes,
    numNotificationObjects,
    numNotifyingObjects,
    numNotificationClassIds,
    numSourceIndicators
):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfObjectCreateDeleteNotificationFilterT *notificationFilter,
        SaUint16T numEventTypes,
        SaUint16T numNotificationObjects,
        SaUint16T numNotifyingObjects,
        SaUint16T numNotificationClassIds,
        SaUint16T numSourceIndicators

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfObjectCreateDeleteNotificationFilterAllocate(
        ntfHandle,
        ctypes.byref(notificationFilter),
        numEventTypes,
        numNotificationObjects,
        numNotifyingObjects,
        numNotificationClassIds,
        numSourceIndicators
    )

def saNtfAttributeChangeNotificationFilterAllocate(
    ntfHandle,
    notificationFilter,
    numEventTypes,
    numNotificationObjects,
    numNotifyingObjects,
    numNotificationClassIds,
    numSourceIndicators
):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfAttributeChangeNotificationFilterT *notificationFilter,
        SaUint16T numEventTypes,
        SaUint16T numNotificationObjects,
        SaUint16T numNotifyingObjects,
        SaUint16T numNotificationClassIds,
        SaUint32T numSourceIndicators

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfAttributeChangeNotificationFilterAllocate(
        ntfHandle,
        ctypes.byref(notificationFilter),
        numEventTypes,
        numNotificationObjects,
        numNotifyingObjects,
        numNotificationClassIds,
        numSourceIndicators
    )

def saNtfStateChangeNotificationFilterAllocate_2(
    ntfHandle,
    notificationFilter,
    numEventTypes,
    numNotificationObjects,
    numNotifyingObjects,
    numNotificationClassIds,
    numSourceIndicators,
    numChangedStates
):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfStateChangeNotificationFilterT_2 *notificationFilter,
        SaUint16T numEventTypes,
        SaUint16T numNotificationObjects,
        SaUint16T numNotifyingObjects,
        SaUint16T numNotificationClassIds,
        SaUint32T numSourceIndicators,
        SaUint32T numChangedStates

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfStateChangeNotificationFilterAllocate_2(
        ntfHandle,
        ctypes.byref(notificationFilter),
        numEventTypes,
        numNotificationObjects,
        numNotifyingObjects,
        numNotificationClassIds,
        numSourceIndicators,
        numChangedStates
    )

def saNtfAlarmNotificationFilterAllocate(
    ntfHandle,
    notificationFilter,
    numEventTypes,
    numNotificationObjects,
    numNotifyingObjects,
    numNotificationClassIds,
    numProbableCauses,
    numPerceivedSeverities,
    numTrends
):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfAlarmNotificationFilterT *notificationFilter,
        SaUint16T numEventTypes,
        SaUint16T numNotificationObjects,
        SaUint16T numNotifyingObjects,
        SaUint16T numNotificationClassIds,
        SaUint32T numProbableCauses,
        SaUint32T numPerceivedSeverities,
        SaUint32T numTrends

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfAlarmNotificationFilterAllocate(
        ntfHandle,
        ctypes.byref(notificationFilter),
        numEventTypes,
        numNotificationObjects,
        numNotifyingObjects,
        numNotificationClassIds,
        numProbableCauses,
        numPerceivedSeverities,
        numTrends
    )

def saNtfSecurityAlarmNotificationFilterAllocate(
    ntfHandle,
    notificationFilter,
    numEventTypes,
    numNotificationObjects,
    numNotifyingObjects,
    numNotificationClassIds,
    numProbableCauses,
    numSeverities,
    numSecurityAlarmDetectors,
    numServiceUsers,
    numServiceProviders
):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfSecurityAlarmNotificationFilterT *notificationFilter,
        SaUint16T numEventTypes,
        SaUint16T numNotificationObjects,
        SaUint16T numNotifyingObjects,
        SaUint16T numNotificationClassIds,
        SaUint32T numProbableCauses,
        SaUint32T numSeverities,
        SaUint32T numSecurityAlarmDetectors,
        SaUint32T numServiceUsers,
        SaUint32T numServiceProviders

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfSecurityAlarmNotificationFilterAllocate(
        ntfHandle,
        ctypes.byref(notificationFilter),
        numEventTypes,
        numNotificationObjects,
        numNotifyingObjects,
        numNotificationClassIds,
        numProbableCauses,
        numSeverities,
        numSecurityAlarmDetectors,
        numServiceUsers,
        numServiceProviders
    )

def saNtfNotificationFilterFree(notificationFilterHandle):
    """
    arg types:
        SaNtfNotificationFilterHandleT notificationFilterHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationFilterFree(notificationFilterHandle)

def saNtfNotificationSubscribe_3(notificationFilterHandles, subscriptionId):
    """
    arg types:
        SaNtfNotificationTypeFilterHandlesT_3 *notificationFilterHandles,
        SaNtfSubscriptionIdT subscriptionId

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationSubscribe_3(
        ctypes.byref(notificationFilterHandles),
        subscriptionId
    )

def saNtfNotificationReadInitialize_3(searchCriteria, notificationFilterHandles, readHandle):
    """
    arg types:
        SaNtfSearchCriteriaT *searchCriteria,
        SaNtfNotificationTypeFilterHandlesT_3 *notificationFilterHandles,
        SaNtfReadHandleT *readHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationReadInitialize_3(
       ctypes.byref(searchCriteria),
       ctypes.byref(notificationFilterHandles),
       ctypes.byref(readHandle)
    )

def saNtfNotificationUnsubscribe_2(ntfHandle, subscriptionId):
    """
    arg types:
        SaNtfHandleT ntfHandle,
        SaNtfSubscriptionIdT subscriptionId

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationUnsubscribe_2(ntfHandle, subscriptionId)

def saNtfNotificationReadNext(readHandle, searchDirection, notification):
    """
    arg types:
        SaNtfReadHandleT readHandle,
        SaNtfSearchDirectionT searchDirection,
        SaNtfNotificationsT *notification

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationReadNext(
        readHandle,
        searchDirection,
        ctypes.byref(notification)
    )

def saNtfNotificationReadFinalize(readHandle):
    """
    arg types:
        SaNtfReadHandleT readHandle

    return type:
        SaAisErrorT
    """
    return clLib.libmw_so.saNtfNotificationReadFinalize(readHandle)
