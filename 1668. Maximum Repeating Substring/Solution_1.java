class Solution {
    public int maxRepeating(String sequence, String word) {
        int n = sequence.length();
        int m = word.length();
        int[] dp = new int[n+1];
        for(int i=m;i<n+1;i++){
            if(sequence.substring(i-m,i).equals(word)){
                dp[i] = dp[i-m] + 1;
            }
        }
        int maxTimes = 0;
        for(int i=0;i<dp.length;i++){
            if (dp[i] > maxTimes){
                maxTimes = dp[i];
            }
        }
        return maxTimes;
    }
}
