class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indices = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    indices.append((i,j))
        
        def makeZeros():
            while indices:
                index = indices.pop()
                for i in range(len(matrix)):
                    matrix[i][index[1]] = 0 

                for i in range(len(matrix[0])):
                    matrix[index[0]][i] = 0 
                    
        makeZeros()
