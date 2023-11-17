@validation
Feature: Check that imsc-hrm-tests pass and fail correctly

    Scenario: imsc-hrm-tests fail tests fail
        Given an xml file <xml_file>
        When the xml file is parsed as a valid EBU-TT-D document
        Then the EBU-TT-D document is not valid wrt the IMSC HRM

        Examples:
            | xml_file                              |
            | imsc-hrm-tests/fail/dur001-fail.ttml  |
            | imsc-hrm-tests/fail/dur002-fail.ttml  |
            | imsc-hrm-tests/fail/dur003-fail.ttml  |
            | imsc-hrm-tests/fail/dur004-fail.ttml  |
            | imsc-hrm-tests/fail/dur005-fail.ttml  |
            | imsc-hrm-tests/fail/dur006-fail.ttml  |
            | imsc-hrm-tests/fail/dur007-fail.ttml  |
            | imsc-hrm-tests/fail/dur008-fail.ttml  |
            | imsc-hrm-tests/fail/dur009-fail.ttml  |
            | imsc-hrm-tests/fail/dur010-fail.ttml  |
            | imsc-hrm-tests/fail/dur011-fail.ttml  |
            # | imsc-hrm-tests/fail/dur012-fail.ttml  | textOutline not permitted in EBU-TT-D
            # | imsc-hrm-tests/fail/dur013-fail.ttml  | textShadow not permitted in EBU-TT-D
            | imsc-hrm-tests/fail/dur014-fail.ttml  |
            | imsc-hrm-tests/fail/ipd001-fail.ttml  |
            | imsc-hrm-tests/fail/ipd002-fail.ttml  |
            | imsc-hrm-tests/fail/ipd003-fail.ttml  |
            | imsc-hrm-tests/fail/ipd004-fail.ttml  |
            | imsc-hrm-tests/fail/ipd005-fail.ttml  |
            | imsc-hrm-tests/fail/ipd006-fail.ttml  |
            | imsc-hrm-tests/fail/ngbs001-fail.ttml |
            | imsc-hrm-tests/fail/ngbs002-fail.ttml |

    Scenario: imsc-hrm-tests pass tests pass
        Given an xml file <xml_file>
        When the xml file is parsed as a valid EBU-TT-D document
        Then the EBU-TT-D document is valid wrt the IMSC HRM

        Examples:
            | xml_file                              |
            | imsc-hrm-tests/pass/dur001-pass.ttml  |
            | imsc-hrm-tests/pass/dur002-pass.ttml  |
            | imsc-hrm-tests/pass/dur003-pass.ttml  |
            | imsc-hrm-tests/pass/dur004-pass.ttml  |
            | imsc-hrm-tests/pass/dur005-pass.ttml  |
            | imsc-hrm-tests/pass/dur006-pass.ttml  |
            | imsc-hrm-tests/pass/dur007-pass.ttml  |
            | imsc-hrm-tests/pass/dur008-pass.ttml  |
            | imsc-hrm-tests/pass/dur009-pass.ttml  |
            | imsc-hrm-tests/pass/dur010-pass.ttml  |
            | imsc-hrm-tests/pass/dur011-pass.ttml  |
            # | imsc-hrm-tests/pass/dur012-pass.ttml  | textOutline not permitted in EBU-TT-D
            # | imsc-hrm-tests/pass/dur013-pass.ttml  | textShadow not permitted in EBU-TT-D
            | imsc-hrm-tests/pass/dur014-pass.ttml  |
            | imsc-hrm-tests/pass/dur015-pass.ttml  |
            | imsc-hrm-tests/pass/dur016-pass.ttml  |
            | imsc-hrm-tests/pass/ipd001-pass.ttml  |
            | imsc-hrm-tests/pass/ipd002-pass.ttml  |
            | imsc-hrm-tests/pass/ipd003-pass.ttml  |
            | imsc-hrm-tests/pass/ipd004-pass.ttml  |
            | imsc-hrm-tests/pass/ipd005-pass.ttml  |
            | imsc-hrm-tests/pass/ipd006-pass.ttml  |
            | imsc-hrm-tests/pass/ngbs001-pass.ttml |
            | imsc-hrm-tests/pass/ngbs002-pass.ttml |
