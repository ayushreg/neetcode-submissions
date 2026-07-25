class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        # First we can do binary search to find what row our value is in 
        row = 0
        l = 0
        r = len(matrix) - 1
        while(l <= r):
            mid = (l + r) // 2

            if(matrix[mid][0] > target):
                r = mid - 1
            elif(matrix[mid][-1] < target):
                l = mid + 1
            else:
                row = mid
                break
            
        
        # now do binary search on the that row 

        l = 0
        r = len(matrix[row]) - 1

        while(l <= r):
            mid = (l+r) // 2

            if(matrix[row][mid] == target):
                return True
            elif(matrix[row][mid] > target):
                r = mid -1
            else:
                l = mid + 1

        return False
        



