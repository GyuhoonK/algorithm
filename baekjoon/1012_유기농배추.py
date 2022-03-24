# https://www.acmicpc.net/problem/1012

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_node, K, left):
    Q = deque([start_node])
    while Q : 
        current = Q.popleft()
        cur_x, cur_y = current
        
        left.remove(current)
        K -= 1 
        X = [1, 0, -1, 0]
        Y = [0, 1, 0, -1]
        for x,y in zip(X,Y) : 
            next_x = cur_x + x
            next_y = cur_y + y
            if (next_x, next_y) in left and (next_x, next_y) not in Q: 
                Q.append((next_x, next_y))
    return

T = int(input())
for _ in range(T) : 
    M, N, K = map(int, input().split())
    NODE = [[0 for _ in range(N)] for _ in range(M)]
    left = []
    for _ in range(K) : 
        pass
        x, y = map(int, input().split())
        NODE[x][y] = 1
        left.append((x,y))
    
        
    answer = 0
    while left :
        
        answer += 1
        bfs(left[0], K, left)
        
    print(answer)
    