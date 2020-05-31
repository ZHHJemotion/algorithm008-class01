# Given an array which consists of non-negative integers and an integer m, you c
# an split the array into m non-empty continuous subarrays. Write an algorithm to
# minimize the largest sum among these m subarrays.
#
#
#  Note:
# If n is the length of array, assume the following constraints are satisfied:
#
#  1 ≤ n ≤ 1000
#  1 ≤ m ≤ min(50, n)
#
#
#
#  Examples:
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#
#  Related Topics Binary Search Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 动态规划
        n = len(nums)
        if not n:
            return 0

        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        sub = [0 for _ in range(n + 1)]

        for i in range(n):
            sub[i + 1] = sub[i] + nums[i]

        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(0, i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sub[i] - sub[k]))

        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
