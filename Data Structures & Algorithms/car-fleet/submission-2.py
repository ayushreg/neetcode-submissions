class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Add the pairs to a list
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
         # Sort the pair where the highest position is at the first element
        pairs.sort(key=lambda x:x[0], reverse = True)
        
        #Stack to hold the fleets
        stack = []
    
        # Loop through each pair
        for pair in pairs:
            if(stack): # If stack is not empty
                timeA = (target-stack[-1][0]) / (stack[-1][1])
                timeB = (target-pair[0]) / (pair[1] )
                if(timeB > timeA):
                    stack.append(pair)
            else:
                stack.append(pair)

        return len(stack)
