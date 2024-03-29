class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dt = Counter(tasks)
        count = 0
        for v in dt.values():
            if v <2 :
                return -1
            count += (v//3)
            if v%3:
                count += 1
        return count
