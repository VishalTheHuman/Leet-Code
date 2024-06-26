class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def find(r,c):
            nonlocal m,n
            coordinates = [r, c]
            while r < m and land[r][coordinates[1]]:
                r += 1
            while c < n and land[coordinates[0]][c]:
                c += 1
            coordinates += [r-1,c-1]
            for i in range(coordinates[0],r):
                for j in range(coordinates[1],c):
                    land[i][j] = 0
            return coordinates
        m, n = len(land), len(land[0])
        result = []
        for i in range(m):
            for j in range(n):
                if land[i][j]:
                    result.append(find(i,j))
        return result
