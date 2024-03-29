class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ########################################
        def f(word):
            char = word[0]
            for i in range(1,len(word)):
                if word[i] < char:
                    char = word[i]
            return word.count(char)
        ########################################
        result = []
        freq_words = [f(word) for word in words]
        freq_queries = [f(q) for q in queries]
        freq_words.sort(reverse=True)
        for i in range(len(freq_queries)):
            val = 0
            for j in range(len(freq_words)):
                if freq_words[j] <= freq_queries[i]:
                    break
                else:
                    val += 1
            result.append(val)
        return result
