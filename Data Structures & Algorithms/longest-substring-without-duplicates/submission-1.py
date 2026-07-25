class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Left pointer to track the start of the substring
        l =0 
        length  = 0
        
        # We need a set to check for duplicates in o(1) constant time
        seen = set()

        for r in range(len(s)):
            while(s[r] in seen):
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            length = max(length, r - l + 1) # Think when l and r are at the first index we need to do r-l which is 0, then add 1

        return length


        