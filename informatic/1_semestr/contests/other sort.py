A = [j for j in input().split()]
L1 = len(A)

for m in range(L1):                                  #сортируем массив значений
    for n in range(0, L1 - m - 1):
        if int(A[n]) > int(A[n + 1]):
            A[n], A[n + 1] = A[n + 1], A[n]
            #print(A)
B = []
Numbers = {}


for i in range(len(A)):
    sum = 0
    if int(A[i])//10 != 0:
        for el in A[i]:
            sum += int(el)
        #print('*', sum)
        while sum // 10 != 0:
            nsum = 0
            for m in str(sum):
                nsum += int(m)
            sum = nsum
            
        Numbers[int(A[i])] = sum
    else:
        Numbers[int(A[i])] = int(A[i])    # создаем cловарь число - сумма
        
for key in Numbers:
    B.append(Numbers.get(key)) # создаем массив В со значениями

#print(Numbers)
#print(B)
'''MIN = []
while len(B) != 0:
    MIN.append(min(B))
    B.remove(min(B))
'''
L = len(B)

for i in range(L):                                  #сортируем массив значений
    for j in range(0, L - i - 1):
        if B[j] > B[j + 1]:
            B[j], B[j + 1] = B[j + 1], B[j]

Val = list(Numbers.values())

for znach in B:
    #print(znach)
    print(list(Numbers.keys())[list(Numbers.values()).index(znach)], end = ' ')
    
    K = list(Numbers.keys())[list(Numbers.values()).index(znach)]
    Numbers[K] = 0
    B[B.index(znach)] = 0
