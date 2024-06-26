class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        rows = len(board)
        cols = len(board[0])
        w_len = len(word)
        def bfs(i,j,ind):
            nonlocal result, rows, cols, word, w_len, seen
            if ind >= w_len:
                result = True
                return
            if result:
                return
            moves = [(1,0),(0,1),(-1,0),(0,-1)]
            for i_1, j_1 in moves:
                if 0 <= i+i_1 < rows and 0 <= j+j_1 < cols and (i+i_1,j+j_1) not in seen and board[i+i_1][j+j_1]==word[ind]:
                    seen.add((i+i_1,j+j_1))
                    bfs(i+i_1, j+j_1, ind+1)
                    seen.remove((i+i_1,j+j_1))
        seen = set()
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    seen.add((i,j))
                    bfs(i,j,1)
                    seen.remove((i,j))
        return result
