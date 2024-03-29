class SmallestInfiniteSet:

    def __init__(self):
        self.heap = set()
        self.min = 1

    def popSmallest(self) -> int:
        if self.heap:
            val = min(self.heap)
            self.heap.remove(val)
            return val
        self.min+=1
        return self.min-1

    def addBack(self, num: int) -> None:
        if num < self.min:
            self.heap.add(num)
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
