class Solution:

    def __init__(self, nums: List[int]):
        self.dt = {}
        for ind, val in enumerate(nums):
            if not self.dt.get(val,False):
                self.dt[val] = [0, [ind]]
            else:
                self.dt[val][1].append(ind)
    
    def pick(self, target: int) -> int:
        val = self.dt[target][1][self.dt[target][0]]
        self.dt[target][0] = (self.dt[target][0] + 1) % len(self.dt[target][1])
        return val

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
