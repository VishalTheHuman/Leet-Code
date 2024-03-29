class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dt = {}
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in dt:
                dt[size] = [[i]]
            else:
                ins = False
                for x in dt[size]:
                    if len(x)<size:
                        x.append(i)
                        ins = True
                if not ins:
                    dt[size] = dt[size]+[[i]]
        
        ls = []
        for x in dt.values():
            ls.extend(x)
        return ls
