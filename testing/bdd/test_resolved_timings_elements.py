from pytest_bdd import scenarios, when, then, given
import pytest
import xml.etree.ElementTree as ET

scenarios('features/timing/resolved_time_on_elements.feature')

@when('it has timeBase <time_base>')
def when_time_base(time_base, template_dict):
    template_dict['time_base'] = time_base

@when('it has sequenceIdentifier <sequence_identifier>')
def when_seq_id(sequence_identifier, template_dict):
    template_dict['sequence_identifier'] = sequence_identifier

@when('it contains p begin time <p_begin> and end time <p_end>')
def given_p_begin(p_begin, p_end ,template_dict):
    template_dict['p_begin'] = p_begin
    template_dict['p_end'] = p_end

@when('it contains span begin time <span_begin> and end time <span_end>')
def given_span_begin(span_begin, span_end ,template_dict):
    template_dict['span_begin'] = span_begin
    template_dict['span_end'] = span_end

@then('timings are not present on p element')
def then_timings_are_not_present(test_context):
    ebuttd_document = test_context['ebuttd_document']
    tree = ET.fromstring(ebuttd_document.get_xml())
    elements = tree.findall('{http://www.w3.org/ns/ttml}body/{http://www.w3.org/ns/ttml}div/')
    for element in elements:
        if 'begin' and 'end' in element.keys():
            assert False
        else:
            assert True