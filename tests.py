def test(arr):
    positive = 0
    negative = 0
    zero = 0
    for x in arr:
        if x > 0:
            positive += 1
        elif x < 0:
            negative += 1
        else:
            zero += 1

