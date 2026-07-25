class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = l
        seen = set()
        maxL = 0
        for r in range(len(s)):
            while(s[r] in seen):
                seen.remove(s[l])
                l += 1
            maxL = max(maxL, r-l + 1)
            seen.add(s[r])

        return maxL
