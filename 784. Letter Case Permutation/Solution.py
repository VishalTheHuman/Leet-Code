class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutations = []
        def perms(string, curr="):
            if not string:
                permutations.append(curr)
                return
            if string[0].isalpha():
                perms(string[1:], curr+string[0].lower())
                perms(string[1:], curr+string[0].upper())
            else:
                perms(string[1:], curr+string[0])
        perms(s)
        return permutations
