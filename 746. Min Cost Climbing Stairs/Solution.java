class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] store = new int[cost.length+1];
        store[1] = cost[0];
        for(int i=2;i<store.length;i++){
            store[i] = Math.min(store[i-1],store[i-2]) + cost[i-1];
        }
        return Math.min(store[store.length-1], store[store.length-2]);
    }
}
