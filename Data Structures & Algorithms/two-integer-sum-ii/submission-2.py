class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #left and right pointers
        l = 0
        r = len(numbers) - 1

        # Loop until left and right pointer cross
        while(l < r):
            sum = numbers[l] + numbers[r] # Get the sum

            # if the sum is to small we can increment left 
            # if larger than target decremenet right pointer

            if(sum == target):
                return [l +1, r +1]
            elif(sum < target):
                l +=1
            else:
                r -= 1

        return []




