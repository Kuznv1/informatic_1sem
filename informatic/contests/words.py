Words = [i for i in input().split()]
Words_ready = Words.copy()

def Quicksort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    ref = A[len(A)//2]
    small = [number for number in A if number < ref]
    equal = [number for number in A if number == ref]
    big = [number for number in A if number > ref]
    return Quicksort(small) + equal + Quicksort(big)

MWord = []
Groups = []
Len_groups = []
One = []
#gln krc srp kte rrc def dfe edf efd khn knh kas hep erd sam obo cpk mil aha
ln = len(Words[0])
l = 0
while l != len(Words) :
    Letters = list(Words_ready[0])
    p = 1
    if Letters[0] == '1':
        while Letters[0] == '1':
            Letters = list(Words_ready[p])
            p+= 1
    for i in Words_ready:       
        wrd = list(i)
        A = Letters.copy()
        z = 0
        for k in range(ln): #проверяем буквы
            if wrd[k] in A:
                A[A.index(wrd[k])] = 0
            else:
                z = 1
                break

        if z != 1:
            MWord.append(i)
            Words_ready[Words_ready.index(i)] = '1'
            l +=1
    #print(l, MWord)

                

    #print(MWord, Letters)

    if len(MWord) == 1:
        One.append(MWord)
    else: 
        Groups.append(MWord)      #запоминается группа слов
        Len_groups.append(len(MWord))

    MWord = []



    
'''Len_groups = Quicksort(Len_groups)

Len_groups.reverse()
One = Quicksort(One)


for group1 in Groups:
    g = group1
    #print(g)
    g = Quicksort(g)
    #print(group1)
    Groups[Groups.index(group1)] = g
    #print(g)
'''
print(Groups, One)
# for Len in Len_groups: #вывод
for group in Groups:
    # if len(group) == Len :
    print(*group, sep = ' ', end = ' ')
    Groups[Groups.index(group)] = '0'
    break
#print(1)               
for gr in One: #вывод
    print(*gr, end = ' ')

        

