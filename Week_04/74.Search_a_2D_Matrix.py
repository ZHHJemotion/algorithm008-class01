# Write an efficient algorithm that searches for a value in an m x n matrix. Thi
# s matrix has the following properties:
#
#
#  Integers in each row are sorted from left to right.
#  The first integer of each row is greater than the last integer of the previou
# s row.
#
#
#  Example 1:
#
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
#
#
#  Example 2:
#
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false
#  Related Topics Array Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二分查找
        # 2D -> 1D
        new_matrix = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))]

        l, r = 0, len(new_matrix)-1
        while l <= r:
            mid = (l+r) // 2
            if new_matrix[mid] == target:
                return True
            elif new_matrix[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

# leetcode submit region end(Prohibit modification and deletion)
