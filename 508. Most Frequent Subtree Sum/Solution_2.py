# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        dt = defaultdict(int)
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            val = root.val + l + r
            dt[val]+=1
            return val
        dfs(root)
        max_freq = max(dt.values())     
        ls = []
        for k,v in dt.items():
            if v==max_freq:
                ls.append(k)
        return ls
