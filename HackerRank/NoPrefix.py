
def noPrefix(words):
    words = sorted(words)
    for i in range(len(words)):
        if words[i] in words[i+1]:
            print('BAD SET')
            print(words[i])
            return
    print('GOOD SET')



noPrefix(['aab', 'defgab', 'abcde', 'aabcde'])