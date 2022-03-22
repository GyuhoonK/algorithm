# https://www.acmicpc.net/problem/1260

from collections import deque
import sys 
input = sys.stdin.readline

def bfs(start_node, nodes, visited):
    Q = deque([start_node])
    order = 1
    while Q : 
        current = Q.popleft()
        visited[current] = order
        for next_node in nodes[current]:
            if visited[next_node] == 0 and next_node not in Q: 
                Q.append(next_node)
        order += 1
    return visited 

def dfs(current, nodes, visited, order):
    visited[current] = order
    for next_node in nodes[current] : 
        if visited[next_node] == 0 : 
            dfs(next_node, nodes, visited, max(visited)+1)
    return
N, M, V = map(int, input().split())

nodes = [[] for _ in range(N+1)]
for _ in range(M) : 
    p, q = map(int, input().split())
    nodes[p].append(q)
    nodes[q].append(p)
for idx in range(1, N+1) : 
    nodes[idx].sort()

visited = [0 for _ in range(N+1)]
dfs(V, nodes, visited, 1)
answer = sorted([(idx, order) for idx, order in enumerate(visited[1:], 1)], key = lambda x:x[1])
for idx, order in answer :
    if visited[idx] == 0 : 
        continue
    print(idx, end = ' ')
print()

visited = [0 for _ in range(N+1)]
visited = bfs(V, nodes, visited)
answer = sorted([(idx, order) for idx, order in enumerate(visited[1:], 1)], key = lambda x:x[1])
for idx, order in answer :
    if visited[idx] == 0 : 
        continue
    print(idx, end = ' ')