class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dt = Counter(arr)
        return len(dt.values()) == len(set(dt.values()))
