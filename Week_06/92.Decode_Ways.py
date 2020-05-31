# A message containing letters from A-Z is being encoded to numbers using the fo
# llowing mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
#  Given a non-empty string containing only digits, determine the total number o
# f ways to decode it.
#
#  Example 1:
#
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
#  Example 2:
#
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)
# .
#  Related Topics String Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings(self, s: str) -> int:
        # 动态规划
        if not s:
            return 0

        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        else:
            dp[1] = 0

        for i in range(1, n):
            if s[i] != '0':
                dp[i + 1] += dp[i]
            if s[i - 1:i + 1] >= '10' and s[i - 1:i + 1] <= '26':
                dp[i + 1] += dp[i - 1]

        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
