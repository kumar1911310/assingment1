from itertools import permutations

n = list(input().split())

un = n[0].upper()

my_list = list(permutations(un, int(n[1])))
my_list.sort()

for i in range(len(my_list)):
    print(*my_list[i], sep='')