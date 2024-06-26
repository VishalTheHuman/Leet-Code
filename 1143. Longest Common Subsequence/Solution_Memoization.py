class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Memoization Approach
        def lcs(i,j):
            if i >= len(text2) or j >= len(text1):
                return 0
            if table[i][j] is not None:
                return table[i][j]
            if text2[i] == text1[j]:
                table[i][j] = 1 + lcs(i+1,j+1)  
            else:
                table[i][j] = max(lcs(i+1,j), lcs(i,j+1))
            return table[i][j]
            
        table = [[None] * len(text1) for _ in range(len(text2))]
        return lcs(0,0)
