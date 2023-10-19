# What happens in linear regression is that we minimize the sum of delta i
# i.e. the distance between the points to the most common fitted line and
# we try to sum that up and then we try yo minimize the sum

# price = area * m + b || y = m*x + b

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("canada_per_capita_income.csv")
print(df)