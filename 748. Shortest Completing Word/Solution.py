class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower() 
        ls = [(ch,licensePlate.count(ch)) for ch in licensePlate if ch not in "0123456789 "]
        words = sorted(words,key=len)
        for word in words:
            is_feasible = True
            for k,v in ls:
                if word.count(k) < v:
                    is_feasible = False
                    break
            if is_feasible:
                return word
