#!/usr/bin/env python
"""reducer.py"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    word_count =[]
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            word_count.append((current_word,total_count))
        except ValueError:
            pass

    sorted_word_count = sorted(word_count, key=itemgetter(1), reverse=True)

    for word, count in sorted_word_count[:3]:
        print("%s%s%d" %(word,separator, count))

if __name__ == "__main__":
    main()
