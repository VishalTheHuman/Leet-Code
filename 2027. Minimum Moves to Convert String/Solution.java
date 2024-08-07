class Solution {
    public int minimumMoves(String s) {
        int change = 0;
        int moves = 0;
        for (char x : s.toCharArray()){
            if (x=='X'){
                if (change == 0){
                    moves++;
                    change = 3;
                }
            }
            if (change>0){
                change--;
            }
        }
        return moves;
    }
}
