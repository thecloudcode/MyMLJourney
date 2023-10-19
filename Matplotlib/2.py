# Format strings in plot function

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]

plt.plot(x,y,'g+--')
# or comment any one of the out
plt.plot(x,y,color='green',marker='D',linestyle='')
plt.show()