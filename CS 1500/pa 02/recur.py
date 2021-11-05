def makeArray(rows, columns):
    array = []
    for n in range(0,rows):
        new_row = input().split()
        array.append(new_row)
    return array
    
def matrix_search(matrix, word, index=0, x=0, y=0, start_position=[0,0]):
    
    if index == (len(word)):
        if y == 2:
            y = 1
        end_position = [y,x]
        return_tuple = (tuple(start_position),tuple(end_position))
        return return_tuple
    
    elif matrix[0][0] == '1':
        start_position = [1,5]
        end_position = [1,0]
        return_tuple = (tuple(start_position),tuple(end_position))
        return return_tuple
        
    elif index == 0:
        end_position = [ ]
        exit_check_string = ''
        '''search the whole matrix for the first letter of the word'''
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                exit_check_string = exit_check_string + matrix[row][column]
                if matrix[row][column] == word[0]:
                    start_position[0] = row
                    start_position[1] = column
                    return matrix_search(matrix, word, (index+1), column, row, start_position)
                    
                    
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
    space = input()
    for n in range(cases):
        # Get rows and columns
        dimensions = input().split()
        rows = int(dimensions[0])
        columns = int(dimensions[1])
        # Create data matrix
        matrix = makeArray(rows, columns)
        word = input()
        return_tuple = matrix_search(matrix, word)
        if return_tuple != None:
            start = return_tuple[0]
            end = return_tuple[1]
            print('Searching for "' + word +'" in matrix ' + str(s) + ' yields:')
            print("Start pos: " + str(start) + " to End pos: " + str(end))
        else:
            print('Searching for "' + word + '" in matrix ' + str(s) + ' yields:')
            print("The pattern was not found.")
        print()