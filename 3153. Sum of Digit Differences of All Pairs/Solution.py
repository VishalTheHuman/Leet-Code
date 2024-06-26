class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        nums = list(map(str, nums))
        store = defaultdict(dict)
        for num in nums:
            for idx, x in enumerate(num):
                store[idx][x] = store[idx].get(x,0) + 1
        diff = 0
        total_nums = len(nums)
        print(store)
        for pos in store.keys():
            for val in store[pos].values():
                diff += (total_nums - val) * val
        return diff//2
