/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let countZero = ((arr)=>{
        let count = 0;
        for(let i=0;i<arr.length;i++){
            if (arr[i]==0){
                count++;
            }
        }
        return count;
    });
    let zeros = countZero(nums);
    if (zeros > 1){
        return new Array(nums.length).fill(0);
    }
    let ind = null;
    let prod = 1;
    let arr = new Array(nums.length).fill(0);
    for(let i = 0;i<nums.length;i++){
        if(nums[i]==0){
            ind = i;
        }else{
            prod *= nums[i];
        }
    }
    if(ind!=null){
        arr[ind] = prod;
    }else{
        for(let i=0;i<nums.length;i++){
            arr[i] = prod/nums[i];
        }
    }
    return arr;
};
