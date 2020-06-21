# Given an input string (s) and a pattern (p), implement wildcard pattern matchi
# ng with support for '?' and '*'.
#
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
#
#  The matching should cover the entire input string (not partial).
#
#  Note:
#
#
#  s could be empty and contains only lowercase letters a-z.
#  p could be empty and contains only lowercase letters a-z, and characters like
#  ? or *.
#
#
#  Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
#  Example 2:
#
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
#
#  Example 3:
#
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not mat
# ch 'b'.
#
#
#  Example 4:
#
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' ma
# tches the substring "dce".
#
#
#  Example 5:
#
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
#
#  Related Topics String Dynamic Programming Backtracking Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        # base cases
        if p == s or p == '*':
            return True
        if p == '' or s == '':
            return False

        # init all matrix except [0][0] element as False
        d = [[False] * (s_len + 1) for _ in range(p_len + 1)]
        d[0][0] = True

        # DP compute
        for p_idx in range(1, p_len + 1):
            # the current character in the pattern is '*'
            if p[p_idx - 1] == '*':
                s_idx = 1

                # d[p_idx - 1][s_idx - 1] is a string-pattern match
                # on the previous step, i.e. one character before.
                # Find the first idx in string with the previous math.
                while not d[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
                    s_idx += 1

                # If (string) matches (pattern),
                # when (string) matches (pattern)* as well
                d[p_idx][s_idx - 1] = d[p_idx - 1][s_idx - 1]

                # If (string) matches (pattern),
                # when (string)(whatever_characters) matches (pattern)* as well
                while s_idx < s_len + 1:
                    d[p_idx][s_idx] = True
                    s_idx += 1

            # the current character in the pattern is '?'
            elif p[p_idx - 1] == '?':
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1]
                    # the current character in the pattern is not '*' or '?'
            else:
                for s_idx in range(1, s_len + 1):
                    # Match is possible if there is a previous match
                    # and current characters are the same
                    d[p_idx][s_idx] = \
                        d[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]

        return d[p_len][s_len]

# leetcode submit region end(Prohibit modification and deletion)
