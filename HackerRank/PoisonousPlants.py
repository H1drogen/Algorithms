
# There are a number of plants in a garden. Each of the plants has been treated with some amount of pesticide. After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.
#
# You are given the initial values of the pesticide in each of the plants. Determine the number of days after which no plant dies, i.e. the time after which there is no plant with more pesticide content than the plant to its left.

def poisonousPlants(p):
    x = True
    day = 0
    def check_left_plant(index, array):
        changetag = False
        while index < len(array) - 1:
            if p[index] < p[index + 1]:
                check_left_plant(index + 1, p)
                p.pop(index + 1)
                changetag = True
            index += 1
        return changetag
    while x:
        day += 1
        x = check_left_plant(0, p)
    return day - 1


print(poisonousPlants([6, 5, 8, 4, 7, 10, 9]))
