# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def insert(depth, node):
            if not stk:
                nonlocal root
                root = node
                stk.append((depth,node))
            else:
                d, parent = stk[-1]
                while (depth-1)!=d:
                    d,parent = stk.pop()
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
                stk.append((depth,node))
        # Main
        stk = []
        num = ""
        l = 0
        root = None
        for x in traversal:
            if x in "0123456789":
                num += x
            else:
                if num:
                    insert(l, TreeNode(int(num)))
                    l=0
                    num = ""
                l+=1
        if num:
            insert(l,TreeNode(int(num)))
        return root
