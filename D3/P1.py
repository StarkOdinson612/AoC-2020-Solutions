with open('crap.txt', 'r') as f:
    bruv=[x.strip()for x in f.readlines()]

def p1(ri,ru):
  ouch=j=0
  for k in range(0,len(bruv),ri):
    if bruv[k][j%len(bruv[0])]=='#': ouch+=1
    j+=ru
  return ouch
if __name__=='__main__':
  print(p1(1,3))