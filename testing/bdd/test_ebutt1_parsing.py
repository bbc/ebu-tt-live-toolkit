import pytest
from pytest_bdd import parsers, scenarios, when, then
from ebu_tt_live.documents import EBUTT1Document, EBUTT3Document
from ebu_tt_live.documents.converters import EBUTT1EBUTT3Converter
from pyxb.exceptions_ import IncompleteElementContentError, UnrecognizedAttributeError
import xml.etree.ElementTree as ET

# scenarios('features/ebutt1/ebutt1_validity.feature')
scenarios('features/ebutt1/tt1_tt3_conversion.feature')


@when(parsers.parse('the document contains a "{element}" element'))
def when_document_contains_element(template_dict, element):
    template_dict[element] = True


@when(parsers.parse('the document body contains a "{attribute}" attribute'))
def when_document_body_contains_attribute(template_dict, attribute):
    template_dict[attribute] = True


@when(parsers.parse('the document has metadata "{key}" set to "{value}"'))
def when_document_has_metadata(template_dict, key, value):
    template_dict[key] = value


@when('the document\'s timeBase is set to <timebase>')
def when_document_timebase(template_dict, timebase):
    # timeBase in ebutt1_template.xml is 'media' by default
    template_dict['timeBase'] = timebase


@when('the document contains an ebuttp attribute <attribute>')
def when_document_contains_ebuttp_attribute(template_dict, attribute):
    template_dict['ebuttp'] = True
    template_dict[attribute] = True


@when('the XML is parsed as an EBU-TT-1 document')
def when_document_parsed_ebutt1(test_context, template_file, template_dict):
    xml_text = template_file.render(template_dict)
    print(xml_text)
    ebutt1_document = EBUTT1Document.create_from_xml(xml_text)
    test_context['ebutt1_document'] = ebutt1_document


@when('the EBU-TT-1 document is converted to EBU-TT-3')
def when_convert_tt1_tt3(test_context):
    converter = EBUTT1EBUTT3Converter()
    ebutt1 = test_context['ebutt1_document']
    converted_bindings = converter.convert_document(ebutt1.binding)
    test_context['ebutt3_binding'] = converted_bindings


@then('the document fails to parse as an EBU-TT-1 document because of an IncompleteElementContentError')
def then_document_fails_ebutt1_element(template_file, template_dict):
    xml_text = template_file.render(template_dict)
    print(xml_text)
    with pytest.raises(IncompleteElementContentError):
        EBUTT1Document.create_from_xml(xml_text)


@then('the document fails to parse as an EBU-TT-1 document because of an UnrecognizedAttributeError')
def then_document_fails_ebutt1_attribute(template_file, template_dict):
    xml_text = template_file.render(template_dict)
    print(xml_text)
    with pytest.raises(UnrecognizedAttributeError):
        EBUTT1Document.create_from_xml(xml_text)


@then('the EBU-TT-1 document is valid')
def then_ebutt1_valid(test_context):
    document = test_context['ebutt1_document']
    document.validate()


@then('the EBU-TT-3 document is valid')
def then_ebutt3_valid(test_context):
    converted_bindings = test_context['ebutt3_binding']
    converted_document = EBUTT3Document.create_from_raw_binding(converted_bindings)
    test_context['ebutt3_document'] = converted_document
    converted_document.validate()


namespaces = {
    'ebuttp': 'urn:ebu:tt:parameters',
    'ttp': 'http://www.w3.org/ns/ttml#parameter',
}


@then(parsers.parse('the tt element contains the attribute "{attribute}" set to "{value}"'))
def then_ebutt3_tt_has_attribute(test_context, attribute, value):
    attribute_pair = attribute.split(':')
    if len(attribute_pair) == 2:
        attribute_namespace = namespaces[attribute_pair[0]]
        attribute_name = attribute_pair[1]
        path = '{%s}%s' % (attribute_namespace, attribute_name)
    else:
        path = attribute_pair[0]
    converted_document = test_context['ebutt3_document']
    tree = ET.fromstring(converted_document.get_xml())
    assert tree.get(path) == value
