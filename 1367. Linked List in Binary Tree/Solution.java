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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean result = false;
    public boolean isSubPath(ListNode head, TreeNode root) {
        dfs(head, root);
        return result;
    }
    
    public void dfs(ListNode head, TreeNode root){
        if (root==null){
            return;
        }
        if (head.val==root.val){
            find(head.next, root.left);
            find(head.next, root.right);
        }
        dfs(head, root.left); 
        dfs(head, root.right);
    }

    public void find(ListNode head, TreeNode root){
        if (head==null){
            result = true; 
            return;
        }
        if (root==null || head.val != root.val) return;
        find(head.next, root.left);
        find(head.next, root.right);
    }
}
