class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convertToMapping(num):
            if num==0:
                return mapping[0]
            newNum = i = 0
            while num:
                newNum = (mapping[num%10] * (10)**i )+ newNum
                num//=10
                i+=1
            return newNum
        nums.sort(key = convertToMapping)
        return nums
