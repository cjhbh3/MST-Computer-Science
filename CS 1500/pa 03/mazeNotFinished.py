'''
trick to put stuff in input without typing
python3 mazeNotFinished.py < sample_input.txt

to check unit test
exec run_me_local_for_faster_testing.sh
'''
#!/usr/bin/python3


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
        print(''.join(row))
    print()

def find_start(matrix, rows):
    '''
    used for determining where Niobe is at in the maze,
    return starting row, col
    '''
    for row in matrix:
        for col in range(len(row)):
            if row[col] == 'N':
                return matrix.index(row), col


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
    if matrix[row][col]=='E':
        return True
    if matrix[row][col-1]=='E':
        return True
    if matrix[row][col+1]=='E':
        return True
    if matrix[row-1][col]=='E':
        return True
 else:
        return False

def find_exit(matrix, row, col):
    '''
    used for finding the exit,
    this will be the recursive function
    returns True or False
    use solvesudoku as the basis of your code here.
    '''
    if at_end(matrix, row, col):
        return True
    if valid_move(matrix, row, col, 'NORTH'):
        matrix[row-1][col] = '@'
        if not find_exit(matrix, row-1, col):
            matrix[row-1][col] = ' '
        else:
            return True
    if valid_move(matrix, row, col, 'SOUTH'):
        matrix[row+1][col] = '@'
        if not find_exit(matrix, row+1, col):
            matrix[row+1][col] = ' '
        else:
            return True
    if valid_move(matrix, row, col, 'EAST'):
        matrix[row][col+1] = '@'
        if not find_exit(matrix, row, col+1):
            matrix[row][col+1] = ' '
        else:
            return True
    if valid_move(matrix, row, col, 'WEST'):
        matrix[row][col-1] = '@'
        if not find_exit(matrix, row, col-1):
            matrix[row][col-1] = ' '
        else:
            return True
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

