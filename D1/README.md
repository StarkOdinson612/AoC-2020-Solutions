# Explanation

```py
with open('crap.txt', 'r') as f:
  n=[int(x.strip())for x in f.readlines()]
t=2020

for p in __import__('itertools').permutations(n,2): # Change 2 to 3 for Part 2 :)
  if sum(p)==t: bruv=p;break
print(__import__('math').prod(bruv))
```

The first 2 lines reads the input data given in the question as input data.
This gets stored to a variable named `n`

3rd line defines a variable named `t` which is the target value which needs to be obtained by adding some 2 numbers.

The next 2 lines iterates over every permutations of 2 numbers and checks if the sum is equal to `t`.

If the number is found, it assigns a variable called `bruv` to the iterable of the 2 numbers.

Since the question stated the product of the 2 numbers which add up to 2020, we take the product of all the elements (2 elements) in the iterable.

Finally, it gets printed.

Part 2 just wanted the product of **3** numbers instead so we change the size of the permutation to 3, and then take the product following that, printing.
