import pytest
from pytest_bdd import scenarios, when, then, parsers
from ebu_tt_live.errors import OverlappingActiveElementsError, RegionExtendingOutsideDocumentError
from ebu_tt_live.documents import EBUTT3Document, EBUTT3DocumentSequence
scenarios('features/timing/ebuttd_multiple_active_regions_overlapping.feature')


@when(parsers.parse('it has region "{region_id}"'))
def when_it_contains_region(test_context, template_dict, region_id):
    if 'regions' not in template_dict:
        template_dict['regions'] = list()
    region = {"id": region_id}    
    template_dict['regions'].append(region)
    test_context[region_id] = region

@when(parsers.parse('it has p_element "{p_id}"'))
def when_it_contains_p_element(test_context, template_dict, p_id):
    if 'p_elements' not in template_dict:
        template_dict['p_elements'] = list()
    p_element = {"id": p_id}    
    template_dict['p_elements'].append(p_element)
    test_context[p_id] = p_element

@when(parsers.parse('p_element "{p_id}" has attribute "{attribute}" set to <p1_begin>'))
def when_p1_has_attribute_extent(test_context, p_id, attribute ,p1_begin):
    test_context[p_id][attribute] = p1_begin

@when(parsers.parse('p_element "{p_id}" has attribute "{attribute}" set to <p1_end>'))
def when_p1_has_attribute_extent(test_context, p_id, attribute ,p1_end):
    test_context[p_id][attribute] = p1_end

@when(parsers.parse('p_element "{p_id}" has attribute "{attribute}" set to <p2_begin>'))
def when_p2_has_attribute_extent(test_context, p_id, attribute ,p2_begin):
    test_context[p_id][attribute] = p2_begin

@when(parsers.parse('p_element "{p_id}" has attribute "{attribute}" set to <p2_end>'))
def when_p2_has_attribute_extent(test_context, p_id, attribute ,p2_end):
    test_context[p_id][attribute] = p2_end

@when(parsers.parse('p_element "{p_id}" has attribute "{attribute}" set to "{value}"'))
def when_region1_has_attribute_origin(test_context, p_id, attribute ,value):
    test_context[p_id][attribute] = value

@when(parsers.parse('region "{region_id}" has attribute "{attribute}" set to <r1_origin>'))
def when_region1_has_attribute_origin(test_context, region_id, attribute ,r1_origin):
    test_context[region_id][attribute] = r1_origin

@when(parsers.parse('region "{region_id}" has attribute "{attribute}" set to <r1_extent>'))
def when_region1_has_attribute_extent(test_context, region_id, attribute ,r1_extent):
    test_context[region_id][attribute] = r1_extent

@when(parsers.parse('region "{region_id}" has attribute "{attribute}" set to <r2_origin>'))
def when_region2_has_attribute_origin(test_context, region_id, attribute ,r2_origin):
    test_context[region_id][attribute] = r2_origin

@when(parsers.parse('region "{region_id}" has attribute "{attribute}" set to <r2_extent>'))
def when_region2_has_attribute_extent(test_context, region_id, attribute ,r2_extent):
    test_context[region_id][attribute] = r2_extent

@when(parsers.parse('region "{region_id}" has attribute "{attribute}" set to <r3_origin>'))
def when_region3_has_attribute_origin(test_context, region_id, attribute ,r3_origin):
    test_context[region_id][attribute] = r3_origin

@when(parsers.parse('region "{region_id}" has attribute "{attribute}" set to <r3_extent>'))
def when_region3_has_attribute_extent(test_context, region_id, attribute ,r3_extent):
    test_context[region_id][attribute] = r3_extent

@when(parsers.parse('it contains element with region1 "{region_id}"'))
def when_element_has_attribute_region1(template_dict, region_id):
    template_dict['text_region1'] = region_id

@when(parsers.parse('it contains element with region2 "{region_id}"'))
def when_element_has_attribute_region2(template_dict, region_id):
    template_dict['text_region2'] = region_id

@then(parsers.parse('application should exit with error OverlappingActiveElementsError'))
def then_application_should_exit_overlapping_active_region_error(test_context, template_dict, template_file):
     with pytest.raises(OverlappingActiveElementsError) as e:
       xml_file = template_file.render(template_dict)
       document = EBUTT3Document.create_from_xml(xml_file)
       test_context['document'] = document
     
@then(parsers.parse('application should exit with error RegionExtendingOutsideDocumentError'))
def then_application_should_exit_with_region_error(test_context, template_dict, template_file):
     with pytest.raises(RegionExtendingOutsideDocumentError ) as e:
       xml_file = template_file.render(template_dict)
       document = EBUTT3Document.create_from_xml(xml_file)
       test_context['document'] = document