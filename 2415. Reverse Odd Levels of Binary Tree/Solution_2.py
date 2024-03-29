# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        lvl = 0
        while q and root:
            vals = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    vals.append(node.right.val)
            if lvl%2==0:
                for i in range(len(q)):
                    q[i].val = vals.pop()
            lvl+=1
        return root
