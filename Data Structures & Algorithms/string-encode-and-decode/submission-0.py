class Solution:

    def encode(self, strs: List[str]) -> str:
        #Just append each string in the list
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string 
        return result


    def decode(self, s: str) -> List[str]:
        # What to return
        result = []
        i = 0 # Start at the first index

        # Loop through the whole string
        while(i < len(s)):
            j = i # J is the pointer to our delimiter
             
            while(s[j] != "#"):
                j += 1

            # Our length can be double digit so we have to actual get the string from i to j for the actual length
            str_length = int(s[i:j]) # this has to a int

            # now we could loop through the length BUT WHY you dont have to
            # We know the length we can move the pointers and slice the string
            i = j + 1
            # THIS IS WRONG j = str_length + 1
            # This is right because we need to move relative to i the above would give us a infite loop
            j = str_length + i

            decoded_Str = s[i:j]
            
            # Move i to where J is (this is where the number is)
            i = j

            # Add to our result
            result.append(decoded_Str)


        return result



