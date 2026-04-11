class Solution:
    def maxArea(self, height: List[int]) -> int:
        # use two pointers that start at opposite sides
        left, right = 0, len(height) - 1
        max_water = 0

        while left <= right:
            min_height = min(height[left], height[right])
            distance = right - left
            # calculate the max water, and keep track of the max update if necessary
            water = min_height * distance
            max_water = max(max_water, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # return the max water
        return max_water
