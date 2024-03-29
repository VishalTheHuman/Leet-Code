# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        n1 = head
        while count < k:
            n1 = n1.next
            count+=1
        n2 = head
        itr = n1
        while itr.next:
            itr = itr.next
            n2 = n2.next
        n1.val, n2.val = n2.val ,n1.val
        return head
