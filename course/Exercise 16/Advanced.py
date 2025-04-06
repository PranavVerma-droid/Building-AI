import numpy as np
from sklearn.datasets import make_blobs #type:ignore
from sklearn.preprocessing import MinMaxScaler #type:ignore
from sklearn.model_selection import train_test_split #type:ignore


# create random data with two classes
X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []

# distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):

    global y_predict
    global lines

    k = 3 

    for i, test_item in enumerate(X_test):
        distances = [dist(train_item, test_item) for train_item in X_train]

        nearest_indices = np.argsort(distances)[:k]

        lines.append(np.stack((test_item, X_train[nearest_indices[0]])))

        neighbor_labels = [y_train[j] for j in nearest_indices]

        if neighbor_labels.count(1) > neighbor_labels.count(0):
            y_predict[i] = 1
        else:
            y_predict[i] = 0
    
    print(y_predict)

main(X_train, X_test, y_train, y_test)
