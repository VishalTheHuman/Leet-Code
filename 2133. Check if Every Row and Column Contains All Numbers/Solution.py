class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            s1 = set()
            s2 = set()
            for j in range(len(matrix)):
                s1.add(matrix[i][j])
                s2.add(matrix[j][i])
            if len(s1) < len(matrix) or len(s2) < len(matrix):
                return False
        return True
