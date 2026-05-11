class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums[::-1]:
            while x>0:
                ans.append(x%10)
                x//=10
        return ans[::-1]
