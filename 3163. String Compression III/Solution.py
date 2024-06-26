class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 1:
            return "1" + word
        prev = word[0]
        count = 1
        comp = ""
        for x in word[1:]:
            if count == 9:
                comp += str(count) + prev
                count = 0
            if x != prev:
                if count:
                    comp += str(count) + prev
                count = 1
            else:
                count += 1

            prev = x
        if count:
            comp += str(count) + prev
        return comp
