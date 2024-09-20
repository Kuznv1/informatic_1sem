A = [int(i) for i in input().split()]
print(" ".join(map(str, [A[n] for n in [len(A)-1]+[r for r in range(0, (len(A)-1))]])))