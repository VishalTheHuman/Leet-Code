class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
        Arrays.sort(nums);
        for(int i=1;i<nums.length;i++){
            nums[i] += nums[i-1];
        }
        for(int i=0;i<queries.length;i++){
            queries[i] = search(nums, queries[i]);
        }
        return queries;
    }

    public int search(int[] arr, int value){
        int start = 0, end = arr.length, idx = 0;
        int mid = (start + end)/2;
        while(mid < arr.length && start <= end){
            if (arr[mid]==value){
                return mid+1;
            }else if(arr[mid] > value){
                end = mid-1;
            }else{
                idx = Math.max(idx, mid+1);
                start = mid+1;
            }
            mid = (start+end)/2;
        }
        return idx;
    }
}
