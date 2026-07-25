class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq1 = {}

        freq2 = {}

        for char1 in s:
            freq1[char1] = freq1.get(char1, 0) + 1

        for char2 in t:
            freq2[char2] = freq2.get(char2, 0) + 1
        
        return freq1 == freq2