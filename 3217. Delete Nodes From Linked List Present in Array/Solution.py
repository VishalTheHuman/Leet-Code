# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        obj = set(nums)
        dummy = ListNode()
        ptr = dummy
        while head:
            if head.val not in obj:
                ptr.next = head
                ptr = ptr.next
            nxt = head.next 
            head.next = None
            head = nxt
        return dummy.next
