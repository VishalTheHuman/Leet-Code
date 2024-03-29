class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        itr = self.root
        for ch in word:
            is_inserted = False
            if ch in itr:
                itr = itr[ch]
            else:
                itr[ch] = {}
                itr = itr[ch]
        itr["*"]="*"
    
    def search(self, word: str) -> bool:
        itr = self.root
        for ch in word:
            if ch not in itr:
                return False
            itr = itr[ch]
        return "*" in itr

    def startsWith(self, prefix: str) -> bool:
        itr = self.root
        for ch in prefix:
            if ch not in itr:
                return False
            itr = itr[ch]
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
