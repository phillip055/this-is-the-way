class DoublyLinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.kvs = {}

    def get(self, key: int) -> int:
        if key not in self.kvs:
            return -1
        node = self.kvs[key]
        self.remove(node)
        self.insert(node)
        return node.val
    
    def remove(self, node):
        del self.kvs[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self.kvs[node.key] = node

    def put(self, key: int, value: int) -> None:
        if key in self.kvs:
            node = self.kvs[key]
            self.remove(node)
            self.insert(DoublyLinkedListNode(key, value))
        else:
            if len(self.kvs) == self.capacity:
                self.remove(self.head.next)
            self.insert(DoublyLinkedListNode(key, value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
