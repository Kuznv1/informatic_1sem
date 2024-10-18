import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(311) 
ax2 = fig.add_subplot(312) 
ax3 = fig.add_subplot(313)

values1 = np.random.normal(0, 10, 100)
 

ax1.hist(values1, 50, color = 'green')
ax1.grid()

values2 = np.random.normal(0, 10, 1000)
ax2.hist(values2, 50)
ax2.grid() 

ax2.set_title('second graph') 

values3 = np.random.normal(0, 10, 2000)
ax3.hist(values3, 50)
ax3.grid() 

ax3.set_title('third graph') 


plt.show()