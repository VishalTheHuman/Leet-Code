class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def check(): 
            nonlocal n
            for i in range(n): 
                for j in range(n): 
                    if mat[i][j] != target[i][j]: 
                        return False
            return True

        def rotate(): 
            nonlocal mat,n
            temp = [[0]*n for i in range(n)]
            for i in range(n): 
                for j in range(n): 
                    temp[j][n-i-1] = mat[i][j]
            mat = temp

        if check(): 
            return True

        for _ in range(3): 
            rotate()
            if check(): 
                return True
            
        return False
