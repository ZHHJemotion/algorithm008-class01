# Given an array nums, write a function to move all 0's to the end of it while m
# aintaining the relative order of the non-zero elements.
#
#  Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
#  Note:
#
#
#  You must do this in-place without making a copy of the array.
#  Minimize the total number of operations.
#  Related Topics Array Two Pointers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        return nums

# leetcode submit region end(Prohibit modification and deletion)
