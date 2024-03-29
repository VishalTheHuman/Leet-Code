class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dt = sorted(Counter(nums).items() , key = lambda x : x[1], reverse = True)
        n = len(nums)//2
        a1 = 0
        a2 = 0
        for x, y in dt:
            if a1 < n and a2 < n and y == 2:
                a1 += 1
                a2 += 1
            elif a1 < n and y == 1:
                a1 += 1
            elif a2 < n and y == 1:
                a2 += 1
            else:
                return False
        return a1 == a2 == n
