# Algorithm Implemented

## Goal

Cluster a data set into k different clusters. The data set is unlabeled (unsupervised learning). Each sample is assigned to the cluster with the nearest mean.

## Iterative optimization

1. Initialize cluster centers (e.g. randomly)

2. Repeat until converged:

• Update cluster labels: Assign points to the nearest cluster center (centroid)

• Update cluster centers (centroids): Set center to the mean of each cluster

## Euclidean distance

Get the distance between two feature vectors

d(p,q) =√Σ(q - p)^2]

Where,

“d” is the Euclidean distance

p, q are two euclidean vectors

