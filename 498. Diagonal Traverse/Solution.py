class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dt = {}
        ls = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if dt.get(i+j):
                    dt[i+j].append(mat[i][j])
                else:
                    dt[i+j] = [mat[i][j]]
        for x in sorted(dt.keys()):
            if x%2==0:
                ls.extend(dt[x][::-1])
            else:
                ls.extend(dt[x])
        return ls
