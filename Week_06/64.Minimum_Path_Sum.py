# Given a m x n grid filled with non-negative numbers, find a path from top left
#  to bottom right which minimizes the sum of all numbers along its path.
#
#  Note: You can only move either down or right at any point in time.
#
#  Example:
#
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
#  Related Topics Array Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 动态规划
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, cols):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
