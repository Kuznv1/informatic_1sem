mirror = {'A':'A', 'H':'H', 'I':'I', 'M':'M', 'O':'O', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', '1':'1', '8':'8', 'E':'3', 'J':'L', 'S':'2', 'Z':'5'}
A = [i for i in input()]
k = 0
m = ''.join(map(str, A))

for sm in A:
    if sm in mirror:
        k += 1


       
if A != A[::-1]:
    if k == len(A):
        mirror_A = []
        for sm in A:
            mirror_A.append(mirror[sm])
        mirror_A =''.join(map(str, A))  
        if mirror_A == m:
            print(m, 'is a mirrored string')
        else:
            print(m, 'is not a palindrom')
    else:
        print(m, 'is not a palindrom')
    
elif A == A[::-1]:
    if k == len(A):
        mirror_A = []
        for sm in A:
            mirror_A.append(mirror[sm])
        mirror_A =''.join(map(str, A))  

        #print('!', mirror_A, A)
        if mirror_A == m:
            print(m, 'is a mirrored palindrom')
        else:
            print(m, 'is a regular palindrom')
    else:
        print(m, 'is regular palindrom')





         
    














