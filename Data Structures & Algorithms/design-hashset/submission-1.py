class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.arr = [ListNode(-1) for i in range(10000)]

    def add(self, key: int) -> None:
        hash_ = key % len(self.arr)
        curr = self.arr[hash_]

        while curr.next:
            curr = curr.next
            if curr.val == key:
                return
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        hash_ = key % len(self.arr)
        curr = self.arr[hash_]

        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        hash_ = key % len(self.arr)
        curr = self.arr[hash_]

        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)