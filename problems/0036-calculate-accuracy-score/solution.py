import numpy as np

def accuracy_score(y_true, y_pred):
    # Your code here
    correct_pred = 0
    for i in range(len(y_pred)):
        if y_true[i] == y_pred[i]:
            correct_pred += 1

    accuracy_score = correct_pred / len(y_pred)

    return accuracy_score
    pass