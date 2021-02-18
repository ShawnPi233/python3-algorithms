"""
方法一: 深度优先搜索(DFS) 之 "自底向上" 的递归
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/

解题模板：
1. return specific value for null node
2. left_ans = bottom_up(root.left)          // call function recursively for left child
3. right_ans = bottom_up(root.right)        // call function recursively for right child
4. return answers                           // answer <-- left_ans, right_ans, root.val

适用场景：
当遇到树问题时，请先思考一下：
对于树中的任意一个节点，如果你知道它的子节点的答案，你能计算出该节点的答案吗？

解题思路：
如果我们知道一个根节点，以其左子节点为根的左子树的最大深度为 l 和以其右子节点为根的右子树的最大深度为 r，我们是否可以回答前面的问题？
当然可以，我们可以选择它们之间的最大值，再加上 1 来获得根节点所在的子树的最大深度：x = max(l，r) + 1


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点在递归中只被遍历一次。
空间复杂度：O(h)，其中 h 表示二叉树的高度。递归函数需要函数栈空间，而栈空间取决于递归的深度，因此空间复杂度等于二叉树的高度。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
