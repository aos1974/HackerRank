from audioop import reverse


m = int(input())
m_set = set(map(int, input().split()))

n = int(input())
n_set = set(map(int, input().split()))

dif_set = m_set.difference(n_set)
lst = list(dif_set)
dif_set = n_set.difference(m_set)
lst.extend(list(dif_set))
lst.sort()

for l in lst:
    print(l)
