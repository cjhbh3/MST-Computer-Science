'''
trick to put stuff in input without typing
python3 mazeNotFinished.py < sample_input.txt

to check unit test
exec run_me_local_for_faster_testing.sh
'''
def fill_matrix(matrix, rows):
    '''
    generate the matrix that is inputted via standard input
    '''
    for n in range(rows):
        string = list(input())
        matrix.append(string)
    
    return matrix


def print_matrix(matrix):
    '''
    simply print the matrix
    '''
    for row in matrix:
        for col in range(len(row) - 1):
            print(row[col], end ='')
            if col == len(row) - 1:
                print()


def find_start(matrix, rows):
    '''
    used for determining where Niobe is at in the maze,
    return starting row, col
    '''
    start_point = (0,0)
    for n in range(rows):
        for i in matrix[n]:
            if i == 'N':
                o = matrix[n].index(i)
                start_point = (n,o)
            
    return start_point

def valid_move(matrix, row, col, direction):
    '''
    used for determining if the current move is valid,
    Note: checks AHEAD in direction if move is ok
          (not row col itself, but the next move)
    return True if move is valid False otherwise
    '''
    if direction == 'NORTH':
        return matrix[row-1][col] == ' '
    elif direction == 'WEST':
        return matrix[row][col-1] == ' '
    elif direction == 'EAST':
        return matrix[row][col+1] == ' '
    elif direction == 'SOUTH':
        return matrix[row+1][col] == ' '
           


def at_end(matrix, row, col):
    '''
    used for determining if Noibe is at the exit,
    return True if at the exit False otherwise
    '''
    '''end_point = (0,0)
    for n in range(len(matrix)):
        for i in matrix[n]:
            if i == 'E':
                o = matrix[n].index(i)
                end_point = (n,o)'''
    return (matrix[row][col] == 'E') or (matrix[row-1][col] == 'E') or (matrix[row][col+1] == 'E') or (matrix[row+1][col] == 'E') or (matrix[row][col-1] == 'E')

def find_exit(matrix, row, col):
    '''
    used for finding the exit,
    this will be the recursive function
    returns True or False
    use solvesudoku as the basis of your code here.
    '''
    directions = ['NORTH','WEST','EAST','SOUTH']

    if at_end(matrix,row,col):
        # Base case
        return True
    for x in directions:
        if valid_move(matrix,row,col,x):
            if x == 'NORTH':
                matrix[row-1][col] = '@'
                return find_exit(matrix,row-1,col)
            elif x == 'WEST':
                matrix[row][col-1] = '@'
                return find_exit(matrix,row,col-1)
            elif x == 'EAST':
                matrix[row][col+1] = '@'
                return find_exit(matrix,row,col+1)
            elif x == 'SOUTH':
                matrix[row+1][col] = '@'
                return find_exit(matrix,row+1,col)
        else:
            if matrix[row][col-1] == '@':
                matrix[row][col] = ' '
                matrix[row][col-1] = ' '
                return find_exit(matrix,row,col)
            elif matrix[row+1][col] == '@':
                matrix[row][col] = ' '
                matrix[row+1][col] = ' '
                return find_exit(matrix,row,col)
            elif matrix[row][col+1] == '@':
                matrix[row][col] = ' '
                matrix[row][col+1] = ' '
                return find_exit(matrix,row,col)
            elif matrix[row-1][col] == '@':
                matrix[row][col] = ' '
                matrix[row-1][col] = ' '
                return find_exit(matrix,row,col)
            else:
                matrix[row][col] = ' '
                return False

    

def main():
    '''
    Write your main here
    '''
    
    mapNum = 0
    numRows = int(input())
    while numRows != 0:
        matrix = []
        matrix = fill_matrix(matrix,numRows)
        row, col = find_start(matrix, numRows)
        if find_exit(matrix, row, col):
            print('Map %d -- Solution found:' % mapNum)
            print_matrix(matrix)
            mapNum = mapNum + 1
        else:
            print('Map %d -- No solution found:' % mapNum)
            print_matrix(matrix)
            mapNum = mapNum + 1
        
        # Dag nab space
        space = input()
        numRows = int(input())
        
    


# Do NOT edit below this line:
if __name__ == '__main__':
    main()

