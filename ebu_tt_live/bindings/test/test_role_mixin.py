from unittest import TestCase

from ebu_tt_live.bindings import d_div_type, d_br_type, d_body_type, d_p_type, d_span_type, div_type, \
    br_type, body_type, p_type, span_type

from ebu_tt_live.bindings._ebuttm import pMetadata_type, divMetadata_type


class TestElementRoleMixin(TestCase):
    class Metadata:
        def __init__(self, role=None):
            self.role = role

    def setUp(self):
        self.elements = {
            'd_div': d_div_type(),
            'd_br': d_br_type(),
            'd_body': d_body_type(),
            'd_p': d_p_type(),
            'd_span': d_span_type(),
            'div': div_type(),
            'br': br_type(),
            'body': body_type(),
            'p': p_type(),
            'span': span_type()
        }
        self.dataset = {'role_stack': []}
        self.metadata_types = {
            'div': divMetadata_type,
            'p': pMetadata_type
        }

    def test_initial_computed_role(self):
        """Test that computed_role is None when no role is set and role_stack is empty for different element types."""
        for element_name, element in self.elements.items():
            with self.subTest(element=element_name):
                self.assertEqual(element.computed_roles, set(),
                                 f"Initial computed role should be None for {element_name}.")

    def test_role_propagation(self):
        """Test proper propagation of directly set role to computed_role for different element types."""
        for element_name, element in self.elements.items():
            with self.subTest(element=element_name):
                element.role = 'caption'
                element._semantic_compute_roles({})
                self.assertEqual(element.computed_roles, {'caption'},
                                 f"Computed role should match the directly set role for {element_name}.")

    def test_role_inheritance(self):
        """Test role inheritance from role_stack when no role is directly set for different element types."""
        for element_name, element in self.elements.items():
            with self.subTest(element=element_name):
                self.dataset['role_stack'].append({'caption'})
                element._semantic_compute_roles(self.dataset)
                self.assertEqual(element.computed_roles, {'caption'},
                                 f"Computed role should inherit from role_stack for {element_name}.")
                self.dataset['role_stack'].pop()

    def test_role_absence(self):
        """Test that computed_role is None when no role is set and role_stack is empty for different element types."""
        for element_name, element in self.elements.items():
            with self.subTest(element=element_name):
                element._semantic_compute_roles({})
                self.assertEqual(element.computed_roles, set(),
                                 f"Computed role should be empty when role_stack is empty for {element_name}.")

    def test_role_stack_management(self):
        """Test that role_stack is properly managed during element processing."""
        for element_name, element in self.elements.items():
            with self.subTest(element=element_name):
                initial_stack_length = len(self.dataset['role_stack'])
                element._semantic_push_computed_roles(self.dataset)
                element._semantic_pop_computed_roles(self.dataset)
                self.assertEqual(len(self.dataset['role_stack']), initial_stack_length)

    def test_metadata_role_merging_after_traversal(self):
        """Metadata roles should merge with element roles after traversal."""
        for element_name, element in self.elements.items():
            if element_name in self.metadata_types:
                with self.subTest(element=element_name):
                    metadata_instance = self.metadata_types[element_name]()
                    metadata_instance.role = 'description'
                    element.metadata = metadata_instance
                    element._semantic_compute_roles(self.dataset)
                    self.assertIn('description', element.computed_roles)

