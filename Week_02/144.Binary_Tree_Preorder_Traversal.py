# Given a binary tree, return the preorder traversal of its nodes' values.
#
#  Example:
#
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,2,3]
#
#
#  Follow up: Recursive solution is trivial, could you do it iteratively?
#  Related Topics Stack Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        res = []

        def helper(root):
            if not root:
                return

            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        # return res

        # 迭代
        res = []
        stack = []
        while stack or res:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            stack.append(root.right)

        return res



# leetcode submit region end(Prohibit modification and deletion)
