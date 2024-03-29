# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 2
        itr = head.next
        prev = head
        while itr:
            count = 1
            while itr and count < i:
                itr = itr.next
                count+=1
            if count%2==0 and itr:
                temp = itr.next
                itr.next = None
                new_prev = prev.next
                prev.next = self.reverse(prev.next)
                itr = temp
                new_prev.next = itr
                prev = new_prev
            elif itr:
                prev = itr
                itr = itr.next
            elif count%2!=0:
                prev.next = self.reverse(prev.next)
            i+=1
        return head

    def reverse(self,head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
        
