# Algorithm Implemented

## Goal

Cluster a data set into k different clusters. The data set is unlabeled (unsupervised learning). Each sample is assigned to the cluster with the nearest mean.

## Iterative optimization

1. Initialize cluster centers (e.g. randomly)

2. Repeat until converged:

Update cluster labels: Assign points to the nearest cluster center (centroid)

• Update cluster centers (centroids): Set center to the mean of each cluster

## Euclidean distance

Get the distance between two feature vectors

In the Euclidean plane, let point {\displaystyle p}p have Cartesian coordinates {\displaystyle (p_{1},p_{2})}(p_{1},p_{2}) and let point {\displaystyle q}q have coordinates {\displaystyle (q_{1},q_{2})}(q_{1},q_{2}). Then the distance between {\displaystyle p}p and {\displaystyle q}q is given by:[2]

{\displaystyle d(p,q)={\sqrt {(q_{1}-p_{1})^{2}+(q_{2}-p_{2})^{2}}}.}{\displaystyle d(p,q)={\sqrt {(q_{1}-p_{1})^{2}+(q_{2}-p_{2})^{2}}}.}

