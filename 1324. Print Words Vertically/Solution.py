class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        max_len = max(len(txt) for txt in s)
        ls = [""]*max_len
        for i in range(max_len):
            for word in s:
                if i < len(word):
                    ls[i]+=word[i]
                else:
                    ls[i]+=" "
            ls[i] = ls[i].rstrip()
        return ls
