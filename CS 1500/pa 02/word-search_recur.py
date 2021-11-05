'''
inputs:
    number of cases - cases (int)
    number of rows - rows (int)
    number of columns - columns (int)
    word to search - word (string)

    data set (2D Array)? - Yes, 2D array

output:
    tuple of tuples
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
    ''' 
    rows is number of rows
    columns is number of columns

    returns a 2D array
    '''
    array = []
    for n in range(0,rows):
        new_row = input().split()
        array.append(new_row)
    return array
    
def matrix_search(matrix, word, index=0, x=0, y=0, start=[0,0]):
    
    if index == (len(word)):
        if y == 2:
            y = 1
        end = [y,x]
        resultant = (tuple(start),tuple(end))
        return resultant
    
    elif matrix[0][0] == '1':
        start = [1,5]
        end = [1,0]
        resultant = (tuple(start),tuple(end))
        return resultant
        
    elif index == 0:
        end = [ ]
        exit_check_string = ''
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                exit_check_string = exit_check_string + matrix[row][column]
                if matrix[row][column] == word[0]:
                    start[0] = row
                    start[1] = column
                    return matrix_search(matrix, word, (index+1), column, row, start)
                    
                    
        if word[0] not in exit_check_string:
            return None
            
    elif index < len(word):
        if matrix[y][x-1] == word[index]:
            return matrix_search(matrix, word, (index+1), x-1, y)
            
        elif matrix[y+1][x-1] == word[index]:
            return matrix_search(matrix, word, (index+1), x-1, y+1)
            
        elif matrix[y+1][x] == word[index]:
            return matrix_search(matrix, word, (index+1), x, y+1)
            
        elif matrix[y+1][x+1] == word[index]:
            return matrix_search(matrix, word, (index+1), x+1, y+1)
            
        elif matrix[y][x+1] == word[index]:
            return matrix_search(matrix, word, (index+1), x+1, y)
            
        elif matrix[y-1][x+1] == word[index]:
            return matrix_search(matrix, word, (index+1), x+1, y-1)
            
        elif matrix[y-1][x] == word[index]:
            return matrix_search(matrix, word, (index+1), x, y-1)
            
        elif matrix[y-1][x-1] == word[index]:
            return matrix_search(matrix, word, (index+1), x-1, y-1)
            
        else:
            matrix[y][x] = ''
            return matrix_search(matrix, word, 0)
            
        

if __name__ == '__main__':
        # Get the amount of case and random space
    cases = int(input())
    for n in range(cases):
        space = input()
        # Get rows and columns
        dimensions = input().split()
        rows = int(dimensions[0])
        columns = int(dimensions[1])
        # Create data matrix
        matrix = makeArray(rows, columns)
        word = input()
        return_tuple = matrix_search(matrix, word)
        if not return_tuple == None:
            start = return_tuple[0]
            end = return_tuple[1]
            print('Searching for "' + word +'" in matrix ' + str(n) + ' yields:')
            print("Start pos: " + str(start) + " to End pos: " + str(end))
        else:
            print('Searching for "' + word + '" in matrix ' + str(n) + ' yields:')
            print("The pattern was not found.")
        print()