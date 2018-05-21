from clean_data import *
from sklearn import svm
from sklearn.metrics import confusion_matrix
import time

# calculate performing time
start = time.time()


file_data = "agaricus-lepiota.data.txt"
data_frame = clean_data(file_data)
X_train, Y_train, X_test, Y_test = X_train_Y_train_X_test_Y_test(data_frame)

clf = svm.SVC()
clf.fit(X_train, Y_train)
y_pre_test = clf.predict(X_test)

cm_svm = confusion_matrix(Y_test, y_pre_test)
print('Confusion matrix SVM:\n', cm_svm)
print('Accuracy of SVM classifier on test set: ', clf.score(X_test, Y_test))

end = time.time()
print("Time: ", end - start)
