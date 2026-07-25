class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
     

        #Hash map where key is the string of frequency and value is a list of string that maps to that frequnecy
        hash_map = {}

        # Loop through each string in the array and caculate its frequency
        for string in strs:
            # Create our frequency array
            freq = [0]*26
            
            # Get freq of each char
            for char in string:
                freq[ord(char) - ord('a')] += 1
            # Convert the freq arr into a tuple so we can hash it
            freq_arr = tuple(freq)

            # If the key is not in the map yet, we need to make a empty list 
            if(freq_arr not in hash_map):
                hash_map[freq_arr] = []

            # Add the string to the list
            hash_map[freq_arr].append(string);

        return list(hash_map.values())

