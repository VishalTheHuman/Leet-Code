class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()
        self.root = {}
        for word in dictionary:
            root = self.buildTrie(word)
        for i in range(len(sentence)):
            sentence[i] = self.inTrie(sentence[i])
        return " ".join(sentence)
    
    def buildTrie(self,word):
        itr = self.root
        i = 0
        while i < len(word):
            if word[i] in itr:
                itr = itr[word[i]]
            else:
                itr[word[i]] = {}
                itr = itr[word[i]]
            i+=1
        itr["*"] = {}

    def inTrie(self,word):
        itr = self.root
        i = 0
        w=""
        while i < len(word):
            if word[i] not in itr:
                break
            if word[i] in itr and "*" in itr:
                itr = itr[word[i]]
                w+=word[i]
                return w
            if word[i] in itr:
                itr = itr[word[i]]
                w+=word[i]
            if "*" in itr:
                return w
            i+=1
        return word
