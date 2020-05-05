# Given preorder and inorder traversal of a tree, construct the binary tree.
#
#  Note:
# You may assume that duplicates do not exist in the tree.
#
#  For example, given
#
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
#
#  Return the following binary tree:
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  Related Topics Array Tree Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 递归 1
        # terminator
        if not inorder:
            return None

        # process current logic
        root = TreeNode(preorder[0])
        mid = inorder.index([preorder[0]])

        # drill down
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

        # 递归 2
        def helper(left_idx=0, right_idx=len(inorder)):
            nonlocal pre_idx
            # terminator
            if left_idx == right_idx:
                return None

            # process current logic
            # get root val and root from preorder
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            pre_idx += 1

            # get the root index or inorder
            in_idx = idx_map[root_val]

            # drill down
            root.left = helper(left_idx, in_idx)
            root.right = helper(in_idx+1, right_idx)

            return root

        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()




# leetcode submit region end(Prohibit modification and deletion)
