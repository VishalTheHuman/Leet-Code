class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        spaces = [0] + spaces
        for i in range(1, len(spaces)):
            result.append(s[spaces[i-1]:spaces[i]])
        result.append(s[spaces[-1]:])
        return 
.join(result)
