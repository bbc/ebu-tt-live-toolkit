from collections import namedtuple
from datetime import timedelta
from ebu_tt_live.documents import EBUTTDDocument
from ebu_tt_live.bindings import d_p_type, d_span_type
from ebu_tt_live.bindings._ebuttdt import CellFontSizeType, PercentageOriginType, PercentageExtentType, rgbHexColorType, rgbaHexColorType, namedColorType, named_color_to_rgba
from pyxb.binding.basis import NonElementContent, ElementContent
import ebu_tt_live.uax24 as uax24
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
glyph_tuple_fieldnames = glyphStyles[:]  # copy not reference
glyph_tuple_fieldnames.append('characterCode')
glyph = namedtuple('glyph', glyph_tuple_fieldnames)

GCpy12_chars = set(
    uax24.Latin_list + 
    uax24.Greek_list + 
    uax24.Cyrillic_list +
    uax24.Hebrew_list +
    uax24.Common_list)

Ren0_6_chars = set(
    uax24.Han_list +
    uax24.Katakana_list +
    uax24.Hiragana_list +
    uax24.Bopomofo_list +
    uax24.Hangul_list
)

class imscHrmValidator:
    """Class for validating an EBU-TT-D document against the IMSC-HRM.

    IMSC-HRM is specified at https://www.w3.org/TR/imsc-hrm/ .
    """

    # IMSC HRM constants
    _ipd = 1
    _BDraw = 12

    # Things we need
    _glyphCache = set()  # Array of glyphs
    _doc = None
    _p_to_parent_div_with_background_color = {}
    _cell_height = float(1/15)

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

            if not empty:
                break

        return empty

    def _hasBackgroundColor(self, element) -> bool:
        rv = False

        backgroundColor = element.computed_style.backgroundColor
        if backgroundColor is not None:
            if isinstance(backgroundColor, namedColorType):
                backgroundColor = rgbaHexColorType(named_color_to_rgba(backgroundColor))
            if isinstance(backgroundColor, rgbaHexColorType) and len(backgroundColor) == 9:
                opacity = backgroundColor[-2:]
                rv = (opacity != '00')
            elif isinstance(backgroundColor, rgbHexColorType):
                rv = True

        print('backgroundColor {} has opacity {}'.format(backgroundColor, rv))
        return rv

    def _preprocess_divs(self):
        """For all divs with an opaque backgroundColor, record their p children
        
        This is so we can count divs in NGP: the timeline only gives us p elements."""

        self._p_to_parent_div_with_background_color.clear()
        for div in self._doc.binding.body.div:
            if (self._hasBackgroundColor(div)):
                for p in div.p:
                    # div elements might not have an id, so we need to map to the object
                    self._p_to_parent_div_with_background_color[p.id] = div

    def _drawingAreaS(self, isd) -> float:
        """Calculate the drawing area of the active regions in the ISD.

        We need to sum the product of region area and total number of elements
        in the tree rooted at each region including body, div, p and span that
        have a tts:backgroundColor whose opacity is not zero.

        A feature of EBU-TT-D is that divs cannot contain divs and spans cannot
        contain spans, so we can check the body's style once, for each region,
        and need to traverse up to the div parent of each p to count the unique
        divs too. We can ignore character content children because by definition
        they cannot set the backgroundColor attribute,
        whose default has opacity 0."""

        region_set = set()
        region_to_element_count = {}
        region_to_div_map = {}  # will map all the divs selected into each region
        body_has_background_color = 0
        body = self._doc.binding.body
        if self._hasBackgroundColor(body):
            body_has_background_color = 1
            print('body has background color')
        for e in isd:
            if isinstance(e, d_p_type):
                print('processing p id {}'.format(e.id))
                region = e._validated_region
                if region is None:
                    region = e._inherited_region
                region_set.add(region)
                if region.id not in region_to_element_count:
                    print('adding new region id {}'.format(region.id))
                    region_to_element_count[region.id] = body_has_background_color
                    region_to_div_map[region.id] = set()
                    if self._hasBackgroundColor(region):
                        region_to_element_count[region.id] += 1
                        print('region has a background color')
                if self._hasBackgroundColor(e):
                    region_to_element_count[region.id] += 1
                    print('p has a background color')
                # Make sure we count the div for this region if it has a backgroundColor
                if e.id in self._p_to_parent_div_with_background_color:
                    print('this p is in a div with a background color')
                    region_to_div_map[region.id].add(self._p_to_parent_div_with_background_color[e.id])
                print('processing {} span children of p id {}'.format(len(e.span), e.id))
                for span_child in e.span:
                    if self._hasBackgroundColor(span_child):
                        print('span has background color')
                        region_to_element_count[region.id] += 1
                    else:
                        print('span with no background color')

        for rid in region_to_element_count.keys():
            region_to_element_count[rid] += len(region_to_div_map[rid])
        print(region_to_element_count)

        PAINT = 0.0
        for region in region_set:
            origin = PercentageOriginType(region.origin)
            extent = PercentageExtentType(region.extent)

            NSIZE = extent.horizontal/100 * extent.vertical/100
            PAINT += NSIZE * region_to_element_count[region.id]
            log.debug('Region {} has NSIZE = {} and NBG = {}'.format(
                region.id,
                NSIZE,
                region_to_element_count[region.id]
            ))

        S = 1 + PAINT  # CLEAR = 1
        log.debug('S = {}, PAINT = {}'.format(S, PAINT))

        return S

    def _getGlyphStyles(self, e) -> dict:
        """ Get the set of glyph styles from the provided element."""

        rv = dict.fromkeys(glyphStyles)
        cs = e.computed_style
        for style_attr in glyphStyles:
            rv[style_attr] = getattr(cs, style_attr)
        return rv

    def _calc_NRGA(self, fontSize) -> float:
        if isinstance(fontSize, CellFontSizeType):
            return (fontSize.vertical * self._cell_height)**2
        else:
            log.error('unexpected fontSize {} of type {}'.format(
                fontSize,
                type(fontSize).__name__))
            breakpoint()

        return 100  # silly big number

    def _GCpy(self, char) -> float:
        log.debug('char {} is {}in GCpy12_chars'.format(
            char,
            '' if char in GCpy12_chars else 'not '
        ))
        return 12 if char in GCpy12_chars else 3

    def _Ren(self, char) -> float:
        log.debug('char {} is {}in Ren0_6_chars'.format(
            char,
            '' if char in Ren0_6_chars else 'not '
        ))
        return 0.6 if char in Ren0_6_chars else 1.2

    def _checkGlyphCacheSize(self) -> bool:
        """Compute sum of NRGA over all glyphs and check it is not largher than NGBS"""
        NGBS = 1
        NRGA_SUM = 0
        for g in self._glyphCache:
            NRGA_SUM += self._calc_NRGA(g.fontSize)

        log.debug('Glyph cache size check: NRGA_SUM = {}'.format(NRGA_SUM))

        return (NRGA_SUM <= NGBS)

    def _textDuration(self, isd) -> float:
        """Compute the painting duration for the text in the ISD.
        
        We will assume that the glyph cache is in a good state to start."""
        this_text = ''
        this_style = dict.fromkeys(glyphStyles)
        DURT = 0

        next_glyph_cache = set()

        # breakpoint()
        for p in isd:
            # should be a p
            if isinstance(p, d_p_type):
                for poci in p.orderedContent():
                    if isinstance(poci, NonElementContent):
                        print('processing character content child of p')
                        this_text = poci.value
                        this_style = self._getGlyphStyles(p)
                    elif isinstance(poci.value, d_span_type):
                        print('processing a span')
                        this_style = self._getGlyphStyles(poci.value)
                        this_text = ''
                        for soci in poci.value.orderedContent():
                            if isinstance(soci, NonElementContent):
                                this_text += soci.value

                    print('this_text: {}'.format(this_text))
                    print('this_style: {} '.format(this_style))
                    this_NRGA = self._calc_NRGA(this_style['fontSize'])
                    print('this_NRGA = {}'.format(this_NRGA))
                    # iterate through text and style processing glyphs
                    for char in this_text:
                        charCode = ord(char)
                        # there must be a better way to make our glyph tuple
                        # than the next 3 lines, but I haven't found it.
                        tsc = this_style.copy()
                        tsc.update({'characterCode': charCode})
                        this_glyph = glyph(**tsc)
                        if this_glyph in self._glyphCache:
                            print('glyph for {} ({}) is in the glyph cache'.format(char, charCode))
                            DURT += this_NRGA / self._GCpy(charCode)
                            next_glyph_cache.add(this_glyph)
                        elif this_glyph in next_glyph_cache:
                            print('glyph for {} ({}) already rendered in this ISD'.format(char, charCode))
                            DURT += this_NRGA / self._GCpy(charCode)
                        else:
                            print('rendering glyph for {} ({})'.format(char, charCode))
                            DURT += this_NRGA / self._Ren(charCode)
                            next_glyph_cache.add(this_glyph)
            else:  # not a p
                log.warning('Found non p element type {}'.format(type(p).__name__))

        self._glyphCache = next_glyph_cache

        log.debug('Returning DURT = {}'.format(DURT))
        return DURT

    def _paintingDuration(self, isd) -> float:
        """Compute the total painting duration for the ISD."""
        return self._drawingAreaS(isd)/self._BDraw + self._textDuration(isd)

    def validate(self, doc: EBUTTDDocument) -> bool:
        """Validate the EBU-TT-D document against the IMSC-HRM."""

        # reset
        self._glyphCache = set()
        self._doc = doc
        self._preprocess_divs()
        if doc.binding.cellResolution is not None:
            self._cell_height = 1/doc.binding.cellResolution.vertical
        else:
            self._cell_height = 1/15
        log.debug('Cell height = {}'.format(self._cell_height))

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

            if not self._checkGlyphCacheSize():
                rv = False
                log.error('Glyph cache total NRGA is larger than NGBS')

        if rv:
            log.info('Document is valid')
        else:
            log.error('Document is not valid')

        return rv



