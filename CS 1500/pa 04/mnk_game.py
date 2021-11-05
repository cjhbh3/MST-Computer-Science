#!/usr/bin/env ipython3

# do NOT change the next two lines of code...
import sys
assert ('linux' in sys.platform), "This code should be run on Linux, just a reminder to follow instructions..."
import random

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

def inputPlayerLetter(): # Finished

    # Have test case - check_player_letter.py <input_player_letter.txt
    # Function inputPlayerLetter() lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    # the first element in the list is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst(): # No Change

    # Function whoGoesFirst() randomly choose the player who goes first.
    random.seed(0)
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"

def makeMove(board, letter, row, col): # Finished

    # Function makeMove(List, str, int) places player's letter or computer's letter at the specified
    # position i.e. move. Very simple function
    board[row][col] = letter


def checkAcross(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j): # Finished
    # Have test case - check_across_test.py
    # Function checkAcross(List, str, int, int, int, int, int) checks if player's letter is in all the
    # adjacent k (numberOfMatches) positions across the row from left to right.
    # Returns True if k-match pattern is found for player's letter across the row (corresponding to i,j)
    # Return False otherwise
    across = True
    try:
        for n in range(numberOfMatches):
            if board[i][j+n] != letter:
                across = False
    except IndexError:
        across = False
    
    return across


def checkDown(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j): # Finished
    # Have test case - check_down_test.py
    # Function checkDown(List, str, int, int, int, int, int) checks if player's letter is in all
    # the k (numberOfMatches) positions down the column from top to bottom
    # Returns True if k-match pattern is found for player's letter down the column
    # returns False otherwise
    down = True
    try:
        for n in range(numberOfMatches):
            if board[i+n][j] != letter:
                down = False
    except IndexError:
        down = False
    
    return down

def checkDiagonalRight(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j): # Finished
    # Have test case - check_diagonal_right_test.py
    # Function checkDiagonalRight(List, str, int, int, int, int, int) checks if player's letter is in
    # all the k (numberOfMatches) positions diagonally towards right
    # Returns True if k-match pattern is found for player's letter diagonally towards right
    # returns False otherwise
    right = True
    try:
        for n in range(numberOfMatches):
            if board[i+n][j+n] != letter:
                right = False
    except IndexError:
        right = False

    return right

def checkDiagonalLeft(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j): # Finished
    # Have test case - check_diagonal_left_test.py
    # Function checkDiagonalLeft(List, str, int, int, int, int, int) checks if player's letter is in
    # all the k (numberOfMatches) positions diagonally towards left
    # Returns True if k-match pattern is found for player's letter diagonally towards left
    # returns False otherwise
    left = True
    try:
        for n in range(numberOfMatches):
            if board[i+n][j-n] != letter:
                left = False
    except IndexError:
        left = False

    return left

