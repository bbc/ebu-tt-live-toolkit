from pytest_bdd import scenarios, when, then, given, parsers
import xml.etree.ElementTree as ET

scenarios('features/styles/ebuttd_style_references.feature')


@when(parsers.parse('it contains style "{style_name}"'))
def when_it_contains_style(test_context, template_dict, style_name):
    if 'styles' not in template_dict:
        template_dict['styles'] = list()
    style = {"id": style_name}    
    template_dict['styles'].append(style)
    test_context[style_name] = style


@when(parsers.parse('style "{style_name}" has attribute "{attribute}" set to "{value}"'))
def when_style_has_attribute(test_context, style_name, attribute, value):
    test_context[style_name][attribute] = value


@then(parsers.parse('the ebu_tt_d document contains style "{style_name}" with attribute "{attribute}" set to "{value}"'))
def then_converted_document_has_style(test_context, style_name, attribute, value):
    print(test_context['document'].get_xml())
    print(test_context['ebuttd_document'].get_xml())
    ebuttd_document = test_context['ebuttd_document']
    tree = ET.fromstring(ebuttd_document.get_xml())
    elements = tree.findall('{http://www.w3.org/ns/ttml}head/{http://www.w3.org/ns/ttml}styling/{http://www.w3.org/ns/ttml}style[@{http://www.w3.org/XML/1998/namespace}id="%s"]' %style_name)
    assert len(elements) == 1
    assert elements[0].get('{http://www.w3.org/ns/ttml#styling}%s' % attribute) == value
