class Solution:
    def minimumPushes(self, word: str) -> int:
        dt = sorted(list(Counter(word).items()), key = lambda x : x[1], reverse = True)
        count = 0
        i = 0
        for key, val in dt:
            count += (((i//8)+1)*val)
            i+=1
        return count
