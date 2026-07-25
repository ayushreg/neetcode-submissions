class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        sequence = 1
        longest_sequence = 0

        for i in range(len(nums) - 1):
            next_num = nums[i + 1]
            if((nums[i] + 1) == next_num): # it can go out of bound so we need to do -1
                sequence += 1
            elif(nums[i] == nums[i+1]):
                sequence *=1
            else:
                sequence = 1
    
            if(longest_sequence <= sequence):
                longest_sequence = sequence
            
        if(len(nums) == 1):
            longest_sequence =1
        return longest_sequence
