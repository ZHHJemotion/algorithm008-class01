# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
#
#  Example:
#
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
#  Related Topics Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 递归回溯
        def backtrack(first=0, cur=[]):
            # terminator
            if len(cur) == k:
                res.append(cur[:])

            for i in range(first, n+1):
                # process current logics
                cur.append(i)
                # drill down
                backtrack(i+1, cur)
                # backtrack
                cur.pop()

        res = []
        backtrack()
        return res

# leetcode submit region end(Prohibit modification and deletion)
