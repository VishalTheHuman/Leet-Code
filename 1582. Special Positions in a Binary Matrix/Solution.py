class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check(index):
            return sum(1 for i in range(len(mat)) if mat[i][j])==1
        i = 0
        total = 0
        while i < len(mat):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    if mat[i].count(1)==1 and check(j):
                        total +=1
                    else:
                        break
            i+=1
        return total
