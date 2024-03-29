class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dt = sorted(Counter(arr).values(), reverse = True)
        s = 0; arr_half = len(arr)/2
        for ind, freq in enumerate(dt):
            s += freq
            if s >= arr_half:
                return ind+1
        return 0
