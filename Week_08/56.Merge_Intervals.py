# Given a collection of intervals, merge all overlapping intervals.
#
#  Example 1:
#
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
#
#  Example 2:
#
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#  NOTE: input types have been changed on April 15, 2019. Please reset to defaul
# t code definition to get new method signature.
#  Related Topics Array Sort


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            else:
                size = len(res)
                if (res[size - 1][0] <= intervals[i][0]) and (intervals[i][0] <= res[size - 1][1]):
                    res[size - 1][1] = max(res[size - 1][1], intervals[i][1])
                else:
                    res.append(intervals[i])

        return res

# leetcode submit region end(Prohibit modification and deletion)
