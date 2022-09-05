# Algorithm Implemented

## Goal

Assign a class label to the new data point by calculating distances from K neighbors.

## Iterative optimization

Step 1. Figure out an appropriate distance metric to calculate the distance between the data points in our case we are using Euclidean distance.

Step 2. Store the distance in an array and sort it according to the ascending order of their distances (preserving the index i.e. can use NumPy argsort method).

Step 3. Select the first K elements in the sorted list.

Step 4. Perform the majority Voting and the class with the maximum number of occurrences will be assigned as the new class for the data point to be classified.

## Euclidean distance

Get the distance between two feature vectors

d(p,q) =√Σ(q - p)^2

Where,

“d” is the Euclidean distance

p, q are two euclidean vectors

