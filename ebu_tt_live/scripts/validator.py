"""
Validates an EBU-TT or EBU-TT-D file.

The ``validator`` script validates the specified input file as either an
EBU-TT Part 1, Part 3 or EBU-TT-D file, reporting the first error that is
found, or that everything is fine, if no errors are found. If the format
is not specified, the default is EBU-TT-D.

Basic usage:
------------

  ::

    validator -i [input-file] -f [1|3|D] [--hrm]
"""

from ebu_tt_live.documents import EBUTTDDocument, \
                                  EBUTT1Document, \
                                  EBUTT3Document
from imsc_hrm_validator import imscHrmValidator, log as hrm_log
import argparse
import os
import logging

log = logging.getLogger()

type_lookup = {
    '1': EBUTT1Document,
    '3': EBUTT3Document,
    'D': EBUTTDDocument,
}


def main():
    parser = argparse.ArgumentParser(description='Validate a local file')
    parser.add_argument('--input', '-i', type=str, metavar='FILE',
                        help='Input file in desired format', required=True)
    parser.add_argument('--format', '-f', 
                        choices=['1', '3', 'D'],
                        default='D', type=str,
                        metavar='FORMAT',
                        help='Format desired: 1 for EBU-TT Part 1, 3 for Part'
                        ' 3, D for EBU-TT-D')
    parser.add_argument('--hrm',
                        action='store_true',
                        required=False,
                        help='Also validate with the IMSC HRM (EBU-TT-D only)')
    parser.add_argument('--verbose', '-v',
                        action='store_true',
                        required=False,
                        help='Output verbose logging details.')
    args = parser.parse_args()

    in_file = args.input
    format = args.format

    if args.verbose:
        hrm_validator_log = logging.getLogger('imsc_hrm_validator')
        hrm_validator_log.setLevel(logging.DEBUG)
        hrm_log.setLevel(logging.DEBUG)
        log.setLevel(logging.DEBUG)
        log.debug('Verbose logging enabled')

    with open(os.path.join(os.getcwd(), os.path.expanduser(in_file)),
              'r') as f:
        in_data = f.read()

    file_type = type_lookup[format]
    document = file_type.create_from_xml(in_data)
    document.validate()

    valid = True
    if format == 'D' and args.hrm:
        hrmValidator = imscHrmValidator()
        valid = hrmValidator.validate(document)

    if valid:
        print('Everything seems fine')
    else:
        print('Validation errors encountered. Document is not valid.')


if __name__ == '__main__':
    main()
