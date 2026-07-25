class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # To store the final result
        max_water = 0

        # Loop through everysingle combination
        for i in range(len(heights)):
            area = 0 # to hold the amount of water for each iteration
            for j in range(i, len(heights)):
                min_height = min(heights[i], heights[j]) # get the smaller height
                length = j - i # the length of rectangle
                area = min_height * length

                if(max_water < area):
                    max_water = area
        
        return max_water