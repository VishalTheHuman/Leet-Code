# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, itr: Optional[ListNode], x: int) -> Optional[ListNode]:
        first_head = first = ListNode()
        second_head = second = ListNode()
        while itr:
            nxt = itr.next
            itr.next = None
            if itr.val >= x:
                second.next = itr
                second = second.next
            else:
                first.next = itr
                first = first.next
            itr = nxt
        first.next = second_head.next
        return first_head.next
