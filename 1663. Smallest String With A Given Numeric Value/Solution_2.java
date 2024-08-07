class Solution {
    public String getSmallestString(int n, int k) {
        StringBuilder result = new StringBuilder();
        while(n>1){
            for(int i=0;i<26;i++){
                if (((double)(k-i-1)/(n-1))<=26){
                    result.append((char)('a'+i));
                    k = k - i - 1;
                    break;
                }
            }
            n--;            
        }
        result.append((char)('a' + k - 1));
        return result.toString();
    }
}
