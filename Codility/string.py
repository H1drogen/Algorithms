import heapq


def solution(S: str):
    heapq.heapify(S)

    
    # for count, letter in enumerate(S):
    #     if letter[count] == letter:
    #         final_string.pop()
    #     else:
    #         final_string.append(letter)
    # return str(final_string)

solution("ACCAABBC")