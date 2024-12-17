A = [int(i) for i in input().split()]

B = [A[n] for n in [1, 0]+ [r+1 if r % 2==0 and r != len(A)-1 else  r-1  for r in range(2, len(A)) ]]

print(*B) if len(A)%2 ==0 else print(*(B[:(len(A)-1)] + [A[-1]]))