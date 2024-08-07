class Solution:
    def minFlips(self, target: str) -> int:
        prev = target[0]
        count = 1 if target[0] == "1" else 0
        for x in target[1:]:
            if x != prev:
                count += 1
                prev = x
        return count
