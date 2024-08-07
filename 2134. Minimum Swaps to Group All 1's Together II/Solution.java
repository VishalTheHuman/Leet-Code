class Solution {
    public int minSwaps(int[] nums) {
        int windowSize = 0;
        for(int i=0;i<nums.length;i++){
            windowSize += nums[i];
        }
        int ones = 0;
        for(int i=0;i<windowSize;i++){
            ones += nums[i];
        }
        int swaps = windowSize - ones;
        for(int i=0;i<nums.length;i++){
            ones -= nums[i];
            ones += nums[(i+windowSize)%nums.length];
            swaps = Math.min(swaps, windowSize - ones);
        }
        return swaps;
    }
}
