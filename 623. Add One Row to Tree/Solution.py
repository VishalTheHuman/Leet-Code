# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val,root)
        
        q = deque([root])
        lvl = 1
        
        while q and root:
            if lvl+1==depth:
                break
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl+=1
        
        for i in range(len(q)):
            q[i].left = TreeNode(val,left = q[i].left)
            q[i].right = TreeNode(val,right = q[i].right)
        
        return root
