class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        prev = [1,1]
        for x in range(2,rowIndex+1):
            i = 0
            j = 1
            ls = prev + [1]
            while j<len(prev):
                ls[j] = prev[i]+prev[j]
                i+=1
                j+=1 
            prev = ls
        return ls
