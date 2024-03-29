class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        for x in set(words1+words2):
            if words1.count(x) == words2.count(x) == 1:
                count+=1
        return count
