from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    citations.sort()
    total_papers = len(citations)
    for i in range(0, total_papers):
        if(citations[i] >= total_papers - i):
            h = total_papers - i
            return h
    return 0 # only the case if all papers have no citations


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
