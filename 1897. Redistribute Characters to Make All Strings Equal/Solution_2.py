class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dt = defaultdict(int)
        for i in range(len(words)):
            for ch in words[i]:
                dt[ch]+=1
        s = set(dt.values())
        l = len(words)
        return all(x%l==0 for x in s)
