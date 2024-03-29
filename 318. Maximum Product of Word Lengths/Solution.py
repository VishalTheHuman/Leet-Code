class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def uncommon(w1,w2):
            if len(w2) > len(w1):
                w1,w2 = w2,w1
            for ch in w2:
                if ch in w1:
                    return False
            return True
        product = 0 
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if uncommon(words[i],words[j]):
                    val  = len(words[i])*len(words[j])
                    product = max(product,val)
        return product
