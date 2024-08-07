/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        int first = -1, last = -1;
        int prev = head.val, minDistance = Integer.MAX_VALUE, maxDistance = -1, idx = 0;
        ListNode curr = head.next;
        while (curr.next!=null){
            if ((prev < curr.val && curr.next.val < curr.val) || (prev > curr.val && curr.next.val > curr.val)){
                if (first==-1){
                    first = idx;
                }
                minDistance = Math.min(minDistance, last!=-1 ? idx-last : Integer.MAX_VALUE);
                last = idx;
            }
            idx++;
            prev = curr.val;
            curr = curr.next; 
        }
        if (first != -1 && last != -1 && first != last){
            maxDistance = last - first;
        }
        return new int[]{minDistance <= Math.pow(10,5) ? minDistance : -1, maxDistance};
    }
}
