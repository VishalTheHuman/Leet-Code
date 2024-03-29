"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        q = deque([root])
        while q and root:
            n = len(q)
            i = 1
            for _ in range(n):
                node = q.popleft()
                node.next = q[0] if i < n and q else None
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                i+=1
        return root
