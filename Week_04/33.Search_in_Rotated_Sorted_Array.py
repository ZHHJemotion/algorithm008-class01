# Suppose an array sorted in ascending order is rotated at some pivot unknown to
#  you beforehand.
#
#  (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
#  You are given a target value to search. If found in the array return its inde
# x, otherwise return -1.
#
#  You may assume no duplicate exists in the array.
#
#  Your algorithm's runtime complexity must be in the order of O(log n).
#
#  Example 1:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
#
#  Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#  Related Topics Array Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            # l-mid 有序
            elif nums[mid] > target:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # mid-r 有序
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)
