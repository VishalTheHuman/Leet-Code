class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.ls = set()
        self.permsModified(tiles)
        return len(self.ls)
    def permsModified(self,string):
        if len(string)==1:
            self.ls.add(string)
            return string
        l = set()
        for i in range(len(string)):
            ch = string[i]
            text = string[:i]+string[i+1:]
            for x in self.permsModified(text):
                a = x + ch
                l.add(a)
                self.ls.add(a)
        return l
