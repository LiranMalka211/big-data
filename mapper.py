#!/usr/bin/env python
"""mapper.py"""

import sys
import re
def read_input(file):
    seperator = r'[,.\ ]+'
    for line in file:
        # split the line into words
        list = re.split(seperator, line.strip())
        yield [word.lower() for word in list if word]

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            print ('%s%s%d' % (word, separator, 1))

if __name__ == "__main__":
    main()
