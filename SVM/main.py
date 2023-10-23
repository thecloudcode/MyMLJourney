import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

cancer = datasets.load_breast_cancer()

# print(cancer.feature_names)
# print(cancer.target_names)

x=cancer.data
y=cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.2)

print(x_train,y_train)
classes = ['malignant','benign']

# margin : the distance between the 2 extreme point planes is called margin in SVM diagram
# the larger the distance between the two extremes, the more we can separate the two classes, and do more accurate prediction

# in case we cannot find a hyper plane
# kernals : 2D -> 3D, using kernal (just a function) that takes inputs and returns the higher dimension

# Soft Margin : watch it, and Hard Margin

# clf = svm.SVC()

#lets give a parameter
# clf = svm.SVC(kernel="linear", C=2) # Here C is the soft margin or Hard margin
# clf = svm.SVC(kernel="poly", degree=2)

clf = KNeighborsClassifier(n_neighbors=17)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
acc = metrics.accuracy_score(y_test, y_pred)
print(acc)