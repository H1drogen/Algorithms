def solution(A):
    count = 0
    square = 0
    dice_roll = 1
    numbers_left = []
    while dice_roll < 7:
        if A[square] >= 0:
            square += dice_roll
            count += A[square]
        else:
            dice_roll += 1
            numbers_left.append(A[square])




