from itertools import combinations_with_replacement as cwr

S, k = input().split()

for c in cwr(sorted(S), int(k)):
    print (*[''.join(c)])
