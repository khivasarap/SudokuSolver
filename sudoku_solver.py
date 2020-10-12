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
        if grid[column][i] == number and i!= row:
            return False

    return possible_box(row,column,number)

def possible_box(row,column,number):
    # Perform floor division
    row_index = (row // 3)*3
    col_index = (column //3)*3
    for x in range(row_index,row_index+3):
        for y in range(col_index,col_index+3):
            if grid[x][y] == number:
                return False
    #print(row_index, col_index)


possible_axis(8,0,6)