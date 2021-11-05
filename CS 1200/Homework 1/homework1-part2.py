# Question 2
hyps = [ '((not m) and c) <= (not t)','(not c) <= ((not m) or (not t))']
concl = 'm <= c'

fst = "{0:^3s}|{1:^3s}|{2:^3s}|{3:^3s}|{4:^8s}|  {5:^7s}   |"
fst2 = "{0:^3d}|{1:^3d}|{2:^3d}|      {3:^3d}     | {4:^8d}      |   {5:^7d}  |"
div = "---+---+---+--------------+---------------+------------+"

print(fst.format('m','c','t','(~m & c) -> ~t','~c -> (~m | ~t)','m -> c'))
for m in range(2):    
  for c in range(2):        
    for t in range(2):   
        print(div)                
        print (fst2.format(m,c,t, eval(hyps[0]),                          
              eval(hyps[1]),eval(concl)))