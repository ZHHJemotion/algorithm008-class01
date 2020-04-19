# Merge two sorted linked lists and return it as a new list. The new list should
#  be made by splicing together the nodes of the first two lists.
#
#  Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#  Related Topics Linked List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # terminator
        if not l1:
            return l2
        if not l2:
            return l1

        # drill down
        while l1 and l2:
            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l2
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l1

# leetcode submit region end(Prohibit modification and deletion)
