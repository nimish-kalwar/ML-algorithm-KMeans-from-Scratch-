# Algorithm Implemented

## Goal

Depicts the relationship between the dependent variable y(categorical) and the independent variables xi  ( or features ).  
The hypothetical function used for prediction is represented by h( x ).

## Iterative optimization

  h( x ) = sigmoid( wx + b )

  Here, w is the weight vector.
  x is the feature vector. 
  b is the bias.

  ### sigmoid( z ) = 1 / ( 1 + e( - z ) )
  
  The cost function for Logistic Regression is represented by J.
  
  ### J = - ylog( h(x) ) - ( 1 - y )log( 1 - h(x) )

  here, y is the real target value
  
  h( x ) = sigmoid( wx + b )

  For y = 0,

  J = - log( 1 - h(x) )

  and y = 1,

  J = - log( h(x) )
  
  This cost function is we train, we need to maximize the probability by minimizing the loss function
  
  To do this, we have to find the weights at which J is minimum.  One such algorithm which can be used to minimize any differentiable function is Gradient Descent. 
  It is a first-order iterative optimizing algorithm that takes us to a minimum of a function.
  
  
## Gradient descent

1: Start with some w

2: Keep changing w to reduce J( w ) until we hopefully end up at a minimum.

Algorithm: 
repeat until convergence  {
       tmpi = wi - alpha * dwi          
       wi = tmpi              
}

where alpha is the learning rate.
