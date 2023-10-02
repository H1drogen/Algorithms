#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x: int):
        if 10 > x > 0:
            return True
        if x > 10:
            mockx = x
            reversed = 0
            while int(mockx) != 0:
                last_digit = int(mockx) % 10

                reversed = (reversed * 10) + last_digit
                mockx /= 10
        return bool(reversed == x)






