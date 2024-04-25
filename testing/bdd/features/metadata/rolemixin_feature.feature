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
            | role_inherited_content.xml | p1      | caption, sound |
            | role_inherited_content.xml | d5      | caption        |

    Scenario Outline: If a role inherited properly with metadata
        Given an xml file <xml_file>
        When the document is generated
        And the EBU-TT-Live document is valid
        Then the role in <elem_id> is <computed_value>

        Examples:
            | xml_file                            | elem_id | computed_value              |
            | role_inherited_content_metadata.xml | d1      | caption, description        |
            | role_inherited_content_metadata.xml | d2      | caption, description        |
            | role_inherited_content_metadata.xml | p1      | caption, sound, description |
            | role_inherited_content_metadata.xml | d5      | caption, description        |
