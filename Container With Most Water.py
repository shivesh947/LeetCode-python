class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        res = 0
        while  left < right:
            water = min(height[left], height[right]) * (right - left)
            res = water if res < water else res
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    print s.maxArea([1,1])
