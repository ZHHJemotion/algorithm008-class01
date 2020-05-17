# Let's play the minesweeper game (Wikipedia, online game)!
#
#  You are given a 2D char matrix representing the game board. 'M' represents an
#  unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a re
# vealed blank square that has no adjacent (above, below, left, right, and all 4 d
# iagonals) mines, digit ('1' to '8') represents how many mines are adjacent to th
# is revealed square, and finally 'X' represents a revealed mine.
#
#  Now given the next click position (row and column indices) among all the unre
# vealed squares ('M' or 'E'), return the board after revealing this position acco
# rding to the following rules:
#
#
#  If a mine ('M') is revealed, then the game is over - change it to 'X'.
#  If an empty square ('E') with no adjacent mines is revealed, then change it t
# o revealed blank ('B') and all of its adjacent unrevealed squares should be reve
# aled recursively.
#  If an empty square ('E') with at least one adjacent mine is revealed, then ch
# ange it to a digit ('1' to '8') representing the number of adjacent mines.
#  Return the board when no more squares will be revealed.
#
#
#
#
#  Example 1:
#
#
# Input:
#
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
#
# Click : [3,0]
#
# Output:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
#
#
#  Example 2:
#
#
# Input:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Click : [1,2]
#
# Output:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
#
#
#
#
#  Note:
#
#
#  The range of the input matrix's height and width is [1,50].
#  The click position will only be an unrevealed square ('M' or 'E'), which also
#  means the input board contains at least one clickable square.
#  The input board won't be a stage when game is over (some mines have been reve
# aled).
#  For simplicity, not mentioned rules should be ignored in this problem. For ex
# ample, you don't need to reveal all the unrevealed mines when the game is over,
# consider any cases that you will win the game or flag any squares.
#
#  Related Topics Depth-first Search Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # DFS
        def dfs(board, i, j):
            # terminator
            if board[i][j] != 'E':
                return

                # process current logic
            # 判断周围是否有地雷和统计地雷数量
            mine_num = 0
            directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < nr and 0 <= nj < nc and board[ni][nj] == 'M':
                    mine_num += 1
            # 为当前位置标 B 或者 周围地雷数量
            if mine_num == 0:
                board[i][j] = 'B'
            else:
                board[i][j] = str(mine_num)
                return

            # drill down
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < nr and 0 <= nj < nc:
                    dfs(board, ni, nj)

        if not board:
            return []

        i, j = click[0], click[1]
        # 挖到地雷
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        nr, nc = len(board), len(board[0])
        dfs(board, i, j)
        return board


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # BFS
        if not board:
            return []

        i, j = click[0], click[1]
        # 挖到地雷
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        nr, nc = len(board), len(board[0])
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        queue = collections.deque()
        queue.append((i, j))
        visited = []
        while queue:
            x, y = queue.popleft()
            visited.append((x, y))

            if board[x][y] == 'E':
                mine_num = 0
                # 遍历八个方向，计数地雷数量
                for d in directions:
                    ni, nj = x + d[0], y + d[1]
                    if 0 <= ni < nr and 0 <= nj < nc and board[ni][nj] == 'M':
                        mine_num += 1
                # 为当前位置标 B 或者 周围地雷数量
                if mine_num == 0:
                    board[x][y] = 'B'  # 周围八个位置没有地雷，标注B
                else:
                    board[x][y] = str(mine_num)  # 周围八个位置有地雷，标注地雷数量

                for d in directions:
                    ni, nj = x + d[0], y + d[1]
                    # 只对当前位置标B进行下一步的遍历
                    if 0 <= ni < nr and 0 <= nj < nc and board[x][y] == 'B':
                        visited.append((ni, nj))
                        queue.append((ni, nj))
        return board

# leetcode submit region end(Prohibit modification and deletion)
