import matplotlib.pyplot as plt
# %matplotlib inline

x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]

plt.plot(x,y, color="blue", linewidth=2, linestyle="dashdot")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weather")
plt.show()