# Given a 2D board and a list of words from the dictionary, find all words in th
# e board.
#
#  Each word must be constructed from letters of sequentially adjacent cell, whe
# re "adjacent" cells are those horizontally or vertically neighboring. The same l
# etter cell may not be used more than once in a word.
#
#
#
#  Example:
#
#
# Input:
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]
#
#
#
#
#  Note:
#
#
#  All inputs are consist of lowercase letters a-z.
#  The values of words are distinct.
#
#  Related Topics Backtracking Trie


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 字典树
        # 构造字典树
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        # dfs
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y, node, pre, visited):
            # terminator
            if '#' in node:  # 已有的字典树结束
                res.add(pre)  # 添加答案

            # drill down
            for di, dj in directions:
                xi = x + di
                yj = y + dj
                if 0 <= xi < rows and 0 <= yj < cols and board[xi][yj] in node and (xi, yj) not in visited:  # 可继续搜索
                    visited.add((xi, yj))
                    # drill down
                    dfs(xi, yj, node[board[xi][yj]], pre + board[xi][yj], visited)
                    # backtrace
                    visited.remove((xi, yj))

        res = set()
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:  # 可以继续搜索
                    dfs(i, j, trie[board[i][j]], board[i][j], {(i, j)})

        return list(res)

# leetcode submit region end(Prohibit modification and deletion)
