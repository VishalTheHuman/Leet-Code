# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode],lvl = 1) -> int:
        q = deque([root])
        lvl = 0
        while q and root:
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return lvl+1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl+=1
        return lvl
