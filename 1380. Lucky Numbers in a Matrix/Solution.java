class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        int[] rows = new int[matrix.length]; 
        int[] cols = new int[matrix[0].length];
        for(int i=0;i<rows.length;i++){
            rows[i] = Integer.MAX_VALUE;
        }
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                if(matrix[i][j]<rows[i]){
                    rows[i] = matrix[i][j];
                }
                if(matrix[i][j]>cols[j]){
                    cols[j] = matrix[i][j];
                }
            }
        }
        List<Integer> result = new ArrayList<>();
        for(int i=0;i<rows.length;i++){
            for(int j=0;j<cols.length;j++){
                if(rows[i]==cols[j]){
                    result.add(rows[i]);
                }
            }
        }
        return result;
    }
}
