class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ls = []
        for i in range(len(words)):
            try:
                words[i].index(x)
                ls.append(i)
            except:
                pass
        return ls
