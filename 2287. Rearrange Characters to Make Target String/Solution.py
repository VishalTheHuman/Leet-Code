class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        copies = float("inf")
        s = Counter(s)
        target = Counter(target)
        for k, v in target.items():
            copies = min(copies, s[k]//v)
        return copies if copies < float("inf") else 0
