
def solution(A, B, q):
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0
    for patient_number in range(len(A)):
        if A[patient_number] == B[patient_number]:
            if A[patient_number] == 1:
                true_positives += 1
            else:
                true_negatives += 1
        else:
            if B[patient_number] == 1:
                false_positives += 1
            else:
                false_negatives += 1
    if q:
        specificity = true_negatives / (true_negatives + false_positives)
        return specificity
    else:
        sensitivity = true_positives / (true_positives + false_negatives)
        return sensitivity

solution([1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 0, 1], False)