# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(root,parent=None):
            if not root:
                return
            
            if parent is None and root.val not in to_delete:
                forest.append(root)
                parent = root
            
            if root.left:
                if root.left.val in to_delete:
                    dfs(root.left.left)
                    dfs(root.left.right)
                    root.left = None
                else:
                    dfs(root.left, parent)
            if root.right:
                if root.right.val in to_delete:
                    dfs(root.right.left)
                    dfs(root.right.right)
                    root.right = None
                else:
                    dfs(root.right, parent)   
        to_delete = set(to_delete)
        forest = []
        dfs(root)
        return forest
