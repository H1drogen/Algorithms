# It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from to
#
# . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.
#
# Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.


def minimumBribes(q):
    bribes = 0
    index = 0
    for value in q:
        if (value - index) == 2:
            bribes += 1
        if (value - index) == 3:
            bribes += 2
        if (value - index) >= 4:
            return 'Too chaotic'
        index += 1
    return bribes

print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))

