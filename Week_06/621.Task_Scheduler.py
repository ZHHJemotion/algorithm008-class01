# Given a char array representing tasks CPU need to do. It contains capital lett
# ers A to Z where different letters represent different tasks. Tasks could be don
# e without original order. Each task could be done in one interval. For each inte
# rval, CPU could finish one task or just be idle.
#
#  However, there is a non-negative cooling interval n that means between two sa
# me tasks, there must be at least n intervals that CPU are doing different tasks
# or just be idle.
#
#  You need to return the least number of intervals the CPU will take to finish
# all the given tasks.
#
#
#
#  Example:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
#
#
#
#  Constraints:
#
#
#  The number of tasks is in the range [1, 10000].
#  The integer n is in the range [0, 100].
#
#  Related Topics Array Greedy Queue


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for t in tasks:
            count[ord(t) - ord("A")] += 1
        count = sorted(count, reverse=True)
        rounds = count[0] - 1
        # 1) 至少需要rounds*(n+1)个时间槽来完成所有任务
        ans = rounds * (n + 1)
        for i in range(0, 26):
            # 2) 如果有一个任务在rounds这么多轮没有完全执行完，那就把多的放到第rounds+1轮执行.
            ans += max(0, count[i] - rounds)
        # 3) 最后这个max是精华
        return max(ans, len(tasks))

# leetcode submit region end(Prohibit modification and deletion)
