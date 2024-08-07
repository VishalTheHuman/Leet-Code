class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int sum = Math.min(numOnes,k);
        k -= sum;
        if (k > 0){
            k -= Math.min(numZeros,k);
        }
        if (k > 0){
            sum -= k;
        }
        return sum;
    }
}
