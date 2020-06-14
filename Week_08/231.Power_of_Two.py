# Given an integer, write a function to determine if it is a power of two.
#
#  Example 1:
#
#
# Input: 1
# Output: true
# Explanation: 20 = 1
#
#
#  Example 2:
#
#
# Input: 16
# Output: true
# Explanation: 24 = 16
#
#  Example 3:
#
#
# Input: 218
# Output: false
#  Related Topics Math Bit Manipulation


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 位运算
        return n != 0 and (n & (n-1)) == 0

# leetcode submit region end(Prohibit modification and deletion)
