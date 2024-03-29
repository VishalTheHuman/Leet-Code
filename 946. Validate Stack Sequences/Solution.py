class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        i = 1
        j = 0 
        stk = [pushed[0]]
        while i<len(pushed) and j<len(popped):
            if stk:
                if stk[-1] == popped[j]:
                    stk.pop()
                    j+=1
                else:
                    stk.append(pushed[i])
                    i+=1
            else:
                stk.append(pushed[i])
                i+=1
        while j<len(popped):
            if not stk:
                break
            if stk[-1]==popped[j]:
                stk.pop()
                j+=1
            else:
                break
        return len(stk)==0
