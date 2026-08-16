# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence(s: str, t: str) -> bool:
    for char in s:
        for char2 in t:
            if char == char2:
                break
            else:
                continue
        if char != char2:
            return False
    return True

# Example usage:
print(isSubsequence("abc", "ahbgdc"))  # Outputs: True
print(isSubsequence("axc", "ahbgdc"))  # Outputs: False