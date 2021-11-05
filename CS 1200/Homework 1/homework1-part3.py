# Question 3
hyps = [ 'p <= q','r or s', '(not s) <= (not t)', '(not q) or s', '(not s)', '((not p) and r) <= u', 'w or t']
concl = 'u and w'

fst = "{0:^3s}|{1:^3s}|{2:^3s}|{3:^3s}|{4:^3s}|{5:^3s}|{6:^3s}|{7:^3s}|{8:^3s}|{9:^3s}|{10:^3s}|{11:^3s}|{12:^3s}|{13:^3s}|"
fst2 = "{0:^3d}|{1:^3d}|{2:^3d}|{3:^3d}|{4:^3d}|{5:^3d}|{6:^3d}| {7:^3d} | {8:^3d} | {9:^3d} | {10:^3d} | {11:^3d} | {12:^3d} |   {13:^3d}   |"
div = "---+---+---+---+---+---+---+-----+-----+-----+-----+-----+-----+----------+"

print(fst.format('p','q','r', 's', 't', 'w', 'u', 'prem1','prem2','prem3','prem4','prem5','prem6','conclusion'))
for p in range(2):    
  for q in range(2):        
    for r in range(2):   
      for s in range(2):
        for t in range(2):
          for w in range(2):
            for u in range(2):
              print(div)                
              print (fst2.format(p,q,r,s,t,w,u, eval(hyps[0]),                          
                    eval(hyps[1]), eval(hyps[2]), eval(hyps[3]), eval(hyps[4]), 
                    eval(hyps[5]), eval(concl)))