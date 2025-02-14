class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        highArea = -1
        while l < r:
            b = r - l
            h = min(heights[l], heights[r])
            area = b * h
            highArea = max(highArea, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return highArea
