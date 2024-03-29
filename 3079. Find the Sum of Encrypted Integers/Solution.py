class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        sum_encrypted = 0
        for x in nums:
            val = str(x)
            max_digit = max(val, key=lambda x : ord(x))
            sum_encrypted += int(len(val)*max_digit)
        return sum_encrypted
