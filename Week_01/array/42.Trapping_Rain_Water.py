# Given n non-negative integers representing an elevation map where the width of
#  each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos
#  for contributing this image!
#
#  Example:
#
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#  Related Topics Array Two Pointers Stack


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        max_h = max(height)
        rain = max_h * len(height) - sum(height)

        m_h = 0
        for h in height:
            if h >= max_h:
                break
            m_h = max(m_h, h)
            rain -= max_h - m_h

        m_h = 0
        for h in reversed(height):
            if h >= max_h:
                break
            m_h = max(m_h, h)
            rain -= max_h - m_h

# leetcode submit region end(Prohibit modification and deletion)
