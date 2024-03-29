/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
    dt = {}
    nums.forEach(num=>{
        dt[num] = (dt[num] | 0) + 1;
    })
    let max_val = Math.max(...Object.values(dt));
    let count = 0;
    for(let key in dt){
        if(dt[key] == max_val){
            count += dt[key];
        }
    }
    return count;
};
