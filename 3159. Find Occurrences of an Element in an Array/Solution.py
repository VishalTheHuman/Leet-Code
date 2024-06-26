class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        storage = []
        for idx,num in enumerate(nums):
            if num == x:
                storage.append(idx)
        result = []
        for q in queries:
            if q > len(storage):
                result.append(-1)
            else:
                result.append(storage[q-1])
        return result
