# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.normalDfs(root)
        return self.count

    def normalDfs(self,root):
        if not root:
            return 
        ls = self.dfs(root)
        if sum(ls)//len(ls) == root.val:
            self.count+=1
        self.normalDfs(root.left) 
        self.normalDfs(root.right) 
    
    def dfs(self,root):
        elements = [root.val]
        if root.left:
            elements +=self.dfs(root.left)      
        if root.right:
            elements+= self.dfs(root.right)
        return elements
