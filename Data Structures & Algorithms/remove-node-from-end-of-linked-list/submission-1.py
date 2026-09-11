# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. find length of the linkedlist - l
        # 2. find n's value from the beginneing
        # 3. iterate till nth node and keep one node prior to it
        # 4. connect the prior node an dnode next of nth node

        if not head:
            return []

        list_len = 0
        curr = head

        while curr:
            list_len += 1
            curr = curr.next

        m = list_len - n + 1
        # print(list_len, m)

        finder = head
        dummy = prev = ListNode(0)
        dummy.next = head

        while m > 1:
            m -= 1
            prev = prev.next
            

        # print(prev.val, finder.val)
        prev.next = prev.next.next

        return dummy.next




