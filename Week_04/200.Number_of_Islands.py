# Given a 2d grid map of '1's (land) and '0's (water), count the number of islan
# ds. An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all su
# rrounded by water.
#
#  Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
#  Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#  Related Topics Depth-first Search Breadth-first Search Union Find


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_island = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_island += 1
                    grid[r][c] = '0'  # visited

                    queue = deque()
                    queue.append((r, c))
                    while queue:
                        cur_r, cur_c = queue.popleft()
                        for x, y in [(cur_r-1, cur_c), (cur_r+1, cur_c), (cur_r, cur_c-1), (cur_r, cur_c+1)]:
                            if 0 <= x < nr and 0 <= y < nr and grid[x][y] == '1':
                                queue.append((x, y))
                                grid[x][y] = '0'  # visited
        return num_island

        # DFS
        def dfs(grid, r, c):
            grid[r][c] = '0'
            for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= x < nr and 0 <= y < nr and grid[x][y] == '1':
                    dfs(grid, x, y)

        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_island = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_island += 1
                    grid[r][c] = '0'  # visited
                    dfs(grid, r, c)

        return num_island


# leetcode submit region end(Prohibit modification and deletion)
