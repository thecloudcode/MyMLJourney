import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data")
# print(data.head())

le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

predict = "class"

X = list(zip(buying,maint, door,persons, lug_boot, safety))
Y = list(cls)

X_train,X_test,Y_train,Y_test = sklearn.model_selection.train_test_split(X,Y,test_size=0.1)
# print(X_train, X_test)

# In KNN classification, we should always keep K value as odd as it will
# ensure that there is always a winner
model = KNeighborsClassifier(n_neighbors=7)

model.fit(X_train, Y_train)
acc = model.score(X_test, Y_test)
print(acc)

predicted = model.predict(X_test)
names = ["unacc","acc","good","vgood"]
for i in range(len(predicted)):
    print("Predicted: ",names[predicted[i]],"Data: ",X_test[i],"Actual: ",names[Y_test[i]])
    print("miss" if predicted[i]!=Y_test[i] else "")

    n = model.kneighbors([X_test[i]], 9, True)
    print(n)


