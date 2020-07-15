@styles @document @ebuttd_conversion @fontSize
Feature: Convert fontSize from EBU-TT Live to EBU-TT-D when two elements reference the same style

  Examples:
  | local_time_mapping | xml_file                           | style_attribute |
  | 00:00:00           | ebuttd_fontsize_same_style_ref.xml | tts:fontSize    |

  # If specified in cell units, the computation must take into account cellResolution.
  # If not region element, calculation is relative to parent element's font size; otherwise, relative to the Computed Cell Size.
  # The second value for font size is ignored in the conversion.

  Scenario: Inherited font size calculation
    Given an xml file <xml_file>
    When it has a cell resolution of <cell_resolution>
    And it has extent of <extent>
    And it contains style S1 with <style_attribute> value <S1_value>
    And the document is generated
    And the document is converted to EBUTTD with <local_time_mapping>
    Then EBUTTD document is valid
    And the EBUTTD has div fontSize <ttd_div_fontSize>
    And the EBUTTD has p fontSize of <ttd_p_fontSize>

  Examples:
  | cell_resolution | extent       | S1_value | ttd_div_fontSize | ttd_p_fontSize |
  | 40 24           |              | 1c 2c    | 200%             |                |
  | 32 15           |              | 1c       |                  |                |
  | 32 15           |              | 2c       | 200%             |                |
  | 32 15           |              | 100%     |                  |                |
  | 32 15           |              | 200%     | 200%             | 200%           |
  | 32 15           |              |          |                  |                |
  | 32 15           | 1280px 720px | 24px     | 50%              |                |
  | 32 15           | 1280px 720px | 48px     |                  |                |