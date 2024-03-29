class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        int max_release = releaseTimes[0];
        char max_time_char = keysPressed[0];
        for(int i=1;i<keysPressed.length();i++){
            int val = releaseTimes[i] - releaseTimes[i-1];
            if (max_release < val || (max_time_char < keysPressed[i] && max_release == val)){
                max_release = val;
                max_time_char = keysPressed[i];
            }
        }
        return max_time_char;
    }
};
