class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)<=numRows:
            return s
        ls = ["" for x in range(numRows)]
        i = 0
        while i < len(s):
            for j in range(numRows):
                if i<len(s):
                    ls[j] +=s[i]
                else:
                    return "".join(ls)
                i+=1 
            for j in range(numRows-2,0,-1):
                if i<len(s):
                    ls[j] +=s[i]
                else:
                    return "".join(ls)
                i+=1
        return "".join(ls)
