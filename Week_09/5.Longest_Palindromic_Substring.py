# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
#  Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
#  Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#  Related Topics String Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            # 只有下面这一行代码不一样
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]

# leetcode submit region end(Prohibit modification and deletion)
