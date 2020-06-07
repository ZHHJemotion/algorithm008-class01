#
# There are N students in a class. Some of them are friends, while some are not.
#  Their friendship is transitive in nature. For example, if A is a direct friend
# of B, and B is a direct friend of C, then A is an indirect friend of C. And we d
# efined a friend circle is a group of students who are direct or indirect friends
# .
#
#
#
# Given a N*N matrix M representing the friend relationship between students in
# the class. If M[i][j] = 1, then the ith and jth students are direct friends with
#  each other, otherwise not. And you have to output the total number of friend ci
# rcles among all the students.
#
#
#  Example 1:
#
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a frie
# nd circle. The 2nd student himself is in a friend circle. So return 2.
#
#
#
#  Example 2:
#
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd stude
# nts are direct friends, so the 0th and 2nd students are indirect friends. All of
#  them are in the same friend circle, so return 1.
#
#
#
#
#  Note:
#
#  N is in range [1,200].
#  M[i][i] = 1 for all students.
#  If M[i][j] = 1, then M[j][i] = 1.
#
#  Related Topics Depth-first Search Union Find


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # DFS
        def dfs(i):
            visited[i] = 1

            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    dfs(j)

        visited = [0 for _ in range(len(M))]
        res = 0
        for i in range(len(M)):
            if visited[i] == 0:
                dfs(i)
                res += 1

        return res

        # 并查集
        if not M:
            return 0

        # 创建并查集
        n = len(M)
        p = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
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
            x = i;
            i = p[i];
            p[x] = root
        return root

# leetcode submit region end(Prohibit modification and deletion)
