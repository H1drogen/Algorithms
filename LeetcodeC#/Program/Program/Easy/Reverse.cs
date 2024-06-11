namespace DefaultNamespace;

public class Reverse
{
    public void ReverseString(char[] s) {
        for (int i = 0; i < s.Length / 2; i++)
        {
            char temp = s[i];
            s[i] = s[s.Length - 1 - i];
            s[s.Length - 1 - i] = temp;
        }
    }
// use Array.Reverse(s); or swap via deconstruction below:
// for (int i = 0; i < s.Length / 2; i++)
// {
//     (s[i], s[s.Length - 1 - i]) = (s[s.Length - 1 - i], s[i]);
// }

    
    public int ReverseInteger(int x)
    {
        long reversed = 0;
        while (Math.Abs((long) x) > 0)
        {
            reversed *= 10;
            reversed += x % 10;
            x = x / 10;
        }

        if (reversed > int.MaxValue || reversed < int.MinValue)
        {
            return 0;
        }

        return (int) reversed;
    }
    // converted to long because int.MinValue is 1 less than int.Max Value
}