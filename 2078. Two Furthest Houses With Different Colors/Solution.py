class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        distance = 0
        for j in range(len(colors)-1,-1,-1):
            if colors[j]!=colors[0]:
                distance = j 
                break

        for j in range(len(colors)):
            if colors[j]!=colors[-1]:
                distance = max(distance,len(colors) - j - 1)
                break
        
        return distance
