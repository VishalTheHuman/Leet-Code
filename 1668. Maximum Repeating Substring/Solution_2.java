class Solution {
    public int maxRepeating(String sequence, String word) {
        int maxCount = 0;
        String compare = word;
        while(sequence.contains(compare)){
            maxCount++;
            compare+=word;
        }
        return maxCount;
    }
}
