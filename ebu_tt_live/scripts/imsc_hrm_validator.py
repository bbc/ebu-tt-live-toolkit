from collections import namedtuple
from datetime import timedelta
from ebu_tt_live.documents import EBUTTDDocument
from ebu_tt_live.bindings import d_p_type, d_span_type
from pyxb.binding.basis import NonElementContent, ElementContent
import logging


log = logging.getLogger('imsc_hrm_validator')
log.setLevel(logging.DEBUG)

glyphStyles = [
    'color',
    'fontFamily',
    'fontSize',
    'fontStyle',
    'fontWeight',
    'textDecoration',
    # 'textOutline',  # textOutline is not permitted in EBU-TT-D
    # 'textShadow',   # textShadow is not permitted in EBU-TT_D
]

"Tuple to represent a Glyph"
glyph_tuple_fieldnames = glyphStyles
glyph_tuple_fieldnames.append('characterCode')
glyph = namedtuple('glyph', glyph_tuple_fieldnames)


class imscHrmValidator:
    """Class for validating an EBU-TT-D document against the IMSC-HRM.

    IMSC-HRM is specified at https://www.w3.org/TR/imsc-hrm/ .
    """

    # IMSC HRM constants
    _ipd = 1
    _BDraw = 1/12

    # Things we need
    _glyphCache = set([])  # Array of glyphs
    _doc = None

    def _getIsdTimes(self) -> list:
        """Get the set of ISD times."""
        return self._doc.timeline

    def _getIsd(self, isd_begin_time, isd_end_time):
        """Get the elements in the ISD for a particular time"""
        return self._doc.lookup_range_on_timeline(isd_begin_time.when, isd_end_time.when if isd_end_time is not None else None)

    def _isEmptyISD(self, isd) -> bool:
        """Determine if the ISD is empty or renders some text."""
        empty = True
        for e in isd:
            print(e)
            for c in e.orderedContent():
                v = c.value
                if isinstance(c, NonElementContent):
                    empty = (len(v) == 0)
                elif isinstance(v, d_span_type):
                    for sc in v.orderedContent():
                        if isinstance(sc, NonElementContent):
                            empty = (len(sc.value) == 0)
                        if not empty:
                            break
            # breakpoint()

            if not empty:
                break

        # breakpoint()
        return empty

    def _drawingArea(self, isd) -> float:
        """Calculate the drawing area of the active regions in the ISD."""
        return 1

    def _textDuration(self, isd) -> float:
        """Compute the painting duration for the text in the ISD."""
        return 1

    def _paintingDuration(self, isd) -> float:
        """Compute the total painting duration for the ISD."""
        return self._drawingArea(isd)/self._BDraw + self._textDuration(isd)

    def validate(self, doc: EBUTTDDocument) -> bool:
        """Validate the EBU-TT-D document against the IMSC-HRM."""

        # reset
        self._glyphCache = set([])
        self._doc = doc

        last_nonzero_presentation_time = timedelta(seconds=0 - self._ipd)

        rv = True

        timeline = self._getIsdTimes();
        log.debug('timeline: {}'.format(timeline))

        timeline_entries = len(timeline)

        for timeline_idx in range(0, timeline_entries):
            isd = self._getIsd(
                timeline[timeline_idx],
                timeline[timeline_idx + 1] if (timeline_idx + 1) < timeline_entries else None)

            if self._isEmptyISD(isd):
                log.debug('ISD beginning at {} is empty'.format(timeline[timeline_idx]))
                continue
            else:
                log.debug('ISD beginning at {} is not empty'.format(timeline[timeline_idx]))

            # Work out how long we have to draw this
            available_draw_time = \
                (timeline[timeline_idx].when - last_nonzero_presentation_time).total_seconds()
            if available_draw_time > self._ipd:
                available_draw_time = self._ipd

            # remember for next time round the loop
            last_nonzero_presentation_time = timeline[timeline_idx].when

            painting_dur = self._paintingDuration(isd)
            log.debug(
                'ISD beginning at {} has painting duration {} and available time {}'.format(
                    timeline[timeline_idx],
                    painting_dur,
                    available_draw_time
                ))
            if painting_dur > available_draw_time:
                rv = False
                log.error('ISD at {} fails validation'.format(timeline[timeline_idx]))

        return rv



