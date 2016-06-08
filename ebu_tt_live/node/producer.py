
from .base import ProducerNode
from datetime import timedelta
from ebu_tt_live.bindings import div_type, br_type, p_type


class SimpleProducer(ProducerNode):

    _document_sequence = None
    _input_blocks = None
    _reference_clock = None

    def __init__(self, node_id, document_sequence, input_blocks):
        super(SimpleProducer, self).__init__(node_id)
        self._document_sequence = document_sequence
        self._input_blocks = input_blocks
        self._reference_clock = document_sequence.reference_clock

    @staticmethod
    def _interleave_line_breaks(items):
        end_list = []
        for item in items:
            end_list.append(item)
            end_list.append(br_type())
        # We don't require the last linebreak so remove it.
        end_list.pop()
        return end_list

    def _create_fragment(self, lines):
        return div_type(
            p_type(
                *self._interleave_line_breaks(lines),
                id='ID{:03d}'.format(1)
            )
        )

    def process_document(self, document):

        activation_time = self._reference_clock.get_time() + timedelta(seconds=1)

        if self._input_blocks:
            lines = self._input_blocks.next()
        else:
            lines = [activation_time]

        document = self._document_sequence.new_document()

        document.add_div(
            self._create_fragment(
                lines
            )
        )

        document.set_dur(timedelta(seconds=1))
        document.set_begin(activation_time)

        document.validate()

        self.emit_document(document)