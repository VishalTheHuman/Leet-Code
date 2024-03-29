# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        q = deque([root])
        while q and root:
            for _ in range(len(q)):
                node = q.popleft()
                ls = self.dfs(node)
                if sum(ls)//len(ls) == node.val:
                    count+=1
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right)
        return count 
        
    def dfs(self,root):
        if not root:
            return
        elements = [root.val]
        if root.left:
            elements +=self.dfs(root.left)      
        if root.right:
            elements+= self.dfs(root.right)
        return elements
