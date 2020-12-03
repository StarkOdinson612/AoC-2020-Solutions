with open('crap.txt', 'r') as f:
  n=[int(x.strip())for x in f.readlines()]
t=2020

for p in __import__('itertools').permutations(n,3): # Change 3 to 2 for Part 1 :)
  if sum(p)==t: bruv=p;break
print(__import__('math').prod(bruv))
