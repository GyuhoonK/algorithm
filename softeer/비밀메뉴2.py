import sys
from itertools import product

N, M, K = list(map(int, sys.stdin.readline().rstrip().split(' ')))
# P1 = list(map(int, sys.stdin.readline().rstrip().split(' ')))
# P2 = list(map(int, sys.stdin.readline().rstrip().split(' ')))
P1 = " ".join(['3' for i in range(3000)])
P2 = " ".join(['3' for i in range(3000)])

if N > M :
    shorter = P2
    longer = P1
else :
    shorter = P1
    longer = P2

answer = 0
def getMaxLen(t, s) : 
    L = min(len(t), len(s))
    if set(t) == set(s) :
        return L
    idx_list = []
    for idx in range(L) : 
        if (t[idx] == s[idx]): 
            idx_list.append(idx) 
    if not idx_list :
        return 0
    dp = [1 for _ in range(len(idx_list))]
    for i in range(len(idx_list)) :
        for j in range(i) :
            if idx_list[i] == idx_list[j]+1 :
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                # dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

        
for start_i in range(len(longer)) : 
    longer_part = longer[start_i : ]
    tmp = getMaxLen(shorter, longer_part)
    if tmp > answer : 
        answer = tmp

for end_i in range(1, len(shorter)) : 
    longer_part = longer[:end_i]
    tmp = getMaxLen(shorter[-end_i:], longer_part)
    if tmp > answer : 
        answer = tmp 
print(answer)
        