# https://www.acmicpc.net/problem/5719

import sys
input = sys.stdin.readline
import heapq
from collections import deque
from math import inf

def dikstra(start_node, node) : 
    dist = [inf] * len(node) 
    dist[start_node] = 0 
    Q = [(0, start_node)]
    while Q : 
        cur_dist, cur_node = heapq.heappop(Q)
        if cur_dist > dist[cur_node] : 
            continue
        for (v, w) in node[cur_node] :
            if w + cur_dist < dist[v] : 
                dist[v] = w + cur_dist
                heapq.heappush(Q, (w+cur_dist, v))
    return dist 

def bfs(start_node, node, S, dist): 
    Q = deque([start_node])
    drop = []
    while Q :
        current = Q.popleft() 
        if current == S :
            continue 
        for (v, w) in node[current] : 
            if dist[current] == dist[v] + w : 
                if (v, current) not in drop : 
                    drop.append((v, current))
                Q.append(v)
    return drop

def dfs(current, node, S, dist, drop): 
    if current == S : 
        return
    for (v, w) in node[current] : 
        if dist[current] == dist[v] + w : 
            # if (v, current) not in drop : 
            drop.append((v, current)) 
            dfs(v, node, S, dist, drop)
    return

def dikstra_drop(start_node, node, drop) : 
    dist = [inf] * len(node) 
    dist[start_node] = 0 
    Q = [(0, start_node)]
    while Q : 
        cur_dist, cur_node = heapq.heappop(Q)
        if cur_dist > dist[cur_node] : 
            continue
        for (v, w) in node[cur_node] :
            if (cur_node, v) in drop : 
                continue
            if w + cur_dist < dist[v] : 
                dist[v] = w + cur_dist
                heapq.heappush(Q, (w+cur_dist, v))
    return dist 
while True : 
    N, M = map(int, input().split()) 
    if (N, M) == (0, 0) : 
        break
    NODE = [[] for _ in range(N)] # NODE[i] : (weight, node)
    NODE_reversed = [[] for _ in range(N)] # NODE[i] : (weight, node)
    S, D = map(int, input().split()) 
    for _ in range(M) : 
        u, v, p = map(int, input().split())
        NODE[u].append((v, p))
        NODE_reversed[v].append((u, p))
    dist = dikstra(S, NODE)
    # S->D path를 찾기 위해 BFS 실시
    drop = []
    dfs(D, NODE_reversed, S, dist, drop)
    # drop = bfs(D, NODE_reversed, S, dist)
    # S->D 에서 사용된 path를 제외하고 다익스트라 수행
    print(drop)
    dist = dikstra_drop(S, NODE, drop)
    if dist[D] == inf :
        print(-1)
    else : 
        print(dist[D])

# 메모리 초과 해결 안됨