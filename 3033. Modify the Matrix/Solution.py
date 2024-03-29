class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        max_vals = []
        for j in range(len(matrix[0])):
            max_vals.append(max(matrix[i][j] for i in range(len(matrix))))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==-1:
                    matrix[i][j] = max_vals[j]
        return matrix
