#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        if 10 > x > 0:
            return True
        if x > 10:
            while x != 0:
                last_digit = x % 10
                reversed = (reversed * 10) + last_digit
                x /= 10
            if reversed == x:
                return True
        else:
            return False






