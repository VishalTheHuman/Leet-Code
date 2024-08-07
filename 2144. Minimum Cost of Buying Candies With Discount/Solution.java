class Solution {
    public int minimumCost(int[] cost) {
        Arrays.sort(cost);
        int i = cost.length-1, spent =0;
        while (i - 2 >=0){
            spent += cost[i] + cost[i-1];
            i-=3;
        }
        while (i>=0){
            spent += cost[i];
            i--;
        }
        return spent;
    }
}
