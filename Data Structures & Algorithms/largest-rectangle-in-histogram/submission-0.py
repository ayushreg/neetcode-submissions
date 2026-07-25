class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i in range(len(heights)):
            index = i
            # Initally the stack has nothing so stack[-1][1] wont be evaluated so dont worry about that
            while (stack and stack[-1][1] > heights[i]):
                value = stack.pop() # this will return [index, height], which will be poped because it cant extend to the right anymore
                maxArea = max(maxArea, value[1] * (i - value[0])) # calculate the area for the poped height
                # Now our current value can extend to the left
                index = value[0]
            stack.append([index, heights[i]])

        # We could have values left in the stack
        while(stack):
            value = stack.pop()
            maxArea = max(maxArea, value[1]*(len(heights) - value[0]))  # We need to do len(heights), think about it when the last element is in the stack len(heights) -1 - index would give 0 area
        return maxArea
        