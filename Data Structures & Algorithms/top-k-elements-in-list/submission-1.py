class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashmap to store the frequency of each value
        freq_table = {}
        for num in nums:
            if num not in freq_table:
                freq_table[num] = 1
            else:
                freq_table[num] += 1

        # Now need a array that is the same size as nums +1 because we dont need the 0 index
        # If we have 6 of same nums the freq would be 7 indexs. To say that value occured 6 times at index 6.
        bucket = [[] for i in range(len(nums) + 1)] # Creats [ [], [] , []]

        # Now put the numbers in the coresponding frequency index
        for key, value in freq_table.items():
            bucket[value].append(key)
        
        # Now we need to get K frequent
        result = [] # Arraylist

        # Now we need to loop from the end 
        for i in range(len(bucket) - 1, 0, -1):
            # Now each array element has a list 
            for j in bucket[i]:
                result.append(j)
                if(len(result) == k):
                    return result

        return result
