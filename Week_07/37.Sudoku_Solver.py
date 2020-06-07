# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
#  A sudoku solution must satisfy all of the following rules:
#
#
#  Each of the digits 1-9 must occur exactly once in each row.
#  Each of the digits 1-9 must occur exactly once in each column.
#  Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-b
# oxes of the grid.
#
#
#  Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
#  Note:
#
#
#  The given board contain only digits 1-9 and the character '.'.
#  You may assume that the given Sudoku puzzle will have a single unique solutio
# n.
#  The given board size is always 9x9.
#
#  Related Topics Hash Table Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 收集行/列/block所剩余的数字
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]

        # 收集需要填空的位置
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    # 更新可用数字
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        # 回溯
        def backtrace(iter=0):
            # terminator
            if iter == len(empty):  # 解题完毕
                return True

            # process current logic
            i, j = empty[iter]
            b_idx = (i // 3) * 3 + j // 3
            for val in row[i] & col[j] & block[b_idx]:
                row[i].remove(val)
                col[j].remove(val)
                block[b_idx].remove(val)
                board[i][j] = str(val)

                # drill down
                if backtrace(iter + 1):
                    return True

                # backtrace
                row[i].add(val)
                col[j].add(val)
                block[b_idx].add(val)

            return False

        backtrace()

# leetcode submit region end(Prohibit modification and deletion)
