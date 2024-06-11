namespace DefaultNamespace;

public class ValidPalindrome
{
    // A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    // TODO Given a string s, return true if it is a palindrome, or false otherwise.
    public bool IsPalindrome(string s)
    {
        int start_pointer = 0;
        int end_pointer = s.Length - 1;
        while (start_pointer < end_pointer)
        {
            while (!char.IsLetterOrDigit(s[start_pointer]) && start_pointer < end_pointer)
            {
                start_pointer++;
            }

            while (!char.IsLetterOrDigit(s[end_pointer]) && start_pointer < end_pointer)
            {
                end_pointer--;
            }

            if (char.ToLower(s[start_pointer]) != char.ToLower(s[end_pointer]))
            {
                return false;
            }

            start_pointer++;
            end_pointer--;
        }
        return true;
    }
}

// code can be made more readable by using if statements and continues (instead of while loops to check letter/digit)