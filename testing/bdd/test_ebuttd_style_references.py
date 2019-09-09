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


@when(parsers.parse('it contains some text with style "{style_name}"'))
def when_text_has_style(template_dict, style_name):
    template_dict['text_style'] = style_name


@when(parsers.parse('it contains some text with region "{region_name}"'))
def when_text_has_region(template_dict, region_name):
    template_dict['text_region'] = region_name


@when(parsers.parse('it contains region "{region_id}"'))
def when_it_contains_region(test_context, template_dict, region_id):
    if 'regions' not in template_dict:
        template_dict['regions'] = list()
    region = {"id": region_id}
    template_dict['regions'].append(region)
    test_context[region_id] = region


@when(parsers.parse('region "{region_id}" has attribute "{attribute}" set to "{value}"'))
def when_region_has_attribute(test_context, region_id, attribute, value):
    test_context[region_id][attribute] = value


@then(parsers.parse('the ebu_tt_d document contains style "{style_name}" with attribute "{attribute}" set to "{value}"'))
def then_converted_document_has_style(test_context, style_name, attribute, value):
    ebuttd_document = test_context['ebuttd_document']
    tree = ET.fromstring(ebuttd_document.get_xml())
    elements = tree.findall('{http://www.w3.org/ns/ttml}head/'
                            '{http://www.w3.org/ns/ttml}styling/'
                            '{http://www.w3.org/ns/ttml}style[@{http://www.w3.org/XML/1998/namespace}id="%s"]' % style_name)
    assert len(elements) == 1
    assert elements[0].get('{http://www.w3.org/ns/ttml#styling}%s' % attribute) == value


@then(parsers.parse('the ebu_tt_d document contains region "{region_id}" with attribute "{attribute}" set to "{value}"'))
def then_converted_document_has_region_with_styling_attribute(test_context, region_id, attribute, value):
    ebuttd_document = test_context['ebuttd_document']
    tree = ET.fromstring(ebuttd_document.get_xml())
    elements = tree.findall('{http://www.w3.org/ns/ttml}head/'
                            '{http://www.w3.org/ns/ttml}layout/'
                            '{http://www.w3.org/ns/ttml}region[@{http://www.w3.org/XML/1998/namespace}id="%s"]' % region_id)
    assert len(elements) == 1
    assert elements[0].get('{http://www.w3.org/ns/ttml#styling}%s' % attribute) == value


@then(parsers.parse('the ebu_tt_d document contains style "{style_id}" without a "{attribute}" attribute'))
def then_converted_document_has_style_without_attribute(test_context, style_id, attribute):
    ebuttd_document = test_context['ebuttd_document']
    tree = ET.fromstring(ebuttd_document.get_xml())
    elements = tree.findall('{http://www.w3.org/ns/ttml}head/'
                            '{http://www.w3.org/ns/ttml}styling/'
                            '{http://www.w3.org/ns/ttml}style[@{http://www.w3.org/XML/1998/namespace}id="%s"]' % style_id)
    assert len(elements) == 1
    assert elements[0].get('{http://www.w3.org/ns/ttml#styling}%s' % attribute) == None
