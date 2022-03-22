# https://www.acmicpc.net/problem/9251
# DP[i][j] 일 때, 
# X[i] = Y[j]인 경우에, DP[i][j] = DP[i-1][j-1] + 1
# X[i] != Y[j]인 경우에, DP[i][j] = max(DP[i][j-1], DP[i-1][j])

import sys 
input = sys.stdin.readline

X = list(input().strip())
Y = list(input().strip())
print(X, Y)
DP = [[0 for _ in range(len(Y)+1)] for _ in range(len(X)+1)]

for i in range(1, len(X)+1) : 
    for j in range(1, len(Y)+1) : 
        if X[i-1] == Y[j-1] : 
            DP[i][j] = DP[i-1][j-1] + 1 
        else : 
            DP[i][j] = max(DP[i][j-1], DP[i-1][j])
print(DP[len(X)][len(Y)])
# print(DP)