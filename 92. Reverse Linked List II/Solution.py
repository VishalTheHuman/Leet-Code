# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        itr = head
        prev = None
        while i<left:
            i+=1
            prev = itr
            itr = itr.next
        left = itr
        while i<right:
            i+=1
            itr = itr.next
        right = itr.next
        itr.next = None
        if prev:
            prev.next = self.reverse(left)
        else:
            head = self.reverse(left)
        if right:
            while itr.next:
                itr = itr.next
            itr.next = right
        return head

    def reverse(self,head):
        prev = None
        while head:
            nxt = head
            head = head.next
            nxt.next = prev
            prev = nxt
        return prev
