"""St = 3
Subject = int(input())
str = input()
N_tickets = [int(i) for i in list(str.split())]

First = []
Second = []
Third = 0
One = 1
N_one = sum(N_tickets)//3


if sum(N_tickets) % 3 != 0:
    print(0)
else:
    
   '''
   '''

First.append(max(N_tickets))
N_tickets.remove(max(N_tickets))

while Third == 0:
    if sum(First) > sum(N_tickets):
        print(0)
        Third = 1
    
    if sum(First) * 2 < sum(N_tickets):
        while sum(First) * 2 < sum(N_tickets):
            First.append(min(N_tickets))
            N_tickets.remove(min(N_tickets))

    if sum(First) > sum(N_tickets):
        print(0)
        Third = 1
    
    if sum(First)*2 == sum(N_tickets):
        Second.append(max(N_tickets))
        N_tickets.remove(max(N_tickets))

        if sum(Second) > sum(N_tickets):
            print(0)
            Third = 1

        elif sum(Second) < sum(N_tickets):
            while sum(Second) < sum(N_tickets):
                Second.append(min(N_tickets))
                N_tickets.remove(min(N_tickets))

    if sum(Second) > sum(N_tickets):
        print (0)
        Third = 1
    
    Third = 1

if sum(First) == sum(Second) and sum(First) == sum(N_tickets):
    print(1)
else:
    print(0)"""
N_point = 4
Vectors = [[1 for j in range(3)] for i in range(N_point)]
print(Vectors)