class RideSharingSystem:

    def __init__(self):
        self.t = 1
        self.dq = []
        self.rq = []
        self.cs = defaultdict(int)

    def addRider(self, riderId: int) -> None:
        self.rq.append(
            (self.t, riderId)
        )
        self.cs[riderId] = self.t
        self.t += 1

    def addDriver(self, driverId: int) -> None:
        self.dq.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if len(self.rq)==0 or len(self.dq)==0: 
            return [-1,-1]

        while len(self.rq) > 0: 
            t, r = self.rq.pop(0)
            if t == self.cs[r]: 
                d = self.dq.pop(0)
                return [d,r]

        return [-1,-1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.cs:
            del self.cs[riderId]


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)
