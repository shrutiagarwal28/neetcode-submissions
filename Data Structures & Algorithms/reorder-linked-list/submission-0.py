# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the mid node:
        slow = head
        fast = head.next        

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        curr = slow.next
        slow.next = None
        prev = None

        # Reverse the second half:

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # l2 = prev
        # while l2:
        #     print(l2.val)
        #     l2 = l2.next
        
        # Merge the 2 lists
        l1 = head
        l2 = prev

        while l2:
            print(l1.val, l2.val)
            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2
            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2

        
     

