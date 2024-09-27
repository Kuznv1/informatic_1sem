import numpy as np
N = 3 
a = np.array([[1., 2., 3.],
              [2., 3., 4.],
              [1., 5., 1.]])

b = np.array([[1.],
             [0],
             [0]])
D = np.linalg.det(a)
print(D)

a1 = np.copy(a)
for i in range(N):
    a1[i][0] = b[i][0]
d1 = np.linalg.det(a1)

print(d1, a1.shape)

a2 = np.copy(a)
for i in range(N):
    a2[i][1] = b[i][0]
d2 = np.linalg.det(a2)

a3 = np.copy(a)
for i in range(N):
    a3[i][2] = b[i][0]
d3 = np.linalg.det(a3)

print(d1/D)
print(d2/D)
print(d3/D)
x1 = d1/D
x2 = d2/D
x3 = d3/D

A = np.array([[x1],
              [x2],
              [x3]])

c = np.dot(a, A)

print(c)




