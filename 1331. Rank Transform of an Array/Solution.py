class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dt = {x : idx+1 for idx, x in enumerate(sorted(list(set(arr))))}
        return [dt[x] for x in arr]
