from unittest import TestCase
from ebu_tt_live.documents.ebutt3 import EBUTT3Document
from ebu_tt_live.node.denester import DenesterNode, ELEMENT_TIMES_KEY, \
    ElementTimes
from ebu_tt_live.bindings import style_type
from ebu_tt_live.bindings._ebuttdt import FullClockTimingType


class TestDenesterNode(TestCase):
    # Given a div within a div, only a single div is returned

    def setUp(self):
        xml_file = "testing/bdd/templates/nested_elements_hardcoded.xml"
        with open(xml_file, 'r') as in_file:
            input_xml = in_file.read()
        self.actual_doc = EBUTT3Document.create_from_xml(input_xml)

        xml_file_2 = "testing/bdd/templates/unnested_elements_hardcoded.xml"
        with open(xml_file_2, 'r') as in_file:
            expected_xml = in_file.read()
        self.expected_doc = EBUTT3Document.create_from_xml(expected_xml)

        xml_file_3 = "testing/bdd/templates/many_nested_elements_hardcoded.xml"
        with open(xml_file_3, 'r') as in_file:
            input_xml_2 = in_file.read()
        self.actual_doc_2 = EBUTT3Document.create_from_xml(input_xml_2)

        xml_file_4 = \
            "testing/bdd/templates/many_unnested_elements_hardcoded.xml"
        with open(xml_file_4, 'r') as in_file:
            expected_xml_2 = in_file.read()
        self.expected_doc_2 = EBUTT3Document.create_from_xml(expected_xml_2)

        xml_file_5 = \
            "testing/bdd/templates/regions_nested_elements_hardcoded.xml"
        with open(xml_file_5, 'r') as in_file:
            input_xml_3 = in_file.read()
        self.actual_doc_3 = EBUTT3Document.create_from_xml(input_xml_3)

        xml_file_6 = \
            "testing/bdd/templates/regions_unnested_elements_hardcoded.xml"
        with open(xml_file_6, 'r') as in_file:
            expected_xml_3 = in_file.read()
        self.expected_doc_3 = EBUTT3Document.create_from_xml(expected_xml_3)

        xml_file_7 = "testing/bdd/templates/nested_spans_hardcoded.xml"
        with open(xml_file_7, 'r') as in_file:
            input_xml_4 = in_file.read()
        self.actual_doc_4 = EBUTT3Document.create_from_xml(input_xml_4)

        xml_file_8 = "testing/bdd/templates/unnested_spans_hardcoded.xml"
        with open(xml_file_8, 'r') as in_file:
            expected_xml_4 = in_file.read()
        self.expected_doc_4 = EBUTT3Document.create_from_xml(expected_xml_4)

    def test_merged_attr_styles_(self):
        excepted_div_attr = {
            "styles": ["S1", "S2"],
        }
        parent_attr = {
            "styles": ["S2"],
            "lang": None,
            "region": None,
            "begin": None,
            "end": None,
            "metadata": None
        }
        actual_div = self.actual_doc_2.binding.body.div[0].div[0]
        actual_divs_attr = \
            DenesterNode.merge_attr(
                parent_attr,
                DenesterNode.div_attr(actual_div))
        assert excepted_div_attr["styles"] == actual_divs_attr["styles"]

    def test_recurse_many_child(self):
        expected_divs = self.expected_doc_2.binding.body.div
        nested_divs = self.actual_doc_2.binding.body.div
        dataset = {}
        dataset["document"] = self.actual_doc_2.binding
        dataset[ELEMENT_TIMES_KEY] = [
            ElementTimes(
                begin=self.actual_doc_2.binding.body.begin,
                end=self.actual_doc_2.binding.body.end
            )
        ]
        unnested_divs = []
        for nested_div in nested_divs:
            unnested_divs.extend(
                (DenesterNode.combine_divs(
                    DenesterNode.recurse(nested_div, dataset))))
        assert len(unnested_divs) == len(expected_divs)

    def test_merged_attr_lang_only_on_child(self):
        expected_div_attr = {
            "styles": ["S1", "S2"],
            "lang": "fr"
        }
        parent_attr = {
            "styles": ["S2"],
            "lang": None,
            "region": None,
            "begin": None,
            "end": None,
            "metadata": None
        }
        actual_div = self.actual_doc_2.binding.body.div[0].div[0]
        actual_divs_attr = \
            DenesterNode.merge_attr(
                parent_attr,
                DenesterNode.div_attr(actual_div))
        assert expected_div_attr["lang"] == actual_divs_attr["lang"]

    def test_merged_attr_lang_only_on_parent(self):
        expected_div_attr = {
            "styles": ["S1", "S2"],
            "lang": "fr"
        }
        parent_attr = {
            "styles": ["S2"],
            "lang": "fr",
            "region": None,
            "begin":  None,
            "end": None,
            "metadata": None
        }
        actual_div = self.actual_doc.binding.body.div[0].div[0]
        actual_divs_attr = \
            DenesterNode.merge_attr(
                parent_attr,
                DenesterNode.div_attr(actual_div))
        assert expected_div_attr["lang"] == actual_divs_attr["lang"]

    def test_merged_attr_lang_only_on_both_child_and_parent(self):
        expected_div_attr = {
            "styles": ["S1", "S2"],
            "lang": "en-GB"
        }
        parent_attr = {
            "styles": ["S2"],
            "lang": "fr",
            "region": None,
            "begin": None,
            "end": None,
            "metadata": None
        }
        actual_div = self.actual_doc.binding.body.div[0].div[1]
        actual_divs_attr = \
            DenesterNode.merge_attr(
                parent_attr,
                DenesterNode.div_attr(actual_div))
        assert expected_div_attr["lang"] == actual_divs_attr["lang"]

    def test_merged_attr_begin_end_times_on_child_and_parent(self):
        expected_div_attr = {
            "styles": ["S1", "S2"],
            "region": None,
            "lang": "fr",
            "begin": FullClockTimingType("00:00:11"),
            "end": FullClockTimingType("00:00:15"),
            "metadata": None
        }
        parent_attr = {
            "styles": ["S2"],
            "lang": "fr",
            "region": None,
            "begin": FullClockTimingType("00:00:10"),
            "end": FullClockTimingType("00:00:20"),
            "metadata": None
        }
        actual_div = self.actual_doc.binding.body.div[0].div[0]
        actual_divs_attr = \
            DenesterNode.merge_attr(
                parent_attr,
                DenesterNode.div_attr(actual_div))
        actual_begin_time = actual_divs_attr["begin"]
        expected_begin_time = expected_div_attr["begin"].timedelta
        assert expected_begin_time == actual_begin_time
        actual_end_time = actual_divs_attr["end"]
        expected_end_time = expected_div_attr["end"].timedelta
        assert expected_begin_time == actual_begin_time
        assert expected_end_time == actual_end_time

    def test_merged_attr_begin_end_times_on_child_no_end_on_parent(self):
        expected_div_attr = {
            "styles": ["S1", "S2"],
            "region": None,
            "lang": "fr",
            "begin": FullClockTimingType("00:00:11"),
            "end": FullClockTimingType("00:00:15"),
            "metadata": None
        }
        parent_attr = {
            "styles": ["S2"],
            "lang": "fr",
            "region": None,
            "begin": FullClockTimingType("00:00:10"),
            "end": None,
            "metadata": None
        }
        actual_div = self.actual_doc.binding.body.div[0].div[0]
        actual_divs_attr = \
            DenesterNode.merge_attr(
                parent_attr,
                DenesterNode.div_attr(actual_div))
        actual_begin_time = actual_divs_attr["begin"]
        expected_begin_time = expected_div_attr["begin"].timedelta
        assert expected_begin_time == actual_begin_time
        actual_end_time = actual_divs_attr["end"]
        expected_end_time = expected_div_attr["end"].timedelta
        assert expected_begin_time == actual_begin_time
        assert expected_end_time == actual_end_time

    def test_merged_attr_different_region(self):
        expected_divs = self.expected_doc_3.binding.body.div
        nested_divs = self.actual_doc_3.binding.body.div
        dataset = {}
        dataset["document"] = self.actual_doc_3.binding
        dataset[ELEMENT_TIMES_KEY] = [
            ElementTimes(
                begin=self.actual_doc_3.binding.body.begin,
                end=self.actual_doc_3.binding.body.end
            )
        ]
        unnested_divs = []
        for nested_div in nested_divs:
            unnested_divs.extend(
                (DenesterNode.combine_divs(
                    DenesterNode.recurse(nested_div, dataset))))
        assert len(expected_divs) == len(unnested_divs)

    def test_merged_attr_same_region(self):
        expected_divs = self.expected_doc_3.binding.body.div
        nested_divs = self.actual_doc_3.binding.body.div
        dataset = {}
        dataset["document"] = self.actual_doc_3.binding
        dataset[ELEMENT_TIMES_KEY] = [
            ElementTimes(
                begin=self.actual_doc_3.binding.body.begin,
                end=self.actual_doc_3.binding.body.end
            )
        ]
        unnested_divs = []
        for nested_div in nested_divs:
            unnested_divs.extend(
                (DenesterNode.combine_divs(
                    DenesterNode.recurse(nested_div, dataset))))
        assert unnested_divs[0].region == expected_divs[0].region

    def test_merged_attr_metadata(self):
        expected_divs = self.expected_doc_3.binding.body.div
        nested_divs = self.actual_doc_3.binding.body.div
        dataset = {}
        dataset["document"] = self.actual_doc_3.binding
        dataset[ELEMENT_TIMES_KEY] = [
            ElementTimes(
                begin=self.actual_doc_3.binding.body.begin,
                end=self.actual_doc_3.binding.body.end
            )
        ]
        unnested_divs = []
        for nested_div in nested_divs:
            unnested_divs.extend(
                (DenesterNode.combine_divs(
                    DenesterNode.recurse(nested_div, dataset))))
        self.assertEqual(
            len(unnested_divs[0].metadata.orderedContent()),
            len(expected_divs[0].metadata.orderedContent())
        )
        pass

    def test_combine_same_divs(self):
        expected_divs = self.expected_doc_2.binding.body.div
        dataset = {}
        dataset["document"] = self.actual_doc_2.binding
        dataset[ELEMENT_TIMES_KEY] = [
            ElementTimes(
                begin=self.actual_doc_2.binding.body.begin,
                end=self.actual_doc_2.binding.body.end
            )
        ]
        nested_divs = self.actual_doc_2.binding.body.div
        unnested_divs = []
        for nested_div in nested_divs:
            unnested_divs.extend(
                DenesterNode.combine_divs(
                    DenesterNode.recurse(nested_div, dataset)))
        assert len(unnested_divs) == len(expected_divs)

    def test_nested_spans(self):
        expected_spans = self.expected_doc_4.binding.body.div[0].p[0].span
        nested_spans = self.actual_doc_4.binding.body.div[0].p[0].span
        unnested_spans = []
        dataset = {}
        dataset["document"] = self.actual_doc_4.binding
        for nested_span in nested_spans:
            unnested_spans.extend(
                DenesterNode.recurse_span(nested_span, dataset))
        assert len(expected_spans) == len(unnested_spans)

    def test_nested_spans_preserve_brs(self):
        expected_brs = self.count_brs_recursively(
            self.expected_doc_4.binding.body.div[0].p[0])
        nested_spans = self.actual_doc_4.binding.body.div[0].p[0].span
        unnested_spans = []
        dataset = {}
        dataset["document"] = self.actual_doc_4.binding
        for nested_span in nested_spans:
            unnested_spans.extend(
                DenesterNode.recurse_span(nested_span, dataset))
        unnested_brs = len(self.actual_doc_4.binding.body.div[0].p[0].br)
        for unnested_span in unnested_spans:
            unnested_brs += len(unnested_span.br)
        self.assertEqual(expected_brs, unnested_brs)

    def count_brs_recursively(self, element):
        num_brs = len(element.br)
        for s in element.span:
            num_brs += self.count_brs_recursively(s)
        return num_brs

    def test_compute_spans_have_valid_styles(self):
        nested_spans = self.actual_doc_4.binding.body.div[0].p[0].span
        dataset = {}
        unnested_spans = []
        dataset["document"] = self.actual_doc_4.binding
        for nested_span in nested_spans:
            unnested_spans.extend(
                DenesterNode.recurse_span(nested_span, dataset))
        self.expected_doc_4.binding.body.div[0].p[0].span = unnested_spans
        expected_styles = [
            style.id for style in
            self.expected_doc_4.binding.head.styling.style]
        for span in unnested_spans:
            assert span.style[0] in expected_styles

    # yet to remove unused styles, but that is outside scope of denester
    def test_should_create_new_span_style(self):
        expected_style = style_type(
            id="outerinnerYellow",
            backgroundColor="#000000",
            color="#ffff00",
        )
        dataset = {}
        dataset["document"] = self.actual_doc_4.binding
        span_styles = ['outer', 'innerYellow']
        actual_style = \
            DenesterNode.compute_span_merged_styles(span_styles, dataset)
        assert expected_style.id == actual_style.id

    def test_three_styles_should_create_new_span_style(self):
        expected_style = style_type(
            id="outerinnerYellowinnerWhite",
            backgroundColor="#000000",
            color="#FFFFFF",
        )
        dataset = {}
        dataset["document"] = self.actual_doc_4.binding
        span_styles = ['outer', 'innerYellow', 'innerWhite']
        actual_style = \
            DenesterNode.compute_span_merged_styles(span_styles, dataset)
        assert expected_style.id == actual_style.id

    def test_span_computed_font_size_both_parent_child_have_percentages(self):
        expected_style_font_size = "300%"
        span_styles = ["outer", "innerWhite"]
        dataset = {}
        styles = []
        for style_name in span_styles:  # go through styles in xml
            for style in self.actual_doc_4.binding.head.styling.style:
                if style.id == style_name:
                    styles.append(style)
        actual_style_font_size = DenesterNode.calculate_font_size(styles)
        assert expected_style_font_size == actual_style_font_size

    def test_span_computed_font_size_only_child_has_percentage(self):
        expected_style_font_size = "200%"
        span_styles = ["outer", "innerYellow"]
        dataset = {}
        styles = []
        for style_name in span_styles:  # go through styles in xml
            for style in self.actual_doc_4.binding.head.styling.style:
                if style.id == style_name:
                    styles.append(style)
        actual_style_font_size = DenesterNode.calculate_font_size(styles)
        assert expected_style_font_size == actual_style_font_size

    # assuming that child fontsize if absolute it doesn't change
    def test_span_computed_font_size_both_have_absolute_fontsize(self):
        expected_style_font_size = "2c"
        span_styles = ["outerGreen", "innerRed"]
        dataset = {}
        styles = []
        for style_name in span_styles:  # go through styles in xml
            for style in self.actual_doc_4.binding.head.styling.style:
                if style.id == style_name:
                    styles.append(style)
        actual_style_font_size = DenesterNode.calculate_font_size(styles)
        assert expected_style_font_size == actual_style_font_size

    def test_span_computed_font_size_only_parent_has_absolute_fontsize(self):
        expected_style_font_size = "1.5c"
        span_styles = ["outerGreen", "innerYellow"]
        dataset = {}
        styles = []
        for style_name in span_styles:  # go through styles in xml
            for style in self.actual_doc_4.binding.head.styling.style:
                if style.id == style_name:
                    styles.append(style)
        actual_style_font_size = DenesterNode.calculate_font_size(styles)
        assert expected_style_font_size == actual_style_font_size

    def test_span_computed_font_size_only_child_has_absolute_fontsize(self):
        expected_style_font_size = "2c"
        span_styles = ["outer", "innerRed"]
        dataset = {}
        styles = []
        for style_name in span_styles:  # go through styles in xml
            for style in self.actual_doc_4.binding.head.styling.style:
                if style.id == style_name:
                    styles.append(style)
        actual_style_font_size = DenesterNode.calculate_font_size(styles)
        assert expected_style_font_size == actual_style_font_size

    def test_nesting_within_absolute_fontsize_c(self):
        expected_style_font_size = "4c"
        span_styles = ["innerRed", "outer"]
        dataset = {}
        styles = []
        for style_name in span_styles:  # go through styles in xml
            for style in self.actual_doc_4.binding.head.styling.style:
                if style.id == style_name:
                    styles.append(style)
        actual_style_font_size = DenesterNode.calculate_font_size(styles)
        assert expected_style_font_size == actual_style_font_size

    def test_nesting_within_absolute_fontsize_px(self):
        expected_style_font_size = "750px"
        style1 = style_type(
            id="style1",
            fontSize="500px"
        )
        style2 = style_type(
            id="style2",
            fontSize="150%"
        )
        styles = [style1, style2]
        actual_style_font_size = DenesterNode.calculate_font_size(styles)
        assert expected_style_font_size == actual_style_font_size

    def test_nesting_around_absolute_fontsize_px(self):
        expected_style_font_size = "750px"
        style1 = style_type(
            id="style1",
            fontSize="500px"
        )
        style2 = style_type(
            id="style2",
            fontSize="150%"
        )
        style3 = style_type(
            id="style2",
            fontSize="300%"
        )
        styles = [style3, style1, style2]
        actual_style_font_size = DenesterNode.calculate_font_size(styles)
        assert expected_style_font_size == actual_style_font_size

    def test_duplicate_styles_are_not_created(self):
        span_styles = ["nest", "nest"]
        dataset = {}
        dataset["document"] = self.actual_doc_4.binding
        styles = []
        for style_name in span_styles:  # go through styles in xml
            for style in self.actual_doc_4.binding.head.styling.style:
                if style.id == style_name:
                    styles.append(style)
        assert \
            DenesterNode.compute_span_merged_styles(span_styles, dataset).id \
            == "nest"
