package leetcode.easy;

public class two_sum {
    public int[] twoSum(int[] nums, int target) {
        for (int i=0; i < nums.length; i++) {
            for(int k=0; k < nums.length - 1; k++) {
                if (nums[i] + nums[k+1] == target) {
                    return new int[]{i,k+1};
                }
            }
        }


        return nums;
    }
}

