Words = [i for i in input().split()]


def Quicksort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    ref = A[len(A)//2]
    small = [number for number in A if number < ref]
    equal = [number for number in A if number == ref]
    big = [number for number in A if number > ref]
    return Quicksort(small) + equal + Quicksort(big)

Words = Quicksort(Words)
Words_ready = Words.copy()
MWord = []
Groups = []
Len_groups = []
One = []
Len_gr = {}
#gln krc srp kte rrc def dfe edf efd khn knh kas hep erd sam obo cpk mil aha
# ran nra bat eat tea aet ate 
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
    

    if len(MWord) == 1:
        One.append(MWord)
    else: 
        Groups.append(MWord)      #запоминается группа слов
        Len_groups.append(len(MWord))
        Len_gr[len(MWord)] = MWord

    MWord = []

#print(Words, Groups, One)
Len_groups = Quicksort(Len_groups)

Len_groups.reverse()


for Len in Len_groups: #вывод
    print(*Len_gr[Len], sep = ' ', end = ' ')
            
#print(1)               
for gr in One: #вывод
    print(*gr, end = ' ')

#def dfe edf efd khn knh aha cpk erd gln hep kas krc kte mil obo rrc sam srp