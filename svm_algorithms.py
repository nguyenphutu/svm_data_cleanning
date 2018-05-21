from clean_data import *
from sklearn import svm
from sklearn.metrics import confusion_matrix
import time


def svm_algorithm(file_data_name):

    # calculate performing time
    start = time.time()
    data_frame = clean_data(file_data_name)
    X_train, Y_train, X_test, Y_test = X_train_Y_train_X_test_Y_test(data_frame)

    # print data's size
    print('X train: ', X_train.shape)
    print('y train: ', Y_train.shape)
    print('X test: ', X_test.shape)
    print('y test: ', Y_test.shape)

    clf = svm.SVC()
    clf.fit(X_train, Y_train)
    y_pre_test = clf.predict(X_test)

    cm_svm = confusion_matrix(Y_test, y_pre_test)
    print('Confusion matrix SVM:\n', cm_svm)

    precision = clf.score(X_test, Y_test)
    print('Accuracy of SVM classifier on test set: ', precision)

    end = time.time()
    performing_time = end - start

    return performing_time, precision
