import logging
from common import create_loggers
from ebu_tt_live import bindings
from pyxb import BIND

log = logging.getLogger('ebu_dummy_encoder')


def main():
    create_loggers()
    log.info('Dummy XML Encoder')

    region = bindings.Region(
        id='ID003',
        origin='0px 0px',
        extent='1px 1px'
    )

    tt = bindings.tt(
        timeBase='smpte',
        lang='en-GB',
        head=bindings.Head(
            bindings.Metadata(),
            bindings.Styling(
                bindings.Style(
                    id='ID001'
                )
            ),
            bindings.Layout(
                region
            )
        ),
        body=BIND(
            bindings.Div(
                bindings.P(
                    id='ID005',
                    begin='00:00:00:00',
                    end='00:00:00:00'
                )
            )
        )
    )

    print(
        tt.toDOM().toprettyxml(
            indent='  '
        )
    )
