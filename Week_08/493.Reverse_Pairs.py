# Given an array nums, we call (i, j) an important reverse pair if i < j and num
# s[i] > 2*nums[j].
#
#  You need to return the number of important reverse pairs in the given array.
#
#
#  Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
#
#
#  Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
#
#
#  Note:
#
#  The length of the given array will not exceed 50,000.
#  All the numbers in the input array are in the range of 32-bit integer.
#
#  Related Topics Binary Search Divide and Conquer Sort Binary Indexed Tree Segm
# ent Tree


# leetcode submit region begin(Prohibit modification and deletion)
import bisect
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 归并排序
        if not nums:
            return 0
        return self.merge_sort(nums)[1]

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums, 0

        m = len(nums) // 2
        left, countl = self.merge_sort(nums[:m])
        right, countr = self.merge_sort(nums[m:])

        count = countl + countr
        for r in right:
            temp = len(left) - bisect.bisect(left, 2 * r)
            if temp == 0:
                break
            count += temp

        return sorted(left + right), count

# leetcode submit region end(Prohibit modification and deletion)
