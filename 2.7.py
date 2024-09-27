A = [i for i in input().split()]
el = A[0]
k = 0
for m in A:
    if A.count(m) >= k:
        el = m
        k = A.count(m)

print(el) 
