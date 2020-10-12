grid = [
[4,0,0,0,0,5,0,0,0],
[0,0,0,0,0,0,1,9,8],
[3,0,0,0,8,2,4,0,0],
[0,0,0,1,0,0,0,8,0],
[9,0,3,0,0,0,0,0,0],
[0,0,0,0,3,0,6,7,0],
[0,5,0,0,0,9,0,0,0],
[0,0,0,2,0,0,9,0,7],
[6,4,0,3,0,0,0,0,0]]

# defines row and column position of number n in the grid
def possible_axis(row, column, number):
    #Check if exists in row
    for i in range(0,9):
        if grid[i][row] == number and i!=column:
            return False
    #Check if exists in column
    for j in range(0,9):
        if grid[column][j] == number and j!=row:
            return False
    return True


def validate(row,column,number):
    return possible_axis(row, column, number) and possible_box(row,column,number)

def possible_box(row,column,number):
    # Perform floor division
    row_index = (row // 3)*3
    col_index = (column //3)*3
    for a in range(row_index,row_index+3):
        for b in range(col_index,col_index+3):
            if grid[b][a] == number:
                return False
    
    return True

def display(matrix):
    for i in range(9):
        print(matrix[i])


# Solve using Backtracking. Place the number in the box and check if valid.
def solve_backtrack():
    global grid
    for x in range(9):
        for y in range(9):
            # 0 means it is not filled in the grid
            if grid[x][y] == 0:
                # Check from 1-9 what fits in
                for n in range(1,10):
                    if validate(y, x, n):
                        grid[x][y] = n
                        solve_backtrack()
                        # Ensure we backtrack
                        grid[x][y] = 0
                return
    display(grid)
 

solve_backtrack()
