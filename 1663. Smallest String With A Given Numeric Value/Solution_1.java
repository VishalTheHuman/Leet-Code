class Solution {
    public String getSmallestString(int n, int k) {
        char[] result = new char[n];
        for(int i=0;i<n;i++){
            result[i] = 'a';
            k--;
        }
        if(k>0){
            for(int i=n-1;i>=0 && k>0;i--){
                result[i] = (char) ('a'+Math.min(k,25));
                k-=25;
            }
        }
        return String.valueOf(result);
    }
}
