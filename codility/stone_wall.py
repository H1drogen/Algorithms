from Tools.scripts.findlinksto import visit


def solution(H):
    count = 0
    base = H[0]
    visited_heights = []
    for height in H:
        if height < base:
            base = height
            visited_heights = [height]
            count += 1
        if height not in visited_heights:
            count += 1
            visited_heights.append(height)
    return count

solution([8,8,5,7,9,8,7,4,8])