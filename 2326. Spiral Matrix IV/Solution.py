# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1]*n for _ in range(m)]
        i = j = 0
        itr = head
        m_top = m
        m_bottom = 1
        n_top = n
        n_bottom = 0
        while itr:
            while itr and j < n_top:
                result[i][j] = itr.val
                itr = itr.next
                j += 1
            n_top -= 1
            j -= 1
            i += 1
            while itr and i < m_top:
                result[i][j] = itr.val
                itr = itr.next
                i += 1
            m_top -=1 
            i -= 1
            j -= 1
            while itr and j >= n_bottom:
                result[i][j] = itr.val
                itr = itr.next
                j-=1
            n_bottom += 1
            j += 1
            i -= 1
            while itr and i >= m_bottom:
                result[i][j] = itr.val
                itr = itr.next
                i -= 1
            m_bottom += 1
            i += 1
            j += 1
        return result
