Subject = int(input())
str = input()
N_tickets = [int(i) for i in list(str.split())]

First = []
Second = []
Third = 0
C = []
a = 0
N_tickets.sort(reverse = True)

N = len(N_tickets)
N_tickets1 = N_tickets.copy()
Third_all = 0
N_one = sum(N_tickets)//3

if sum(N_tickets) % 3 != 0:
    print(0)
else:
    N_one = sum(N_tickets)//3
    while Third_all == 0:
        First.append(N_tickets1[0])
        for j in range(N):
            if sum(First) == N_one:
                break

            if sum(First) > N_one:
                print(0)
                Third_all = 1
                a = 1
                break
                
        
            if sum(First)  < N_one:
                if sum(First) + N_tickets1[j] <= N_one:
                        First.append(N_tickets1[j])
                        N_tickets1[j]
            
            continue   
        
        
        if First == C:
            print(0)
            a = 1
            # Third_all = 1
            break
        Nt = N_tickets1.copy()
        A = []
        for i in range(len(N_tickets1)):
            if N_tickets1[i] in First and N_tickets1[i] not in A:
                Nt.remove(N_tickets1[i])
                A.append(N_tickets1[i])
                
        N_tickets1 = Nt
        print(N_tickets1)
        

        Second.append(N_tickets1[0])
        for j1 in range(N):
            if sum(Second) == N_one:
                Third1 = 1
                break

            if sum(Second) > N_one:
                print(0)
                a = 1
                Third_all = 1
                break
                
        
            if sum(Second)  < N_one:
                if sum(Second) + N_tickets1[j1] <= N_one:
                    Second.append(N_tickets1[j1])
                    
            
            if sum(Second) == N_one:
                Third1 = 1
            continue
                
        if Second == C:
            print(0)
            a = 1
            Third_all = 1
            break
        
        
        Nt = N_tickets1.copy()
        A = []

        for i1 in range(len(N_tickets1)):
            if N_tickets1[i1] in Second and N_tickets1[i1] not in A:
                Nt.remove(N_tickets1[i1])
                A.append(N_tickets1[i1])
        N_tickets1 = Nt
        
        #print(N_tickets1)

        
        if sum(First) == sum(Second) and sum(First) == sum(N_tickets1):
            print(1)
            Third_all = 1
        else:
            if a == 0:
                print(0)
                break

        Third_all = 1


        

    
    


    
        



