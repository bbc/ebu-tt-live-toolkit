from pytest_bdd import parsers, scenarios, then, when
from ebu_tt_live.documents import EBUTTDDocument
from ebu_tt_live.scripts.imsc_hrm_validator import imscHrmValidator

scenarios('features/validation/imsc-hrm-validator.feature')


@when('the xml file is parsed as a valid EBU-TT-D document')
def when_document_parsed_ebuttd(test_context, template_file, template_dict):
    xml_text = template_file.render(template_dict)
    ebuttd_document = EBUTTDDocument.create_from_xml(xml_text)
    ebuttd_document.validate()
    test_context['ebuttd_document'] = ebuttd_document

@then('the EBU-TT-D document is not valid wrt the IMSC HRM')
def then_ebuttd_document_invalid_for_imsc_hrm(test_context):
    imsc_hrm_validator = imscHrmValidator()
    ebuttd_document = test_context['ebuttd_document']
    assert imsc_hrm_validator.validate(ebuttd_document) == False

@then('the EBU-TT-D document is valid wrt the IMSC HRM')
def then_ebuttd_document_valid_for_imsc_hrm(test_context):
    imsc_hrm_validator = imscHrmValidator()
    ebuttd_document = test_context['ebuttd_document']
    assert imsc_hrm_validator.validate(ebuttd_document) == True
