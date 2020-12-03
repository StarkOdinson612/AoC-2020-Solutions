with open('crap.txt', 'r') as f:
  n=[int(x.strip())for x in f.readlines()]
t=2020

for p in __import__('itertools').permutations(n,2): # Change 2 to 3 for Part 2 :)
  if sum(p)==t: bruv=p;break
print(__import__('math').prod(bruv))
