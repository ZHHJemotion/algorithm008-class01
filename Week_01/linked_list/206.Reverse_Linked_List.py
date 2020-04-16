# Reverse a singly linked list.
#
#  Example:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
#
#  Follow up:
#
#  A linked list can be reversed either iteratively or recursively. Could you im
# plement both?
#  Related Topics Linked List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursion
        if not head or not head.next:
            return head

        p = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return p

        # iteratively
        if not head or not head.next:
            return head

        pre = None
        cur = head

        while cur:
            cur.next, pre, cur = pre, cur, cur.next

        return pre
# leetcode submit region end(Prohibit modification and deletion)
