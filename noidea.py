n, m = input().split()

n = int(n)
m = int(m)

n_set = list(input().split())
a_set = set(input().split())
b_set = set(input().split())

happiness = 0

for i in n_set:
    if i in a_set:
        happiness += 1
    if i in b_set:
        happiness -= 1

print(happiness)
