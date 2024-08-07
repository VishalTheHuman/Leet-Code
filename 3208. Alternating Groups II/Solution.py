class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l = count = r = 0
        length = len(colors)
        while r < length + k - 1:
            possible = True
            while l < length and r < length + k - 1 and r-l < k-1:
                r += 1
                if colors[r%length] == colors[(r-1)%length]:
                    possible = False
                    l = r
                    break

            if l >= length: 
                break
            if possible:
                count += possible
                l += 1
        return count
                
