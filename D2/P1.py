with open('crap.txt', 'r') as f:
  bruv=[x.strip()for x in f.readlines()]

pog=0
for i in bruv:
  d=i.split()
  l=d[1][0]
  r1,r2=map(int,d[0].split('-'))
  ur_crap_pw=d[2]
  if r1<=ur_crap_pw.count(l)<=r2: pog+=1
print(pog)