class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ls = []
        i = 0
        for word in words:
            word = word.lower()
            row = self.findRow(word[0])
            inRow = True
            for x in word:
                if row != self.findRow(x):
                    inRow = False
            if inRow:
                ls.append(words[i])
            i+=1
        return ls
    
    def findRow(self,ch):
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]
        i = 0
        for x in rows:
            if ch in x:
                return i
            i+=1
        return -1
            
