
def solution(N: int):
    binary_array = []
    called = 0
    counter = 0
    max_count = 0
    while N != 0:
        binary_array.append(int(N % 2))
        N /= 2
        N = int(N)
    for digit in binary_array:
        if digit == 0 and called == 0:
            continue
        if digit == 1:
            called += 1
            if counter > max_count:
                max_count = counter
            counter = 0
        if digit == 0:
            counter += 1
            continue
    if called == 1:
        return 0
    else:
        return max_count


solution(1041)