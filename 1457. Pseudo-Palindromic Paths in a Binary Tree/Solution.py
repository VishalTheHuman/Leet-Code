# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        count = 0

        def dfs(node,prev):
            nonlocal count
            prev[node.val]+=1
            if not node.left and not node.right:
                if sum(1 for x in prev.values() if x%2) <=1:
                    count += 1
            if node.left:
                dfs(node.left,prev)
            if node.right:
                dfs(node.right,prev)
            prev[node.val]-=1
        dfs(root,Counter())

        return count
