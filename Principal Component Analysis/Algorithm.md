# Algorithm Implemented

## Goal

PCA finds a new set of dimensions such that all the dimesions are orthogonal (and hence linearly independent) and ranked according to the variance of data along them.

Find a transformation such that

* The transformed features are linearly independent
* Dimensionality can be reduced by taking only the dimensions with the highest   importance
* Those newly found dimensions should minimize the projection error
* The Projected points should have maximum spred, i.e. maximum variance

## Steps to Implement PCA.

  Step 1: Subtract the mean from X.
  
  Step 2: Calculate Cov(X, X)
  * The covariance matrix is a square matrix denoting the covariance of the elements with each other. The covariance of an element with itself is nothing but just its     Variance.
  
  Step 3: Calculate eignevectors and eigenvalues in decreasing order
   * A Higher Eigenvalue corresponds to a higher variability. Hence the principal axis with the higher Eigenvalue will be an axis capturing higher variability in the       data.
   * Each column in the Eigen vector-matrix corresponds to a principal component, so arranging them in descending order of their Eigenvalue will automatically arrange      the principal component in descending order of their variability.
  
  Step 4: Choose first k eigenvectors and that will be the new k dimensions
  
  Step 5: Transform the n dimensional data points into k dimensions (= Projections with dot product)


  ### Variance
  
  How much variation or spread the data has.
  
  Var(X) = 1/n*sigma(Xi - Xm)^2
  
  where Xi is the data point,
  
        Xm is the mean of dataset,
        
        n total number of samples
