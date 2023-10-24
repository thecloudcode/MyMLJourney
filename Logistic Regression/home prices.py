import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('homeprices.csv')
print(df)

# plt.xlabel("Area (Square Feet)")
# plt.ylabel("Price USD")
# plt.scatter(df.area,df.price,color="red",marker="+")
# plt.show()

reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)

# Now in case you have another area dataset with no prices
# You can predict the prices of the area

# and convert the file into a .csv file

d = pd.read_csv("areas.csv")
# print(d.head(7))

p=reg.predict(d)
d['prices'] = p
d.to_csv("prediction.csv", index=False)

predicted_price = reg.predict(np.array([[3300]]))
print(predicted_price)

# now as a line equation is y = m*x + b
# Linear regression calculated the values for m and b

# value of m and b
print(reg.coef_, reg.intercept_)

# Displaying the Linear Regression Line
plt.xlabel('area',fontsize=17)
plt.ylabel('price',fontsize=17)
plt.scatter(df.area,df.price,color='red',marker='+')
plt.plot(df.area,reg.predict(df[['area']]),color='blue')
plt.show()