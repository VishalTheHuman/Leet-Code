class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def check(word_1,word_2):
            if len(word_1)!=len(word_2):
                return False
            count = 0
            for i in range(len(word_1)):
                if word_1[i]!=word_2[i]:
                    count+=1
                    if count > 2:
                        return False
            return True
        ans = []
        for i in range(len(queries)):
            for j in range(len(dictionary)):
                if check(queries[i],dictionary[j]):
                    ans.append(queries[i])
                    break
        return ans
