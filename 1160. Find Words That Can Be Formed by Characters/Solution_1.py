class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            possible = True
            for ch in word:
               if chars.count(ch) < word.count(ch):
                   possible = False
                   break
            if possible:
                count+=len(word)
        return count
