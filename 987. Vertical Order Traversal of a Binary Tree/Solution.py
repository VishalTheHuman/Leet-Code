# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(dict)
        def dfs(node, row = 0, col = 0):
            if not node:
                return
            if row in store[col]:
                store[col][row].append(node.val)
            else:
                store[col][row]= [node.val]
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        dfs(root)
        result = []
        for col in sorted(store.keys()):
            answer = []
            for row in sorted(store[col].keys()):
                if len(store[col][row])>1:
                    store[col][row].sort()
                answer.extend(store[col][row])
            result.append(answer)
        return result
