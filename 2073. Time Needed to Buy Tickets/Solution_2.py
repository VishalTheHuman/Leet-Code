class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while True:
            for idx in range(len(tickets)):
                if tickets[idx]:
                    tickets[idx] -= 1
                    time += 1
                    if idx == k and tickets[k] == 0:
                        return time
        return 0
