class Solution:
    def minimumLength(self, s: str) -> int:
        store = defaultdict(list)
        stack = list(s)
        for idx, val in enumerate(s):
            if len(store[val]) == 2:
                stack[store[val].pop(0)] = ""
                stack[idx] = ""
            else:
                store[val].append(idx)
        
        return len("".join(stack))
