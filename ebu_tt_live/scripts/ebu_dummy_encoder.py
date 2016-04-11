import logging
from common import create_loggers
from ebu_tt_live import bindings
from pyxb import BIND

log = logging.getLogger('ebu_dummy_encoder')


def main():
    create_loggers()
    log.info('Dummy XML Encoder')

    tt = bindings.tt(
        sequenceIdentifier='testSequence001',
        sequenceNumber='1',
        timeBase='smpte',
        lang='en-GB',
        head=bindings.Head(
            bindings.Metadata(),
            bindings.Styling(
                bindings.Style(
                    id='ID001'
                )
            ),
            bindings.Layout()
        ),
        body=BIND(
            bindings.Div(
                bindings.P(
                    bindings.Span(
                        'Some example text...'
                    ),
                    bindings.Br(),
                    bindings.Span(
                        'And another line'
                    ),
                    id='ID005',
                    begin='00:00:00:50',
                    end='00:00:03:24',
                )
            )
        )
    )

    print(
        tt.toDOM().toprettyxml(
            indent='  '
        )
    )
    log.info('XML output printed')
