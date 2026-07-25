class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a hashtable to hold the frequency of each number
        freq = {} 

        #Loop through to get the frequency
        for i in nums:
            if i not in freq: # If not in the table yet the frequency needs to be 0
                freq[i] = 0
            freq[i] += 1 # Then we can increment
        

        # How we need to sort them depending on thier frequency(the value part)
        # Stored will return a list

        sorted_freq = []

        sorted_freq = sorted(freq.items(), key = lambda x:x[1], reverse = True) # Sort based on keys in ascending then reverse for descending

        result = []
        for i in range(k):
            #result[i] = sorted_freq[i] results is not a array with indices
            result.append(sorted_freq[i][0])

        return result



        