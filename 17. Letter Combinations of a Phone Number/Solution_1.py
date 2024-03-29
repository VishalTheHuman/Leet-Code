class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        def tree(original, string=""):
            if not original:
                possible.append(string)
                return
            for x in mapping[original[0]]:
                tree(original[1:],string+x)
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        possible = []
        tree(digits)
        return possible
