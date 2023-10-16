class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for x in range(1,rowIndex+1):
            i = 0
            j = 1
            ls = prev + [1]
            while j<len(prev):
                ls[j] = prev[i]+prev[j]
                i+=1
                j+=1 
            prev = ls
        return prev
