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
def searchCardinalDirections(point, word, matrix):
    ''' 
    Recursive


def findStartingPoint(word, matrix,startPoint=[0,0]):
    '''
    first_letter is the first_letter and we will be searching for that letter

    returns list of coordinates [row, column]
    '''
    all_points = []
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
    print(findStartingPoint(word,matrix))
    '''
    for n in range(0, len(word)):
        searchCardinalDirections(0,1,n,word,matrix)
    '''
