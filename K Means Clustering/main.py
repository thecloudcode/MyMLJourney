# Any diff : Watch Tech with Team video again K-Means Clustering

# Repeat the process
# Mark centroids and then between their distance draw a line at 90 degrees and separate the two clusters
# Keeping repeating this process
# Disadvantage : Slow

# Now if we have X1, X2 and X700, it needs to 700 iterations features.

import numpy as np
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics

digits = load_digits()
data = scale(digits.data) # scaling them down to small values
#it makes things faster

y = digits.target
k = 10
samples, features = data.shape

# use : bench_k_means
# use Kmeans ++ for fast iteration and performance

# max_iter : maximum iterations : 300 (default)




