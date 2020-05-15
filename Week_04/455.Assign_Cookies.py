#
# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie. Each child i has a greed fac
# tor gi, which is the minimum size of a cookie that the child will be content wit
# h; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to t
# he child i, and the child i will be content. Your goal is to maximize the number
#  of your content children and output the maximum number.
#
#
#  Note:
# You may assume the greed factor is always positive.
# You cannot assign more than one cookie to one child.
#
#
#  Example 1:
#
# Input: [1,2,3], [1,1]
#
# Output: 1
#
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 childre
# n are 1, 2, 3.
# And even though you have 2 cookies, since their size is both 1, you could only
#  make the child whose greed factor is 1 content.
# You need to output 1.
#
#
#
#  Example 2:
#
# Input: [1,2], [1,2,3]
#
# Output: 2
#
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 childre
# n are 1, 2.
# You have 3 cookies and their sizes are big enough to gratify all of the childr
# en,
# You need to output 2.
#
#  Related Topics Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 贪心
        g.sort()
        s.sort()

        if not g or not s or s[-1] < g[0]:
            return 0

        si, gi = 0, 0
        count = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                count += 1
                s[si] = 0
                gi += 1
            si += 1

        return count

# leetcode submit region end(Prohibit modification and deletion)
