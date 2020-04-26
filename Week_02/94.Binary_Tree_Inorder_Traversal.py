# Given a binary tree, return the inorder traversal of its nodes' values.
#
#  Example:
#
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
#
#  Follow up: Recursive solution is trivial, could you do it iteratively?
#  Related Topics Hash Table Stack Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        res = []

        def helper(root):
            if not root:
                return

            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res

        # 迭代
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            stack.append(root.right)

        return res



# leetcode submit region end(Prohibit modification and deletion)
