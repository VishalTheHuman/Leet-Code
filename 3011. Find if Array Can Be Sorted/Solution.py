class Solution:
    def canSortArray(self, arr: List[int]) -> bool:
        def isSorted():
            for i in range(1,len(arr)):
                if arr[i-1]>arr[i]:
                    return False
            return True
        operations = 10
        while operations:
            operations = 0
            for i in range(1,len(arr)):
                if arr[i] < arr[i-1]:
                    num1 = bin(arr[i-1])[2:]
                    num2 = bin(arr[i])[2:]
                    if num1.count("1") == num2.count("1"):
                        arr[i],arr[i-1] = arr[i-1],arr[i]
                        operations+=1
            if isSorted():
                return True
        return False
