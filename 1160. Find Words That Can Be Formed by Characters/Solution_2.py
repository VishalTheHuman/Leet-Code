class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dt = Counter(chars)
        count = 0
        for word in words:
            possible = True
            dt_word = Counter(word)
            for ch in word:
                if dt.get(ch,0)-dt_word.get(ch) < 0:
                    possible = False
            if possible:
                count+=len(word)
        return count
