# The n-queens puzzle is the problem of placing n queens on an n×n chessboard su
# ch that no two queens attack each other.
#
#
#
#  Given an integer n, return all distinct solutions to the n-queens puzzle.
#
#  Each solution contains a distinct board configuration of the n-queens' placem
# ent, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
#  Example:
#
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as show
# n above.
#
#  Related Topics Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # DFS
        def dfs(queens, xy_diff, xy_sum):
            # queens 表示皇后所在的列
            p = len(queens)

            # terminator
            if p == n:
                res.append(queens)
                return

                # drill down
            for q in range(n):
                if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                    dfs(queens + [q], xy_diff + [p - q], xy_sum + [p + q])

        res = []
        dfs([], [], [])
        return [["." * col + "Q" + "." * (n - col - 1) for col in sol] for sol in res]

# leetcode submit region end(Prohibit modification and deletion)
