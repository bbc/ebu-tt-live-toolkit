from collections import namedtuple
from ebu_tt_live.documents import EBUTTDDocument


"Tuple to represent a Glyph"
glyph = namedtuple('glyph', [
    'color',
    'fontFamily',
    'fontSize',
    'fontStyle',
    'fontWeight',
    'textDecoration',
    # 'textOutline',  # textOutline is not permitted in EBU-TT-D
    # 'textShadow',   # textShadow is not permitted in EBU-TT_D
])


class imscHrmValidator:
    """Class for validating an EBU-TT-D document against the IMSC-HRM.

    IMSC-HRM is specified at https://www.w3.org/TR/imsc-hrm/ .
    """

    # IMSC HRM constants
    _ipd = 1
    _BDraw = 1/12

    # Things we need
    _GlyphCache = set([])  # Array of glyphs

    def getISDs(self, doc: EBUTTDDocument) -> list:
        """Get the set of ISD times."""
        return doc.timeline

    def isEmptyISD(self, isd) -> bool:
        """Determine if the ISD is empty or renders some text."""
        pass

    def drawingArea(self, isd) -> float:
        """Calculate the drawing area of the active regions in the ISD."""
        pass

    def textDuration(self, isd) -> float:
        """Compute the painting duration for the text in the ISD."""
        pass

    def paintingDuration(self, isd) -> float:
        """Compute the total painting duration for the ISD."""
        return self.drawingArea(isd)/self._BDraw + self.textDuration(isd)

    def validate(self, doc: EBUTTDDocument) -> bool:
        """Validate the EBU-TT-D document against the IMSC-HRM."""
        return False
        pass


