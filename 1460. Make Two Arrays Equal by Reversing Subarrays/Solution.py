class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(arr)!= len(target):
            return False
        target = Counter(target)
        arr = Counter(arr)
        for x in target.keys():
            if target[x] != arr.get(x,0):
                return False
        return True
