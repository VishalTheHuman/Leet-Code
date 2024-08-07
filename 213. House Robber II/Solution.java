class Solution {
    public int rob(int[] nums) {
        if (nums.length==1){
            return nums[0];
        }
        int s1=0, s2=0;
        for(int i=0;i<nums.length-1;i++){
            int temp = Math.max(nums[i] + s1, s2);
            s1 = s2;
            s2 = temp;
        }
        int rob1 = s2;
        s1 = 0; s2 = 0;
        for(int i=1;i<nums.length;i++){
            int temp = Math.max(nums[i] + s1, s2);
            s1 = s2;
            s2 = temp;
        }
        return Math.max(rob1,s2);
    }
}
