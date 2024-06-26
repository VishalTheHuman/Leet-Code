class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def helper(ver):
            i = 0
            consider_0 = False
            num = ""
            arr = []
            while i < len(ver):
                if ver[i] == "0" and not consider_0:
                    i += 1
                    continue
                elif ver[i] == ".":
                    arr.append(int(num) if num else 0)
                    num = ""
                    consider_0 = False
                else:
                    num += ver[i]
                    if not consider_0:
                        consider_0 = True
                i+=1
            arr.append(int(num) if num else 0)
            while arr and arr[-1] == 0:
                arr.pop()
            return arr
        arr_1 = helper(version1)
        arr_2 = helper(version2)
        if len(arr_1) < len(arr_2):
            arr_1 += [0]*(len(arr_2)- len(arr_1))
        else:
            arr_2 += [0]*(len(arr_1)- len(arr_2))
        idx = 0 
        while idx < len(arr_1):
            if arr_1[idx] > arr_2[idx]:
                return 1
            elif arr_1[idx] < arr_2[idx]:
                return -1
            idx += 1
        return 0
