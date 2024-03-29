# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        dummy = headA
        while dummy:
            s.add(dummy)
            dummy = dummy.next
        dummy = headB
        while dummy:
            if dummy in s:
                return dummy
            s.add(dummy)
            dummy = dummy.next
        return None
