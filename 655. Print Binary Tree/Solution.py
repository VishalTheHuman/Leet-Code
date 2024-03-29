# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def getLevel(root,lvl = 0):
            if not root:
                return lvl
            lvl+=1
            l = getLevel(root.left,lvl)
            r = getLevel(root.right,lvl)
            return max(r,l)
        def dfs(root, r = 0, c = 0):
            nonlocal lvl
            if not root:
                return
            if root.left:
                arr[r+1][c-(2**(lvl-r-1))] = str(root.left.val)
                dfs(root.left, r+1, c-(2**(lvl-r-1)) )
            if root.right:
                arr[r+1][c+(2**(lvl-r-1))] = str(root.right.val)
                dfs(root.right, r+1, c+(2**(lvl-r-1)) )
        
        lvl = getLevel(root)-1
        arr = [["]*(2*(2**lvl)-1) for _ in range(lvl+1)]
        cols = len(arr[0]) if arr and arr[0] else 0
        if root:
            arr[0][(cols-1)//2] = str(root.val)
            dfs(root,0, (cols-1)//2)
        return arr
