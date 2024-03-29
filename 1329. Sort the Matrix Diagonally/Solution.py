class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ind = [(len(mat)-1,0)]
        q = [mat[len(mat)-1][0]]
        while ind:
            q.sort()
            for i,j in ind:
                mat[i][j] = q.pop(0)
            new_ind = []
            for i,j in ind:
                if i-1 >=0  and (i-1,j) not in new_ind:
                    q.append(mat[i-1][j])
                    new_ind.append((i-1,j))
                if j+1 < len(mat[0]) and (i,j+1) not in new_ind:
                    q.append(mat[i][j+1])
                    new_ind.append((i,j+1))
            ind = new_ind
        return mat
