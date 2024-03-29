class MapSum:

    def __init__(self):
        self.trie = {}
        self.table = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.table:
            self.table[key] = val
            return
        self.table[key] = val
        curr = self.trie
        for x in key:
            if x in curr:
                curr[x][1].append(key)
            else:
                curr[x] = [{}, [key]]
            curr = curr[x][0]

    def sum(self, prefix: str) -> int:
        curr = self.trie
        s = 0
        for x in prefix:
            if x not in curr: 
                return 0
            s = curr[x][1]
            curr = curr[x][0]
        return sum(self.table[x] for x in s)
    
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
