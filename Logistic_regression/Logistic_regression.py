from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt 
import numpy as np

class Logistic_Regression:
    def __init__(self, lr, n_iters):
        self.lr = lr
        self.n_iters = n_iters
        self.weight = None
        self.bias = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        
        # initialize parameters
        self.weight = np.zeros(n_features)
        self.bias = 0
        l=[]
        
        # gradient descent
        for _ in range(self.n_iters):
            # approximate y with linear combination of weights and x, plus bias
            linear_model = np.dot(X, self.weight) + self.bias
            # apply sigmoid function
            predicted = self._sigmoid(linear_model)
            
            # compute gradients
            dw = (1/n_samples)*2*np.dot(X.T, (predicted- y))
            db = (1/n_samples)*2*np.sum(predicted - y)
            
            self.weight = self.weight - self.lr*dw
            self.bias = self.bias - self.lr*db
            l.append(self.loss(y,predicted))
        print("we minimized loss/cost function from",l[0],"to",l[-1])
        
        plt.plot(l)
        plt.title("Loss Function")
        plt.show()
        
    
    def loss(self,y, y_hat):
        loss = -np.mean(y*(np.log(y_hat)) - (1-y)*np.log(1-y_hat)) #Loss/Cost function
        return loss

    def predict(self, X):
        linear_model = np.dot(X, self.weight) + self.bias
        predicted = self._sigmoid(linear_model)
        predicted_label = [1 if i >0.5 else 0 for i in predicted]
        return predicted_label
    
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

if __name__=="__main__":
    bc = datasets.load_breast_cancer()
    X, y = bc.data, bc.target
    print("shape of dataset",X.shape)
    X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.2, random_state=1000)
    
    def accuracy(y_pred, y_true):
        return np.sum(y_pred==y_true) / len(y_true)
    
    log_reg = Logistic_Regression(lr=0.00001, n_iters=1000)
    log_reg.fit(X_train, y_train)
    y_pred = log_reg.predict(X_test)
    print("Accuracy: ", accuracy(y_pred, y_test))

    m1 = plt.scatter(X_test[:,0], y_test, color="blue", s=20) # we are taking the first feature out of 30
    m1 = plt.scatter(X_test[:,0], y_pred, color="green", s=20)
    
    plt.show()