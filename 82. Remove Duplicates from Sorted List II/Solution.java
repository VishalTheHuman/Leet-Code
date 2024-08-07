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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode();
        ListNode ptr = dummy;
        while (head!=null){
            if (head.next!=null && head.val==head.next.val){
                int val = head.val;
                while (head.next!=null && head.next.val==val){
                    head = head.next;
                }
                head = head.next;
            }else{
                ptr.next = head;
                ptr = ptr.next;
                head = head.next;
                ptr.next = null;
            }
            
        }
        return dummy.next;
    }
}
