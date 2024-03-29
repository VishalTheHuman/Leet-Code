class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width = 0
        i = 0 
        while i < len(s):
            w = ord(s[i])-97
            if widths[w]+width <= 100:
                width += widths[w]
                i+=1
            else:
                width = 0
                lines+=1
        return [lines,width]
