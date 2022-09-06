# Algorithm Implemented

## Goal

Depicts the relationship between the dependent variable y and the independent variables xi  ( or features ).  
The hypothetical function used for prediction is represented by h( x ).

## Iterative optimization

  h( x ) = w * x + b  
    
  here, b is the bias.
  x represents the feature vector
  w represents the weight vector.
  
  The cost function (or loss function) is used to measure the performance of a machine learning model or quantifies the error between the expected values 
  and the values predicted by our hypothetical function. The cost function for Linear Regression is represented by J.
  
  So, our objective is to minimize the cost function J (or improve the performance of our machine learning model). 
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
