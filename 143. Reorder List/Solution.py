# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        stk = []
        while slow:
            stk.append(slow)
            slow = slow.next
        itr = head
        while len(stk)>1:
            node = stk.pop()
            itr.next,node.next = node,itr.next
            itr = node.next
        itr.next = stk.pop()
        itr.next.next = None
