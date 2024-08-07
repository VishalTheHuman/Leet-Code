class Solution {
    public int maxHeightOfTriangle(int red, int blue) {
        return Math.max(solve(red, blue, true), solve(red, blue, false)); 
    }

    public int solve(int red, int blue, boolean turn){
        for(int i=1;i<1000;i++){
            if (turn){
                if(red>=i){
                    red-=i;
                }else{
                    return i-=1;
                }
            }else{
                if(blue>=i){
                    blue-=i;
                }else{
                    return i-1;
                }
            }
            turn = !turn;
        }
        return 0;
    }
}
