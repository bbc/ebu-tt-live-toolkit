@timing @document @ebuttd_conversion
Feature: Resolving timings on elements

    Examples:
      | xml_file                   |
      | resolved_time_elements.xml |

  Scenario: Timings present on both p and span elements
    Given an xml file <xml_file>
    When   it has body begin time <body_begin>
    And   it has body end time <body_end>
    And  it has p begin time <p_begin>
    And   it has p end time <p_end>
    And   it has span1 begin time <span1_begin>
    And   it has span1 end time <span1_end>
    And   it has span2 begin time <span2_begin>
    And   it has span2 end time <span2_end>
    And   it has p1 begin time <p1_begin>
    And   it has p1 end time <p1_end>
    And   it has span3 begin time <span3_begin>
    And   it has span3 end time <span3_end>
    When  the document is generated
    And   the EBU-TT-Live document is converted to EBU-TT-D
    Then  EBUTTD document is valid
    Then  it has computed begin time <computed_begin>
    And   it has computed end time <computed_end>

    Examples:
      | body_begin | body_end | p_begin    | p_end      | span1_begin | span1_end  | span2_begin | span2_end | p1_begin | p1_end   | span3_begin | span3_end | computed_begin | computed_end |
      | 00:00:10.0 |          | 00:00:11.0 |            | 00:00:01.0  | 00:00:20.0 |             |           |          |          |             |           | 00:00:10.0     | 00:00:41.0   |
      |            |          |            |            |             |            |             |           | 00:01:13 |          | 00:00:01.0  | 00:00:20  | 00:01:13.0     | 00:01:33.0   |
      |            |          | 00:00:10.0 | 00:00:11.0 | 00:00:08    | 00:00:10   |             |           | 00:00:13 |          | 00:00:13.0  | 00:00:15  | 00:00:10.0     | 00:00:28.0   |

  Scenario: Timings specified on div shall be removed
    Given an xml file <xml_file>
    When  it has div begin time <div_begin>
    And   it has div end time <div_end>
    And   it has body begin time <body_begin>
    And   it has body end time <body_end>
    And   it has p begin time <p_begin>
    And   it has p end time <p_end>
    And   it has p1 begin time <p1_begin>
    And   it has p1 end time <p1_end>
    And   it has span1 begin time <span1_begin>
    And   it has span1 end time <span1_end>
    When  the document is generated
    And   the EBU-TT-Live document is converted to EBU-TT-D
    Then  EBUTTD document is valid

    Examples:
      | body_begin | body_end | div_begin | div_end  | p_begin  | p_end    | span1_begin | span1_end | p1_begin | p1_end   |
      | 00:01:10   | 00:01:30 | 00:01:00  | 00:01:30 | 00:01:00 | 00:01:30 | 00:00:08    | 00:00:20  | 00:01:13 | 00:01:15 |
      |            |          | 00:01:00  | 00:01:30 | 00:01:00 | 00:01:30 | 00:00:08    | 00:00:20  |          |          |
      | 00:01:10   | 00:01:30 |           |          | 00:01:00 | 00:01:30 | 00:00:08    | 00:00:20  |          |          |
      | 00:01:10   | 00:01:30 | 00:01:00  | 00:01:30 |          |          | 00:00:08    | 00:00:20  |          |          |
      | 00:01:10   | 00:01:30 | 00:01:00  | 00:01:30 | 00:01:00 | 00:01:30 |             |           | 00:01:13 | 00:01:15 |
