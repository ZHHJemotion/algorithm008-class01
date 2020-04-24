# Given two strings s and t , write a function to determine if t is an anagram o
# f s.
#
#  Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
#  Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
#  Note:
# You may assume the string contains only lowercase alphabets.
#
#  Follow up:
# What if the inputs contain unicode characters? How would you adapt your soluti
# on to such case?
#  Related Topics Hash Table Sort


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# leetcode submit region end(Prohibit modification and deletion)
