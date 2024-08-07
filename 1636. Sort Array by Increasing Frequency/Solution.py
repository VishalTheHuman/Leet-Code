class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        temp = defaultdict(list)
        for x,y in Counter(nums).items():
            temp[y].append(x)

        result = []
        for x in sorted(temp):
            temp[x].sort(reverse=True)
            for y in temp[x]:
                result.extend([y]*x)
        return result
        
