from unittest import TestCase, skip
from ebu_tt_live.scripts.imsc_hrm_validator import imscHrmValidator, glyph
from ebu_tt_live.bindings._ebuttdt import CellFontSizeType, rgbHexColorType, cellFontSizeType, fontWeightType
from ebu_tt_live.documents import EBUTTDDocument
import os
from datetime import timedelta

class TestImscHRMValidator(TestCase):

    _ihv = imscHrmValidator()
    _doc = None

    def setUp(self) -> None:
        xml = ""
        file_path = os.path.join(os.path.dirname(__file__), 'data', 'document_ebuttd.xml')
        with open(file_path) as xml_file:
            xml = xml_file.read()
        self._doc = EBUTTDDocument.create_from_xml(xml)
        self._doc.validate()
        self._ihv._setup(self._doc)
        return super().setUp()
    
    def tearDown(self) -> None:
        self._ihv = None
        self._doc = None
        return super().tearDown()

    def testGetIsdTimes(self):
        """Note that when there's a region with a background color
        that has showBackground=always, the results are different.
        There's a separate test for that in a different test class
        later in this file."""
        expected_times = [
            2.5,
            3,
            4,
            5,
            6,
            7,
            8,
        ]
        expected = [timedelta(seconds=t) for t in expected_times]
        self.assertSequenceEqual(expected, self._ihv._getIsdTimes())

    def testIsEmptyISD(self):
        """Note that when there's a region with a background color
        that has showBackground=always, the results are different.
        There's a separate test for that in a different test class
        later in this file."""
        empty_isds = [
            (timedelta(seconds=2.5), timedelta(seconds=3)),
            (timedelta(seconds=6), timedelta(seconds=7)),
        ]
        non_empty_isds = [
            (timedelta(seconds=3), timedelta(seconds=4)),
            (timedelta(seconds=4), timedelta(seconds=5)),
            (timedelta(seconds=5), timedelta(seconds=6)),
            (timedelta(seconds=7), timedelta(seconds=8)),
        ]
        for (isd_begin_time, isd_end_time) in empty_isds:
            isd = self._ihv._getIsd(
                isd_begin_time=isd_begin_time,
                isd_end_time=isd_end_time)
            with self.subTest(isd = isd):
                self.assertTrue(self._ihv._isEmptyISD(isd))
        for (isd_begin_time, isd_end_time) in non_empty_isds:
            isd = self._ihv._getIsd(
                isd_begin_time=isd_begin_time,
                isd_end_time=isd_end_time)
            with self.subTest(isd = isd):
                self.assertFalse(self._ihv._isEmptyISD(isd))

    def testHasBackgroundColor(self):
        ttd_doc = self._doc.binding
        elems_with_background_color = [
            ttd_doc.body.div[2],
            ttd_doc.head.layout.region[0],
            ttd_doc.body.div[0].p[1].span[0],
        ]
        elems_without_background_color = [
            ttd_doc.body.div[0].p[0],
            ttd_doc.body.div[0].p[1],
            ttd_doc.body.div[1],
            ttd_doc.body.div[1].p[0]
        ]
        for elem in elems_with_background_color:
            with self.subTest(elem=elem):
                self.assertTrue(self._ihv._hasBackgroundColor(elem))
        for elem in elems_without_background_color:
            with self.subTest(elem=elem):
                self.assertFalse(self._ihv._hasBackgroundColor(elem))

    def testPreprocessDivs(self):
        # Call to _preprocess_divs was already made in setup(),
        # we just need to check the outcome was as expected.
        expected_p_ids = [
            'p4'
        ]
        self.assertListEqual(
            list(self._ihv._p_to_parent_div_with_background_color.keys()),
            expected_p_ids)
        self.assertEqual(
            self._doc.binding.body.div[2],
            self._ihv._p_to_parent_div_with_background_color['p4']
        )

    def testPreprocessRegions(self):
        """Note that when there's a region with a background color
        that has showBackground=always, the results are different.
        There's a separate test for that in a different test class
        later in this file."""

        # Call to _preprocess_regions was already made in setup(),
        # we just need to check the outcome was as expected.
        self.assertEqual(len(self._ihv._region_ids_with_always_background), 0)

    def testDrawingAreaS(self):
        """Note that when there's a region with a background color
        that has showBackground=always, the results are different.
        There's a separate test for that in a different test class
        later in this file."""
        expected_S_for_each_ISD = [
            1,  # 2.5s
            3,  # 3s
            2,  # 4s
            2,  # 5s
            1,  # 6s
            3,  # 7s
            1,  # 8s
        ]
        isd_times = self._ihv._getIsdTimes()
        isd_times.append(None)
        for i in range(0, len(expected_S_for_each_ISD)):
            expected_S = expected_S_for_each_ISD[i]
            isd = self._ihv._getIsd(
                isd_times[i],
                isd_times[i+1])
            with self.subTest(expected_S=expected_S, isd=isd, isd_time=isd_times[i]):
                if expected_S == 1:
                    self.assertTrue(self._ihv._isEmptyISD(isd))
                else:
                    self.assertEqual(expected_S, self._ihv._drawingAreaS(isd))

    def testGetGlyphStyles_all(self):
        expected = {
            'color': rgbHexColorType('#00ff00'),
            'fontFamily': 'george',
            'fontSize': CellFontSizeType(2),
            'fontStyle': 'italic',
            'fontWeight': 'bold',
            'textDecoration': 'underline'
        }
        self.assertEqual(
            expected,
            self._ihv._getGlyphStyles(self._doc.binding.body.div[0].p[2].span[0]))

    def testGetGlyphStyles_none(self):
        expected = {
            'color': None,
            'fontFamily': 'default',
            'fontSize': CellFontSizeType(1),
            'fontStyle': 'normal',
            'fontWeight': 'normal',
            'textDecoration': 'none'
        }
        self.assertEqual(
            expected,
            self._ihv._getGlyphStyles(self._doc.binding.body.div[0].p[0]))

    def testCalcNRGA(self):
        self.assertAlmostEqual(
            self._ihv._calc_NRGA(CellFontSizeType('2c')),
            0.01777777778)

    def testGCpy(self):
        gcpy12charcodes = [
            0x45,     # Latin
            0x370,    # Greek
            0x1E08F,  # Cyrillic
            0x05c6,   # Hebrew
            0x37e,    # Common
        ]
        gcpy3charcodes = [
            0x20789,  # Han
            0x30ff,   # Katakana
            0x3041,   # Hiragana
            0x31bf,   # Bopomofo
            0xd7fb,   # Hangul
        ]
        for charcode in gcpy12charcodes:
            with self.subTest(charcode=charcode):
                self.assertEqual(self._ihv._GCpy(charcode), 12)
        for charcode in gcpy3charcodes:
            with self.subTest(charcode=charcode):
                self.assertEqual(self._ihv._GCpy(charcode), 3)

    def testRen(self):
        ren06charcodes = [
            0x20789,  # Han
            0x30ff,   # Katakana
            0x3041,   # Hiragana
            0x31bf,   # Bopomofo
            0xd7fb,   # Hangul
        ]
        ren12charcodes = [
            0x45,     # Latin
            0x05c6,   # Hebrew
        ]
        for charcode in ren06charcodes:
            with self.subTest(charcode=charcode):
                self.assertEqual(self._ihv._Ren(charcode), 0.6)
        for charcode in ren12charcodes:
            with self.subTest(charcode=charcode):
                self.assertEqual(self._ihv._Ren(charcode), 1.2)

    def testCheckGlyphCacheSize(self):
        ok_glyph_cache = set([
            glyph(
                color=rgbHexColorType('#ffffff'),
                fontFamily='default',
                fontSize=CellFontSizeType('4.99c'),  # almost 1/3 of height
                fontStyle='normal',
                fontWeight=fontWeightType('normal'),
                textDecoration='none',
                characterCode=cc
            ) for cc in range(ord('a'), ord('j'))  # 9 chars
        ])
        self._ihv._glyphCache = ok_glyph_cache
        self.assertTrue(self._ihv._checkGlyphCacheSize())

        # take it over the edge
        self._ihv._glyphCache.add(
            glyph(
                color=rgbHexColorType('#ffffff'),
                fontFamily='default',
                fontSize=CellFontSizeType('5c'),  # 1/3 of height
                fontStyle='normal',
                fontWeight=fontWeightType('normal'),
                textDecoration='none',
                characterCode=ord('j')
            )
        )
        self.assertFalse(self._ihv._checkGlyphCacheSize())

    @skip
    def testTextDuration(self):
        # Don't test this here - the feature tests check a variety of cases
        # that do a good enough job.
        pass

    @skip
    def testPaintingDuration(self):
        # Don't test this here - the feature tests check a variety of cases
        # that do a good enough job.
        pass


