class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words = [Counter(x) for x in words]
        ls = []
        for ch in "abcdefghijklmnopqrstuvwxyz":
            min_val = 1000
            is_valid = True
            for i in range(len(words)):
                min_val = min(min_val,words[i].get(ch,0))
                if min_val==0:
                    is_valid=False
                    break
            if is_valid:
                ls += [ch for x in range(min_val)]
        return ls
