A = [i for i in input().split()]
n = A[0]
for r in range(len(A)):
    n = A[r]
    if (r != len(A)-1) and  n != A[r+1] and n != A[r-1]:
        print(n, end=' ')
    if r == len(A)-1:
        n = A[r]
        if n != A[r-1]:
            print(n, end=' ')
    





