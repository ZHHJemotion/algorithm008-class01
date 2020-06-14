# The n-queens puzzle is the problem of placing n queens on an n×n chessboard su
# ch that no two queens attack each other.
#
#
#
#  Given an integer n, return the number of distinct solutions to the n-queens p
# uzzle.
#
#  Example:
#
#
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown
# below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#
#  Related Topics Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalNQueens(self, n: int) -> int:
        # DFS
        def dfs(queens, xy_diff, xy_sum):
            # queens 表示皇后所在的列
            p = len(queens)

            # terminator
            if p == n:
                self.res += 1
                return

            # dril down
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    dfs(queens+[q], xy_diff+[p-q], xy_sum+[p+q])

        self.res = 0
        dfs([], [], [])
        return self.res

        # 位运算
        def dfs(n, row, cols, pie, na):
            # terminator
            if row >= n:
                self.count += 1
                return

            # current logics
            bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 获取当前所有空位1

            # drill down
            while bits:
                p = bits & -bits  # 获取最低位的1
                bits = bits & (bits - 1)  # 将皇后放到p位置上 置为0
                dfs(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)

        if not n:
            return 0
        self.count = 0
        dfs(n, 0, 0, 0, 0)
        return self.count

# leetcode submit region end(Prohibit modification and deletion)
