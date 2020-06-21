#
# Given a string and an integer k, you need to reverse the first k characters fo
# r every 2k characters counting from the start of the string. If there are less t
# han k characters left, reverse all of them. If there are less than 2k but greate
# r than or equal to k characters, then reverse the first k characters and left th
# e other as original.
#
#
#  Example:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#
#
#
# Restrictions:
#
#  The string consists of lower English letters only.
#  Length of the given string and k will in the range [1, 10000]
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        flag = True
        for i in range(0, len(s), k):
            if flag:
                res += s[i: i + k][::-1]
            else:
                res += s[i: i + k]

            flag = not flag

        return res

# leetcode submit region end(Prohibit modification and deletion)
