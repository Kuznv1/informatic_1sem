import numpy as np
import math

M = 2925
L = 2.201
m = np.array([0.502, 0.506, 0.509, 0.497, 0.513])

g = 9.81
Delta_x = np.array([11.5, 11.25, 12, 12.25, 13])
u = [107.8, 116.6, 110.4, 111.4, 106.7 ]
'''u = (M/(m) * np.sqrt(g/L) * Delta_x*10**(-3))'''
u_mean = np.mean(u)
sigmasluch_u = np.sqrt( 1 / (10 - 1) * np.sum( (u - u_mean)**2 ) )

print(sigmasluch_u)
sigmasis_u = u * ((0.5)/(Delta_x)**2 + (5/2925)**2  + (0.02/m)**2 + (0.001/(2*L))**2 )**0.5
sigma_u = (sigmasluch_u**2 + sigmasis_u**2)**0.5
print('u: ', u)
print('sigma_u: ', sigma_u)
print('mean: ', u_mean)
print(np.mean(sigma_u))
