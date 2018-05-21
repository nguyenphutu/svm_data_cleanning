from clean_data import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import time


def lr_algorithms(file_data_name):
    # calculate performing time
    start = time.time()
    data_frame = clean_data(file_data_name)
    X_train, Y_train, X_test, Y_test = X_train_Y_train_X_test_Y_test(data_frame)

    # print data's size
    print('X train: ', X_train.shape)
    print('y train: ', Y_train.shape)
    print('X test: ', X_test.shape)
    print('y test: ', Y_test.shape)

    # call model and fit model and training data
    clf_lr = LogisticRegression().fit(X_train, Y_train)

    # predict test data
    y_pred_lr = clf_lr.predict(X_test)

    cm_lr = confusion_matrix(Y_test, y_pred_lr)
    print('Confusion matrix SVM:\n', cm_lr)
    precision = clf_lr.score(X_test, Y_test)
    print('Accuracy of Logistic Regression on test set: ', precision)

    end = time.time()
    performing_time = end - start

    return performing_time, precision
