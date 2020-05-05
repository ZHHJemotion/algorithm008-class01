# Given a collection of numbers that might contain duplicates, return all possib
# le unique permutations.
#
#  Example:
#
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#
#  Related Topics Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 递归回溯
        def dfs(depth=0, path=[]):
            # terminator
            if depth == n:
                res.append(path[:])

            for i in range(n):
                if not visited[i]:
                    # pruning the duplicates
                    if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                        continue

                    # process current logic
                    visited[i] = True
                    path.append(nums[i])

                    # drill down
                    dfs(depth+1, path)

                    # backtrack
                    visited[i] = False
                    path.pop()

        res = []
        nums.sort()
        n = len(nums)
        visited = [False for _ in range(n)]


# leetcode submit region end(Prohibit modification and deletion)
