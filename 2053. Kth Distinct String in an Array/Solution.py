class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dt = Counter(arr)
        ls = [key for key,val in dt.items() if val==1]
        return "" if k > len(ls) else ls[k-1]
