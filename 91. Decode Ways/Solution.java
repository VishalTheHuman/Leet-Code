class Solution {
    public int numDecodings(String s) {
        int[] dp = new int[s.length()+1];
        dp[0] = 1;
        for(int i=0;i<s.length();i++){
            if (s.charAt(i)=='0'){
                if(i>0 && (s.charAt(i-1)=='1' || s.charAt(i-1)=='2')){
                    dp[i+1] = dp[i-1];
                }else{
                    return 0;
                }
            }else{
                dp[i+1] = dp[i];
                if(i>0){
                    if (s.charAt(i-1)=='1' || (s.charAt(i-1)=='2' && s.charAt(i)<='6')){
                        dp[i+1] = dp[i] + dp[i-1];
                    }
                }
            }
        }
        return dp[s.length()];
    }
}
