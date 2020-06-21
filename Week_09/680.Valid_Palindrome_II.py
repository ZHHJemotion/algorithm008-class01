#
# Given a non-empty string s, you may delete at most one character. Judge whethe
# r you can make it a palindrome.
#
#
#  Example 1:
#
# Input: "aba"
# Output: True
#
#
#
#  Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#
#
#
#  Note:
#
#  The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
#
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 双指针夹逼
        ispalindrome = lambda x: x == x[::-1]
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return ispalindrome(s[l:r]) or ispalindrome(s[l + 1:r + 1])
        return True

# leetcode submit region end(Prohibit modification and deletion)
