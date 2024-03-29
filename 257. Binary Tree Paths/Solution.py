# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ls = []
        def dfs(root,string):
            if not root:
                return 
            if root.left is None and root.right is None:
                ls.append(string+str(root.val))
                return 
            string+=(str(root.val)+"->")
            dfs(root.left,string)
            dfs(root.right,string)
        dfs(root,"")
        return ls
