class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Our left and right pointers
        left = 0
        right = len(s) - 1

        # Loop until left becomes greater than right
        while(left < right):

            # Now we need to compare and left and right pointer
            # But we need to skip alpha numeric values
            while(left < right and not s[left].isalnum()): # s = '.,' it would break the code unless we check the boundaries again
                left += 1

            while(left < right and not s[right].isalnum()):
                right -= 1

            # need to check the lowercase version
            if(s[left].lower() != s[right].lower()):
                return False
            left += 1
            right -= 1

        return True

        