def isWinner(board, letter, numberOfRows, numberOfCols, numberOfMatches): # No Change

    # Funtion isWinner(List, str, int, int, int) determines if the player has won or not, given a board,
    # a player's letter, number of rows in board,number of columns in board, and number of matches needed
    # for player's letter to win.

    # Returns True if k-matches for player's letter were found across the rows or down the columns or
    # diagonally towards right or diagonally towards left on the board
    for i in range(numberOfRows):
        for j in range(numberOfCols):
            if board[i][j] == letter:
                if checkAcross(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
                    return True
                if checkDown(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
                    return True
                if checkDiagonalRight(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
                    return True
                if checkDiagonalLeft(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
                    return True
    return False


def getBoardCopy(board): # No Change

    # Function getBoardCopy(List) makes a copy of the board list and returns it.
    boardCopy = [[board[i][j] for j in range(len(board[i])) ] for i in range(len(board))]
    return boardCopy


def isSpaceFree(board, row, col): # Finished
    
    # Have test case - space_free_test.py
    # Function isSpaceFree(List, int, int) returns True if the passed move is free on the passed board.
    # Very simple function
    return board[row][col] == ' '


def getPlayerMove(board, numberOfRows, numberOfCols): # Finished

    # Function getPlayerMove(List, int, int) prompts for a valid player's move
    # Print "What is your next move? (0-rows, 0-cols)" where rows and cols are the size of your game.
    # See test for formatting
    # Take integer input with spaces, eg., 1 2
    coords = []
    attempting = True
    while attempting:
        print('What is your next move? (0-%d, 0-%d)' % (numberOfRows-1, numberOfCols-1))
        move = input().split()
        x = int(move[0])
        y = int(move[1])
        if ((x>=0 and x <= numberOfRows - 1) and (y>=0 and y <= numberOfCols-1)):
            if isSpaceFree(board,x,y):
                coords = [x,y]
                attempting = False

    return coords


def chooseRandomMoveFromList(board, movesList): # No Change

    # Function chooseRandomMoveFromList(List, List) randomly returns a computer move from the available moves
    random.seed(0)
    if len(movesList) != 0:
        move = random.choice(movesList)
        return move[0], move[1]
    else:
        return None


def getEmptySpaces(board, numberOfRows, numberOfCols): # Should be finished

    # Have test case - check_valid_random_moves.py
    # Function getEmptySpaces(List, int, int) returns a list of possible moves where the cell holds a space
    # Spaces should be in order of reading them out, e.g.,: [[0, 0], [1, 1], [1, 2]]
    emptySpaces = []
    for i in range(numberOfRows):
        for j in range(numberOfCols):
            if board[i][j] == ' ':
                emptySpaces.append([i,j])

    return emptySpaces
    

def getComputerMove(board, computerLetter, numberOfRows, numberOfCols, numberOfMatches):
    # Function getComputerMove(List, str, int, int, int) determines computer's move, given a board,
    # the computer's letter, number of rows of the board, the number of columns of the board, and
    # number of matches.
    # Returns a computer's move.
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    # Here is our algorithm for our m-n-k AI:
    # First, check if we can win in the next move
        ''' 
            Copy board, play a move at each spot. If winner, return that.
        '''
    for i in range(numberOfRows):
        for j in range(numberOfCols):
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy,i,j):
                makeMove(boardCopy,computerLetter,i,j)
                if isWinner(boardCopy,computerLetter,numberOfRows,numberOfCols,numberOfMatches):
                    return i,j
    # Check if the player could win on next move, and block them.
        '''
            Copy board, play a move at each spot. If the play would win, make that play.
        '''
    for i in range(numberOfRows):
        for j in range(numberOfCols):
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy,i,j):
                makeMove(boardCopy,playerLetter,i,j)
                if isWinner(boardCopy,playerLetter,numberOfRows,numberOfCols,numberOfMatches):
                    return i,j
    # Check for empty spaces on the board
    emptySpaces = getEmptySpaces(board, numberOfRows, numberOfCols)

    # Try to place a random move in the empty cell.
    return chooseRandomMoveFromList(board, emptySpaces)


def isBoardFull(board, numberOfRows, numberOfCols): # Should be finished

    # Have test case - board_full_test.py
    # Function isBoardFull(List, int, int) checks if every space on the board has been taken.
    # Returns True if the board is full, Otherwise returns False.
    boardFull = True
    for i in range(numberOfRows):
        for j in range(numberOfCols):
            if board[i][j] == ' ':
                boardFull = False

    return boardFull


def main():
    print("Welcome to m-n-k game!")

    while True:
        m = int(input("Enter number of rows, m : "))
        n = int(input("Enter number of columns, n : "))
        k = 0
        print("k should be greater than 2 and should not be greater than m or n")
        while k <= 2 or k > m or k > n:
            k = int(input("Enter valid number of matches, k : "))
        # Reset the board
        theBoard = [[" "] * n for i in range(m)]
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print("The " + turn + " will go first.")
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == "player":
                # Player's turn.
                drawBoard(theBoard, m, n)
                row, col = getPlayerMove(theBoard, m, n)
                makeMove(theBoard, playerLetter,  row, col)
                
                if isWinner(theBoard, playerLetter, m, n, k):
                    drawBoard(theBoard, m, n)
                    print("Hooray! You have won the game!")
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard, m, n):
                        drawBoard(theBoard, m, n)
                        print("The game is a tie!")
                        break
                    else:
                        turn = "computer"
            else:
                # Computer's turn.
                row, col = getComputerMove(theBoard, computerLetter, m, n, k)
                makeMove(theBoard, computerLetter, row, col)

                if isWinner(theBoard, computerLetter, m, n, k):
                    drawBoard(theBoard, m, n)
                    print("The computer has beaten you! You lose.")
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard, m, n):
                        drawBoard(theBoard, m, n)
                        print("The game is a tie!")
                        break
                    else:
                        turn = "player"

        print("Do you want to play again? (y or n)")
        if not input().lower().startswith("y"):
            break

if __name__ == '__main__':
    main()

