class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        itr = self.root
        for ch in word:
            is_inserted = False
            for child in itr.children:
                if child.val == ch:
                    itr = child
                    is_inserted = True
                    break
            if not is_inserted:
                itr.children.append(TrieNode(ch))
                itr = itr.children[-1]
        itr.is_end_word = True

    def search(self, word: str) -> bool:
        itr = self.root
        for ch in word:
            found = False
            for child in itr.children:
                if child.val == ch:
                    found = True
                    itr = child
                    break
            if not found:
                return False
        return itr.is_end_word

    def startsWith(self, prefix: str) -> bool:
        itr = self.root
        for ch in prefix:
            found = False
            for child in itr.children:
                if child.val == ch:
                    found = True
                    itr = child
                    break
            if not found:
                return False
        return True

class TrieNode:
    def __init__(self,val):
        self.val = val
        self.children = []
        self.is_end_word = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
