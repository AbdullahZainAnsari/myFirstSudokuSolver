#a sudoku solver python program 
"""Given a incomplete sudoku to the program
   and it will give out the complete sudoku as a result"""
"""The given sudoku solver will be in int mode and 
    the space or the incomplete value contains empty """   
   
class Solution:
    def __init__(self,sudoku):
        self.sudoku = sudoku
    
    #Function for checking if the sudoku is valid or not!
    def isValidSudoku(self):
        #condition to check if the sudoku contains 9 rows and 9 columns!
        if len(self.sudoku) != 9 or len(self.sudoku[0]) != 9:
            return False
        
        #Creating the set arr for checking the unique values in the rows, columns and 3X3 sub boxes!
        arr = set()
        
        #for checking if the value is present in rows or not.
        #if not then it returns False
        for row in range(len(self.sudoku)):
            for col in range(len(self.sudoku[0])):
                if self.sudoku[row][col] != ".":
                    if self.sudoku[row][col] in arr:
                        return False
                    else:
                        arr.add(self.sudoku[row][col])
            arr.clear()    
        
        #clear the arr set for use checking in row wise   
        arr.clear()
        
        #for checking if the values are unique in columns or not
        for col in range(len(self.sudoku[0])):
            for row in range(len(self.sudoku)):
                if self.sudoku[row][col] != '.':
                    if self.sudoku[row][col] in arr:
                        return False
                    else:
                        arr.add(self.sudoku[row][col])
            arr.clear()    
        
        #making this array, it'll help us to travel through the 3X3 sub-arrays        
        threeXthree = [0,3,6]
        
        #again clear the arr set so that you can check the 3X3 sub boxes of the sudoku
        arr.clear()
        
        for subRow in threeXthree:
            for subCol in threeXthree:
                for row in range(3):
                    for col in range(3):
                        if self.sudoku[row+subRow][col+subCol] != ".":
                            if not self.sudoku[row+subRow][col+subCol] in arr:
                                arr.add(self.sudoku[row+subRow][col+subCol])
                            else:
                                return False    
                arr.clear()    
        return True                    
    
    
    #Function to print the three rows of the sudoku 
    def printTheThreeRows(self,starting,ending):
        for row in range(starting, ending):
            for col in range(0,9):
                if col == 2 or col == 5:
                    print(self.sudoku[row][col],'|',end='')
                else:
                    print(' ',self.sudoku[row][col],',',sep='',end='')
            print()
                        
    #Function for printing the complete sudoku
    def printTheSudoku(self):
        if len(self.sudoku) == 9 and len(self.sudoku[0]) == 9:
            self.printTheThreeRows(0,3)
            print("---------------------------")
            self.printTheThreeRows(3,6)
            print('---------------------------')
            self.printTheThreeRows(6,9)
        else:
            print('''Your entered sudoku is not valid.
                  i.e., it is not 9X9 sudoku.''')                      
    
    
    #function of solving the incomplete sudoku
    def solve(self,sudoku,i,j):
        if i==9:
            return True
        if j == 9:
            return self.solve(sudoku,i+1,0)
        if self.sudoku[i][j] != '.':
            return self.solve(sudoku,i,j+1)
        nums = "123456789"
        
        for num in nums:
            if self.check(sudoku,i,j,num) == True:
                self.sudoku[i][j] = num
                if self.solve(self.sudoku,i,j) == True:
                    return True
                self.sudoku[i][j] = "."
        return False        
    
    def check(self,sudoku,i,j,val):
        row = i - i%3
        col = j - j%3
        for x in range(0,9):
            if self.sudoku[i][x] == val:
                return False
        for y in range(0,9):
            if self.sudoku[y][j] == val:
                return False
        for x in range(0,3):
            for y in range(0,3):
                if self.sudoku[x+row][y+col] == val:
                    return False
        return True                
        
    
"""
    A sudoku given for practice!

    [['.','.','1', '8','.','.', '.','.','5'],
     ['.','.','.', '1','.','5', '3','.','7'],
     ['.','6','.', '.','.','.', '2','.','.'],
     
     ['9','8','.', '.','4','.', '.','.','.'],
     ['.','.','.', '.','.','.', '.','.','.'],
     ['.','.','.', '.','8','.', '.','7','3'],
     
     ['.','.','2', '.','.','.', '.','9','.'],
     ['5','.','4', '9','.','7', '.','.','.'],
     ['3','.','.', '.','.','2', '7','.','.']]
"""    
    
if __name__ == '__main__':
    a = Solution([['.','.','1', '8','.','.', '.','.','5'],
     ['.','.','.', '1','.','5', '3','.','7'],
     ['.','6','.', '.','.','.', '2','.','.'],
     
     ['9','8','.', '.','4','.', '.','.','.'],
     ['.','.','.', '.','.','.', '.','.','.'],
     ['.','.','.', '.','8','.', '.','7','3'],
     
     ['.','.','2', '.','.','.', '.','9','.'],
     ['5','.','4', '9','.','7', '.','.','.'],
     ['3','.','.', '.','.','2', '7','.','.']])
    
    #print(a.isValidSudoku())
    #a.printTheSudoku()
    print(a.isValidSudoku())
    
    
    
    board = [['.','.','1', '8','.','.', '.','.','5'],
     ['.','.','.', '1','.','5', '3','.','7'],
     ['.','6','.', '.','.','.', '2','.','.'],
     
     ['9','8','.', '.','4','.', '.','.','.'],
     ['.','.','.', '.','.','.', '.','.','.'],
     ['.','.','.', '.','8','.', '.','7','3'],
     
     ['.','.','2', '.','.','.', '.','9','.'],
     ['5','.','4', '9','.','7', '.','.','.'],
     ['3','.','.', '.','.','2', '7','.','.']]
    a.solve(board,0,0)
    a.printTheSudoku()