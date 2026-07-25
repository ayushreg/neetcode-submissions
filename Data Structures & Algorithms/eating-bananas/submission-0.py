class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We will do a binary search on the possible K values
        # Lower bound is 1 banara per hour and upper would be the greatest element in our array
        l = 1
        r = max(piles)
        rate = float('inf')
        # We keep looping until L < right
        while(l <= r):
            # get the mid point
            k = (l + r) // 2
            
            # Caclulate the total hour if our K was the mid point
            totalHour = 0
            for num in piles:
                totalHour += math.ceil(num/k)
            # Now if the total hour calcualted is greather than our limit we need to increase the amount of bananas we are eating per hour
            if(totalHour > h):
                l = k + 1
            elif(totalHour <= h):
                # Now we can still check if we can get a lower value
                r = k - 1
                # This condition means we bound a valid answer
                # But we need to make sure keep the lowest
                rate = min(rate, k)
            

        return rate
