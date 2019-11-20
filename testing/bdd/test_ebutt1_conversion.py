import pytest
from pytest_bdd import parsers, scenarios, then, when
from pyxb.exceptions_ import (IncompleteElementContentError,
                              UnrecognizedAttributeError)

from ebu_tt_live.documents import EBUTT1Document, EBUTT3Document
from ebu_tt_live.bindings.converters.ebutt1_ebutt3 import EBUTT1EBUTT3Converter

scenarios('features/ebutt1/ebutt1_conversion.feature')

@when(parsers.parse('the document contains a "{element}" element'))
def when_document_contains_element(template_dict, element):
    template_dict[element] = True

@when(parsers.parse('the document head metadata contains a documentIdentifier element'))
def when_document_head_metadata_contains_documentIdentifier(template_dict):
    template_dict['head_metadata_documentIdentifier'] = True

@when(parsers.parse('the documentMetadata contains a documentIdentifier element'))
def when_documentMetadata_contains_documentIdentifier(template_dict):
    template_dict['doc_metadata_documentIdentifier'] = True

@when('the XML is parsed as a valid EBU-TT-1 document')
def when_document_parsed_ebutt1(test_context, template_file, template_dict):
    xml_text = template_file.render(template_dict)
    ebutt1_document = EBUTT1Document.create_from_xml(xml_text)
    ebutt1_document.validate()
    test_context['ebutt1_document'] = ebutt1_document

@when('the EBU-TT-1 document is converted to EBU-TT-3')
def when_ebutt1_converted_to_ebutt3(test_context, template_file, template_dict):
    ebutt1_converter = EBUTT1EBUTT3Converter(sequence_id = 'TestConverter')
    doc_xml = test_context["ebutt1_document"].get_xml()
    ebutt1_doc = EBUTT1Document.create_from_xml(doc_xml)
    converted_bindings = ebutt1_converter.convert_document(ebutt1_doc.binding)
    ebutt3_document = EBUTT3Document.create_from_raw_binding(converted_bindings)
    test_context['ebutt3_document'] = ebutt3_document

@then('the EBU-TT-3 document is valid')
def then_ebutt3_doc_valid(test_context):
    test_context['ebutt3_document'].validate()
    assert isinstance(test_context['ebutt3_document'], EBUTT3Document)

@then(parsers.parse('the sequenceIdentifier is "{value}"'))
def then_sequence_identifier_is_value(test_context, value):
    assert test_context['ebutt3_document'].sequence_identifier == value

