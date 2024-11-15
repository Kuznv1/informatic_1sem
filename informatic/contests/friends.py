People = [int(j) for j in input().split()]

A = []
for person in People:
    Quantity = 0
    persondim = person
    #print('/', People.index(person))
    for i in range(People.index(person)+1, len(People)):
        if People[i] > persondim:
            Quantity += 1
            persondim = People[i]
    People[People.index(person)] = 0
    A.append(Quantity)

print(*A, sep = ' ')