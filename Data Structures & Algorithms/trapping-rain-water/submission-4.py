class Solution:
    def trap(self, height: List[int]) -> int:
        
        # To hold max left and right so far
        maxLeft = height[0] # Intiall the first element
        maxRight = height[-1] # intially the last element

        # To hold our answer
        water = 0

        # Our two pointers
        left = 0
        right = len(height) - 1

        while(left < right):
            if(maxLeft < maxRight): # we use the left pointer
                currWater = maxLeft - height[left] #calculate the water at that position
                if(currWater > 0 ):
                    water += currWater
                maxLeft = max(maxLeft, height[left]) # Update the maxLeft
            else:
                currWater = maxRight - height[right] 
                if(currWater > 0 ):
                    water += currWater
                maxRight = max(maxRight, height[right]) # Update the maxRight

            if(maxLeft < maxRight): # Move our pointers based on the maxleft and right
                left += 1
            else:
                right -= 1

        return water
