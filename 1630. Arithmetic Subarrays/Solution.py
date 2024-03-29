class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            is_true = True
            for i in range(1,len(arr)-1):
                if arr[i+1] - arr[i] != arr[1] - arr[0]:
                    is_true = False
                    break
            if is_true:
                result.append(True)
            else:
                result.append(False)
        return result
