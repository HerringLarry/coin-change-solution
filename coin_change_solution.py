#!/bin/python

import sys

def getWays(n, c):
    total = 0
    sol = [[1]]
    for x in range(0,len(c)):
        sol.append([1])
    for x in range(1,(n+1)):
        sol[0].append(0)
    for i in range(1,len(c)+1):
        for j in range(1,(n+1)):
            if j >= c[i-1]:
                sol[i].append(sol[i-1][j] + sol[i][j - c[i-1]])
            else:
                sol[i].append(sol[i-1][j])
    print sol[len(c)][n]

n = sys.argv[1]
n = n.split(',')
c = sys.argv[2]
c = c.split(',')
n = map(int,n)
c = map(int,c)
print n
print c
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n[0], c)
