from random import choice
class RandomizedSet:

    def __init__(self):
        self.ls = []

    def insert(self, val: int) -> bool:
        if val not in self.ls:
            self.ls.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.ls:
            return False
        self.ls.remove(val)
        return True

    def getRandom(self) -> int:
        return choice(self.ls)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
