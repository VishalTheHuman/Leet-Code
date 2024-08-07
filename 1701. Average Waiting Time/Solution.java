class Solution {
    public double averageWaitingTime(int[][] customers) {
        double currentTime = 0;
        double waitTime = 0;
        for(int i=0;i<customers.length;i++){
            if (currentTime > customers[i][0]){
                waitTime += (currentTime - customers[i][0]);
            }else{
                currentTime = customers[i][0];
            }
            currentTime += customers[i][1];
            waitTime += customers[i][1];
        }
        return waitTime/customers.length;
    }
}
