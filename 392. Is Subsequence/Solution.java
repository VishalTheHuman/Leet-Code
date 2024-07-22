class Solution {
    public boolean isSubsequence(String s, String t) {
        int ptr = 0;
        for(int i=0;i<t.length();i++){
            if(ptr==s.length()) break;
            if(s.charAt(ptr)==t.charAt(i)) ptr++;
        }
        return ptr == s.length();
    }
}
