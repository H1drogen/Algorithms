

def Solution(S, P, Q):
    ans = []
    for i in range(len(P)):
        splice = S[P[i]:Q[i]]
        if splice == '':
            splice = S[P[i]]
        if min(splice) == 'A':
            ans.append(1)
        elif min(splice) == 'C':
            ans.append(2)
        elif min(splice) == 'G':
            ans.append(3)
        else:
            ans.append(4)
    return ans


Solution('CAGCCTA', [2,5,0],[4,5,6])
