A = [int(i) for i in input().split()]

B = [A[n] for n in [1, 0]+[r for r in range(2, len(A)) if int(r)%2!=0]+[m for m in range(2, len(A)) if int(m)%2==0]]

print(B)