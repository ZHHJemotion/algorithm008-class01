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
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        def dfs(grid, r, c):
            grid[r][c] = '0'  # visited
            for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
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

                    neighbours = collections.deque([(r, c)])
                    while neighbours:
                        cur_r, cur_c = neighbours.popleft()
                        for x, y in [(cur_r-1, cur_c), (cur_r+1, cur_c), (cur_r, cur_c-1), (cur_r, cur_c+1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                                neighbours.append((x, y))
                                grid[x][y] = '0'  # visited

        return num_island

        # 并查集
        if not grid:
            return 0

        # 创建并查集
        n = len(grid)
        p = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    self.union(p, i, j)

        return len(list(set(self.parent(p, i) for i in range(n))))

        # 合并

    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2

        # 找 parent

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:  # 路径压缩 ?
            x = i
            i = p[i]
            p[x] = root
        return root

# leetcode submit region end(Prohibit modification and deletion)
