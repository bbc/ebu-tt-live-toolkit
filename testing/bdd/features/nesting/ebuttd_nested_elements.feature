Feature: Merging nested elements

    Scenario: If a div contains no tt:p elements it is discarded
        Given an xml file <xml_file>
        When the document is generated
        And the EBU-TT-Live document is denested
        And the EBU-TT-Live document is valid
        And the EBU-TT-Live document is converted to EBU-TT-D
        Then EBUTTD document is valid
        And all divs contain at least one p element

        Examples:
            | xml_file                      |
            | nested_elements_hardcoded.xml |

    Scenario: No div should contain any other divs
        Given an xml file <xml_file>
        When the document is generated
        And the EBU-TT-Live document is denested
        And the EBU-TT-Live document is valid
        And the EBU-TT-Live document is converted to EBU-TT-D
        Then EBUTTD document is valid
        And no div contains any other divs

        Examples:
            | xml_file                      |
            | nested_elements_hardcoded.xml |

    Scenario: When the P region matches the div region, remove p region
        Given an xml file <xml_file>
        When it has div_region <div_region>
        And it has p1_region <p1_region>
        And the document is generated
        And the EBU-TT-Live document is denested
        And the EBU-TT-Live document is valid
        And the EBU-TT-Live document is converted to EBU-TT-D
        Then EBUTTD document is valid
        And p elements do not have a region

        Examples:
            | xml_file                      | div_region | p1_region |
            | p_regions_nested_elements.xml | R1         | R1        |

    Scenario: When the P region does not match the div region, remove p
        Given an xml file <xml_file>
        When it has div_region <div_region>
        And it has p1_region <p1_region>
        And it has p2_region <p2_region>
        When the document is generated
        And the EBU-TT-Live document is denested
        And the EBU-TT-Live document is valid
        And the EBU-TT-Live document is converted to EBU-TT-D
        Then EBUTTD document is valid
        And there is one div containing one p

        Examples:
            | xml_file                      | div_region | p1_region | p2_region |
            | p_regions_nested_elements.xml | R1         | R1        | R2        |

    Scenario: No span should contain any other span
        Given an xml file <xml_file>
        When the document is generated
        And the EBU-TT-Live document is denested
        And the EBU-TT-Live document is valid
        And the EBU-TT-Live document is converted to EBU-TT-D
        Then EBUTTD document is valid
        And no span contains any other spans

        Examples:
            | xml_file                   |
            | nested_spans_hardcoded.xml |

    Scenario: Nested spans with styles should create new, combined styles
        Given an xml file <xml_file>
        When the document is generated
        And the EBU-TT-Live document is denested
        And the EBU-TT-Live document is valid
        And the EBU-TT-Live document is converted to EBU-TT-D
        Then EBUTTD document is valid
        And span 1 has style "autogenFontStyle_n_200_n outerinnerYellow"
        And the style "outerinnerYellow" exists
        And span 21 has style "autogenFontStyle_n_12.5_n nestSizingnestSizingnestSizing"
        And the style "nestSizingnestSizingnestSizing" exists

        Examples:
            | xml_file                   |
            | nested_spans_hardcoded.xml |

    Scenario: Nested spans with styles should create new, combined styles that make it to the EBU-TT_D
        Given an xml file <xml_file>
        When the XML is parsed as a valid EBU-TT-1 document
        And the EBU-TT-1 converter is set to use the documentIdentifier as a sequenceIdentifier
        And the EBU-TT-1 converter is set to use a FixedOffsetSMPTEConverter
        And the EBU-TT-1 document is converted to EBU-TT-Live
        And the EBU-TT-Live document is valid
        And the EBU-TT-Live document is denested
        And the EBU-TT-Live document is valid
        And the EBU-TT-Live document is converted to EBU-TT-D
        Then EBUTTD document is valid
        And span 3 has style "S2S6"
        And the style "S2S6" exists

        Examples:
            | xml_file                               |
            | nested_spans_ebuttd_style_creation.xml |

    Scenario: Nested spans with br children should create new spans with br children
        Given an xml file <xml_file>
        When the document is generated
        And the EBU-TT-Live document is denested
        And the EBU-TT-Live document is valid
        And the EBU-TT-Live document is converted to EBU-TT-D
        Then EBUTTD document is valid
        And the second span contains a br

        Examples:
            | xml_file                   |
            | nested_spans_hardcoded.xml |

    Scenario: New styles are not created where the values of the new style match an existing one
        Given an xml file <xml_file>
        When the document is generated
        And the EBU-TT-Live document is denested
        And the EBU-TT-Live document is valid
        And the EBU-TT-Live document is converted to EBU-TT-D
        Then EBUTTD document is valid
        And there is no style named "nestnest"
        And no span references style "nestnest"

        Examples:
            | xml_file                   |
            | nested_spans_hardcoded.xml |

    Scenario: Nested styles with percentage sizes are correctly calculated
        Given an xml file <xml_file>
        When the document is generated
        And the EBU-TT-Live document is denested
        And the EBU-TT-Live document is valid
        And the EBU-TT-Live document is converted to EBU-TT-D
        Then EBUTTD document is valid
        And any span with the style "nestSizing" also has the style "autogenFontStyle_n_50_n"
        And any span with the style "nestSizingnestSizing" also has the style "autogenFontStyle_n_25_n"
        And any span with the style "nestSizingnestSizingnestSizing" also has the style "autogenFontStyle_n_12.5_n"

        Examples:
            | xml_file                   |
            | nested_spans_hardcoded.xml |

    Scenario: p elements with metadata can be denested
        Given an xml file <xml_file>
        When the document is generated
        And the EBU-TT-Live document is denested
        Then the EBU-TT-Live document is valid

        Examples:
            | xml_file                        |
            | nested_p_metadata_hardcoded.xml |
