/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func balanceBST(root *TreeNode) *TreeNode {
    nodes := []int{}
    dfs(root,&nodes)
    return build(0,len(nodes)-1, &nodes)
}

func build(start, end int, nodes *[]int) *TreeNode{
    mid := (start + end)/2
    node := TreeNode{
        Val : (*nodes)[mid],
    }
    if mid - 1 >= start {
        node.Left = build(start, mid-1, nodes)
    }
    if mid + 1 <= end {
        node.Right = build(mid+1, end, nodes)
    }
    return &node
}
func dfs(root *TreeNode, nodes *[]int){
    if root == nil {
        return 
    }
    dfs(root.Left, nodes)
    (*nodes) = append((*nodes), root.Val)
    dfs(root.Right, nodes)
}
