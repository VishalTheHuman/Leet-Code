class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ind = 0
        min_penalty = count = customers.count("Y")
        for i, ch in enumerate(customers):
            count += 1 if ch=="N" else -1
            if count < min_penalty:
                min_penalty = count
                ind = i+1
        return ind
