# Given a string S and a string T, find the minimum window in S which will conta
# in all the characters in T in complexity O(n).
#
#  Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
#  Note:
#
#
#  If there is no such window in S that covers all characters in T, return the e
# mpty string "".
#  If there is such window, you are guaranteed that there will always be only on
# e unique minimum window in S.
#
#  Related Topics Hash Table Two Pointers String Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口， 双指针
        l, r = 0, 0
        t = collections.Counter(t)
        lookup = collections.Counter()
        min_len = float("inf")
        res = ""

        while r < len(s):
            lookup[s[r]] += 1
            r += 1

            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                if r - l < min_len:
                    res = s[l:r]
                    min_len = r - l
                lookup[s[l]] -= 1
                l += 1

        return res

        # 动态规划


# leetcode submit region end(Prohibit modification and deletion)
