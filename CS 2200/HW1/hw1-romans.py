def uncompact_subtractives(num):
  '''
    This function is used for uncompacting subtractives by converting the 
    roman numeral word into an integer and then converting that integer into 
    roman numerals without subtractives
    Returning a roman numeral word without subtractives
  '''
  rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  int_val = 0
  # Convert the roman numerals to a number
  for i in range(len(num)):
    if i > 0 and rom_val[num[i]] > rom_val[num[i-1]]:
      # Subtractives
      int_val += rom_val[num[i]] - 2 * rom_val[num[i-1]]
    else:
      int_val += rom_val[num[i]]
  
  # Break down what symbols need without subtractives
  symbolsNeeded = {'I': 0, 'V': 0, 'X': 0, 'L': 0, 'C': 0, 'D': 0, 'M': 0}
  while int_val > 1000:
    symbolsNeeded['M']+=1
    int_val-=1000
  while int_val > 500:
    symbolsNeeded['D']+=1
    int_val-=500
  while int_val > 100:
    symbolsNeeded['C']+=1
    int_val-=100
  while int_val > 50:
    symbolsNeeded['L']+=1
    int_val-=50
  while int_val > 10:
    symbolsNeeded['X']+=1
    int_val-=10
  while int_val > 5:
    symbolsNeeded['V']+=1
    int_val-=5
  while int_val > 0:
    symbolsNeeded['I']+=1
    int_val-=1

  # Write the new roman numeral word sorted from largest to smallest
  newRomanWord = ""
  while symbolsNeeded['M'] > 0:
    newRomanWord+='M'
    symbolsNeeded['M']-=1
  while symbolsNeeded['D'] > 0:
    newRomanWord+='D'
    symbolsNeeded['D']-=1
  while symbolsNeeded['C'] > 0:
    newRomanWord+='C'
    symbolsNeeded['C']-=1
  while symbolsNeeded['L'] > 0:
    newRomanWord+='L'
    symbolsNeeded['L']-=1
  while symbolsNeeded['X'] > 0:
    newRomanWord+='X'
    symbolsNeeded['X']-=1
  while symbolsNeeded['V'] > 0:
    newRomanWord+='V'
    symbolsNeeded['V']-=1
  while symbolsNeeded['I'] > 0:
    newRomanWord+='I'
    symbolsNeeded['I']-=1

  return newRomanWord


def add_romanNums(num1, num2):
  # Take out the subtractives
  num1 = uncompact_subtractives(num1)
  num2 = uncompact_subtractives(num2)
  # Concatenate
  combined = num1 + num2
  combined = uncompact_subtractives(combined)

  return combined

def subtract_romanNums(num1, num2):
  # Take out the subtractives
  num1 = uncompact_subtractives(num1)
  num2 = uncompact_subtractives(num2)

  num1_dict = {'I': 0, 'V': 0, 'X': 0, 'L': 0, 'C': 0, 'D': 0, 'M': 0}
  num2_dict = {'I': 0, 'V': 0, 'X': 0, 'L': 0, 'C': 0, 'D': 0, 'M': 0}
  

  for i in num1:
    num1_dict[i]+=1
  for j in num2:
    num2_dict[j]+=1
  
  newNum = ''

  for x in ['M','D','C','L','X','V','I']:
    diff = num1_dict[x] - num2_dict[x]
    if (diff > 0):
      newNum+=(diff*x)
  
  return newNum



# 3a
print('QUESTION 3A: ')
print(add_romanNums(add_romanNums('CXCV','XXXI'), 'LXXXVIII'))
# 3b
print('QUESTION 3B: ')
print(subtract_romanNums(subtract_romanNums('CCCXCV','CXV'),'LXX'))
# 3c
print('QUESTION 3C: ')
print(add_romanNums('CCMCCCII', 'MLCLCIII'))