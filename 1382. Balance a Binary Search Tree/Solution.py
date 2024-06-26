# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            nodes.append(root.val)
            dfs(root.right)
        
        def build(start,end):
            if start > end:
                return None
            mid = (start + end )//2
            return TreeNode(
                val = nodes[mid],
                left = build(start, mid-1), 
                right = build(mid+1,end)
            )
        nodes = []
        dfs(root)
        return build(0,len(nodes)-1)
