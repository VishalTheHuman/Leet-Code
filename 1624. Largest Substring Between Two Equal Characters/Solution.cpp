class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int max_len = -1;
        int i = 0;
        while (i < s.length()){
            int j = s.length()-1;
            while (j>i){
                if (s[i]==s[j]){
                    int val = j-i-1;
                    if (max_len <val){
                        max_len = val;
                    }
                }
                j--;
            }
            i++;
        }
        return max_len;
    }
};
