class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for idx in range(0, len(tickets)):
            if idx <=k:
                time += min(tickets[idx], tickets[k])
            elif idx > k:
                time += min(tickets[k]-1, tickets[idx])
                
        return time
