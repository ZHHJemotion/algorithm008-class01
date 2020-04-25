# Given an array of strings, group anagrams together.
#
#  Example:
#
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
#  Note:
#
#
#  All inputs will be in lowercase.
#  The order of your output does not matter.
#
#  Related Topics Hash Table String

import collections

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using hash dict
        res = collections.defaultdict(list)
        for s in strs:
            res[str(sorted(s))].append(s)

        return res.values()

# leetcode submit region end(Prohibit modification and deletion)
