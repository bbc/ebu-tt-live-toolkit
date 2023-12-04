"""Process the UAX24 scripts at https://www.unicode.org/Public/UCD/latest/ucd/Scripts.txt
to generate a Python equivalent.

For example a command like:
python ebu_tt_live/gen_uax24.py -scriptFile uax24scripts.txt -outFile ebu_tt_live/uax24.py

will generate a Python file that specifies script lists that can be queried.
"""

import argparse
import sys
from csv import reader

LIST_SUFFIX='_list'
TRIPLE_QUOTE='"""'
SCRIPTS_TO_LIST={
    'Common': [],
    'Latin': [],
    'Greek': [],
    'Cyrillic': [],
    'Hebrew': [],
    'Han': [],
    'Katakana': [],
    'Hiragana': [],
    'Bopomofo': [],
    'Hangul': [],
}

# https://stackoverflow.com/questions/14158868/python-skip-comment-lines-marked-with-in-csv-dictreader
def decomment(csvfile):
    for row in csvfile:
        raw = row.split('#')[0].strip()
        if raw: yield raw

def writeComments(outFile):
    outFile.write(TRIPLE_QUOTE)
    outFile.write(
        'Utility for discovering which UAX24 script a given character code is in,\n'
        'useful for example in computing the copy or render times in the IMSC-HRM.\n'
        '\n'
        'Auto-generated from UAX24 Scripts.txt using gen_uax24.py\n')
    outFile.write(TRIPLE_QUOTE)
    outFile.write('\n')
    return

def writeFuncs(outFile):
    outFile.write(
        'def lr(a, b):\n'
        '    return list(range(a, b + 1))\n'
        '\n')
    return

def genLists(csv_reader):
    for row in csv_reader:
        scr = row[1].strip().split(' ', maxsplit=1)[0]
        if scr in SCRIPTS_TO_LIST:
            SCRIPTS_TO_LIST[scr].append(row[0].strip())
    return

def charOrRange(char_code: str) -> str:
    range_indicator = char_code.find('..')
    if range_indicator != -1:
        return '*lr(0x{}, 0x{})'.format(
            char_code[0:range_indicator],
            char_code[range_indicator+2:]  # assume already stripped of trailing spaces
        )
    else:
        return '0x{}'.format(char_code)

def writeLists(outFile):
    for script, char_codes in SCRIPTS_TO_LIST.items():
        outFile.write('\n{}{} = [\n'.format(script, LIST_SUFFIX))
        for char_code in char_codes:
            outFile.write('    {},\n'.format(
                charOrRange(char_code)
            ))
        outFile.write(']\n')
    return

def generateUax24(args) -> int:
    csv_reader = reader(decomment(args.scriptFile), delimiter=';', skipinitialspace=True)
    outFile = args.outFile
    writeComments(outFile)
    writeFuncs(outFile)
    genLists(csv_reader)
    writeLists(outFile)

    return 1

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-scriptFile',
        type=argparse.FileType('rt'),
        required=True,
        help='UAX24 Scripts file',
        action='store')

    parser.add_argument(
        '-outFile',
        type=argparse.FileType('wt'),
        default=sys.stdout,
        nargs='?',
        help='Location to write the python file representing the scripts',
        action='store')

    parser.set_defaults(func=generateUax24)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    # execute only if run as a script
    main()
