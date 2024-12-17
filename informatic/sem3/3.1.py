N = int(input())

def Fib(n, A):
    if n == 1:
        A[0] = 0
        return A[0]
    
    if n == 2:
        A[1] = 1
        return A[1]
    
    if A[n-1] != 0:
        return A[n-1]
    
    A[n-1] = Fib(n-1, A) +Fib(n-2, A)
    return A[n-1]

print(Fib(N, [0 for i in range(N)]))
    
    

