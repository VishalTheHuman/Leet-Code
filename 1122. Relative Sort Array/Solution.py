class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1 = Counter(arr1)
        result = []
        for x in arr2:
            if x in arr1:
                result += [x]*arr1[x]
                del arr1[x]
        for x,y in sorted(arr1.items(),key = lambda x : x[0]):
            result += [x]*y
        return result
