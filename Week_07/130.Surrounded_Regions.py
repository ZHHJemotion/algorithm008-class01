# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions su
# rrounded by 'X'.
#
#  A region is captured by flipping all 'O's into 'X's in that surrounded region
# .
#
#  Example:
#
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
#  After running your function, the board should be:
#
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
#  Explanation:
#
#  Surrounded regions shouldn’t be on the border, which means that any 'O' on th
# e border of the board are not flipped to 'X'. Any 'O' that is not on the border
# and it is not connected to an 'O' on the border will be flipped to 'X'. Two cell
# s are connected if they are adjacent cells connected horizontally or vertically.
#
#  Related Topics Depth-first Search Breadth-first Search Union Find


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # dfs
        def dfs(x, y):
            # current logic
            board[x][y] = '#'  # visited

            # drill down
            for di, dj in directions:
                xi, yj = x + di, y + dj
                if 0 <= xi < rows and 0 <= yj < cols and board[xi][yj] == 'O':
                    dfs(xi, yj)

        # 边界情况
        if not board or not board[0]:
            return []

        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])

        # 从第一列和最后一列开始搜索与边界'O'相连的区域
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)

        # 从第一行和最后一行开始搜索与边界'O'相连的区域
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)

        # 将 '#' 改为 'O'，将 'O' 改为 'X'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

        return board

# leetcode submit region end(Prohibit modification and deletion)
