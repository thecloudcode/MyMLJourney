### Outliers
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Define the dataset
dataset = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Find outliers using Z-score
# Three S.Ds : 68%, 95%, 99.7%
# Thus, after the 99.7% the data left is outliers.
outliers=[]

def detect_outliers(data):
    threshold = 3 # after this threshold that will be considered as an outlier
    mean=np.mean(data)
    std=np.std(data)

    for i in data:
        z_score=(i-mean)/std
        if abs(z_score)>threshold:
            outliers.append(i)

    print("Outliers: ",outliers)

detect_outliers(dataset)


# IQR -- Inter Quartile Range
# 1.Sort the Data
# 2.Calculate Q1 and Q3
# 3.IQR(Q3-Q1)
# 4.Find the Lower fence(Q1-1.5(iqr))
# 5.Find the Upper fence(Q3+1.5(iqr))

data=sorted(dataset)
q1,q3 = np.percentile(data,[25,75])
iqr = q3 - q1
lower_fence = q1 - 1.5*iqr
upper_fence = q3 + 1.5*iqr
print(q1,q3)
print(iqr, lower_fence, upper_fence)


# Generate boxplot
sns.boxplot(dataset)
plt.show()


