# https://www.acmicpc.net/problem/1325
# bfs1 이용 시 정답처리 
# bfs2 이용 시 시간초과
# 어떤 차이가 있는 것일까?
import sys
from collections import deque
input = sys.stdin.readline

def bfs1(start_node, node, visited):
    cnt = 1
    Q = deque([start_node])
    visited[start_node] = True 
    while Q : 
        current = Q.popleft()
        for next_node in node[current] : 
            if not visited[next_node] :
                Q.append(next_node)
                visited[next_node] = True 
                cnt += 1
    return cnt

def bfs2(start_node, node, visited):
    cnt = 0
    Q = deque([start_node])
    while Q : 
        current = Q.popleft()
        visited[current] = True 
        cnt += 1
        for next_node in node[current] : 
            if not visited[next_node] :
                Q.append(next_node)
    return cnt

N, M = map(int, input().split())
NODE = [[] for _ in range(N+1)]
for _ in range(M) : 
    p, q = map(int, input().split())
    NODE[q].append(p)
answer = []
max_val = -1
for start_node in range(1, N+1) : 
    visited = [False] * (N+1)
    cnt = bfs1(start_node, NODE, visited)
    # cnt = bfs1(start_node, NODE, visited)
    if cnt > max_val :
        max_val = cnt
        answer = [start_node]
    elif cnt == max_val : 
        answer.append(start_node)
for ans in answer : 
    print(ans, end = ' ')

