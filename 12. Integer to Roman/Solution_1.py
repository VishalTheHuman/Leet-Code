class Solution:
    def intToRoman(self, num: int) -> str:
        def Thousands(num):
            result = ""
            val = num//1000
            if val:
                result += "M"*(val)
                num -= (num//1000)*1000
            return num, result
        
        def Others(num, result, helper = ["", "", ""], div = 1):
            val = num // div
            if val == 9:
                result += (helper[0] + helper[2])
            elif val >=5 :
                result += helper[1] + (helper[0] * (val - 5))
            elif val == 4:
                result += helper[0] + helper[1]
            else:
                result += helper[0]*val
            num -= val * div
            return num, result

        num, result = Thousands(num)   
          
        for div, helper in [
            (100, ["C", "D", "M"]), 
            (10, ["X", "L", "C"]), 
            (1, ["I", "V", "X"])
        ]:
            num, result = Others(num, result,helper , div)   
        return result
                
