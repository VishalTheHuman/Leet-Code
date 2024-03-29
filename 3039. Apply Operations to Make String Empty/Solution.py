class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        dt = Counter(s)
        max_count = [0,[]]
        for k,v in dt.items():
            if v > max_count[0]:
                max_count = [v,[k]]
            elif v==max_count[0]:
                max_count[1].append(k)
        s = s[::-1]
        max_count[1] = set(max_count[1])
        seen = set()
        curr = "
        for x in s:
            if len(curr)==len(max_count[1]):
                break
            if x in max_count[1] and x not in seen:
                seen.add(x)
                curr+=x
        return curr[::-1]
                
            
