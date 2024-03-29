class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_count = defaultdict(int)
        if k>len(arr):
            return max(arr)
        while True:
            win, ind = max(arr[0],arr[1]), 1 if arr[0]>arr[1] else 0
            win_count[win]+=1
            if win_count[win]==k:
                return win
            arr.append(arr.pop(ind))
