class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check each row
        for row in board:
            hashSet = set()
            for col in row:
                if(col == "."):
                    continue
                
                if(int(col) > 9 or int(col) < 1):
                    return False
                else:
                    if(col in hashSet):
                        return False
                    else:
                        hashSet.add(col)

        # Check each column
        for column in range(0,9):
            hashSet = set()
            for row in range(0,9):
                value = board[row][column]
                if(value == "."):
                    continue
                
                if(int(value) > 9 or int(value) < 1):
                    return False
                else:
                    if(value in hashSet):
                        return False
                    else:
                        hashSet.add(value)
            
        start = 0
        end = 3
        # Check boxes of row 1 
        for row1 in range(0,3):
            hashSet = set()
            for row in range(0,3):
                for col in range(start, end):
                    value = board[row][col]
                    if(value == "."):
                        continue
                    
                    if(int(value) > 9 or int(value) < 1):
                        return False
                    else:
                        if(value in hashSet):
                            return False
                        else:
                            hashSet.add(value)
            start += 3
            end += 3


        start = 0
        end = 3 
        # Check boxes of row 2
        for row1 in range(0,3):

            hashSet = set()
            for row in range(3,6):
                for col in range(start, end):
                    value = board[row][col]
                    if(value == "."):
                        continue
                    
                    if(int(value) > 9 or int(value) < 1):
                        return False
                    else:
                        if(value in hashSet):
                            return False
                        else:
                            hashSet.add(value)
            start += 3
            end += 3
        
        start = 0
        end = 3
        # Check boxes of row 3
        for row1 in range(0,3):
            hashSet = set()
            for row in range(6,9):
                for col in range(start, end):
                    value = board[row][col]
                    if(value == "."):
                        continue
                    
                    if(int(value) > 9 or int(value) < 1):
                        return False
                    else:
                        if(value in hashSet):
                            return False
                        else:
                            hashSet.add(value)
            start += 3
            end += 3

        return True
                