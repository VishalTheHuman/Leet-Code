func partitionLabels(s string) []int {
    if len(s) == 1{
        return []int{1}
    }else if s[0] == s[len(s)-1]{
        return []int{len(s)}
    }
    start := make(map[rune]int)
    last := make(map[rune]int)
    for idx, val := range(s) {
        if _,present := start[val]; !present{
            start[val] = idx
        }
        last[val] = idx
    }
    result := []int{}
    length := 0
    partition := 0
    for _,val := range(s){
        pos_start,_ := start[val]
        if pos_start <= partition{
            length += 1
            if pos_end, _ := last[val]; pos_end > partition{
                partition = pos_end
            }
        }else{
            result = append(result,length)
            length = 1
            partition,_ = last[val]
        }
    }
    if length > 0{
        result = append(result, length)
    }
    return result
}
