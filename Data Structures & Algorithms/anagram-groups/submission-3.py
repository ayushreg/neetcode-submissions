class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}

        for string in strs:
            freq = [0]*26
            for char in string:
                freq[ord(char) - ord("a")] += 1

            hashFreq = tuple(freq)
            if hashFreq in hashMap:
                hashMap[hashFreq].append(string)
            else:
                hashMap[hashFreq] = [string]

        return list(hashMap.values())