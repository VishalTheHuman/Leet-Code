class Solution:
    def longestWord(self, words: List[str]) -> str:
        dt = {}
        for word in words:
            dt[len(word)] = dt.get(len(word),[])+[word]
        
        words.clear()

        while dt:
            max_val = max(dt.keys())
            dt[max_val].sort()
            words.extend(dt[max_val])
            del dt[max_val]

        for word in words:
            is_found = True
            for i in range(1,len(word)):
                if word[:i] not in words:
                    is_found = False
                    break
            if is_found:
                return word
        return ""
