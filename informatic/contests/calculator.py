N = int(input())

prices = [[0 for n in range(N+1)], # числа
          [0 for j in range(N+1)]]  # цены
k = 0
for m in range(N+1):
    prices[0][m] = k
    k += 1

prices[1][0] = 0
prices[1][1] = 0
prices[1][2] = 1

       
INF = 1e10

for i in range(3, N+1):
    p2 = INF
    p3 = INF
    if i % 2 == 0:
        i2 = i//2
        p2 = prices[1][i2]

    if i % 3 == 0:
        i3 = i//3
        p2 = prices[1][i3]
    prices[1][i] = min(prices[1][i-1], p2 , p3) + 1

print(prices[1][N])
