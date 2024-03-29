class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root = {}
        dt = {}
        for word in words:
            self.insertTrie(word)
            dt[len(word)]= dt.get(len(word),[]) + [word]

        words.clear()

        while dt:
            max_val = max(dt.keys())
            dt[max_val].sort()
            words.extend(dt[max_val])
            del dt[max_val]

        for word in words:
            val = self.checkWord(word)
            if val:
                return word
        return ""

    def insertTrie(self,word):
        itr = self.root
        for ch in word:
            if ch not in itr:
                itr[ch] = {}
            itr = itr[ch]
        itr["*"] = "*"

    def checkWord(self,word):
        itr = self.root
        if word[0] not in itr:
            return False
        itr = itr[word[0]]
        for ch in word[1:]:
            if "*" not in itr:
                return False
            itr = itr[ch]
        return True
