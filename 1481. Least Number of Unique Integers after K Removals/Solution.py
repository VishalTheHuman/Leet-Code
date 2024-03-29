class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        count = sorted(count.items(), key = lambda x : x[1])
        removed = 0
        for ind,(key,val) in enumerate(count):
            if k<val:
                break
            k-=val
            removed+=1
        return len(count) - removed
