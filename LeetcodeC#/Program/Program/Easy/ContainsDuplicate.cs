namespace DefaultNamespace;

// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

public class ContainsDuplicate
{
    public bool Solution(int[] nums)
    {
        HashSet<int> set = new HashSet<int>(nums);
        if (set.Count == nums.Length)
        {
            return false;
        }
        else
        {
            return true;
        }
    }

// there is a small optimization you can make.
// You can return false as soon as you find a duplicate while adding elements to the set

    public bool EfficientSolution(int[] nums)
    {
        HashSet<int> set = new HashSet<int>();
        foreach (var num in nums)
        {
            if (!set.Add(num))
            {
                return true;
            }
        }
        return false;
    }
}



