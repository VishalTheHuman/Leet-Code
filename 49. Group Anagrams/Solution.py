class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = {}
        for s in strs:
            k = "".join(sorted(s))
            if k  not in dt:
                dt[k] = [s]
            else:
                dt[k] += [s]
        return list(dt.values())
