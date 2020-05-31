# Given a 2D binary matrix filled with 0's and 1's, find the largest square cont
# aining only 1's and return its area.
#
#  Example:
#
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 动态规划
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        max_side = 0

        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:  # 边界
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

                    max_side = max(max_side, dp[i][j])

        return max_side * max_side

# leetcode submit region end(Prohibit modification and deletion)
