class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None]*k
        self.MAX_LEN = k
        self.count = 0
        self.idx = 0
        self.start = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.MAX_LEN:
            return False
        self.count += 1
        self.arr[self.idx] = value
        self.idx = (self.idx + 1) % self.MAX_LEN
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.start = (self.start + 1) % self.MAX_LEN
        self.count -= 1
        return True
    
    def Front(self) -> int:
        if self.count:
            return self.arr[self.start]
        return -1

    def Rear(self) -> int:
        if self.count:
            if self.idx == 0:
                return self.arr[-1]
            else:
                return self.arr[self.idx-1] 
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.MAX_LEN


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
