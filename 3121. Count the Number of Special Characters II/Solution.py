class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        index = {}
        upper = set()
        for idx, ch in enumerate(word):
            if ch.islower():
                index[ch] = idx
            else: 
                if ch not in index:
                    index[ch] = idx
                upper.add(ch)
        count = 0
        for x in list(upper):
            if x.lower() in index and index[x] > index[x.lower()]:
                count += 1
        return count
