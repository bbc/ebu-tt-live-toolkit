
from gettext import gettext

# ERRORS
ERR_CONV_NO_INPUT = gettext('The converter has no input set')
ERR_TIME_WRONG_FORMAT = gettext('Wrong time format. datetime.timedelta is expected')
ERR_TIME_FORMAT_OVERFLOW = gettext('Time value is out of format range')
ERR_DOCUMENT_SEQUENCE_MISMATCH = gettext('sequenceIdentifier mismatch')
ERR_DECODING_XML_FAILED = gettext('XML document parsing failed')
ERR_SEMANTIC_VALIDATION_TIMING_TYPE = gettext('{attr_type}({attr_value}) is not a valid type for {attr_name} in timeBase={time_base}')
ERR_SEMANTIC_VALIDATION_MISSING_ATTRIBUTES = gettext('{elem_name} is missing attributes: {attr_names}')
ERR_SEMANTIC_VALIDATION_INVALID_ATTRIBUTES = gettext('{elem_name} has invalid attributes: {attr_names}')
