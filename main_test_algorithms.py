from svm_algorithms import svm_algorithm
from LogisticRegression_algorithms import lr_algorithms
from neural_network_algorithms import nn_algorithms
import matplotlib.pyplot as plt


def main_test_algorithms():
    file_data = "agaricus-lepiota.data.txt"

    svm_performing_time, svm_precision = svm_algorithm(file_data)
    lr_performing_time, lr_precision = lr_algorithms(file_data)
    nn_performing_time, nn_precision = nn_algorithms(file_data)

    # histogram running time
    y = [svm_performing_time, lr_performing_time, nn_performing_time]
    x = ['SVM', 'LR', 'NN']
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel('Algorithms')
    ax.set_ylabel('Run times')
    plt.savefig('run_times.png')

    # histogram precision
    y = [svm_precision, lr_precision, nn_precision]
    x = ['SVM', 'LR', 'NN']
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel('Algorithms')
    ax.set_ylabel('Precision')
    plt.savefig('precision.png')


if __name__ == '__main__':
    main_test_algorithms()