class TestImscHRMValidatorWhenRegionsAlwaysHaveBackgrounds(TestCase):
    """Some test results need to be different when there is a region
    that has a background colour that is not transparent, and has
    the default value for showBackground, which is 'always'.
    
    This test class tests just those things that should be different,
    using a modified version of the test document."""
    _ihv = imscHrmValidator()
    _doc = None

    def setUp(self) -> None:
        xml = ""
        file_path = os.path.join(os.path.dirname(__file__), 'data', 'document_ebuttd_with_region_backgrounds.xml')
        with open(file_path) as xml_file:
            xml = xml_file.read()
        self._doc = EBUTTDDocument.create_from_xml(xml)
        self._doc.validate()
        self._ihv._setup(self._doc)
        return super().setUp()
    
    def tearDown(self) -> None:
        self._ihv = None
        self._doc = None
        return super().tearDown()

    def testGetIsdTimes(self):
        expected_times = [
            0,
            2.5,
            3,
            4,
            5,
            6,
            7,
            8,
        ]
        expected = [timedelta(seconds=t) for t in expected_times]
        self.assertSequenceEqual(expected, self._ihv._getIsdTimes())

    def testIsEmptyISD(self):
        empty_isds = [
        ]
        non_empty_isds = [
            (timedelta(seconds=0), timedelta(seconds=2.5)),
            (timedelta(seconds=2.5), timedelta(seconds=3)),
            (timedelta(seconds=3), timedelta(seconds=4)),
            (timedelta(seconds=4), timedelta(seconds=5)),
            (timedelta(seconds=5), timedelta(seconds=6)),
            (timedelta(seconds=6), timedelta(seconds=7)),
            (timedelta(seconds=7), timedelta(seconds=8)),
        ]
        for (isd_begin_time, isd_end_time) in empty_isds:
            isd = self._ihv._getIsd(
                isd_begin_time=isd_begin_time,
                isd_end_time=isd_end_time)
            with self.subTest(isd = isd):
                self.assertTrue(self._ihv._isEmptyISD(isd))
        for (isd_begin_time, isd_end_time) in non_empty_isds:
            isd = self._ihv._getIsd(
                isd_begin_time=isd_begin_time,
                isd_end_time=isd_end_time)
            with self.subTest(isd = isd):
                self.assertFalse(self._ihv._isEmptyISD(isd))

    def testPreprocessRegions(self):
        # Call to _preprocess_regions was already made in setup(),
        # we just need to check the outcome was as expected.
        expected = set(['r1'])
        self.assertEqual(expected, self._ihv._region_ids_with_always_background)

    def testDrawingAreaS(self):
        expected_S_for_each_ISD = [
            2,  # 0s
            2,  # 2.5s
            3,  # 3s
            2,  # 4s
            2,  # 5s
            2,  # 6s
            3,  # 7s
            2,  # 8s
        ]
        isd_times = self._ihv._getIsdTimes()
        isd_times.append(None)
        for i in range(0, len(expected_S_for_each_ISD)):
            expected_S = expected_S_for_each_ISD[i]
            isd = self._ihv._getIsd(
                isd_times[i],
                isd_times[i+1])
            with self.subTest(expected_S=expected_S, isd=isd, isd_time=isd_times[i]):
                if expected_S == 1:
                    self.assertTrue(self._ihv._isEmptyISD(isd))
                else:
                    self.assertEqual(expected_S, self._ihv._drawingAreaS(isd))
