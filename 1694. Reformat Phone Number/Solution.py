echo "class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-","")
        if len(number) % 3 == 0:
            return "-".join([number[i:i+3]for i in range(0, len(number), 3)])
        elif len(number) % 3 == 1:
            return "-".join([number[i:i+3] for i in range(0, len(number)-4,3)]+[number[-4:-2], number[-2:]])
        else:
            return "-".join([number[i:i+3] for i in range(0, len(number)-3,3)] + [number[-2:]])
