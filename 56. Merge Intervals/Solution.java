class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (x,y) -> Integer.compare(x[0], y[0]));
        List<int[]> result = new ArrayList<>();
        result.add(intervals[0]);
        for(int i=1;i<intervals.length;i++){
            int[] temp = result.get(result.size()-1);
            if(intervals[i][0]<=temp[1]){
                temp[1] = Math.max(temp[1], intervals[i][1]);
                result.set(result.size()-1,temp);
            }else{
                result.add(intervals[i]);
            }
        }
        return result.toArray(new int[result.size()][2]);
    }
}
