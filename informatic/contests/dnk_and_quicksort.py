def Quicksort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    ref = A[len(A)//2]
    small = [number for number in A if number < ref]
    equal = [number for number in A if number == ref]
    big = [number for number in A if number > ref]
    return Quicksort(small) + equal + Quicksort(big)

Ntests = int(input())

for _ in range(Ntests):
    for __ in range(101):
        str = [sm for sm in input().split( )]
        if len(str) > 1:
            M = []
            Lenstr_n = int(str[0])        
            Nstr_m = int(str[1])
            go = 0
        else:
            M.append(str)
            go += 1
        if go == Nstr_m:
            break

print(str, M)


