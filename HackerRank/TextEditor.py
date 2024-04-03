from unittest.mock import patch
import sys
from io import StringIO

def textEditor(sampleinput):
    sys.stdin = StringIO(sampleinput)

    S = ''
    for i in range(int(input())):
        operation = input().split()
        if operation[0] == '1':
            S += operation[1]
        elif operation[0] == '2':
            final_index = len(S) - int(operation[1])
            S = S[0:final_index]
        elif operation[0] == '3':
            print(S[int(operation[1]) - 1])
        elif operation[0] == '4':
            continue



textEditor('8\n1 abc\n3 3\n2 3\n1 xy\n3 2\n4\n4\n3 1')

# reading operation indices returns strings, not ints!
# -1 to reading position-based characters on strings after collecting the 'nth letter'




