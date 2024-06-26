class Solution:
    def myAtoi(self, s: str) -> int:
        num = ""
        positive = False
        negative = False
        seen = False
        for x in s:
            if x == " ":
                if num or positive or negative or seen:
                    break
                else:
                    continue
            elif x in "0123456789":   
                seen = True                 
                if x == "0" and not num:
                    continue
                num += x
            elif x == ".":
                break
            elif x in ["+","-"]:
                if positive or negative or num or seen:
                    break
                negative = (x=="-")
                positive = (x=="+")
            else:
                break
        if not num:
            return 0 
        if negative:
            num = "-"+num
        num_int = int(num) 
        if num_int - 2**31 + 1 >= 0:
            return 2**31 - 1
        elif num_int + 2**31 <= 0:
            return -2**31
        return num_int
