import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style

data = pd.read_csv('student-mat.csv', sep=";")
# print(data.head())

data = data[["G1","G2","G3", "studytime", "failures", "absences"]]
# print(data.head())

predict = "G3"

X=np.array(data.drop([predict],axis=1))
Y=np.array(data[predict])
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

# best= 0
# for _ in range(27):
#     X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)
#
#     #pickle is used to save everything
#     linear = linear_model.LinearRegression()
#
#     linear.fit(X_train,Y_train)
#     acc= linear.score(X_test,Y_test)
#     print(acc)
#
#     # i am loving it
#     if acc>best:
#         best=acc
#         with open("studentmodel.pickle","wb") as f:
#             pickle.dump(linear,f)
#
# print("Best : ",best)

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

print("Co: ",linear.coef_) # coefficients for 5 different dimensions
print("Intercept: ", linear.intercept_)

predictions = linear.predict(X_test)

# print predictions, lists and test data raw
for x in range(len(predictions)):
    print(predictions[x], X_test[x], Y_test[x])

p="absences"
style.use("ggplot")
pyplot.scatter(data[p],data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()
