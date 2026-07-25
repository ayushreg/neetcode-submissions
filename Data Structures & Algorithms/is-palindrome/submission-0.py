class Solution:
    def isPalindrome(self, s: str) -> bool:
        # To store the cleaned string
        cleaned = ""

        # loop through and only add aplha numeric characters in lowercase
        for char in s:
            if(char.isalnum()):
                cleaned += char.lower()

        return cleaned == cleaned[::-1]
        
       

        