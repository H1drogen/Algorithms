namespace DefaultNamespace;

// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

// Each row must contain the digits 1-9 without repetition.
// Each column must contain the digits 1-9 without repetition.
// Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.


public class ValidSudoku
{
    public bool IsValidSudoku(char[][] board)
    {
        HashSet<char> top_box = new HashSet<char>();
        HashSet<char> middle_box = new HashSet<char>();
        HashSet<char> lower_box = new HashSet<char>();
        for (int i = 0; i < 9; i++)
        {
            char[] rows = board[i];
            HashSet<char> set = new HashSet<char>();
            foreach (char number in rows)
            {
                if (set.Add(number) == false && number != '.')
                {
                    return false;
                }
            }
            set.Clear();
            for (int j = 0; j < 9; j++)
            {
                char column = board[j][i];
                if (set.Add(column) == false && column != '.')
                {
                    return false;
                }
                if (j > 0 && j < 3)
                {
                    if (top_box.Add(column) == false && column != '.')
                    {
                        return false;
                    }
                    if ((i + 1) % 3 == 0 && j == 2)
                    {
                        top_box.Clear();
                    }
                }
                if (j > 3 && j < 6)
                {
                    if (middle_box.Add(column) == false && column != '.')
                    {
                        return false;
                    }
                    if ((i + 1) % 3 == 0 && j == 5)
                    {
                        middle_box.Clear();
                    }
                }
                if (j > 6 && j < 9)
                {
                    if (lower_box.Add(column) == false && column != '.')
                    {
                        return false;
                    }
                    if ((i + 1) % 3 == 0 && j == 8)
                    {
                        lower_box.Clear();
                    }
                }
            }
            set.Clear();
        }
        return true;
    }
}