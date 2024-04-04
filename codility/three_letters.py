
def solution(A, B):
    string = ''
    while A > B:
        if A != 0:
            string += 'aa'
            A -= 2
        if B != 0:
            string += 'b'
            B -= 1
    while B > A:
        if B != 0:
            string += 'bb'
            B -= 2
        if A != 0:
            string += 'a'
            A -= 1
    while (A + B != 0):
        string += 'ba'
        A -= 1
        B -= 1

    return string


solution(20,36)
