# https://www.acmicpc.net/problem/1904
# Dynamic Programming
# D[i] = D[i-1] + D[i-1]

import sys 
input = sys.stdin.readline

n = int(input()) 

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1) : 
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])