func numberOfSubarrays(nums []int, k int) int {
    count := 0 
    store := make(map[int]int)
    if nums[0]%2==1{nums[0] = 1}else {nums[0] = 0}
    store[nums[0]] = 1
    for i:=1;i<len(nums);i++ {
        if nums[i]%2 == 1{
            nums[i] = nums[i-1] + 1
        } else {
            nums[i] = nums[i-1]
        }
        if _, contains := store[nums[i]]; contains{
            store[nums[i]] += 1
        } else {
            store[nums[i]] = 1
        }
        if val,contains := store[nums[i]-k]; contains{
            count += val
        }
    }
    if val, contains := store[k]; contains {
        count += val
    }
    return count
}
