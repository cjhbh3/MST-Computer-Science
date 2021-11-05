def gdc():
  a = 1570
  b = 488
  r = 488

  while (b != 0):
    r = a % b
    a = b
    b = r

  print("GCD of %d and %d: %d" % (1570, 488, a))

gdc()