class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dt = {}
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in dt:
                dt[size] = [i]
            else:
                dt[size].append(i)
        ls = []
        for k,v in dt.items():
            val = []
            for x in v:
                if len(val)<k:
                    val.append(x)
                if len(val)==k:
                    ls.append(val)
                    val = []
        return ls
