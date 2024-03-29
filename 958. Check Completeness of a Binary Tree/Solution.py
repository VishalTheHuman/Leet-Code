# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        seenNone = False
        while q and root:
            for _ in range(len(q)):
                node = q.popleft()
                if node is None:
                    seenNone = True
                    continue
                if seenNone and node:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
