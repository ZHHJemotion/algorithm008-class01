# Given a collection of distinct integers, return all possible permutations.
#
#  Example:
#
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
#  Related Topics Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 递归回溯
        def backtrack(first=0):
            # terminator
            if first == n:
                res.append(nums[:])

            for i in range(first, n):
                # process current logic
                nums[first], nums[i] = nums[i], nums[first]
                # drill down
                backtrack(first+1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        res = []
        n = len(nums)
        backtrack()
        return res

# leetcode submit region end(Prohibit modification and deletion)
