# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
        dfs(root)
        min_abs = 1000000
        for i in range(1,len(nums)):
            min_abs = min(min_abs, abs(nums[i]-nums[i-1]))
        return min_abs
