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

d =√[(x2 – x1)2 + (y2 – y1)2]

Where,

“d” is the Euclidean distance

(x1, y1) is the coordinate of the first point

(x2, y2) is the coordinate of the second point.

