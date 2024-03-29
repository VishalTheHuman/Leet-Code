class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        curr = []
        visited = [False]*len(nums)
        def perms(size=0):
            if size==len(nums):
                result.add(tuple(curr))
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1] or visited[i]:
                    continue
                visited[i] = True
                curr.append(nums[i])
                perms(size+1)
                visited[i] = False
                curr.pop()
        perms()
        return result
