# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rec
# tangle in the matrix such that its sum is no larger than k.
#
#  Example:
#
#
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
#              and 2 is the max number no larger than k (k = 2).
#
#  Note:
#
#
#  The rectangle inside the matrix must have an area > 0.
#  What if the number of rows is much larger than the number of columns?
#  Related Topics Binary Search Dynamic Programming Queue


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        maxSum = -9999999
        horizontalSum = [[0 for j in range(0, len(matrix[0]) + 1)] for i in range(0, len(matrix))]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                horizontalSum[i][j] = horizontalSum[i][j - 1] + matrix[i][j]
        for cola in range(0, len(matrix[0])):
            for colb in range(cola, len(matrix[0])):
                bilist, vsum = [0], 0
                for i in range(0, len(matrix)):
                    vsumj = horizontalSum[i][colb] - horizontalSum[i][cola - 1]
                    vsum += vsumj
                    i = bisect.bisect_left(bilist, vsum - k)
                    if i < len(bilist):
                        maxSum = max(maxSum, vsum - bilist[i])
                    bisect.insort(bilist, vsum)
        return maxSum

# leetcode submit region end(Prohibit modification and deletion)
