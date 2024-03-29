class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix = [0]
        curr = 0
        for x in arr:
            curr += x
            prefix.append(curr)
        sum_ = curr
        for i in range(3,len(arr)+1,2):
            for j in range(0,len(arr)-i+1):
                sum_+= (prefix[j+i]-prefix[j])
        return sum_
