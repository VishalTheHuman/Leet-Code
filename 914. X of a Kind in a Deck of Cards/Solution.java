class Solution {
    public int gcd(int a,int b){
        if (a < b){
            int temp = a;
            a = b;
            b = temp;
        }
        if (b==0 || a==b){
            return a;
        }
        return gcd(b,a%b);
    }

    public boolean hasGroupsSizeX(int[] deck) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int x : deck){
            map.put(x,map.getOrDefault(x,0)+1);
        }
        
        int gcdVal = -1;
        
        for(int x : map.values()){
            if (gcdVal==-1){
                gcdVal = x;
            }else{
                gcdVal = gcd(gcdVal, x);
            }
        }

        return gcdVal<=1 ? false : true;
    }
}
