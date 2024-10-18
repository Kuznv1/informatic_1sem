Points = []

f = open('C:/temp/1.txt') #путь к файлу с точками 
for line in f:
    Points.append(int(line))
f.close()

Sum = []
b = 0
index = 0
#там, где сорок, пишешь 10, 20 или 40. Оно суммирует по указ.числу
while index != len(Points):
    for k in range(40):
        b += Points[index + k]
    
    Sum.append(b)
    b = 0
    index += 40

print(Sum)
#результат копируешь, вставляешь в блокнот, сохраняешь. 3 файла должно получится

