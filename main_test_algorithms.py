from svm_algorithms import svm_algorithm
from LogisticRegression_algorithms import lr_algorithms
from neural_network_algorithms import nn_algorithms
import matplotlib.pyplot as plt

def main_test_algorithms():
    file_data = "agaricus-lepiota.data.txt"

    svm_performing_time = round(svm_algorithm(file_data), 2)
    lr_performing_time = round(lr_algorithms(file_data), 2)
    nn_performing_time = round(nn_algorithms(file_data), 2)

    y = [svm_performing_time, lr_performing_time, nn_performing_time]
    x = ['SVM', 'LR', 'NN']
    print(y)
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel('Algorithms')
    ax.set_ylabel('Times run')
    plt.show()

if __name__ == '__main__':
    main_test_algorithms()