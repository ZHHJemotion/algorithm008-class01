# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be val
# idated according to the following rules:
#
#
#  Each row must contain the digits 1-9 without repetition.
#  Each column must contain the digits 1-9 without repetition.
#  Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without r
# epetition.
#
#
#
# A partially filled sudoku which is valid.
#
#  The Sudoku board could be partially filled, where empty cells are filled with
#  the character '.'.
#
#  Example 1:
#
#
# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
#
#
#  Example 2:
#
#
# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
#
#     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is
# invalid.
#
#
#  Note:
#
#
#  A Sudoku board (partially filled) could be valid but is not necessarily solva
# ble.
#  Only the filled cells need to be validated according to the mentioned rules.
#
#  The given board contain only digits 1-9 and the character '.'.
#  The given board size is always 9x9.
#
#  Related Topics Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 暴力 hash
        # 初始化 行、列、每个3x3的block
        row = [dict() for _ in range(9)]
        col = [dict() for _ in range(9)]
        block = [dict() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    block_idx = (i // 3) * 3 + j // 3

                    # count
                    row[i][num] = row[i].get(num, 0) + 1
                    col[j][num] = col[j].get(num, 0) + 1
                    block[block_idx][num] = block[block_idx].get(num, 0) + 1

                    # check the amount more than 1 or not
                    if row[i][num] > 1 or col[j][num] > 1 or block[block_idx][num] > 1:
                        return False

        return True

# leetcode submit region end(Prohibit modification and deletion)
