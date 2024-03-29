# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, arr: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for ind, node in enumerate(arr):
            if node:
                heapq.heappush(heap, (node.val, ind))
        if not heap:
            return None
        head = curr = ListNode()
        while heap:
            _, ind = heapq.heappop(heap)
            node = arr[ind]
            if arr[ind].next:
                heapq.heappush(heap, (arr[ind].next.val, ind))
                arr[ind] = arr[ind].next
            curr.next = node
            node.next = None
            curr = node
        return head.next
