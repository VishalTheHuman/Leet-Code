class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        prev = []
        nxt = []
        for x in nums:
            if x < pivot:
                prev.append(x)
            elif x>pivot:
                nxt.append(x)
        return prev + [pivot]*(nums.count(pivot)) + nxt
