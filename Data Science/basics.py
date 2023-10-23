import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
# %matplotlib inline

# mean, median and mode
df=pd.read_csv('car.data')
x=np.array(df['persons']).astype(int) # use astype to convert all the elements in the array to the same data type in one line

# mean, median and mode of the array
print(np.mean(x))
print(np.median(x))
print(statistics.mode(x))

# Boxplot
# sns.boxplot(x)

# Histplot
# sns.histplot(x,kde=True)
# plt.show()

# Count Plot
# sns.countplot(x)
# plt.show()

# Percentile
print(np.percentile(x,[90,50]))

