class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = bank[0].count("1")
        count = 0
        for x in bank[1:]:
            total = x.count("1")
            if total:
                count+=(prev*total)
                prev = total
        return count
