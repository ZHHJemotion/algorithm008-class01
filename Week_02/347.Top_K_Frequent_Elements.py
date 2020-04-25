# Given a non-empty array of integers, return the k most frequent elements.
#
#  Example 1:
#
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
#
#
#  Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
#  Note:
#
#
#  You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
#  Your algorithm's time complexity must be better than O(n log n), where n is t
# he array's size.
#  It's guaranteed that the answer is unique, in other words the set of the top
# k frequent elements is unique.
#  You can return the answer in any order.
#
#  Related Topics Hash Table Heap


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp_dict = dict()
        for num in nums:
            if num not in tmp_dict:
                tmp_dict[num] = 1
            else:
                tmp_dict[num] += 1
        tmp_dict = dict(sorted(tmp_dict.items(), key=lambda x: x[1], reverse=True))
        res = list(tmp_dict.keys()[:k])

        return res

# leetcode submit region end(Prohibit modification and deletion)
