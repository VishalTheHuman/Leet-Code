type store struct{
    diff int
    prof int
}

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
    sort.Slice(worker, func(i,j int) bool {
        return worker[i] > worker[j]
    })
    value := []store{}
    for i:=0;i<len(profit);i++ {
        value = append(value, store{
            diff:difficulty[i], 
            prof:profit[i],
        })
    }
    sort.Slice(value, func (i,j int) bool {
        return value[i].prof > value[j].prof
    })
    max_profit := 0
    idx := 0
    for _,w := range worker{
        for idx < len(value) {
            if w >= value[idx].diff {
                max_profit += value[idx].prof
                break
            }
            idx += 1
        }
    }

    return max_profit
}
