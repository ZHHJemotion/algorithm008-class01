# Given a string S, return the "reversed" string where all characters that are n
# ot a letter stay in the same place, and all letters reverse their positions.
#
#
#
#
#
#
#
#
#
#
#
#
#
#  Example 1:
#
#
# Input: "ab-cd"
# Output: "dc-ba"
#
#
#
#  Example 2:
#
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#
#
#
#  Example 3:
#
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
#
#
#
#  Note:
#
#
#  S.length <= 100
#  33 <= S[i].ASCIIcode <= 122
#  S doesn't contain \ or "
#
#
#
#
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [c for c in S if c.isalpha()]
        res = []
        for c in S:
            if c.isalpha():
                res.append(letters.pop())
            else:
                res.append(c)

        return ''.join(res)

# leetcode submit region end(Prohibit modification and deletion)
