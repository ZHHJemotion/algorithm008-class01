# Given an array of non-negative integers, you are initially positioned at the f
# irst index of the array.
#
#  Each element in the array represents your maximum jump length at that positio
# n.
#
#  Determine if you are able to reach the last index.
#
#
#  Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
#  Example 2:
#
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jum
# p length is 0, which makes it impossible to reach the last index.
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 3 * 10^4
#  0 <= nums[i][j] <= 10^5
#
#  Related Topics Array Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心
        if 0 not in nums:
            return True
        if len(nums) < 2:
            return True

        max_p = nums[0]  # 第一步的距离
        for i in range(1, len(nums)-1):
            if i <= max_p:  # 当前位置是能到达的
                max_p = max(max_p, i+nums[i])

        return max_p >= len(nums)-1




# leetcode submit region end(Prohibit modification and deletion)
