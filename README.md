# CECS451-Assignment-2
Ian Escalante
Created for CECS 451 Fall 23

Implementation of Hill Climbing and Genetic algorithms to solve collision problems in a simulated chess board.

### Problem
Given a modified version of the 8 queens problem and boards.py, implement the hill climbing and genetic algorithms to create scenarios in which there are 0 pairs of attacking queens (collisions: queens that are in line vertically, horizontally, or diagonally).

## Hill Climbing Algorithm
From an initial state, the neighboring states are each compared to the best fit next move in a greedy search. Using a heuristic cost function (h) that is equal to the number of attacking pairs, the goal is to minimize it and reach 0 for a solution. 

## Genetic Algorithm
Four separate boards are represented by strings of digits representing the positions of the queens; Each of these boards are compared according to the least amount of collisions. 
1. Selection: The likelihood of survival of each board is calculated as the individual board fitness/ total fitness. Boards are chosen by random, with greater likelihood given to the genes with better outcomes.
3. Crossover: A random index of the string is chosen and the corresponding sections of two boards are split, swapped, and concatenated. 
4. Mutation: Each string is subjected to a random probability for if a digit changed to a different, random value.
The process is repeated until the win condition is met (0 colliding queens)

