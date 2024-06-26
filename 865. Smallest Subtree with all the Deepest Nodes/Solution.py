# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def find(root, depth=0):
            if not root:
                return depth - 1
            nonlocal ancestor, max_depth
            if not root.left and not root.right:
                depth += 1
                if depth > max_depth:
                    max_depth = depth
                    ancestor = root
                return depth
            
            l = find(root.left,depth + 1)
            r = find(root.right, depth + 1)
            if l == r == max_depth:
                ancestor = root
            return max(l,r)
        ancestor = None
        max_depth = 0
        find(root)
        return ancestor
