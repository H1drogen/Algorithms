
def solution(S: str):
    # heapq.heapify(S)

    final_string = ''
    for letter in S:
        final_string += letter
        if len(final_string) <= 1:
            continue
        while final_string[-1] == final_string[-2]:
            final_string = final_string[:-2]
            if len(final_string) <= 1:
                break
    return final_string

solution("ACCAABBC")