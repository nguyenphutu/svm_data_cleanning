from clean_data import *
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import time


def nn_algorithms(file_data_name):

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
    clf_ann = MLPClassifier().fit(X_train, Y_train)

    # predict test data
    y_pred_ann = clf_ann.predict(X_test)

    cm_ann = confusion_matrix(Y_test, y_pred_ann)
    print('Confusion matrix SVM:\n', cm_ann)
    precision = clf_ann.score(X_test, Y_test)
    print('Accuracy of Neural Network on test set: ', precision)

    end = time.time()
    performing_time = end - start

    return performing_time, precision
