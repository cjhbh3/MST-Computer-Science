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

def makeArray(rows, columns):
    array = []
    for n in range(0,rows):
        new_row = input().split()
        array.append(new_row)
    return array

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

def findEndingPoint(word, matrix):
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
            if matrix[x][y] == word[len(word)-1]:
                all_points.append([x,y])
    
    return all_points

def findSlope(start, end):
    rise = end[0][1] - start[0][1]
    run = end[0][0] - start[0][0]
    slope = [rise, run]
    return slope

def testSlope(start, slope, matrix, word):
    test = [0,0] # x, y
    slope = slope[0] / slope[1]
    slope = int(slope)
    test[0] = start[0][0] + slope
    test[1] = start[0][1] + slope
    if matrix[test[0]][test[1]] == word[1]:
        return slope
    else:
        return 'fail'

def matrix_search(matrix, word, iteration=0):
    '''Write actual AI here'''
    '''
    for n in range(len(matrix)):
        print(matrix[n], sep='\n')
    '''

    currentIndex = iteration
    x = 0
    y = 0
    while currentIndex < len(word):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == word[currentIndex]:
                    x = i
                    y = j

    



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
        strt = findStartingPoint(word, matrix)
        print(strt)
        end = findEndingPoint(word, matrix)
        print(end)
        slpe = findSlope(strt, end)
        print(testSlope(strt,slpe,matrix,word))
