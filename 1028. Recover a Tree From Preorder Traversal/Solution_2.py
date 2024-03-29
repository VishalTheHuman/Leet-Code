# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        split = [0]
        num = ""
        l = 0
        i = 0
        while i < len(traversal):
            if traversal[i] in "0123456789":
                num+= traversal[i]
                if l:
                    split.append(l)
                    l = 0
            else:
                if num:
                    split.append(int(num))
                    num = ""
                l+=1
            i+=1
        if num:
            split.append(int(num))
        
        root = TreeNode(split[1])
        stk = [(0,root)]

        for i in range(3,len(split),2):
            depth = split[i-1]
            val = split[i]
            b = True
            while stk and b:
                if (depth - 1) == stk[-1][0]:
                    node = TreeNode(val)
                    if not stk[-1][1].left:
                        stk[-1][1].left = node
                    else:
                        stk[-1][1].right = node
                    stk.append((depth,node))
                    b = False
                else:
                    stk.pop()
        return root
