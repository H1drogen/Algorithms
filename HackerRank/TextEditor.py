from unittest.mock import patch
import sys
from io import StringIO

def textEditor(sampleinput):
    sys.stdin = StringIO(sampleinput)

    cache = []
    S = ''
    for i in range(int(input())):
        cache.append(S)
        operator = input().split()
        if operator[0] == '1':
            S += operator[1]
        elif operator[0] == '2':
            final_index = len(S) - int(operator[1])
            S = S[0:final_index]
        elif operator[0] == '3':
            print(S[int(operator[1]) - 1])
        elif operator[0] == '4':
            while cache[-1] == cache[-2]:
                cache.pop()
            cache.pop()
            S = cache[-1]



textEditor('8\n1 abc\n3 3\n2 3\n1 xy\n3 2\n4\n4\n3 1')

# reading operation indices returns strings, not ints!
# -1 to reading position-based characters on strings after collecting the 'nth letter'




