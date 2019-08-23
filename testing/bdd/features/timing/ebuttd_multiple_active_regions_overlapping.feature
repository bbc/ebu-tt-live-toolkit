Feature: Multiple active regions overlapping


Examples:
| xml_file                       |
| active_regions_overlapping.xml |

Scenario: Multiple active regions that overlap the application shall exit with an error.

    Given an xml file <xml_file>
    When  it has region "r1" 
    And   region "r1" has attribute "origin" set to <r1_origin> 
    And   region "r1" has attribute "extent" set to <r1_extent>
    And   it has region "r2" 
    And   region "r2" has attribute "origin" set to <r2_origin> 
    And   region "r2" has attribute "extent" set to <r2_extent>
    And   it has p_element "p1"
    And   it has p_element "p2"
    And   p_element "p1" has attribute "region" set to "r1"
    And   p_element "p2" has attribute "region" set to "r2"
    And   p_element "p1" has attribute "begin" set to <p1_begin>
    And   p_element "p1" has attribute "end" set to <p1_end>
    And   p_element "p2" has attribute "begin" set to <p2_begin>
    And   p_element "p2" has attribute "end" set to <p2_end>
    Then  application should exit with error OverlappingActiveElementsError

    Examples:
    | r1_origin   | r1_extent  | r2_origin | r2_extent | p1_begin     | p1_end       | p2_begin     | p2_end       |
    | 14.375% 50% | 71.25% 45% | 30% 65%   | 50% 30%   | 12:24:25.860 | 12:26:25.860 | 12:25:25.860 | 12:30:25.860 |


Scenario: 1 active region referenced by many elements the application shall exit with an error.

    Given an xml file <xml_file>
    When  it has region "r1" 
    And   region "r1" has attribute "origin" set to <r1_origin> 
    And   region "r1" has attribute "extent" set to <r1_extent>
    And   it has p_element "p1"
    And   it has p_element "p2"
    And   p_element "p1" has attribute "region" set to "r1"
    And   p_element "p2" has attribute "region" set to "r1"
    And   p_element "p1" has attribute "begin" set to <p1_begin>
    And   p_element "p1" has attribute "end" set to <p1_end>
    And   p_element "p2" has attribute "begin" set to <p2_begin>
    And   p_element "p2" has attribute "end" set to <p2_end>
    Then  application should exit with error OverlappingActiveElementsError

    Examples:
    | r1_origin   | r1_extent  | p1_begin     | p1_end       | p2_begin     | p2_end       |
    | 14.375% 50% | 71.25% 45% | 12:24:25.860 | 12:26:25.860 | 12:25:25.860 | 12:30:25.860 |


Scenario: Regions extending outside the root container region

    Given an xml file <xml_file>
    When  it has region "r1" 
    And   region "r1" has attribute "origin" set to <r1_origin> 
    And   region "r1" has attribute "extent" set to <r1_extent>
    And   it has p_element "p1"
    And   p_element "p1" has attribute "region" set to "r1"
    Then  application should exit with error RegionExtendingOutsideDocumentError

    Examples:
    | r1_origin  | r1_extent  |
    | -1% 50%    | 71.25% 45% |
    | 40% 50%    | 71.25% 45% |
    | 40% -5%    | 71.25% 45% |
    | 40% 29.85% | 71.25% 45% |
    