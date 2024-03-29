class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        answer = ""
        def perms(size,string=""):
            nonlocal answer
            if size==1:
                if string+"1" not in nums:
                    answer = string+"1"
                elif string+"0"not in nums:
                    answer = string+"0"
                return 
            perms(size-1,string+"1")
            perms(size-1,string+"0")
        perms(len(nums[0]))
        return answer
