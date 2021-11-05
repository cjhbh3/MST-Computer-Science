# Last Factorial Digit
def factorial(n):

    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

def possibleCombinations(n,k):
    numerator = (factorial(n))
    denominator = (factorial(k) * factorial(n-k))
    if numerator == 1:
        return 1
    if denominator == 0:
        return 1
    else:
        return numerator / denominator


if __name__ == "__main__":
   print(possibleCombinations(10,8))

