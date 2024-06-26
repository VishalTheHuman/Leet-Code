class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        def check(i,j):
            prev = matrix[i][j]
            i, j = i+1, j+1
            while i < m and j < n:
                if matrix[i][j]!=prev:
                    return False
                i, j = i+1, j+1
            return True
        
        for i in range(m):
            res = check(i,0)
            if not res:
                return False
        
        for i in range(n):
            res = check(0,i)
            if not res:
                return False

        return True
