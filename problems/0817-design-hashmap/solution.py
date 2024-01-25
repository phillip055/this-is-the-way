class MyHashMap:

    def __init__(self):
        self.lst = []

    def put(self, key: int, value: int) -> None:
        found_idx = -1
        for idx, (k, v) in enumerate(self.lst):
            if k == key:
                found_idx = idx
                break
        if found_idx == -1:
            self.lst.append((key, value))
        else:
            self.lst[found_idx] = (key, value)

    def get(self, key: int) -> int:
        for (k,v) in self.lst:
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        found_idx = -1
        for idx, (k, v) in enumerate(self.lst):
            if k == key:
                found_idx = idx
                break
        if found_idx == -1:
            return
        self.lst[found_idx], self.lst[len(self.lst) - 1] = self.lst[len(self.lst) - 1], self.lst[found_idx]
        self.lst.pop()
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
