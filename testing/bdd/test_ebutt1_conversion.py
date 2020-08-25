from pytest_bdd import parsers, scenarios, then, when

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


@when(parsers.parse('the EBU-TT-1 converter sequenceIdentifier is "{seq_id}"'))
def when_converter_seq_id(test_context, seq_id):
    test_context['converter_seq_id'] = seq_id


@then(parsers.parse('the sequenceIdentifier is "{value}"'))
def then_sequence_identifier_is_value(test_context, value):
    assert test_context['document'].sequence_identifier == value
