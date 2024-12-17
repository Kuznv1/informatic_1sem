# Evclid
'''a = 8
b = 6
while a != 0 and b != 0:
    if a > b:
        a = a%b
        print(f' a ={a}, b = {b}')
    else:
        b = b % a
        print(f' a ={a}, b = {b}')

print(a + b)
'''
# Решето Эратосфена
'''Primes = [i for i in range(N + 1)]
Primes[1] = 0 # т.к. 1 - не простое число

i = 2
while i <= N:
    if Primes[i] != 0:
        j = i + i
        while j <= N:
            Primes[j] = 0
            j += i
    i += 1

Primes = [i for i in Primes if i != 0]'''

# Разложение на простые множители
def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n = n//d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans
