'''
inputs:
    number of cases - cases (int)
    number of rows - rows (int)
    number of columns - columns (int)
    word to search - word (string)

    data set (2D Array)? - Yes, 2D array

output:
    In the form of: # Assuming that the word is in the data set
        Searching for "{word}" in matrix {cases - 1} yields:
        Start pos: {coordinate of first letter} to End pos: {coordinate of last letter}
    If the word is not in the data set
        Searching for "{word}" in matrix {cases - 1} yields:
        The pattern is not found

        Notes: 
            - do not forget to index properly
            - coordinate goes rows then columns - (rows, columns)
'''
def searchCardinalDirections(x, y, n, word, matrix):
    ''' 
    x and y are the coordinate of the first letter
    n is the index of the letter being searched
    word is the word being searched for
    matrix is the data set

    returns nothing
    '''
    if len(word) > len(matrix):
        print('The pattern was not found.')
    else:
        # if the first letter is in the top corner
        if x == 0 and y == 0: 
            if matrix[n][0] == word[n]:
                if n == len(word) - 1 and matrix[n][0] == word[len(word)-1]:
                    print('Start pos: (0,0) to End pos: (%d, 0)' % n)
            elif matrix[0][n] == word[n]:
                if n == len(word) - 1 and matrix[0][n] == word[len(word)-1]:
                    print('Start pos: (0,0) to End pos: (0, %d)' % n)
        elif x == 0 and y == len(matrix[n]) - 1:
            if matrix[0][y-n] == word[n]:
                if n == len(word) - 1 and matrix[0][y-n] == word[len(word)-1]:
                    print('Start pos: (0,%d) to End pos: (0,%d)' % (y, y-n))
        elif x == len(matrix) - 1 and y == 0:
            if matrix[x-n][0] == word[n]:
                if n == len(word) - 1 and matrix[x-n][0] == word[len(word)-1]:
                    print('Start pos: (%d,0) to End pos: (%d, 0)' % (x, x-n))
        elif x == 0 and not y == 0:
            if matrix[0][y+n] == word[n]:
                if n == len(word) - 1 and matrix[0][y+n] == word[len(word)-1]:
                    print('Start pos: (0,%d) to End pos: (0, %d)' % (y,n))


def findStartingPoint(word, matrix):
    '''
    first_letter is the first_letter and we will be searching for that letter

    returns list of coordinates [row, column]
    '''
    all_points = []
    startPoint=[0,0]
    row = startPoint[0]
    column = startPoint[1]
    for x in range(row, len(matrix)):
       for y in range(column, len(matrix[row])):
            if matrix[x][y] == word[0]:
                all_points.append([x,y])
    
    return all_points

def makeArray(rows, columns):
    array = []
    for n in range(0,rows):
        new_row = input().split()
        array.append(new_row)
    return array

def matrix_search(matrix, word):
    '''Write actual AI here'''
    for n in range(0, len(word)):
        searchCardinalDirections(0,0,n,word,matrix)



if __name__ == '__main__':
    # Get the amount of case and random space
    cases = int(input())
    space = input()
    # Get rows and columns
    dimensions = input().split()
    rows = int(dimensions[0])
    columns = int(dimensions[1])
    # Create data matrix
    matrix = makeArray(rows, columns)
    #Attempt searching down column 1
    word = 'dog'
    for n in range(0,cases):
        matrix_search(matrix,word)
