class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        dt = Counter(nums)
        for val, freq in dt.items():
            buckets[freq].append(val)
        j = len(nums)
        result = []
        while len(result) < k:
            result.extend(buckets[j])
            j-=1
        return result[:k]
