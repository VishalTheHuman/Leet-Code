class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for x in bills:
            if x == 5:
                five += 1
            elif x == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
