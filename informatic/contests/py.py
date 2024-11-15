n = 120
a = [10, 60, 100]
k = len(a)

INF = 1e10; # Значение константы "бесконечность"
F = [0] * (n + 1)
F[0] = 0

for m in range(1, n + 1): # заполняем массив A
                       # m - сумма, которую нужно выдать
    F[m] = INF         # помечаем, что сумму i выдать нельзя
    for i in range(k): # перебираем все номиналы банкнот
        if m >= a[i] and F[m - a[i]] + 1 < F[m]:
            F[m] = F[m-a[i]]+1 # изменяем значение F[m],
            print(F[m])