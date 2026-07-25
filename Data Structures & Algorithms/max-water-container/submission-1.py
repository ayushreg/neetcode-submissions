class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Left and right pointers
        l = 0
        r = len(heights) - 1

        # To hold final result
        max_water = 0

        # Loop until left and right cross
        while(l < r):
            # get the area, where the length is r - l and height is the lower height
            # If its larger than our current max we can make that our max
            area = (r - l) * (min(heights[l],heights[r]))
            max_water = max(max_water, area)

            # Now we need to check the next pair by incrementing/decrementing the lower height
            if(heights[l] < heights[r]):
                l += 1
            else:
                r -= 1

        return max_water
