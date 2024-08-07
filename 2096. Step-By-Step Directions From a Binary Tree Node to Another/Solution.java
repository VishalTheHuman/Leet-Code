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
    int start, end;
    String startPath, destPath;
    public String getDirections(TreeNode root, int startValue, int destValue) {
        start = startValue; 
        end = destValue;
        solve(root, new StringBuilder());
        int toTravese = Math.min(startPath.length(), destPath.length()); 
        int i = 0;
        for(i=0;i<toTravese;i++){
            if(startPath.charAt(i)!=destPath.charAt(i)){
                break;
            }
        }
        StringBuilder result = new StringBuilder();
        for(int j=i; j < startPath.length();j++){
            result.append('U');
        }
        for(int j=i; j < destPath.length();j++){
            result.append(destPath.charAt(j));
        }
        return result.toString();
    }

    public void solve(TreeNode root, StringBuilder path){
        if(root==null){
            return;
        }
        solve(root.left, path.append('L'));
        path.deleteCharAt(path.length()-1);
        solve(root.right, path.append('R'));
        path.deleteCharAt(path.length()-1);
        if (root.val==start){
            startPath = path.toString();
        }
        if (root.val==end){
            destPath = path.toString();
        }
    }
}
