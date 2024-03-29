# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        q = deque([root])
        lvl = 0
        ret = []
        while root and q:
            ls = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                ls.append(node.val)
            lvl+=1
            if lvl%2==0:
                ret.append(ls[::-1])
            else:
                ret.append(ls)
        return ret
