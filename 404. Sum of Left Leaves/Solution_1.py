# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode],sum_val=0) -> int:
        q = deque([root])
        s = 0
        while q and root:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    if not node.left.left and not node.left.right:
                        s += node.left.val
                
                if node.right:
                    q.append(node.right)
        return s
