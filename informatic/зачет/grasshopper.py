price = [0, 1, 3, 2, 4, 5, 1]
S = [0 for i in range(len(price))]
S[0] = 0
S[1] = 1
Way = []
n = 5
for i in range(2, n+1):
    S[i] = min(S[i-1], S[i-2]) + price[i]
#для пути идем вторым циклом назад и в массив добавляем индекс минимума
print(S[n])
print(S)

