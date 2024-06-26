func numberOfSubarrays(nums []int, k int) int {
    count := 0 
    store := make(map[int]int)
    if nums[0] % 2 == 1 {
        nums[0] = 1
    } else {
        nums[0] = 0
    }
    store[nums[0]] = 1
    keys := []int{nums[0]}
    for i:=1;i<len(nums);i++ {
        if nums[i]%2==1{
            nums[i] = nums[i-1] + 1
        } else {
            nums[i] = nums[i-1]
        }
        if _, contains := store[nums[i]]; contains{
            store[nums[i]] += 1
        } else {
            store[nums[i]] = 1
            keys = append(keys,nums[i])
        }
    }
    for i:=0;i<len(keys);i++{
        for j:=i+1;j<len(keys);j++{
            if keys[j] - keys[i] == k {
                count += store[keys[j]]*store[keys[i]]
            }
        }
    }
    
    if val,contains := store[k];contains {
        count += val
    }
    return count
}
