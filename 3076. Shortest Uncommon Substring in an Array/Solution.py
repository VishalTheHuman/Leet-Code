class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        ######################################################
        def generateSubstrings(string):
            if len(string)==1:
                return [string]
            result = []
            for i in range(1, len(string)+1):
                for j in range(len(string)-i+1):
                    result.append(string[j:j+i])
            return result
        ######################################################
        # return generateSubstrings("cab")
        dt = defaultdict(set)
        for ind, x in enumerate(arr):
            subs = generateSubstrings(x)
            for y in subs: 
                dt[y].add(ind)
            arr[ind] = subs
        for ind, x in enumerate(arr):
            result = []
            for y in x:
                if len(dt[y]) == 1:
                    if result: 
                        if len(result[-1]) < len(y):
                            break
                        else:
                            result.append(y)
                    else:
                        result.append(y)
            if result:
                if len(result)==1:
                    arr[ind] = result[0]
                else:
                    arr[ind] = sorted(result)[0]
            else:
                arr[ind] = ""
        return arr
            
