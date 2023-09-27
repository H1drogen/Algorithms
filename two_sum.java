class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(i=0; i < nums.length; i++) {
            for(k=0; k < nums.length - 1; k++) {
                if (nums[i] + nums[k+1] = target) {
                    return int[] [i,k+1]
                }
            }
        }
    }
}