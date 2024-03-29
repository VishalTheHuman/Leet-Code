class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dt = {k:v for k,v in knowledge}
        t = ""
        i = 0
        while i<len(s):
            while i<len(s) and s[i]!="(":
                t+=s[i]
                i+=1
            i+=1
            term = ""
            while i<len(s) and s[i]!=")":
                term+=s[i]
                i+=1
            i+=1
            if term:
                t += dt.get(term,"?")
        return t
