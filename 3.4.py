N, symb = input().split()

#def triangle(n):
#    if m != n:
#        print(m * 'symb')
#        return(m+1)
m = 1
while m <= int(N)/2:
    print(m * symb)
    m += 1

if int(N)%2 == 0:
    m -= 1
    print(m * symb)
    m -= 1
    while m >= 1:
        print(m * symb)
        m -= 1


while m >= 1:
    print(m * symb)
    m -= 1

