class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        twenty_five = len(arr)/4
        for x,y in Counter(arr).items():
            if y > twenty_five:
                return x
