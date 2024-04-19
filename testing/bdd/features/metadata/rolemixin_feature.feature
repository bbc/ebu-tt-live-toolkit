Feature: RoleMixin role assignment functionality

    Scenario Outline: If a role inherited properly
        Given an xml file <xml_file>
        When the document is generated
        And the EBU-TT-Live document is valid
        Then the role in <elem_id> is <computed_value>

        Examples:
            | xml_file                   | elem_id | computed_value |
            | role_inherited_content.xml | d1      | caption        |
            | role_inherited_content.xml | d2      | caption        |
            | role_inherited_content.xml | p1      | sound          |
            | role_inherited_content.xml | d5      | caption        |
