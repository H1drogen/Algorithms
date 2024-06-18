
class Solution(object):
    def groupAnagrams(self, strs):
        test = strs.copy()
        output = []
        for word in strs:
            for test_case in test:
                for letter in word:
                    if letter in test_case and len(word) == len(test_case):
                        pass
                    else:
                        test.remove(test_case)
                        break
            for anagram in test:
                strs.remove(anagram)
            output.append(test)
            test = strs.copy()
        return output


Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])






