class ListNode:
    def  __init__(self, hkey, val):
        self.hkey = hkey
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.arr = [ListNode(-1, -1) for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        curr = self.arr[key % len(self.arr)]

        while curr.next:
            if curr.next.hkey == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        curr = self.arr[key % len(self.arr)]

        while curr.next:
            if curr.next.hkey == key:
                return curr.next.val
            curr = curr.next
        # curr.next = ListNode(key, value)
        return -1

    def remove(self, key: int) -> None:
        curr = self.arr[key % len(self.arr)]

        while curr.next:
            if curr.next.hkey == key:
                # print("enter", curr.next.hkey)
                curr.next = curr.next.next
                return
            curr = curr.next
        # curr.next = ListNode(key, value)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)