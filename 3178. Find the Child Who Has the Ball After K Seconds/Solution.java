class Solution {
    public int numberOfChild(int n, int k) {
        k = k % (2*(n-1));
        if (k<n){
            return k;
        }
        return (n - k%(n-1))-1;
    }
}
