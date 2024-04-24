from unittest import TestCase

from ebu_tt_live.bindings import d_div_type, d_br_type, d_body_type, d_p_type, d_span_type, d_metadata_type, div_type, \
    br_type, body_type, p_type, span_type


class TestElementRoleMixin(TestCase):

    def setUp(self):
        self.elements = {
            'd_div': d_div_type(),
            'd_br': d_br_type(),
            'd_body': d_body_type(),
            'd_p': d_p_type(),
            'd_span': d_span_type(),
            'd_metadata': d_metadata_type(),
            'div': div_type(),
            'br': br_type(),
            'body': body_type(),
            'p': p_type(),
            'span': span_type()
        }
        self.dataset = {'metadata_roles': []}

    def test_initial_computed_role(self):
        """Test that computed_role is None when no role is set and metadata_roles is empty for different element types."""
        for element_name, element in self.elements.items():
            with self.subTest(element=element_name):
                self.assertIsNone(element.computed_roles, f"Initial computed role should be None for {element_name}.")

    def test_role_propagation(self):
        """Test proper propagation of directly set role to computed_role for different element types."""
        for element_name, element in self.elements.items():
            with self.subTest(element=element_name):
                element.role = 'caption'
                element._semantic_compute_roles({})
                self.assertEqual(element.computed_roles, ['caption'], f"Computed role should match the directly set role for {element_name}.")

    def test_role_inheritance(self):
        """Test role inheritance from metadata_roles when no role is directly set for different element types."""
        for element_name, element in self.elements.items():
            with self.subTest(element=element_name):
                self.dataset['metadata_roles'].append(['caption'])
                element._semantic_compute_roles(self.dataset)
                self.assertEqual(element.computed_roles, ['caption'], f"Computed role should inherit from metadata_roles for {element_name}.")
                self.dataset['metadata_roles'].pop()

    def test_role_absence(self):
        """Test that computed_role is None when no role is set and metadata_roles is empty for different element types."""
        for element_name, element in self.elements.items():
            with self.subTest(element=element_name):
                element._semantic_compute_roles({})
                self.assertIsNone(element.computed_roles, f"Computed role should be None when metadata_roles is empty for {element_name}.")

    def test_metadata_roles_pop(self):
        """Test proper popping from metadata_roles after traversal for different element types."""
        for element_name, element in self.elements.items():
            with self.subTest(element=element_name):
                element._semantic_push_computed_roles(self.dataset)
                element._semantic_pop_computed_roles(self.dataset)
                self.assertEqual(len(self.dataset['metadata_roles']), 0, f"Role stack should be empty after pop for {element_name}.")
