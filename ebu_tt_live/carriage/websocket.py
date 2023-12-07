
from .base import AbstractProducerCarriage, AbstractConsumerCarriage
import logging
import six


log = logging.getLogger(__name__)


class WebsocketProducerCarriage(AbstractProducerCarriage):

    _backend_producer = None
    _expects = six.text_type

    def register_backend_producer(self, producer):
        self._backend_producer = producer

    def resume_producing(self):
        # None, since this is a producer module. It will produce a new document.
        self.producer_node.resume_producing()

    def emit_data(self, data, sequence_identifier='default', delay=None, **kwargs):
        if self._backend_producer:
            self._backend_producer.emit_data(sequence_identifier, data.encode(), delay=delay)


class WebsocketConsumerCarriage(AbstractConsumerCarriage):

    _provides = six.text_type

    def on_new_data(self, data, **kwargs):
        self.consumer_node.process_document(data, **kwargs)
