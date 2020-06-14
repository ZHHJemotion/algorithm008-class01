# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all ele
# ments in arr2 are also in arr1.
#
#  Sort the elements of arr1 such that the relative ordering of items in arr1 ar
# e the same as in arr2. Elements that don't appear in arr2 should be placed at th
# e end of arr1 in ascending order.
#
#
#  Example 1:
#  Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
#
#
#  Constraints:
#
#
#  arr1.length, arr2.length <= 1000
#  0 <= arr1[i], arr2[i] <= 1000
#  Each arr2[i] is distinct.
#  Each arr2[i] is in arr1.
#
#  Related Topics Array Sort


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 计数排序
        # 初始化计数
        counter = [0 for _ in range(1001)]

        # 统计 arr1 中的所有元素出现次数
        for num in arr1:
            counter[num] += 1

        # 在 arr1 中，也在 arr2 中
        res = []
        for num in arr2:
            res += [num] * counter[num]
            counter[num] = 0

        # arr1 剩余的加入
        for i in range(len(counter)):
            res += [i] * counter[i]

        return res

# leetcode submit region end(Prohibit modification and deletion)
