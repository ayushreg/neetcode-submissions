class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # First we need to make a set
        nums = set(nums)
        longest = 0
        # Loop through the set
        for num in nums:
            if((num - 1) not in nums): # Check if we have a value that is -1 of the value we are at in the set. To find our starting sequence
                seq_length = 1
                start = num
                while((start+1) in nums):
                    seq_length += 1
                    start += 1
                if(seq_length > longest):
                    longest = seq_length

        return longest

    