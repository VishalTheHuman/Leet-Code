class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(num):
            if num == 1:
                return False
            if num ==2:
                return True
            if num%2==0:
                return False
            for i in range(3, int(num**0.5) + 1, 2):
                if num%i == 0:
                    return False
            return True
        prime_1 = prime_2 = None
        i,j = 0, len(nums)-1
        while i < len(nums):
            if isPrime(nums[i]):
                prime_1 = i
                break
            i += 1
        while j >= i:
            if isPrime(nums[j]):
                prime_2 = j
                break
            j -= 1
        return prime_2 - prime_1
