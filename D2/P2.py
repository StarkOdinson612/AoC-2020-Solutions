with open('crap.txt', 'r') as f:
    bruv=[x.strip()for x in f.readlines()]

pog=0
for i in bruv:
  d=i.split()
  l=d[1][0]
  ur_crap_pw=d[2]
  r1,r2=map(int,d[0].split('-'))
  pog+=(ur_crap_pw[r1-1]==l)^(ur_crap_pw[r2-1]==l)
print(pog)