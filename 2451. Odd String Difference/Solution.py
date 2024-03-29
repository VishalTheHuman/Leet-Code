class Solution:
    def oddString(self, words: List[str]) -> str:
        counter = defaultdict(int)
        word = {}
        for i in range(3):
            result = []
            for j in range(1, len(words[i])):
                ans = ord(words[i][j]) - ord(words[i][j-1])
                result.append(ans)
            counter[tuple(result)] += 1
            word[tuple(result)] = words[i]
        for i in range(3, len(words)):
            result = []
            for j in range(1, len(words[i])):
                ans = ord(words[i][j]) - ord(words[i][j-1])
                result.append(ans)
            counter[tuple(result)] += 1
            word[tuple(result)] = words[i]
            if len(counter) > 1:
                break
        for k, v in counter.items():
            if v == 1:
                return word[k]
