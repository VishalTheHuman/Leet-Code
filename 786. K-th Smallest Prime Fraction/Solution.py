class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        q = []
        heap = heapq.heapify(q)
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i==j:
                    continue
                heapq.heappush(q,(arr[i]/arr[j], (arr[i], arr[j])))
        heapq.heapify(q)
        k -= 1
        while k:
            heapq.heappop(q)
            k -= 1
        return heapq.heappop(q)[1]
