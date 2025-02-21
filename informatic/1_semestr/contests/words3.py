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
Groups = {}
One = []
for word in Words:
    Letters = ''.join(Quicksort(word))
    
    
    if Letters in Groups:
        Groups[Letters].append(word)
    else:
        Groups[Letters] = [word]
Keys = []
for key in Groups:
    if len(Groups[key]) == 1:
        One.append(''.join(Groups[key]))
    else:
        Keys.append(key)


for i in One:
    del Groups[''.join(Quicksort(i))] 
#Groups = Quicksort(Groups(), key=lambda item: item[1], reverse=True)
for i in Keys:
        l = len(Groups[i])
        Groups[l] = Groups.pop(i)
#print(Groups)

Len_groups = Quicksort(list(Groups.keys()))
Len_groups.reverse()
for Len in Len_groups: #вывод
    print(*Groups[Len], sep = ' ', end = ' ')

print(*One)
#def dfe edf efd khn knh aha cpk erd gln hep kas krc kte mil obo rrc sam srp