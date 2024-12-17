import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')
df

fig = plt.figure(figsize = (9, 5))
ax1 = fig.add_subplot(311) 
ax2 = fig.add_subplot(312) 

#Species
ax1.set_title('Species') 

zn1 = 0
zn2 = 0
zn3 = 0
for x in list(df['Species']):
    if x == "Iris-setosa":
        zn1 += 1
    
    if x == 'Iris-versicolor':
        zn2 += 1

    if x == 'Iris-virginica':
        zn3 += 1

ax1.pie([zn1, zn2, zn3], labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], colors = ['cornflowerblue', 'orchid', 'green'])

#Lenght
ax2.set_title('Lenght') 

a1 = 0
a2 = 0
a3 = 0

for i in list(df['PetalLengthCm']):
    if  i > 1.2 :
        a1 += 1
    if i> 1.5 :
        a3 += 1
    if i > 1.2 and int(i) < 1.5:
        a2 += 1

ax2.pie([a1, a2, a3], labels = ['>1.2 cm', '> 1.2 and < 1.5', '>1.5 sm'], colors = ['cornflowerblue', 'palegreen', 'violet'])



plt.show()


    
    
