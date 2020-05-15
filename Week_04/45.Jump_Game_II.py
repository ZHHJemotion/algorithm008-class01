# Given an array of non-negative integers, you are initially positioned at the f
# irst index of the array.
#
#  Each element in the array represents your maximum jump length at that positio
# n.
#
#  Your goal is to reach the last index in the minimum number of jumps.
#
#  Example:
#
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#  Note:
#
#  You can assume that you can always reach the last index.
#  Related Topics Array Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 正向贪心
        max_p, end, step = 0, 0, 0
        for i in range(len(nums)-1):
            if max_p >= i:  # 当前位置是能到达的
                max_p = max(max_p, i+nums[i])  # 当前步数能到达的最远距离
                if i == end:  # 当前步数所有的可能性都遍历完了
                    end = max_p
                    step += 1
        return step

        # 反向贪心
        p = len(nums)-1
        step = 0
        while p:
            for i in range(0, p):
                if i+nums[i] >= p:
                    p = i
                    step += 1
                    break
        return step






# leetcode submit region end(Prohibit modification and deletion)
