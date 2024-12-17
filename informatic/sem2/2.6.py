A = [i for i in input().split()]
n = A[0]
for r in range(len(A)):
    n = A[r]
    if A.count(n) == 1:
        print(n, end=' ')




