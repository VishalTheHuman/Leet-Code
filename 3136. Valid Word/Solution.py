class Solution:
    def isValid(self, word: str) -> bool:
        def check(string):
            for x in string:
                if x in word:
                    return True
            return False
        word = word.lower()
        
        if len(word) <3:
            return False
        word = Counter(word)

        return check("aeiou") and check("qwrtypsdfghjklzxcvbnm") and not check("@#$")
