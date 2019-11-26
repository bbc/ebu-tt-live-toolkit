
from ebu_tt_live.bindings.converters.ebutt3_ebuttd import EBUTT3EBUTTDConverter
from ebu_tt_live.bindings.converters.ebutt1_ebutt3 import EBUTT1EBUTT3Converter
from ebu_tt_live.bindings.converters.timedelta_converter import \
    FixedOffsetSMPTEtoTimedeltaConverter

from ebu_tt_live.documents.ebuttd import EBUTTDDocument
from ebu_tt_live.documents.ebutt1 import EBUTT1Document
from ebu_tt_live.documents.ebutt3 import EBUTT3Document
import logging


log = logging.getLogger(__name__)


def ebutt3_to_ebuttd(ebutt3_in, media_clock):
    """
    This function takes an EBUTT3Document instance and returns the same
    document as an EBUTTDDocument instance.
    :param ebutt3_in:
    :return:
    """

    converter = EBUTT3EBUTTDConverter(media_clock=media_clock)
    # Here we need a thing that makes sure that the times in the input 
    # document do not depend on a body@dur attribute, and that they are
    # absolutised, so a body with no begin or end time but with a dur
    # gets fixed into a body with an end time, which gives the
    # denester an easier job.
    doc_xml = ebutt3_in.get_xml()
    ebutt3_doc = EBUTT3Document.create_from_xml(doc_xml)
    ebuttd_bindings = converter.convert_document(ebutt3_doc.binding)
    ebuttd_document = EBUTTDDocument.create_from_raw_binding(ebuttd_bindings)
    ebuttd_document.validate()
    return ebuttd_document


def ebutt1_to_ebutt3(ebutt1_in, sequence_id, use_doc_id_as_seq_id):
    """
    This function takes an EBUTT1Document instance and returns the same 
    document as an EBUTT3Document instance.
    :param ebutt1_in:
    :return:
    """
    converter = EBUTT1EBUTT3Converter(
        sequence_id=sequence_id, 
        use_doc_id_as_seq_id=use_doc_id_as_seq_id)
    doc_xml = ebutt1_in.get_xml()
    ebutt1_doc = EBUTT1Document.create_from_xml(doc_xml)

    smpte_converter = None
    if ebutt1_doc.binding.timeBase == 'smpte':
        start_of_programme = '00:00:00:00'
        head_metadata = ebutt1_doc.binding.head.metadata
        if head_metadata:
            doc_metadata = head_metadata.documentMetadata
            if doc_metadata and doc_metadata.documentStartOfProgramme:
                start_of_programme = doc_metadata.documentStartOfProgramme
        smpte_converter = \
            FixedOffsetSMPTEtoTimedeltaConverter(
                start_of_programme,
                ebutt1_doc.binding.frameRate,
                ebutt1_doc.binding.frameRateMultiplier,
                ebutt1_doc.binding.dropMode
            )

    ebutt3_bindings = converter.convert_document(
        ebutt1_doc.binding,
        dataset=None,
        smpte_to_timedelta_converter=smpte_converter)
    ebutt3_document = EBUTT3Document.create_from_raw_binding(ebutt3_bindings)
    ebutt3_document.validate()
    return ebutt3_document
