class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        mapping = {}
        for x in words:
            mapping[x] = ".join(sorted(x))
        i = 1
        while i < len(words):
            if mapping[words[i]] == mapping[words[i-1]]:
                words.pop(i)
            else:
                i += 1 
        return words
