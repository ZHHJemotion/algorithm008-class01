# Given an array of integers, return indices of the two numbers such that they a
# dd up to a specific target.
#
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice.
#
#  Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#  Related Topics Array Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力求解
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # using dict hash table
        # key means num, value means num's index
        tmp_dict = dict()
        res = [-1, -1]

        for i in range(len(nums)):
            if target - nums[i] in tmp_dict.keys():
                res[1] = i
                res[0] = tmp_dict.get(target - nums[i])
            else:
                tmp_dict[nums[i]] = i

        return res

# leetcode submit region end(Prohibit modification and deletion)
