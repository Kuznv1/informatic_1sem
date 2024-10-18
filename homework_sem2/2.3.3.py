mirror = {'A':'A', 'H':'H', 'I':'I', 'M':'M', 'O':'O', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', '1':'1', '8':'8', 'E':'3', 'J':'L', 'S':'2', 'Z':'5'}
A = [i for i in input()]
k = 0
m = ''.join(map(str, A))

for sm in A:
    if sm in mirror:
        k += 1

if A == A[::-1]:
        print(m, 'is regular palindrom')
elif k < len(A):
    print(m, 'is not a palindrom')
    














