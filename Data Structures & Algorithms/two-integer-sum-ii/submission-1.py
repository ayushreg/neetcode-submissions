class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0 # Left pointer at the very first element
        right = len(numbers) - 1 # Right pointer at the last element

        # Loop through the list
        while(left < len(numbers)):
            if(numbers[left] + numbers[right] == target): # If our two values = target
                return[(left + 1), (right+1)]
            elif(numbers[left] + numbers[right] < target): # If the sum is lower that means we need to move the left pointer
                left += 1
            else:
                right -= 1 # if the sum is too high we need to reduce the right pointer