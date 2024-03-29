class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dt = {}
        ls = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if dt.get(i+j,False):
                    dt[i+j].insert(0,nums[i][j])
                else:
                    dt[i+j] = [nums[i][j]]
        for x in sorted(dt.keys()):
            ls.extend(dt[x])
        return ls
