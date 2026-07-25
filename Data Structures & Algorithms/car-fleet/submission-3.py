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
            time = (target-pair[0])/ pair[1]

            if stack:  # If stack is not empty
                # Compare with the fleet in front
                if time > stack[-1]:  # Takes longer → cannot catch up → new fleet
                    stack.append(time)
                # else: merges with fleet ahead → do nothing
            else:
                stack.append(time)  # First fleet

        return len(stack)
