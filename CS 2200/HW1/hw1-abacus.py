def print_abacus(num):
  '''
    Print_Abacus takes in a string of a number
    Then it goes through and adjust the default abacus
    Finally it prints the new abacus
  '''
  print(num + " is represent by: ")
  sizeOf = len(num)
  bottomRowEmpty = [5,6,7,8]
  abacus = [['o','o','o','o','o','o','o','o','o','o','o','o','o'],
            ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            ['-','-','-','-','-','-','-','-','-','-','-','-','-'],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
            ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
            ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
            ['o','o','o','o','o','o','o','o','o','o','o','o','o']]
  for i in range(sizeOf):
    colIndex = (13-sizeOf)+i
    numSpacesToMove = int(num[i])
    if (numSpacesToMove >= 5):
      # If we have more than 5, adjust the top row first
      abacus[3][colIndex] = 'o'
      abacus[1][colIndex] = ' '
      numSpacesToMove=numSpacesToMove-5
      # Then we change the bottom row
      # To keep track of how many bottom rows we've changes
      bottomPlaced = 0
      while (numSpacesToMove > 0):
        # Parse the next empty index from our list of bottom row
        rowIndex = bottomRowEmpty[bottomPlaced]
        abacus[rowIndex][colIndex] = 'o'
        bottomPlaced+=1
        numSpacesToMove-=1
      ''' After we place the beads in the right spot, we put empty spots
      in the used beads spots '''
      for x in range(9,9+bottomPlaced):
        abacus[x][colIndex] = ' '
    else:
      # If we have less than 5, we only adjust the bottom row
      # To keep track of how many bottom rows we've changes
      bottomPlaced = 0
      while (numSpacesToMove > 0):
        # Parse the next empty index from our list of bottom row
        rowIndex = bottomRowEmpty[bottomPlaced]
        abacus[rowIndex][colIndex] = 'o'
        bottomPlaced+=1
        numSpacesToMove-=1
      ''' After we place the beads in the right spot, we put empty spots
      in the used beads spots '''
      for x in range(9,9+bottomPlaced):
        abacus[x][colIndex] = ' '
  # Once we finish editing the abacus, we print out the abacus
  for a in range(len(abacus)):
    row = str(abacus[a])
    print(row)


def add_abacus(num1, num2):
  print_abacus(str(num1))
  print('')
  print_abacus(str(num2))
  print('')
  summation = num1 + num2
  print_abacus(str(summation))


# 2a
print('QUESTION 2A: ')
add_abacus(54321, 90678)
# 2b
print('QUESTION 2B: ')
add_abacus(559876543210, 27623428724)
# 2c
print('QUESTION 2C: ')
add_abacus(127002343627, 23412876241)