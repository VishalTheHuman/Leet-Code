class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        word_size = len(words[0])
        total_words = len(words)
        window_size = total_words*word_size
        words = Counter(words)
        for i in range(0,len(s)-window_size+1):
            found = Counter([s[j:j+word_size] for j in range(i,i+window_size,word_size)])
            is_perm = True
            for k in words:
                if words[k]!=found[k]:
                    is_perm = False
                    break
            if is_perm:
                result.append(i)
        return result
