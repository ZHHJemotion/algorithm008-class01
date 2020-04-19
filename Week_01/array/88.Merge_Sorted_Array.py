# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
#  sorted array.
#
#  Note:
#
#
#  The number of elements initialized in nums1 and nums2 are m and n respectivel
# y.
#  You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
#
#
#  Example:
#
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#  Related Topics Array Two Pointers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two pointer
        if m == 0:
            nums1[:n] = nums2[:n]
        elif n == 0:
            pass
        else:
            a, b = m - 1, n - 1
            k = m + n - 1
            while a >= 0 and b >= 0:
                if nums1[a] >= nums2[b]:
                    nums1[k] = nums1[a]
                    k -= 1
                    a -= 1
                else:
                    nums1[k] = nums2[b]
                    k -= 1
                    b -= 1
            if a >= 0:
                pass
            if b >= 0:
                nums1[:b + 1] = nums2[:b + 1]

# leetcode submit region end(Prohibit modification and deletion)
