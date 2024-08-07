class Solution {
    public int[][] generateMatrix(int n) {
        int[][] result = new int[n][n];
        int topLeft = 0, topRight=n, bottomRight=n, bottomLeft = -1; 
        int i = 0, j = 0;
        int value = 1;
        while(value <= n*n){
            while(j<topRight){
                result[i][j] = value;
                value++;
                j++;
            }
            topRight--;
            j--;
            i++;
            while(i<bottomRight){
                result[i][j] = value;
                value++;
                i++;
            }
            bottomRight--;
            i--;
            j--;
            while(j>bottomLeft){
                result[i][j] = value;
                value++;
                j--;
            }
            bottomLeft++;
            j++;
            i--;
            while(i>topLeft){
                result[i][j]= value;
                value++;
                i--;
            }
            topLeft++;
            i++;
            j++;
        }
        return result;
    }
}
