l = open('List.txt').read().split("\n\n")

correct = 0

for m in l:
    if 'byr:' in m and 'iyr:' in m and 'eyr:' in m and 'hgt:' in m and 'hcl:' in m and 'ecl:' in m and 'pid:' in m:
        correct += 1

print(correct)
