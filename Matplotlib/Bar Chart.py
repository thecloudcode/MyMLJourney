import matplotlib.pyplot as plt
import numpy as np
company = ["GOOGL", "AMZN", "MSFT", "FB"]
revenue = [90,136,89,27]
profit = [40,2,34,12]

xpos = np.arange(len(company))
print(xpos)
plt.bar(xpos,revenue)
plt.xticks(xpos, company) #replace 0 1 2 3 by the names on the list
plt.ylabel("revenue(bln)")
plt.title("US Tech Stocks")
plt.bar(xpos-0.2,revenue, width=0.4, label="Revenue")
plt.bar(xpos+0.2,profit, width=0.4, label="Profit")

# Horizontal Bar
# plt.barh(xpos-0.2,revenue, label="Revenue")
# plt.barh(xpos+0.2,profit, label="Profit")

plt.legend()
plt.show()

