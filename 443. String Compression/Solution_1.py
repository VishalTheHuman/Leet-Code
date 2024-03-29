class Solution:
    def compress(self, chars: List[str]) -> int:
        string = ""
        def count():
            nonlocal string
            i = 0
            count = 1
            while i+1 < len(chars):
                if chars[i]!=chars[i+1]:
                    string+=(chars[i]+str(count) if count!=1 else chars[i])
                    count = 1
                else:
                    count+=1
                i+=1
            if count==1:
                string+=chars[i]
            else:
                string+=(chars[i]+str(count))
        count()
        l = len(string)
        chars[:l] = list(string)
        return l
