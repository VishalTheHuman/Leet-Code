class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        data = [[None]*n for _ in range(m)]
        def helper(i,j):
            if i == m-1:
                return matrix[i][j]
            l = r = d = float("inf")
            if j+1 < n:
                if data[i+1][j+1] is not None:
                    r = data[i+1][j+1]
                else:
                    r = helper(i+1,j+1)
            if j-1 >=0:
                if data[i+1][j-1] is not None:
                    l = data[i+1][j-1] 
                else:
                    l = helper(i+1, j-1)
            d = helper(i+1,j) if data[i+1][j] is None else data[i+1][j]
            data[i][j] = min(l,r,d) + matrix[i][j]
            return data[i][j]
        minimum_sum = float("inf")
        for j in range(n):
            value = helper(0,j)
            if value < minimum_sum: 
                minimum_sum = value
        return minimum_sum
