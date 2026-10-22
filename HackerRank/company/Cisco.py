
def groupDivision(levels, maxSpread):
    levels.sort()
    groups = []
    for i in range(len(levels)):
        if i == 0:
            groups.append([levels[i]])
        else:
            if levels[i] - groups[-1][0] <= maxSpread:
                groups[-1].append(levels[i])
            else:
                groups.append([levels[i]])
    return len(groups)


groupDivision([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)