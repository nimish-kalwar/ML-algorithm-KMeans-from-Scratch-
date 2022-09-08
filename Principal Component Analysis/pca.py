from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.mean = None
        self.components = None
        
    def fit(self, X):
        # Mean centering
        self.mean = np.mean(X, axis=0)
        X = X - self.mean
        
        # Covariance, function needs samples as columns i.e. we transpose data
        cov = np.cov(X.T)
        
        # eigenvalues, eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(cov) # each eigenvector represent prinicipal axis
        
        # eigenvector v = [ :, i] column vector, transpose for easier calculations
        # sort eigenvectors
        eigenvectors = eigenvectors.T
        idxs = np.argsort(eigenvalues)[::-1] # get indices in descending order of eigenvalues
        eigenvalues =  eigenvalues[idxs]
        eigenvectors = eigenvectors[idxs]
        
        # store first n eigenvectors
        self.components = eigenvectors[0 : self.n_components]
    
    def transform(self, X):
        # project data 
        X = X - self.mean
        print(X.shape, self.components.T.shape)
        return np.dot(X, self.components.T) # we transpose components to get dot product with X
    
if __name__=="__main__":
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    
    # Project the data onto the 2 primary principal components
    p = PCA(n_components=3)
    p.fit(X)
    X_projected = p.transform(X)
    
    print("Shape of X:", X.shape)
    print("Shape of transformed X:", X_projected.shape)
    
    p1 = X_projected[ :, 0] # first principal component
    p2 = X_projected[ :, 1] # second principal component
    
    plt.figure(figsize = (6,6))
    plt.scatter(p1, p2, c=y, cmap=plt.cm.get_cmap("viridis", 3), alpha=0.8)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.colorbar()
    plt.show()