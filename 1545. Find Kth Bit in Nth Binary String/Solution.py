class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(string):
            s = ""
            for i in string:
                if i=="0":
                    s+="1"
                else:
                    s+="0"
            return s
        string = "0"
        for i in range(1,n):
            string = string + "1" + invert(string)[::-1]
        return string[k-1]
