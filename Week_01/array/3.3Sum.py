# Given an array nums of n integers, are there elements a, b, c in nums such tha
# t a + b + c = 0? Find all unique triplets in the array which gives the sum of ze
# ro.
#
#  Note:
#
#  The solution set must not contain duplicate triplets.
#
#  Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  Related Topics Array Two Pointers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        if n < 3 or not nums:
            return []

        # sort
        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                return res

            # remove duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L, R = i + 1, n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    # remove duplicate
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    # remove duplicate
                    while L > R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    L += 1

        return res

# leetcode submit region end(Prohibit modification and deletion)
