# There is a given list of strings where each string contains only lowercase letters from a - j, inclusive. The set of strings is said to be a GOOD SET if no string is a prefix of another string. In this case, print GOOD SET. Otherwise, print BAD SET on the first line followed by the string being checked.

def noPrefix(words):
    words = sorted(words)
    for i in range(len(words)):
        if words[i] in words[i+1]:
            print('BAD SET')
            print(words[i])
            return
    print('GOOD SET')

#TRICK: The key trick is a trie: while adding each word, detect whether an earlier word ends along its path (the earlier word is a prefix), or whether the current word ends at a trie node that already has children (the current word is a prefix of an earlier one).

def noPrefix(words):
    end = None
    trie = {}

    for word in words:
        node = trie

        for char in word:
            if end in node:  # An earlier word is a prefix of this word
                print('BAD SET')
                print(word)
                return
            node = node.setdefault(char, {})

        if end in node or node:  # Duplicate, or this word prefixes an earlier one
            print('BAD SET')
            print(word)
            return

        node[end] = True

    print('GOOD SET')

# aab was already in the set, and it’s a prefix of aabcde. The original code sorts the words, which can change which word is reported as the first violation, and words[i+1] goes out of bounds on the last iteration. The trie checks words in input order and runs in O(total number of characters).


noPrefix(['aab', 'defgab', 'abcde', 'aabcde'])