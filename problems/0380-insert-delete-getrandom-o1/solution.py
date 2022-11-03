class RandomizedSet:

    def __init__(self):
        self.table = {}
        self.pack = []

    def insert(self, val: int) -> bool:
        if val in self.table:
            return False
        idx = len(self.pack)
        self.table[val] = idx
        self.pack.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.table:
            return False
        idx = self.table[val]
        lastVal = self.pack[-1]
        self.table[lastVal] = idx
        self.pack[idx] = lastVal
        self.pack.pop()
        del self.table[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.pack)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
