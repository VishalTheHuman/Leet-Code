class Solution:
    def grayCode(self, n: int) -> List[int]:
        arr = [0,1]
        for i in range(1,n):
            new_arr = [x<<1 for x in arr] + [x<<1 | 1 for x in arr][::-1]
            arr = new_arr
        return arr
