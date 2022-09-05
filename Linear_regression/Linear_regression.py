from sklearn.model_selection import train_test_split
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
    def __init__(self, learning_rate, no_of_iter):
        self.lr = learning_rate
        self.n_iters = no_of_iter
        self.weight = None
        self.bias = None
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        
        # initializing parameters
        self.weight = np.zeros(n_features)
        self.bias = 0
        
        # gradient descent
        for _ in range(self.n_iters):
            y_pred = np.dot(X, self.weight) + self.bias
            
            # compute gradients
            dw = (1/n_samples)*2*np.dot((X.T), (y_pred - y))
            db= (1/n_samples)*2*np.sum(y_pred - y)
            
            self.weight = self.weight - self.lr*dw
            self.bias = self.bias - self.lr*db
        
    def predict(self, X_test):
        y_approximated = np.dot(X_test, self.weight) + self.bias
        return y_approximated
    
if __name__=="__main__":
    
    X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
    
    def mse(y_test, y_pred):
        return np.mean((y_test - y_pred)**2)
    
    def r2_score(y_test, y_pred):
        corr_matrix = np.corrcoef(y_test, y_pred)
        corr = corr_matrix[0, 1]
        return corr ** 2
    
    LR = LinearRegression(learning_rate=0.001, no_of_iter=1000)
    LR.fit(X_train, y_train)
    predicted = LR.predict(X_test)
    
    print("Mean Squared error: ", mse(y_test, predicted))
    accu = r2_score(y_test, predicted)
    print("Accuracy:", accu)
    
    y_pred_line = LR.predict(X)
    cmap = plt.get_cmap("viridis")
    fig = plt.figure(figsize=(8,6))
    m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
    m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
    plt.plot(X, y_pred_line, color="black", linewidth=2, label="Prediction")
    plt.title("h( x ) = w * x + b ")
    plt.show()
    
    
    
    
    
    