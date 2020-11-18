# MIT-Machine-Learning
MIT ML Lab Assignments BTech Fourth Year MIT School of Engineering, MIT ADT University.

### 1. ID3 Decision Tree Classification Algorithm
> Published Package at : [https://pypi.org/project/classic-ID3-DecisionTree/](https://pypi.org/project/classic-ID3-DecisionTree/)
#### Assignment 1
Dataset Description:- Congressional Voting Records Data Set (UCI ML repository)
In this assignment you will train a decision tree to predict votes of US Congressmen based on
their political party and on other votes they have made in the past. This is based on a data set
from the UCI ML repository. The data contains a total of 435 examples, one for each member
of the US House of Representatives. Each example is described in terms of 17 attributes
including ”party” (democrat or republican), and 16 votes made by this congressperson, such
as “antiSatelliteTestBan” (with values ”y”, ”n” and ”noVote”). These are in comma-
separated-file format, with the first line in the file listing the attribute names (separated by
commas) and each remaining line in the file giving the values of these attributes for a single
congressperson.
* Task 1:- Train your decision tree classifier (without post-pruning) for following
classification problem.
Construct a tree to predict “party” (democrat or republican) based on the 16 votes of the
congressperson. Implement the ID3 decision tree learning algorithm with “Information Gain”
as well as “Gini Index” measures. Use Python programming language. Your program can
assume that all features/attributes take on only discrete values (no real-valued attributes), that
the data contains no missing attributes, and that legal values for each attribute are known in
advance.
Run your algorithm on the training data to learn a decision tree for predicting ”party”. Print
your decision tree.
Answer below questions:
1. What is your learned decision tree’s accuracy over the training set?
2. What is your learned decision tree’s accuracy Over the test set?
3. Suggest why these accuracies might differ in the ways you observe.
Note:- Perform Task 1 for both “Information Gain” and “Gini Index” measures
separately.

### 2. Find-S Algorithm
> Published Package at : [https://pypi.org/project/classic-FindS/](https://pypi.org/project/classic-FindS/)
#### Assignment 2.1
Implement and demonstrate the FIND-S algorithm in Python for finding the most
specific hypothesis using the set of training data examples.
Apply your model to classify test examples.
You must use 10-fold cross-validation technique to partition the data into two sets:- Training
and Test. Report the average accuracy, F1-score and plot AUC (Area Under the Curve).

### 3. Candidate-Elimination Algorithm
> Published Package at : [https://pypi.org/project/classic-CandidateElimination/](https://pypi.org/project/classic-CandidateElimination/)
#### Assignment 2.2
Implement and demonstrate the Candidate-Elimination algorithm in Python to
output a set of all hypotheses consistent with the training examples.
Now apply your obtained version-space of hypothesis to classify test examples.
You must use 10-fold cross-validation technique to partition the data into two sets:- Training
and Test. Report the average accuracy, F1-score and plot AUC (Area Under the Curve).

### 4. SVC kernels
* File - svc_kernels.py
* For Structured Data - svc_kernels.pynb
#### Assignment 3
Write a program to demonstrate the working of SVM classifier with various nonlinear kernels
(Linear/Polynomial/RBF) for a non-linearly separable data. Before constructing SVM model
perform feature selection on the dataset using two different techniques: 1) information gain
and 2) forward feature selection. Use an appropriate nonlinear data set (after feature
selection) for building the SVM model and apply this model to classify a new sample. Find
hyper-parameters (degree, C, and sigma) using k-fold cross-validation technique. Report
accuracy, F-score and ROC curve for the best model created using Linear, Polynomial, and
RBF kernels, respectively.

### 5. Bayesian Belief Network
* File - 2175052_Safir_ML_Lab_Ass5.pynb
#### Assignment 5
Write a python program to construct a Bayesian Belief Network considering medical data.
Use this model to demonstrate the diagnosis of heart patients using the standard Heart
Disease Data Set. Refer the dataset ‘asia’ (also called LUNG CANCER) which is available in
R package ‘bnlearn’ (Link:- https://www.bnlearn.com/bnrepository/discrete-small.html#asia).
Note:- Copy ‘asia’ dataset from the package ‘bnlearn’. Then, develop your code in python to
construct a Bayesian Belief Network. It’s an individual assignment.

### 6. Genetic Algorithm
* File - 2175052_Safir_ML_Lab_Ass6.pynb
* Reference - https://github.com/ezstoltz/genetic-algorithm/blob/master/genetic_algorithm_TSP.ipynb
#### Assignment 6
Write an evolutionary (GA) algorithm that searches for the shortest route between N
cities. Use an encoding method such that the chromosomes consist of lists of integers
determining the indices of the cities. Examples of five-city paths starting in city 4 are e.g. (4,
3, 1, 2, 5), (4, 1, 5, 2, 3), (4, 5, 1, 2, 3) etc. The first chromosome thus encodes the path 4 → 3
→ 1 → 2 → 5 → 4. The fitness should be taken as the inverse of the route length (calculated
using the ordinary cartesian distance measure and not the city-block distance measures). The
program should always generate syntactically correct routes, i.e. routes in which each city is
visited once and only once until, in the final step, the tour ends by a return to the starting city.
Choose a suitable mutation operator for the TSP that maps valid chromosomes (i.e. paths)
onto other valid chromosomes. Choose a suitable crossover operator for the TSP that maps
valid chromosomes onto other valid chromosomes. Using these crossover and mutation
operators, write an Evolutionary Algorithm that solves the Travelling Salesman Problem.
Apply your program to the TSP data given in the file. This file contains a 50 × 2 matrix
with the coordinates (x i , y i ) for city i = 1, . . . , 50. What is the shortest path between the
cities and how long is it?
File Link:- http://ml.informatik.uni-freiburg.de/former/_media/teaching/ss11/citydata.txt
