from ebu_tt_live.bindings.converters.ebutt1_ebutt3 import EBUTT1EBUTT3Converter
from ebu_tt_live.documents.ebutt1 import EBUTT1Document
from .base import AbstractCombinedNode
from ebu_tt_live.documents.ebutt3 import EBUTT3Document
from ebu_tt_live.bindings.converters.timedelta_converter \
    import FixedOffsetSMPTEtoTimedeltaConverter


class EBUTT1EBUTT3ProducerNode(AbstractCombinedNode):
    """
    Produce an EBU-TT-3 document from an EBU-TT-1 input document.

    For conversion of SMPTE timecodes, where ``ttp:timeBase="smpte"``,
    makes a 
    :py:class:`ebu_tt_live.bindings.converters.timedelta_converter.FixedOffsetSMPTEtoTimedeltaConverter` using `00:00:00:00`
    as the start of programme zero point, or if available, uses the
    `ebuttm:documentStartOfProgramme` metadata value as the zero point,
    and discards everything before the value of that element.

    The output sequence identifier can be specified. Alternatively,
    if the ``use_document_identifier_as_sequence_identifier`` parameter
    is ``True`` and the ``ebuttm:documentIdentifier`` element is present
    then that element's value is
    used as the output sequence identifier.
    """
    _ebutt3_converter = None
    _expects = EBUTT1Document
    _provides = EBUTT3Document

    def __init__(self,
                 node_id,
                 consumer_carriage=None,
                 producer_carriage=None,
                 sequence_identifier=None,
                 use_document_identifier_as_sequence_identifier=True,
                 **kwargs):
        super(EBUTT1EBUTT3ProducerNode, self).__init__(
            node_id=node_id,
            consumer_carriage=consumer_carriage,
            producer_carriage=producer_carriage,
            **kwargs
        )
        self._ebutt3_converter = EBUTT1EBUTT3Converter(
            sequence_id=sequence_identifier,
            use_doc_id_as_seq_id=use_document_identifier_as_sequence_identifier)

    def process_document(self, document, **kwargs):
        # Convert each receiver document into EBU-TT-3
        if self.is_document(document):
            smpte_converter = None
            if document.binding.timeBase == 'smpte':
                start_of_programme = '00:00:00:00'
                head_metadata = document.binding.head.metadata
                if head_metadata:
                    doc_metadata = head_metadata.documentMetadata
                    if doc_metadata and doc_metadata.documentStartOfProgramme:
                        start_of_programme = \
                            doc_metadata.documentStartOfProgramme
                smpte_converter = \
                    FixedOffsetSMPTEtoTimedeltaConverter(
                        smpteReference=start_of_programme,
                        frameRate=document.binding.frameRate,
                        frameRateMultiplier=document.binding.
                        frameRateMultiplier,
                        dropMode=document.binding.dropMode
                    )
            converted_doc = EBUTT3Document.create_from_raw_binding(
                self._ebutt3_converter.convert_document(
                    document.binding,
                    dataset=None,
                    smpte_to_timedelta_converter=smpte_converter)
            )
            self.producer_carriage.emit_data(data=converted_doc, **kwargs)
