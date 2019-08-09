Feature: Resolve times on elements




Scenario: Timings present on both p and span elements
    Given an xml file <xml_file>
    When  it contains p begin time <p_begin> and end time <p_end>
    And   it contains span begin time <span_begin> and end time <span_end>
    When  the document is generated
    And   the EBU-TT-Live document is converted to EBU-TT-D
    Then  EBUTTD document is valid
    And   timings are not present on p element

Examples:
  | xml_file                   |  p_begin | p_end  | span_begin | span_end | 
  | resolved_time_elements.xml |  10s     | 15s    |  3s        | 5s       |  

# the library already removes timings on div when converting
@skip
Scenario: Timings specified on div shall be removed
     Given an xml file <xml_file> 
     #todo
     #When  it contains div begin time <div_begin> and end time <div_end>
     And   the EBU-TT-Live document is converted to EBU-TT-D
     Then  EBUTTD document is valid
     #todo
     #And   timings are present on "p" element
@skip
Scenario: Timings specified on body shall be removed
     Given an xml file <xml_file> 
    #todo
     #When  it contains div begin time <body_begin> and end time <body_end>
     #And  it contains div begin time <div_begin> and end time <div_end>
     And   the EBU-TT-Live document is converted to EBU-TT-D
     Then  EBUTTD document is valid
