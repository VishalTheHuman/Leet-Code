# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        while head:
            while stk and head.val > stk[-1].val:
                stk.pop()
            stk.append(head)
            head = head.next
        
        for i in range(len(stk)-1):
            stk[i].next = stk[i+1]
        if stk: 
            stk[-1].next = None
            return stk[0]
        return None
