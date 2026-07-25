class Solution:
    def trap(self, height: List[int]) -> int:

        totalWater = 0
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        # Buliding the left max subarray
        for i in range(len(height)):
            if(i == 0):
                leftMax[i] = height[i]
            else:
                # Get height at curr index
                val = height[i]
                leftMax[i] = max(leftMax[i - 1],val) # Check if this index had a new max left
        
        # Bulding the right max subarray 
        for i in range((len(height) - 1), -1, -1):
            # The max right value is it self at the last index
            if(i == (len(height) - 1)):
                rightMax[i] = height[i]
            else:
                val = height[i] # Current height
                rightMax[i] = max(rightMax[i + 1],val) # Check if this index had a new max left

        # Now we can loop through heights and calculate the total water
        for i in range(len(height)):
            water = min(leftMax[i], rightMax[i]) - height[i]
            if(water > 0):
                totalWater += water

        return totalWater
        