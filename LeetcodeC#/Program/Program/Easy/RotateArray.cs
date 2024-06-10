using System.Runtime.InteropServices;

namespace DefaultNamespace;

// Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

public class RotateArray {
    public void Rotate(int[] nums, int k)
    {
        int replacee = nums[0];
        for (var i = 0; i < nums.Length; i++)
        {
            int index = (i + k) % nums.Length;
            int replaced = nums[index];
            nums[index] = replacee;
            replacee = replaced;
        }
    }
}
