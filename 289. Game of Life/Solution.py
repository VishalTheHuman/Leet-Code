class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def play(i_idx,j_idx):
            count = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if i== 0 and j == 0:
                        continue
                    curr_i = i + i_idx
                    curr_j = j + j_idx
                    if 0 <= curr_i < len(board) and 0 <= curr_j < len(board[0]):
                        if board[curr_i][curr_j]:
                            count += 1
            return count
        to_change = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                neigh = play(i,j)
                if neigh == 3 and not board[i][j]:
                    to_change.append((i,j,1))
                elif (neigh > 3 or neigh < 2) and board[i][j]:
                    to_change.append((i,j,0))
                    
        for i,j, val in to_change:
            board[i][j] = val
