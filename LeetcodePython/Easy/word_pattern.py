
def wordPattern(pattern: str, s: str) -> bool:
    hashmap = {}
    words = s.split()
    if len(words) != len(pattern):
        return False
    for i in range(len(pattern)):
        if words[i] not in hashmap.values():
            if pattern[i] in hashmap.keys():
                return False
            hashmap[pattern[i]] = words[i]
        if pattern[i] not in hashmap.keys():
            return False
        elif words[i] == hashmap[pattern[i]]:
            continue
        else:
            return False
    return True

wordPattern('abba', 'dog cat cat dog')


