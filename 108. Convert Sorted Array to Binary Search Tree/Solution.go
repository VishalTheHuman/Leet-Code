/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
    return build(0,len(nums)-1, &nums)
}

func build(start, end int, nodes *[]int) *TreeNode{
    if start > end {
        return nil
    }
    mid := (start+end)/2
    return &TreeNode{
        Val : (*nodes)[mid], 
        Left : build(start,mid-1, nodes),
        Right : build(mid+1, end, nodes),
    }
}
