# Suppose an array sorted in ascending order is rotated at some pivot unknown to
#  you beforehand.
#
#  (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
#  Find the minimum element.
#
#  You may assume no duplicate exists in the array.
#
#  Example 1:
#
#
# Input: [3,4,5,1,2]
# Output: 1
#
#
#  Example 2:
#
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
#
#  Related Topics Array Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 二分查找
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums)-1
        if nums[l] < nums[r]:
            return nums[0]

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]

            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1

# leetcode submit region end(Prohibit modification and deletion)
