MIN = []
B = [3, 5, 7, 1, 2]
"""for i in range(len(B)-1):
    
    if B[i] > B[i+1]:
        B[i], B[i+1] = B[i+1], B[i]
        print(B)
"""
while len(B) != 0:
    MIN.append(min(B))
    B.remove(min(B))

print(MIN)