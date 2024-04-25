from pytest_bdd import scenarios, then

from ebu_tt_live.bindings import div_type

scenarios('features/metadata/rolemixin_feature.feature')

@then('the role in <elem_id> is <computed_value>')
def then_computed_style_value_is(elem_id, computed_value, test_context):
    document = test_context['document']
    elem = document.get_element_by_id(elem_id)
    if computed_value == '':
        assert elem.computed_roles is None
    else:
        expected_roles = set(computed_value.split(", "))
        assert elem.computed_roles == expected_roles


