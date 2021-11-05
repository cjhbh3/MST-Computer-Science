def drawBoard(board, numberOfRows, numberOfCols):
    # Have test case - draw_board_test.py > draw_board_output.txt
    # Function drawBoard(List, int, int) takes the board list, number of rows (m),
    # and number of columns (n) as input parameters.
    # Prints game board on the screen with X, O, or Space at respective positions
    firstRow = '  '
    for x in range(numberOfCols):
        if not x == numberOfCols - 1:
            firstRow += str(x)
            firstRow += ' '
        else:
            firstRow += str(x)
    print(firstRow)
    row = ''
    for n in range(numberOfRows):
        row += str(n)
        row += '|'
        for o in range(numberOfCols):
            if o == numberOfCols - 1:
                if not n == numberOfRows - 1:
                    row += board[n][o]
                    row += '|\n'
                else:
                    row += board[n][o]
                    row += '|'
            else:
                row += board[n][o]
                row += '|'
        
    print(row)

if __name__ == '__main__':
    board =  [[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']]
    rows = 4
    cols = 5
    drawBoard(board,rows,cols)

    '''
    coords = []
    print('What is your next move? (0-%d, 0-%d)' % (numberOfRows-1, numberOfCols-1))
    move = input().split()
    x = int(move[0])
    y = int(move[1])
    attempting = True
    while attempting:
        if isSpaceFree(board,x,y):
            if (x >=0 and x <= numberOfRows-1) and (y >=0 and y <= numberOfCols-1):
                coords = [x,y]
                return coords
                attempting = False
            else:
                while not((x >=0 and x < numberOfRows-1) and (y >=0 and y < numberOfCols-1)):
                    print('What is your next move? (0-%d, 0-%d)' % (numberOfRows-1, numberOfCols-1))
                    move = input().split()
                    x = int(move[0])
                    y = int(move[1])
                coords = [x,y]
                return coords
                attempting = False
        else:
            print('What is your next move? (0-%d, 0-%d)' % (numberOfRows-1, numberOfCols-1))
            move = input().split()
            x = int(move[0])
            y = int(move[1])
    '''
