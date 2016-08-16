import logging
from argparse import ArgumentParser
from .common import create_loggers

from ebu_tt_live.node.distributing import DistributingNode
from ebu_tt_live.clocks.local import LocalMachineClock
from ebu_tt_live.twisted import TwistedConsumer, UserInputServerProtocol, UserInputServerFactory, BroadcastServerFactory, TwistedPullProducer, StreamingServerProtocol
from ebu_tt_live.carriage.forwarder_carriage import ForwarderCarriage
from ebu_tt_live.carriage.twisted import TwistedConsumerImpl, TwistedProducerImpl
from twisted.internet import reactor


log = logging.getLogger('ebu_simple_consumer')


parser = ArgumentParser()

parser.add_argument('-c', '--config', dest='config', metavar='CONFIG')


def main():
    # args = parser.parse_args()
    create_loggers()
    log.info('This is a Simple Consumer example')

    sub_consumer_impl = TwistedConsumerImpl()
    sub_prod_impl = TwistedProducerImpl()
    carriage_impl = ForwarderCarriage(sub_consumer_impl, sub_prod_impl)

    reference_clock = LocalMachineClock()
    reference_clock.clock_mode = 'local'

    dist_node = DistributingNode(
        node_id='simple-consumer',
        carriage_impl=carriage_impl,
        reference_clock=reference_clock
    )

    # This factory listens for incoming documents from the user input producer.
    user_input_server_factory = UserInputServerFactory(
        url='ws://127.0.0.1:9001',
        consumer=TwistedConsumer(
            custom_consumer=sub_consumer_impl
        )
    )
    user_input_server_factory.protocol = UserInputServerProtocol
    user_input_server_factory.listen()

    # This factory listens for any consumer to forward documents to.
    broadcast_factory = BroadcastServerFactory("ws://127.0.0.1:9000")
    broadcast_factory.protocol = StreamingServerProtocol
    broadcast_factory.listen()

    TwistedPullProducer(
        consumer=broadcast_factory,
        custom_producer=sub_prod_impl
    )

    reactor.run()
