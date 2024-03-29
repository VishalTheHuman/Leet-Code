# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        itr = head
        while itr: 
            count += 1
            itr = itr.next
        elements_in_basket = count//k
        val = count%k 
        remain = val if val else 0
        baskets = [None]*k
        itr = head
        for i  in range(len(baskets)):
            size = elements_in_basket 
            prev = None
            baskets[i] = itr if itr else None
            while itr and size:
                size -= 1
                prev = itr
                itr = itr.next
            if remain:
                remain -= 1
                prev = itr
                itr = itr.next
            if prev:
                prev.next = None
        return baskets
