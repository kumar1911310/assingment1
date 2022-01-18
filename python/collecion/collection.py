from collections import Counter

input()
c = Counter(input().split())
sum = 0
for _ in range(int(input())):
    n,p = input().split()
    if c[n]>0:
        sum += int(p)
        c[n] -= 1
print(sum)