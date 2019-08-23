from pytest_bdd import scenarios, when, then, given, parsers
import xml.etree.ElementTree as ET

scenarios('features/timing/ebuttd_resolved_timings_on_elements.feature')

@then('element p has begin time <p_computed_begin_time>')
def then_it_has_p_computed_time(test_context, p_computed_begin_time):
    document = test_context['ebuttd_document']
    tree = ET.fromstring(document.get_xml())
    elements = tree.findall('{http://www.w3.org/ns/ttml}body/{http://www.w3.org/ns/ttml}div/')
    document_generated_p_begin_time = elements[0].get('begin')
    assert '' == document_generated_p_begin_time

@then('element p has end time <p_computed_end_time>')
def then_it_has_p_computed_time(test_context, p_computed_end_time):
    document = test_context['ebuttd_document']
    tree = ET.fromstring(document.get_xml())
    elements = tree.findall('{http://www.w3.org/ns/ttml}body/{http://www.w3.org/ns/ttml}div/')
    document_generated_p_end_time = elements[0].get('end')
    assert None == document_generated_p_end_time


@then('span1 computed begin time is <span1_computed_begin_time>')
def then_it_has_span1_computed_begin_time(test_context, span1_computed_begin_time):
    document = test_context['ebuttd_document']
    tree = ET.fromstring(document.get_xml())
    elements = tree.findall('{http://www.w3.org/ns/ttml}body/{http://www.w3.org/ns/ttml}div/{http://www.w3.org/ns/ttml}p/')
    print(document.get_xml())
    document_generated_span_begin_time = elements[0].get('begin')
    assert span1_computed_begin_time == document_generated_span_begin_time

@then('span2 computed begin time is <span2_computed_begin_time>')
def then_it_has_span2_computed_end_time(test_context, span2_computed_begin_time):
    document = test_context['ebuttd_document']
    tree = ET.fromstring(document.get_xml())
    elements = tree.findall('{http://www.w3.org/ns/ttml}body/{http://www.w3.org/ns/ttml}div/{http://www.w3.org/ns/ttml}p/')
    document_generated_span_begin_time = elements[1].get('begin')
    assert span2_computed_begin_time == document_generated_span_begin_time

@then('span1 computed end time is <span1_computed_end_time>')
def then_it_has_span1_computed_end_time(test_context, span1_computed_end_time):
    document = test_context['ebuttd_document']
    tree = ET.fromstring(document.get_xml())
    elements = tree.findall('{http://www.w3.org/ns/ttml}body/{http://www.w3.org/ns/ttml}div/{http://www.w3.org/ns/ttml}p/')
    document_generated_span_end_time = elements[0].get('end')
    if document_generated_span_end_time is not None:
        assert span1_computed_end_time == document_generated_span_end_time
    else:
        assert None == document_generated_span_end_time

@then('span2 computed begin time is <span2_computed_begin_time>')
def then_it_has_span2_computed_end_time(test_context, span2_computed_end_time):
    document = test_context['ebuttd_document']
    tree = ET.fromstring(document.get_xml())
    elements = tree.findall('{http://www.w3.org/ns/ttml}body/{http://www.w3.org/ns/ttml}div/{http://www.w3.org/ns/ttml}p/')
    document_generated_span_end_time = elements[1].get('end')
    assert span2_computed_end_time == document_generated_span_end_time
