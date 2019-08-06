Feature: Remove style elements that refer to other style elements


  Scenario: Convert style element with reference to another style to a presentationally equivalent
    Given an xml file <xml_file>
    When  it contains style "s1"
    And   style "s1" has attribute "color" set to "white"
    And   style "s1" has attribute "backgroundColor" set to "black"
    And   it contains style "s2"
    And   style "s2" has attribute "style" set to "s1"
    And   style "s2" has attribute "fontFamily" set to "reith"
    And   it contains style "s3"
    And   style "s3" has attribute "fontFamily" set to "monospace"
    And   it contains style "s4"
    And   style "s4" has attribute "style" set to "s2 s3"
    And   style "s4" has attribute "color" set to "yellow"
    When  the document is generated
    And   the EBU-TT-Live document is converted to EBU-TT-D
    Then  the ebu_tt_d document contains style "s4" with attribute "fontFamily" set to "monospace"
    And   the ebu_tt_d document contains style "s4" with attribute "color" set to "#ffff00ff"
    And   the ebu_tt_d document contains style "s4" with attribute "backgroundColor" set to "#000000ff"

    Examples:
      | xml_file                     |
      | style_element_references.xml |
