# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        dt = defaultdict(int)
        def dfs(root,curr_sum = 0):
            if not root:
                return
            nonlocal count, targetSum, dt
            curr_sum+=root.val
            if curr_sum==targetSum:
                count+=1
            old = curr_sum-targetSum
            if old in dt:
                count+=dt[old]
            dt[curr_sum]+=1
            dfs(root.left,curr_sum)
            dfs(root.right,curr_sum)
            dt[curr_sum]-=1
        dfs(root)
        return count
