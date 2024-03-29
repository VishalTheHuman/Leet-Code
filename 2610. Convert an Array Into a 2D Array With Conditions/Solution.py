class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ls = []
        for num in nums:
            placed = False
            for y in ls:
                if num not in y:
                    placed = True
                    y.append(num)
                    break
            if not placed:
                ls.append([num])
        return ls
