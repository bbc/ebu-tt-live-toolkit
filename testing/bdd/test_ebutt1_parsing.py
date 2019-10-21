import pytest
from pytest_bdd import parsers, scenarios, when, then
from ebu_tt_live.documents import EBUTT1Document
from pyxb.exceptions_ import IncompleteElementContentError

scenarios('features/ebutt1/ebutt1_validity.feature')


@when(parsers.parse('the document contains a "{element}" element'))
def when_document_contains_element(template_dict, element):
    template_dict[element] = True


@when('the XML is parsed as an EBU-TT-1 document')
def when_document_parsed_ebutt1(test_context, template_file, template_dict):
    xml_text = template_file.render(template_dict)
    print(xml_text)
    ebutt1_document = EBUTT1Document.create_from_xml(xml_text)
    test_context['ebutt1_document'] = ebutt1_document


@then('the document fails to parse as an EBU-TT-1 document because of an IncompleteElementContentError')
def then_document_fails_ebutt1(template_file, template_dict):
    xml_text = template_file.render(template_dict)
    with pytest.raises(IncompleteElementContentError):
        EBUTT1Document.create_from_xml(xml_text)


@then('the EBU-TT-1 document is valid')
def then_ebutt1_valid(test_context):
    document = test_context['ebutt1_document']
    document.validate()
