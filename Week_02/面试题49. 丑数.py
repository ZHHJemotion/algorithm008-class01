# Write a program to find the n-th ugly number.
#
#  Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
#  Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ug
# ly numbers.
#
#  Note:
#
#
#  1 is typically treated as an ugly number.
#  n does not exceed 1690.
#  Related Topics Math Dynamic Programming Heap


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1] * n
        id2, id3, id5 = 0, 0, 0
        for i in range(1, n):
            res[i] = min(res[id2]*2, res[id3]*3, res[id5]*5)

            if res[i] == res[id2]*2:
                id2 += 1
            if res[i] == res[id3]*3:
                id3 += 1
            if res[i] == res[id5]*5:
                id5 += 1

        return res[n-1]

# leetcode submit region end(Prohibit modification and deletion)
