Skyscrapers = [int(j) for j in input().split()] 
L = len(Skyscrapers)
Big = Skyscrapers[0]
Index = 0

I = [0]
'''for i in range(L):       
    if i == 0:                  #first
        print(-1, end = ' ')
    
    elif i == 1:
        if Skyscrapers[1] > Skyscrapers[0]:
            print(-1, end = ' ')
            Big = Skyscrapers[1]
            I.append(i)
        else:
            I.append(i)
            print(0, end = ' ')

        
    elif Skyscrapers[i] > Big:    #Bigger
        print(-1,  end = ' ')
        Big = Skyscrapers[i]        
        I.append(i)
        
    elif Skyscrapers[i] <= Big:
        for j in range(i-2, -1, -1):
            if Skyscrapers[j] > Skyscrapers[i]:
                print(I, i, j, '@')
                print(I[j], end =' ')
                I.append(i)  
                break
    #print('!')     '''           

I = []
for i in range(L):       
    if i == 0:                  #first
        I.append(-1)
    
    elif i == 1:
        if Skyscrapers[1] > Skyscrapers[0]:
            Big = Skyscrapers[1]
            I.append(-1)
        else:
            I.append(0)

        
    elif Skyscrapers[i] > Big:    #Bigger
        Big = Skyscrapers[i]        
        I.append(-1)
        
    elif Skyscrapers[i] <= Big:
        for j in range(i-1, -1, -1):
            if Skyscrapers[j] >= Skyscrapers[i]:
                I.append(j)  
                break
    #print('!')                
print(*I, sep = ' ')