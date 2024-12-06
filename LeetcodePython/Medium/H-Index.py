#Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
#The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
from typing import List


def hIndex(citations: List[int]) -> int:

    papercount = 0
    sorted(citations, reverse=True)
    for n in citations:
        if n > papercount:
            return n
        papercount+=1



print(hIndex([3,0,6,1,5]))