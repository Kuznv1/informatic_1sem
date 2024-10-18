f = open('C:/temp/40.txt')
a = f.read()
a1 = list(a.split(', '))
f.close()
Points = [int(i) for i in a1]
#print(Points)
Znach = []
Kolvo = [] 
A = []
num = 100
for i in Points:
    if i not in A:
        n = Points.count(i)
        Znach.append(i)
        Kolvo.append(n)
        A.append(i)

Kolvo1 = sorted(Kolvo)
Dolya = []

for i in Kolvo1:
    Dolya.append(i/num)

print((Znach))
print(Kolvo)
print(Dolya)
print(sum(Points))
print(sum(Points)/num)

Q_otd_sum = 0
for i in Points:
    Q_otd_sum += (i - 41.68)**2
print(Q_otd_sum)

from numpy import sqrt
Q_otd = sqrt((1/num)*Q_otd_sum)
print(Q_otd)