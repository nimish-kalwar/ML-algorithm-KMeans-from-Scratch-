from collections import Counter
from sklearn import datasets
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt

def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2))

class KNN:
    def __init__(self, k):
        self.k=k
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)
    
    def _predict(self, x):
        # Compute distance bewtween x and all examples in the training set
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        
        # Sort by distance and return indices of the first K neighbors
        k_idx = np.argsort(distances)[: self.k]
        
        # Extract the labels of the K nearest training samples
        k_neighbor_labels = [self.y_train[i] for i in k_idx]
        
        # return the most common class label
        most_common_label = Counter(k_neighbor_labels).most_common(1) # most_common_label will be a tuple which having most common label with its frequency
        return most_common_label[0][0]
    
if __name__=="__main__":
    cmap = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
                           
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
    
    def accuracy(pred, y_test):
        return np.sum(pred==y_test)/len(y_test)
    
    print(X.shape)
    print(np.unique(y)) # to find out unique labels to assign test values
    
    k=3 # number of nearest neighbor
    clf = KNN(k)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print("KNN classification accuracy", accuracy(predictions, y_test))

    plt.figure()
    plt.scatter(X_test[:,2], y_test, c =y_test,cmap=cmap, s=20)
    plt.title('test')
    plt.show()
    plt.close()
    plt.scatter(X_test[:,2], predictions, c =predictions,cmap=cmap, s=20)
    plt.title('predictions')
    plt.show()
    
                           
