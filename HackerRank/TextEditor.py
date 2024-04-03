from unittest.mock import patch
import sys
from io import StringIO

def textEditor(sampleinput):
    sys.stdin = StringIO(sampleinput)
    line = input()
    line2 = input()
    print(line)
    print(line2)

textEditor('8\n1 abc\n3 3\n2 3\n1 xy\n3 2\n4\n4\n3 1')




