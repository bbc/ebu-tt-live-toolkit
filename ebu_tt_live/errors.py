
from .strings import ERR_DOCUMENT_EXTENT_MISSING, ERR_EBUTTD_OVERLAPPING_ACTIVE_AREAS, ERR_EBUTTD_REGION_EXTENDING_OUTSIDE_DOCUMENT, ERR_REGION_ORIGIN_TYPE, ERR_REGION_EXTENT_TYPE


class ComponentCompatError(TypeError):
    pass


class DataCompatError(TypeError):
    pass


class DocumentNotLoadedError(Exception):
    pass


class TimeFormatError(Exception):
    pass


class TimeFormatOverflowError(Exception):
    pass


class TimeNegativeError(Exception):
    pass


class XMLParsingFailed(Exception):
    pass


class SemanticValidationError(Exception):
    pass


class EndOfData(Exception):
    pass


class IncompatibleSequenceError(Exception):
    pass


class SequenceNumberCollisionError(IncompatibleSequenceError):
    pass


class DocumentDiscardedError(Exception):
    offending_document = None


class SequenceOverridden(Exception):
    pass


class LogicError(Exception):
    pass


class ExtentMissingError(Exception):

    _attribute = None

    def __init__(self, attribute):
        self._attribute = attribute

    def __str__(self):
        return ERR_DOCUMENT_EXTENT_MISSING.format(type=type(self._attribute), value=self._attribute)


class StopBranchIteration(Exception):
    """
    Let the iterator know that it can proceed to the next branch. It does not need to traverse the current one any
    further.
    """


class OutsideSegmentError(StopBranchIteration):
    """
    This exception is meant to be raised by the copying functionality to make the iterator know that a particular
    subtree is not meant to be parsed.
    """


class DiscardElement(Exception):
    """
    There is a possibility that an element may become superfluous or lose its value. Such a possibility  can happen
    in segmentation when a p element gets selected because it contains 2 spans but the segment happens to be selecting
    an interval between them so the container ends up being empty and thus should be discarded.
    """


class ConfigurationError(Exception):
    pass


class UnexpectedSequenceIdentifierError(Exception):
    pass


class UnexpectedAuthorsGroupError(Exception):
    pass

class OverlappingActiveElementsError(Exception):
    
    _attribute = None
    _region1 = None
    _region2 = None
    _elem1_id = None
    _elem2_id = None

    def __init__(self, attribute, region1, region2, elem1_id, elem2_id):
        self._attribute = attribute
        self._region1 = region1
        self._region2 = region2
        self._elem1_id = elem1_id
        self._elem2_id = elem2_id

    def __str__(self):
        return ERR_EBUTTD_OVERLAPPING_ACTIVE_AREAS.format(
            type=type(self._attribute), 
            value=self._attribute,
            elem1_id=self._elem1_id,
            region1_id=self._region1.id,
            region1_origin=self._region1.origin,
            region1_extent=self._region1.extent,
            elem2_id=self._elem2_id,
            region2_id=self._region2.id,
            region2_origin=self._region2.origin,
            region2_extent=self._region2.extent,
        )


class RegionExtendingOutsideDocumentError(Exception):
    
    _attribute = None

    def __init__(self, attribute):
        self._attribute = attribute

    def __str__(self):
        return ERR_EBUTTD_REGION_EXTENDING_OUTSIDE_DOCUMENT.format(type=type(self._attribute), value=self._attribute)


class InvalidRegionOriginType(Exception):#
    _attribute = None

    def __init__(self, attribute):
        self._attribute = attribute

    def __str__(self):
        return ERR_REGION_ORIGIN_TYPE.format(type=type(self._attribute), value=self._attribute)

class InvalidRegionExtentType(Exception):#
    _attribute = None

    def __init__(self, attribute):
        self._attribute = attribute

    def __str__(self):
        return ERR_REGION_EXTENT_TYPE.format(type=type(self._attribute), value=self._attribute)