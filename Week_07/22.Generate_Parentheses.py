#
# Given n pairs of parentheses, write a function to generate all combinations of
#  well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#  Related Topics String Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 递归剪枝
        res = []

        def generate(left=0, right=0, s=''):
            # terminator
            if len(s) >= 2 * n:
                res.append(s)

            # drill down
            if left < n:
                generate(left + 1, right, s + '(')
            if right < left:
                generate(left, right + 1, s + ')')

        generate()
        return res

# leetcode submit region end(Prohibit modification and deletion)
