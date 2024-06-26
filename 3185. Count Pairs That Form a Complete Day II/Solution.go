func countCompleteDayPairs(hours []int) int64 {
    seen := [24]int64{}
    var pairs int64 = 0
    for _, val := range hours {
        val %= 24
        if val > 0 {
            pairs += seen[24-val]
        } else {
            pairs += seen[0]
        }
        seen[val] += 1
    }
    return pairs
}
