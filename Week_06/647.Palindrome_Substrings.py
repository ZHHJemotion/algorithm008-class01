# Given a string, your task is to count how many palindromic substrings in this
# string.
#
#  The substrings with different start indexes or end indexes are counted as dif
# ferent substrings even they consist of same characters.
#
#  Example 1:
#
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
#
#
#  Example 2:
#
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
#
#  Note:
#
#
#  The input string length won't exceed 1000.
#
#
#  Related Topics String Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 动态规划
        if not s:
            return 0

        n = len(s)
        res = n
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True  # 对角线

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1:  # 相邻
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    res += 1

        return res

# leetcode submit region end(Prohibit modification and deletion)

