class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_val  = [float("inf"),[]]
        for i in range(1, len(arr)):
            val = arr[i] - arr[i-1]
            if val < min_val[0]:
                min_val[0] = val
                min_val[1] = [[arr[i-1], arr[i]]]
            elif val == min_val[0]:
                min_val[1].append([arr[i-1], arr[i]])
        return min_val[1]
