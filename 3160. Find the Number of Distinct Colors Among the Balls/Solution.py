class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colored = {}
        distinct = 0
        storage = defaultdict(int)
        for idx,(x,y) in enumerate(queries):
            if colored.get(x,False):
                if storage[colored[x]]==1:
                    del storage[colored[x]]
                    distinct -= 1
                else:
                    storage[colored[x]] -=1
            colored[x] = y
            if y in storage:
                storage[y] += 1
            else:
                storage[y] = 1
                distinct += 1
            queries[idx] = distinct
        return queries
